from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
import os
from pathlib import Path
from mangum import Mangum


# Create FastAPI app
app = FastAPI(title="IEEE Site", description="IEEE Site with FastAPI backend")

# Get the directory where this file is located
BASE_DIR = Path(__file__).parent.parent

# Mount static files
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Serve the main page"""
    return FileResponse(str(BASE_DIR / "static" / "index.html"))

handler = Mangum(app)
