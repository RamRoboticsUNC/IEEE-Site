from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

# Create FastAPI app
app = FastAPI(title="IEEE Site", description="IEEE Site with FastAPI backend")

# Get the directory where this file is located
BASE_DIR = Path(__file__).parent.parent

# Mount static files
app.mount("/assets", StaticFiles(directory=str(BASE_DIR / "static" / "assets")), name="assets")
app.mount("/images", StaticFiles(directory=str(BASE_DIR / "static" / "images")), name="images")

# HTML content using HTML5UP template
HTML_CONTENT = """<!DOCTYPE HTML>
<!--
	IEEE Site - Based on Eventually by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<html>
	<head>
		<title>IEEE Site</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="assets/css/main.css" />
	</head>
	<body class="is-preload">

		<!-- Header -->
			<header id="header">
				<h1>IEEE</h1>
				<p>Welcome to our IEEE chapter website<br />
				Join us for exciting events, workshops, and networking opportunities.</p>
			</header>

		<!-- Signup Form -->
			<form id="signup-form" method="post" action="#">
				<input type="email" name="email" id="email" placeholder="Email Address" />
				<input type="submit" value="Stay Updated" />
			</form>

		<!-- Footer -->
			<footer id="footer">
				<ul class="icons">
					<li><a href="#" class="icon brands fa-twitter"><span class="label">Twitter</span></a></li>
					<li><a href="#" class="icon brands fa-instagram"><span class="label">Instagram</span></a></li>
					<li><a href="#" class="icon brands fa-github"><span class="label">GitHub</span></a></li>
					<li><a href="#" class="icon fa-envelope"><span class="label">Email</span></a></li>
				</ul>
				<ul class="copyright">
					<li>&copy; IEEE Chapter.</li><li>Template: <a href="http://html5up.net">HTML5 UP</a></li>
				</ul>
			</footer>

		<!-- Scripts -->
			<script src="assets/js/main.js"></script>

	</body>
</html>"""

@app.get("/", response_class=HTMLResponse)
def read_root():
    """Serve the main page"""
    return HTMLResponse(content=HTML_CONTENT)

# For local development with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
