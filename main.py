from fastapi import FastAPI
from routes import init_routes

app = FastAPI()

init_routes(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
