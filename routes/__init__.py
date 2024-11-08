from fastapi import FastAPI

from routes.import_file import router as files

def init_routes(app: FastAPI):
    app.include_router(files)