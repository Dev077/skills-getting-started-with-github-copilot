def test_get_activities_returns_activity_map(client):
    response = client.get("/activities")

    assert response.status_code == 200

    payload = response.json()
    assert isinstance(payload, dict)
    assert payload


def test_activity_entries_include_expected_fields(client):
    response = client.get("/activities")
    payload = response.json()

    for _, details in payload.items():
        assert "description" in details
        assert "schedule" in details
        assert "max_participants" in details
        assert "participants" in details
        assert isinstance(details["participants"], list)
