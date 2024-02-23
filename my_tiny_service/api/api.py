import fastapi
from starlette.middleware.cors import CORSMiddleware

from my_tiny_service.api.routers import maths, root
from my_tiny_service.api.settings import ApiSettings


import fastapi
from starlette.middleware.cors import CORSMiddleware
from my_tiny_service.api.routers import maths, root, time
from my_tiny_service.api.settings import ApiSettings
def get_api() -> fastapi.FastAPI
"""Create and set up the API.

    Register routers, middleware and similar to get a working API.
    """
    app = fastapi.FastAPI()
    app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
    app.include_router(maths.router)
    app.include_router(root.router)
    app.include_router(time.router)
    return app

