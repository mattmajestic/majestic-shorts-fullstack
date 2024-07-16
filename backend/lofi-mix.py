import moviepy.editor as mp
from moviepy.config import change_settings

# Update the path to the ImageMagick binary
change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"})

# Define the input video and the desired output duration for each part
input_video = "edm-viz.mp4"
output_video = "output/output-edm-text.mp4"
desired_duration = 396  # ~ 5 minutes

# Load the input video
clip = mp.VideoFileClip(input_video)

# Calculate the number of times the clip needs to be repeated
clip_duration = clip.duration
num_repeats = int(desired_duration // clip_duration) + 1

# Create a concatenated clip
clips = [clip] * num_repeats
final_clip = mp.concatenate_videoclips(clips)

# Trim the final clip to the exact desired duration
final_clip = final_clip.subclip(0, desired_duration)

# Define the text clip
txt_clip = mp.TextClip("Lofi EDM Mix", fontsize=120, font="Comic-Sans-MS", color='#1e0449')

# Set the position of the text clip in the center and the duration to match the video
txt_clip = txt_clip.set_position('center').set_duration(desired_duration)

# Composite the text clip on top of the video
video = mp.CompositeVideoClip([final_clip, txt_clip])

# Write the output video
video.write_videofile(output_video, codec="libx264", audio=False)
