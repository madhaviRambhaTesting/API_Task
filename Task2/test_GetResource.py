import pytest
import requests

base_url = "https://jsonplaceholder.typicode.com"

#Creating JSON-Data
resources = {
    "/posts/1": ["userId", "id", "title", "body"],
    "/comments/1": ["postId", "id", "name", "email", "body"],
    "/albums/1": ["userId", "id", "title"],
    "/photos/1": ["albumId", "id", "title", "url", "thumbnailUrl"],
    "/todos/1": ["userId", "id", "title", "completed"],
    "/users/1": ["id", "name", "username", "email", "address", "phone", "website", "company"]
}

test_data = list(resources.items())

# Write testcase to pass test cases
@pytest.mark.parametrize("endpoint, expected_fields", test_data)
def test_endpoint(endpoint, expected_fields):
    url = base_url + endpoint
    response = requests.get(url)

    assert response.status_code == 200, f"Status code: {response.status_code}"

    data = response.json()
    missing_fields = [field for field in expected_fields if field not in data]

    assert not missing_fields, f" Missing fields: {', '.join(missing_fields)}"
