from fastapi import FastAPI, HTTPException, responses

app = FastAPI(
    title="Majestic Shorts API",
    description="API to generate short form content quickly and cheaply.",
    version="1.0.0",
    docs_url="/api",  # Change Swagger UI URL to /apik
)

@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return responses.RedirectResponse(url="/api")

@app.get("/generate")
def generate_short_content(topic: str):
    # Placeholder for content generation logic
    return {"topic": topic, "short_content": "This is a short content generated for the topic."}

@app.get("/info")
def api_info():
    return {"API Name": "Majestic Shorts API", "Version": "1.0.0"}