from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routes import router


class AppFactory:
    """Create and configure FastAPI app for movies."""

    def create(self):
        app = FastAPI(title="Movie Search API")
        app.include_router(router)
        app.mount("/static", StaticFiles(directory="static"), name="static")

        @app.get("/")
        def home():
            """Serve frontend HTML page."""
            return FileResponse("templates/index.html")

        return app


app = AppFactory().create()