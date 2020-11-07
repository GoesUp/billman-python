from fastapi import FastAPI
import uvicorn
from billman.base.base import router as base_router


def run() -> None:
    app = FastAPI()
    app.include_router(base_router)
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")


if __name__ == '__main__':
    run()
