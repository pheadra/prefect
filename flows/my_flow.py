# flows/my_flow.py

from prefect import task, Flow, context
from prefect.storage import GitHub

context.setdefault("secrets", {}) # to make sure context has a secrets attribute
context.secrets["GITHUB_ACCESS_TOKEN"] = "fcfd03a0197716a596505b12d315e097775e2bf9"

@task
def get_data():
    return [1, 2, 3, 4, 5]

@task
def print_data(data):
    print(data)

with Flow("file-based-flow") as flow:
    data = get_data()
    print_data(data)

flow.storage = GitHub(
    repo="pheadra/prefect",                 # name of repo
    path="flows/my_flow.py",        # location of flow file in repo
    secrets=["GITHUB_ACCESS_TOKEN"]  # name of personal access token secret
)
 
      
