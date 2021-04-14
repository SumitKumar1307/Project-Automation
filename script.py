#!/bin/python

from github import Github
import sys

project_name = sys.argv[1]
g = Github("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")
user = g.get_user()
user.create_repo(project_name)
