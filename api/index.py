from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path
from mangum import Mangum

# Create FastAPI app
app = FastAPI(title="IEEE Site", description="IEEE Site with FastAPI backend")

# Get the directory where this file is located
BASE_DIR = Path(__file__).parent.parent

@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Serve the main page"""
    # Read the HTML file content directly
    html_file = BASE_DIR / "static" / "index.html"
    with open(html_file, "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

handler = Mangum(app)
