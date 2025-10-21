from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from mangum import Mangum

# Create FastAPI app
app = FastAPI(title="IEEE Site", description="IEEE Site with FastAPI backend")

# HTML content embedded directly
HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IEEE Site</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
        }
        header {
            text-align: center;
            margin-bottom: 40px;
        }
        nav {
            background-color: #f4f4f4;
            padding: 10px;
            margin-bottom: 30px;
            border-radius: 5px;
        }
        nav a {
            margin-right: 20px;
            text-decoration: none;
            color: #333;
            font-weight: bold;
        }
        nav a:hover {
            color: #0066cc;
        }
        .content {
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to IEEE Site</h1>
        <p>A modern IEEE website</p>
    </header>
    
    <nav>
        <a href="/">Home</a>
        <a href="/about">About</a>
        <a href="/contact">Contact</a>
    </nav>
    
    <div class="content">
        <h2>Welcome!</h2>
        <p>This is your IEEE website homepage. You can customize this content and add more pages as needed.</p>
        
        <h3>Getting Started</h3>
        <ul>
            <li>Edit this HTML file in the <code>static/</code> directory</li>
            <li>Add more pages by creating additional HTML files</li>
            <li>Customize the styling to match your IEEE chapter's branding</li>
        </ul>
    </div>
</body>
</html>"""

@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Serve the main page"""
    return HTMLResponse(content=HTML_CONTENT)

# Create the Mangum handler
mangum_handler = Mangum(app)

# Vercel expects a handler function
def handler(event, context):
    return mangum_handler(event, context)
