
@router.get("/timestamp")
async def get_current_timestamp():
    """
    Returns the current timestamp in ISO format.
    """
    return datetime.now().isoformat()
