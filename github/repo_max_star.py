from github import Github


def max_stars():
    username = input("Enter the user name :")
    g = Github()
    user = g.get_user(username)
    list1 = {}

    for repo in user.get_repos():
        list1[repo.name] = repo.stargazers_count
        print(repo.full_name)
        print("Number of stars:", repo.stargazers_count)
        print("-"*50)
    maxstar = max(list1, key=list1.get)
    print("the repo with maximum star count is :", maxstar)


max_stars()
