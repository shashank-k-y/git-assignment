import requests
from github import Github
from pprint import pprint
import json
g = Github("shashank-k-y", "shashank.sky.8@gmail.com")
username = "shashank-k-y"
url = f"https://api.github.com/users/{username}/followers"
user_data = requests.get(url).json()
print(user_data)
# count = 0
# followers_count = {}
# for i in user_data:
#     folow_url = i['followers_url']
#     for j in folow_url:
#         followers_details = requests.get(folow_url).json()
#         count += 1
#     pprint(count)
