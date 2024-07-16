import os
import requests
from datetime import datetime
from dotenv import load_dotenv
from moviepy.editor import VideoFileClip, CompositeVideoClip, AudioFileClip, TextClip, concatenate_videoclips
from gtts import gTTS
from moviepy.config import change_settings
import json

change_settings({"IMAGEMAGICK_BINARY": "C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})

# Load environment variables
load_dotenv()
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
PEXELS_API_KEY = os.getenv('PEXELS_API_KEY')

# Load the JSON file
with open('neon.json', 'r') as file:
    data = json.load(file)

# Load the JSON file
with open('neon-subtitles.json', 'r', encoding='utf-8') as file:
    subtitles = json.load(file)

# Access the title and content
title = data['title']
content = data['content']

def download_video(video_url, download_path, filename):
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    response = requests.get(video_url)
    if response.status_code == 200:
        filepath = os.path.join(download_path, filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)
        print(f"Video downloaded successfully as {filename}")
        return filepath
    else:
        print("Failed to download video")
        return None

def get_stock_video(query='drone', download_path='api_data'):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{query}_{timestamp}.mp4"

    url = 'https://api.pexels.com/videos/search'
    headers = {'Authorization': PEXELS_API_KEY}
    params = {'query': query, 'per_page': 1}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print(f"Error fetching video: {response.status_code}")
        print(response.text)
        return None

    data = response.json()
    if data['videos']:
        video_url = data['videos'][0]['video_files'][0]['link']
        print(f"Video URL: {video_url}")
        return download_video(video_url, download_path, filename)
    else:
        print("No videos found.")
        return None

def text_to_speech(text, output_path='tts_audio'):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    audio_filename = f"{timestamp}.mp3"
    tts = gTTS(text=text, tld='com.au', lang='en', slow=False)
    tts.save(os.path.join(output_path, audio_filename))
    print(f"Speech saved to {audio_filename}")
    return os.path.join(output_path, audio_filename)

def create_horizontal_text(text, fontsize=70, color='white', font='Arial-Bold'):
    """ Creates a horizontally oriented text clip """
    txt_clip = TextClip(text, fontsize=fontsize, color=color, font=font, size=(1080, 200))
    # Set position to a fixed location
    txt_clip = txt_clip.set_position(('center')).set_duration(10)  # Adjust as needed
    return txt_clip


def create_movie_with_audio_and_subtitles(video_filename, audio_filename, text, subtitles, output_path='final_videos'):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    final_video_name = f"{timestamp}.mp4"

    video_clip = VideoFileClip(video_filename)
    video_clip = concatenate_videoclips([video_clip, video_clip, video_clip, video_clip, video_clip])

    # Resize the video to 1080x1920 for YouTube Shorts
    video_clip = video_clip.resize((1080, 1920))

    audio_clip = AudioFileClip(audio_filename)

    # Combine the audio with the video
    video_clip = video_clip.set_audio(audio_clip)

    # Create a list to store subtitle clips
    subtitle_clips = []

    # Generate text clips for subtitles
    for subtitle_data in subtitles:
        subtitle_text = subtitle_data['text']
        start_time = subtitle_data['start']
        end_time = subtitle_data['end']

        # Create horizontally oriented text clip with larger font size
        txt_clip = create_horizontal_text(subtitle_text, fontsize=100)
        txt_clip = txt_clip.set_duration(end_time - start_time).set_start(start_time)
        print(f"Positioning text clip '{subtitle_text}' from {start_time} to {end_time}")

        # Add the subtitle clip to the list
        subtitle_clips.append(txt_clip)

    # Combine all subtitle clips into a single CompositeVideoClip
    subtitles_clip = CompositeVideoClip(subtitle_clips)

    # Composite the video with audio and subtitles
    final_clip = CompositeVideoClip([video_clip, subtitles_clip])

    # Write the final video file
    final_clip.write_videofile(os.path.join(output_path, final_video_name), fps=24)


def main():
    print("Fetching stock video...")
    video_filename = get_stock_video(query='code vertical')
    if video_filename:
        # Load content from neon.json
        with open('neon.json', 'r', encoding='utf-8') as file:
            neon_data = json.load(file)
        neon_content = neon_data['content']

        # Load subtitles from neon-subtitles.json
        with open('neon-subtitles.json', 'r', encoding='utf-8') as file:
            subtitles_data = json.load(file)
        subtitles = subtitles_data['subtitles']

        # Convert neon content to speech
        audio_filename = text_to_speech(neon_content)

        # Create final video with audio and subtitles
        print(f"Creating final video with Neon content audio and subtitles")
        create_movie_with_audio_and_subtitles(video_filename, audio_filename, neon_content, subtitles)

if __name__ == '__main__':
    main()
