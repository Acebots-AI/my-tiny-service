def test_timestamp(client: starlette.testclient.TestClient) -> None:
    """
    Test that the timestamp endpoint returns a 200 status code and the correct format.
    """
    response = client.get("/timestamp")
    assert response.status_code == 200
    # Check if the response is in ISO format
    try:
        datetime.fromisoformat(response.json())
        is_iso_format = True
    except ValueError:
        is_iso_format = False
    assert is_iso_format, "The timestamp is not in ISO format"
