import pytest
import requests

base_url = "https://jsonplaceholder.typicode.com"

endpoint = ["/posts/1", "/comments/1", "/albums/1", "/photos/1", "/todos/1", "/users/1"]
@pytest.mark.parametrize("endpoint", endpoint)
def test_Deleteresource(endpoint):


    url = base_url + endpoint
    response = requests.delete(url)
    assert response.status_code in [200,204]
    print("Deleted successfully")

    data=response.json()
    if response.status_code == 200:
        assert data== {}, f"expected Empty but got {response.status_code}"
        print("Data Deleted successfully")
    elif response.status_code == 204:
        print("Data Deleted successfully")

if __name__=="__main__":
    test_Deleteresource()
