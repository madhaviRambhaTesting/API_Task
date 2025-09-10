import pytest
import requests
base_url = "https://jsonplaceholder.typicode.com"

endpoints=["/posts", "/comments"]
new_resource_data = {
    "title": "My new post",
    "body": "This is the body of the post.",
    "userId": 1
}
@pytest.mark.parametrize("endpoint",endpoints)
def test_createresource(endpoint):
    url=base_url+endpoint
    response=requests.post(url,json=new_resource_data)
    assert response.status_code== 201
    print(f"Data Created successfully at endpoint {endpoint}")
    data=response.json()
    print(data)



