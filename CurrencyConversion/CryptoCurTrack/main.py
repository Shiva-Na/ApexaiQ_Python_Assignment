from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routes import router


class AppFactory:
    """Create and configure FastAPI app."""

    def create(self):
        app = FastAPI(title="Crypto Price Tracker")
        app.include_router(router)
        app.mount("/static", StaticFiles(directory="static"), name="static")

        @app.get("/")
        def home():
            """Serve main HTML page."""
            return FileResponse("templates/index.html")

        return app


app = AppFactory().create()