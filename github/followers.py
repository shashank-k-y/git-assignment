import requests
from pprint import pprint
import json


def display_followers():
    username = input("Enter user name :")
    print('-'*50)
    print("Followers details")
    print('-'*50)

    url = f"https://api.github.com/users/{username}/followers"
    user_data = requests.get(url).json()

    def disp(follow):
        print("name: ", follow['login'])
        print("id: ", follow['id'])
        print("url: ", follow['html_url'])
        print('-'*20)

    for i in user_data:
        follow = i
        disp(follow)


display_followers()
