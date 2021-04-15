#!/bin/python

from github import Github
import sys
from decouple import config

token = config("TOKEN")

project_name = sys.argv[1]
try:
    g = Github(token)
    user = g.get_user()
    if project_name == "1":
        print(user.login)
    else:
        user.create_repo(project_name)
except:
    print("We are sorry, but it seems like something went wrong!"+
    "\nFew tips for troubleshooting:\n1. Make Sure That You Have Entered The Correct Token, If not then re-run ./config\n"+
    "2. Make sure that a repository with the name of your project does not already exists!\n"+
    "3. Run ./config and enter your token if you haven't already done that.")