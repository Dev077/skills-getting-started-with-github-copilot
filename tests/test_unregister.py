def test_unregister_removes_participant_from_activity(client):
    email = "alex@mergington.edu"

    response = client.delete(
        "/activities/Basketball/participants",
        params={"email": email},
    )

    assert response.status_code == 200
    assert response.json() == {"message": f"Removed {email} from Basketball"}

    activities = client.get("/activities").json()
    assert email not in activities["Basketball"]["participants"]


def test_unregister_unknown_participant_returns_404(client):
    response = client.delete(
        "/activities/Basketball/participants",
        params={"email": "notfound@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found"


def test_unregister_unknown_activity_returns_404(client):
    response = client.delete(
        "/activities/Unknown Activity/participants",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
