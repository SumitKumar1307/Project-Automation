from github import Github
import sys

project_name = sys.argv[1]
g = Github("access_token")
user = g.get_user()
user.create_repo(project_name)