import base64
from github import Github
from pprint import pprint
username = "SachinNegali"
g = Github("784e6f4f11259bc22f3e14e93fd1b352279379b6")
user = g.get_user(username)
count = 0

# function to display repositories of an user

print(user)
