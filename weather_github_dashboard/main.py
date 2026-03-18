from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routes import router


class AppFactory:
    """Create and configure FastAPI app for weather+github dashboard."""

    def create(self):
        app = FastAPI(title="Weather + GitHub Dashboard")
        app.include_router(router)
        app.mount("/static", StaticFiles(directory="static"), name="static")

        @app.get("/")
        def home():
            """Return the main HTML page."""
            return FileResponse("templates/index.html")

        return app


app = AppFactory().create()