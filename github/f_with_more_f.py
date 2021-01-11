import requests


def follower_count():

    username = input("Enter the user name :")
    print('-'*50)
    print(f"Followers of {username} are :")
    print('-'*50)
    url = f"https://api.github.com/users/{username}/followers"
    user_data = requests.get(url).json()

    list1 = {}
    for i in user_data:
        folower_url = i["followers_url"]
        foll_name = i["login"]
        print(foll_name)

        follower_data = requests.get(folower_url).json()
        followers_count = len(follower_data)
        list1[foll_name] = followers_count

    print(list1)
    print('-'*50)
    maxfollower = max(list1, key=list1.get)
    print("the follower with maximum follower count is : ", maxfollower)


follower_count()
