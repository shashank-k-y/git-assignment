from github import Github


def display_repos():
    username = input("Enter the user name: ")
    print('-'*50)
    print("Repo details")
    print('-'*50)

    g = Github()
    user = g.get_user(username)
    count = 0

    for repo in user.get_repos():
        print("Full name:", repo.name)
        print("Description:", repo.description)
        print("Date created:", repo.created_at)
        print("Date of last push:", repo.pushed_at)
        print("Home Page:", repo.homepage)
        print("Language:", repo.language)
        print("Number of forks:", repo.forks)
        print("Number of stars:", repo.stargazers_count)
        print("-"*50)
        count += 1

    print('total repos :', count)


display_repos()
