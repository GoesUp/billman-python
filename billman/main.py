from fastapi import FastAPI
import uvicorn
from billman.base.base import router as base_router
from fastapi.middleware.cors import CORSMiddleware


def run() -> None:
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(base_router)
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")


if __name__ == '__main__':
    run()
