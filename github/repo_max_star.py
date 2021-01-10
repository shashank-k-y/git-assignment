import base64
from github import Github
from pprint import pprint


def max_stars():
    username = input("Enter the user name :")
    g = Github()
    user = g.get_user(username)

    count = 0

    # function to display repositories of an user
    list1 = {}

    def print_repo(repo):

        print(repo.full_name)
        print("Number of stars:", repo.stargazers_count)
        print("-"*50)

    for repo in user.get_repos():
        list1[repo.name] = repo.stargazers_count
        print_repo(repo)
    maxstar = max(list1, key=list1.get)
    print("the repo with maximum star count is ", maxstar)


max_stars()
