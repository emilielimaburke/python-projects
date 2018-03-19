## pip3 install PyGithub

import os
from github import Github
from github import Repository
import pandas as pd
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

AUTHKEY = os.environ['GITHUB_TOKEN']
g1 = Github(AUTHKEY)

repo = g1.get_repo('fishtown-analytics/dbt-utils')

collaborators = repo.get_collaborators()
collaborators_list = []
for collaborator in collaborators:
	collaborators_list.append(collaborator)

df = pd.DataFrame(collaborators_list)

print(df)