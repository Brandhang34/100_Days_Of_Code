import requests
from datetime import datetime

USERNAME = "sushilover"
TOKEN = "kj4h5q3kh5t34ye5rh"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
	"token": TOKEN,
	"username": USERNAME,
	"agreeTermsOfService": "yes",
	"notMinor": "yes",
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config={
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}


#response=requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today=datetime.now().strftime("%Y%m%d")
print(today)

pixel_config = { 
        "date": today,
        "quantity": "4.32"
        }

#response = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=headers)
#print(response.text)

put_pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

put_pixel_config = {
        "quantity": "12.4"
        }

#response = requests.put(url=put_pixel_creation_endpoint, json=put_pixel_config, headers=headers)

#print(response.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

response=requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)


