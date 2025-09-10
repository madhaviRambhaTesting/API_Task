import requests
import pytest

Base_url = "https://petstore.swagger.io/v2"

def test_post_pet():
    pet_url = f"{Base_url}/pet"
    payload = {
        "id": 12345,
        "category": {
            "id": 1,
            "name": "dog"
        },
        "name": "snoopie",
        "photoUrls": ["string"],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "pending"
    }

    headers = {
        "Content-Type": "application/json"
    }

    #  - Create Pet
    response = requests.post(pet_url, json=payload, headers=headers)
    assert response.status_code == 200, f"POST failed: {response.text}"
    response_data = response.json()
    assert response_data["id"] == payload["id"]

    #  GET - Retrieve Pet
    get_url = f"{pet_url}/12345"
    response = requests.get(get_url)
    assert response.status_code == 200, f" failed: {response.text}"
    assert "application/json" in response.headers["Content-Type"]
    assert response.json()["id"] == 12345

def test_get_pet_by_id():
    pet_url = f"{Base_url}/pet"
    pet_id = 12345
    get_url = f"{pet_url}/{pet_id}"
    response = requests.get(get_url)
    assert response.status_code == 200, f"GET failed: {response.text}"
    response_data = response.json()

    #  Validations
    assert response_data["category"]["name"].lower() == "dog"
    assert response_data["name"].lower() == "snoopie"
    assert response_data["status"].lower() == "pending"

    # Optional  prints
    print("Content-Type:", response.headers["Content-Type"])
    print("Pet name:", response_data["name"])
    print("Successfully posted and verified pet data.")
    print("Testcase2")

