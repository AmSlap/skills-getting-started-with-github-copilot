def test_get_activities_returns_seeded_data(client):
    # Arrange
    expected_activity = "Chess Club"
    expected_participant = "michael@mergington.edu"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert expected_activity in payload
    assert expected_participant in payload[expected_activity]["participants"]


def test_get_activities_has_expected_structure(client):
    # Arrange
    required_keys = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    for activity_name, details in payload.items():
        assert activity_name
        assert required_keys.issubset(details.keys())
        assert isinstance(details["participants"], list)
