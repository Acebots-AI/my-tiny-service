from datetime import datetime
from datetime import datetime
import fastapi

from my_tiny_service.api.dependencies import get_api_settings
from my_tiny_service.api.settings import ApiSettings

router = fastapi.APIRouter()


@router.get("/", summary="Root endpoint, can be used to see if API is up")
def get_root(
    api_settings: ApiSettings = fastapi.Depends(
        get_api_settings
    ),
) -> str:
    """Root endpoint.

    Example of simple endpoint that returns a string. This endpoint is used by
    the Kubernetes healthcheck and must be present. The returned content does
    not matter.
    """
    return f"{api_settings.title}, version {api_settings.version}"

@router.get("/timestamp")
def get_timestamp() -> str:
    """Endpoint to return the current timestamp in ISO format.
    """
    current_time = datetime.now().isoformat()
    return current_time

@router.get("/timestamp", response_model=str)
def timestamp() -> str:
    return get_timestamp()