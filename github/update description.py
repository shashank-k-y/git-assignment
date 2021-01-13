from github import Github
import requests

g = Github("8b7cdf9c009165536a798548f961e9f5f6fb0935")

reponame = str(input("Enter the repository name : "))

f = g.get_user().get_repo(reponame)
desc = str(input("Enter the description of the repository :"))
print("name of the repository :", f.name)
print("description: ", f.description)
f.edit(description=desc)

# to see all the available attributes and methods
print("updated description: ", f.description)
