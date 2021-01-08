import base64
from github import Github
from pprint import pprint
username = "shashank-k-y"
g = Github()
user = g.get_user(username)


# function to display repositories of an user


def print_repo(repo):
    count = 0

    print("Full name:", repo.full_name)
    # repository description
    print("Description:", repo.description)
    # the date of when the repo was created
    print("Date created:", repo.created_at)
    # the date of the last git push
    print("Date of last push:", repo.pushed_at)
    # home website (if available)
    print("Home Page:", repo.homepage)
    # programming language
    print("Language:", repo.language)
    # number of forks
    print("Number of forks:", repo.forks)
    # number of stars
    print("Number of stars:", repo.stargazers_count)
    print("-"*50)
    # repository content (files & directories)
    print("Contents:")
    count += 1
    print(count)


for repo in user.get_repos():

    print_repo(repo)
    print("="*10)
