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
    secrets=["d770e6ba2de8df0777df22d935a0a13aaa9ea0ed"]  # name of personal access token secret
)
 
      
