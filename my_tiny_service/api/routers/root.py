import fastapi
from my_tiny_service.api.dependencies import get_api_settings
from my_tiny_service.api.settings import ApiSettings
from datetime import datetime

router = fastapi.APIRouter()

def get_root(
    api_settings: ApiSettings = fastapi.Depends(
        get_api_settings
    ),
) -> str
"""Root endpoint.

    Example of simple endpoint that returns a string. This endpoint is used by
    the Kubernetes healthcheck and must be present. The returned content does
    not matter.
    """

@router.get("/timestamp")
def get_current_timestamp() -> str:
    """Endpoint to return the current timestamp in ISO format."""
    return datetime.now().isoformat()