# flows/my_flow.py

from prefect import task, Flow
from prefect.storage import GitHub

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
    secrets=["593846ce1231c0a7075b8d295ae3ae44448136a7"]  # name of personal access token secret
)
 
      
