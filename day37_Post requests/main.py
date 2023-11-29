import requests
import datetime as dt

USERNAME = "mainak"
TOKEN = "MainakPixela"
GRAPH_ID = "nofap"
now = dt.datetime.now()
quantity = input("How many times did you fap yesterday? ")
pixel_header = {
    "X-USER-TOKEN": TOKEN
}

pixela_endpoint = "https://pixe.la/v1/users"
pixela_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=pixela_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_parameters = {
    "id": GRAPH_ID,
    "name": "No Fap Chart",
    "unit": "Number",
    "type": "int",
    "color": "kuro"
}

# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=pixel_header)
# print(response.text)

pixel_post_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_post_parameters = {
    "date": now.strftime("%Y%m%d"),
    "quantity": quantity,
}
# response = requests.post(url=pixel_post_endpoint, json=pixel_post_parameters, headers=pixel_header)
# print(response.text)

pixel_put_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{now.strftime('%Y%m%d')}"
pixel_put_parameters = {
    "quantity": quantity,
}
# response = requests.put(url=pixel_put_endpoint, json=pixel_put_parameters, headers=pixel_header)
# print(response.text)

pixel_delete_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{now.strftime('%Y%m%d')}"

# response = requests.delete(url=pixel_delete_endpoint, headers=pixel_header)
# print(response.text)

response = requests.get(url=pixel_delete_endpoint, headers=pixel_header)
print(response.text)
