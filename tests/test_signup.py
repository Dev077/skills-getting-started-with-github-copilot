def test_signup_adds_participant_to_activity(client):
    email = "newstudent@mergington.edu"

    response = client.post(
        "/activities/Chess Club/signup",
        params={"email": email},
    )

    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for Chess Club"}

    activities = client.get("/activities").json()
    assert email in activities["Chess Club"]["participants"]


def test_signup_duplicate_participant_returns_400(client):
    existing_email = "michael@mergington.edu"

    response = client.post(
        "/activities/Chess Club/signup",
        params={"email": existing_email},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up"


def test_signup_unknown_activity_returns_404(client):
    response = client.post(
        "/activities/Unknown Activity/signup",
        params={"email": "someone@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
