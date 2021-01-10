import requests
from github import Github
from pprint import pprint
import json


def follower_count():
    g = Github()

    username = input("Enter the user name :")
    print('-'*50)
    print(f"Followers of {username} are :")
    print('-'*50)
    url = f"https://api.github.com/users/{username}/followers"
    user_data = requests.get(url).json()

    list1 = {}
    for i in user_data:
        count = 0
        folower = i
        folower_url = folower["followers_url"]
        foll_name = folower["login"]
        print(foll_name)

        follower_data = requests.get(folower_url).json()
        for fol in follower_data:
            user = fol
            name = user["login"]
            count += 1
        list1[foll_name] = count

    print(list1)
    print('-'*50)
    maxfollower = max(list1, key=list1.get)
    print("the follower with maximum follower count is : ", maxfollower)

# pprint(folower_data)
# fol_count(fol)
    print("-"*50)


follower_count()
