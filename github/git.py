import base64
from github import Github
username = "shashank-k-y"
password = "shashank.sky.8@gmail.com"

# authenticate to github
g = Github(username, password)
# get the authenticated user
user = g.get_user()
for repo in user.get_repos():
    print_repo(repo)
