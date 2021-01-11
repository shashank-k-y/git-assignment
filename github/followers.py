import requests


def display_followers():
    username = input("Enter user name :")
    print('-'*50)
    print("Followers details")
    print('-'*50)

    url = f"https://api.github.com/users/{username}/followers"
    user_data = requests.get(url).json()

    for i in user_data:
        follow = i
        print("name: ", follow['login'])
        print("id: ", follow['id'])
        print("url: ", follow['html_url'])
        print('-'*50)


display_followers()
