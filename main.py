from fastapi import FastAPI

import app.routes.file_routes
from app.routes import init_routes

app = FastAPI()

init_routes(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
