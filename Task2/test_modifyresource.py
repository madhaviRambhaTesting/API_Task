import pytest
import requests

base_url = "https://jsonplaceholder.typicode.com"

# creating data
new_data={
    "title":"modifiying new title",
}
endpoint = ["/posts/1", "/comments/1", "/albums/1", "/photos/1", "/todos/1", "/users/1"]
@pytest.mark.parametrize("endpoint", endpoint)
def test_modifyresource(endpoint):


    url = base_url + endpoint
    response = requests.patch(url,json=new_data)
    assert response.status_code == 200
    print("Data modified successfully")

    data=response.json()
    for key,value in data.items():
        assert data[key] == value
    print("Response data modified successfully")
    print(data)
if __name__=="__main__":
    test_modifyresource()
