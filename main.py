import requests
import datetime
import random


pixela_endp = "https://pixe.la/v1/users"
# # username must be between 1 and 32 
# # characters and be all lower case
# USERNAME = "YOUR USERNAME"
# # token must be between 8 and 128 long
# TOKEN = "YOUR SELF GENERATED TOKEN"
# GRAPH_ID = "YOUR GRAPH ID"
USERNAME = "testhabittracker"
TOKEN = "testHabitTracker"
GRAPH_ID = "graph1"

# passing the token via headers
headers = {
    "X-USER-TOKEN": TOKEN
}


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# # create a user account - only needs to be run once
# pixela_response = requests.post(url=pixela_endp, 
#                                 json=user_params
# )
# # # to test for connection issues
# # print(pixela_response.text)

graph_endp = f"{pixela_endp}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

# # create a graph - only needs to be run once
# graph_response = requests.post(url=graph_endp,
#                                 json=graph_config,
#                                 headers=headers
# )
# print(graph_response.text)

today = datetime.datetime.now()   
today_str = today.strftime("%Y%m%d")
# print(f"today_str: {today_str}")

# today_str = "20220518"
post_pixel_params = {
    # yyyyMMdd format
    "date": today_str,
    # Validation rule: int^-?[0-9]+ float^-?[0-9]+.[0-9]+
    "quantity": "99"
}

post_pixel_endp = f"{pixela_endp}/{USERNAME}/graphs/{GRAPH_ID}"
post_pixel_response = requests.post(url=post_pixel_endp,
                                    json=post_pixel_params,
                                    headers=headers
)
# print(f"post_pixel_response:\n{post_pixel_response.text}")














