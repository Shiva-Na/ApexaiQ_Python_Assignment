from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routes import router


class AppFactory:
    def create(self):
        app = FastAPI(title="Public Holiday Calendar API")

        app.include_router(router)

        app.mount("/static", StaticFiles(directory="static"), name="static")

        @app.get("/")
        def home():
            return FileResponse("templates/index.html")

        return app


app = AppFactory().create()