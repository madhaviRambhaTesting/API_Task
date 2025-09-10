import requests

base_url='https://jsonplaceholder.typicode.com'

endpoint=["/posts", "/comments","/albums","/photos","/todos","/users"]

for endpoint in endpoint:
    url=base_url+endpoint
    response=requests.get(url)
    data=response.json()
    if response.status_code==200:
        data=response.json()
        print(f"{endpoint}:{len(data)}")
    else:
        print(f"failed fetch{endpoint}:Status Code{response.status_code}")