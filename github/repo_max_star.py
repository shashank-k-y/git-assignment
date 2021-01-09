import base64
from github import Github
from pprint import pprint
username = "SachinNegali"
g = Github("784e6f4f11259bc22f3e14e93fd1b352279379b6")
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

    print("="*10)
maxstar = max(list1, key=list1.get)
print("the repo with maximum star count is ", maxstar)
