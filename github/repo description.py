import base64
from github import Github
from pprint import pprint


def display_description():
    username = input("Enter the user name: ")

    g = Github()
    user = g.get_user(username)
    count = 0

    def print_repo(repo):

        print("Full name:", repo.name)
        print("Description:", repo.description)

    for repo in user.get_repos():
        count += 1
        print_repo(repo)

    print('total repos :', count)


display_description()
