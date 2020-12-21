# flows/my_flow.py

from prefect import task, Flow
from prefect.executors.dask import DaskExecutor
from prefect.storage import GitHub
from prefect.environments import DaskKubernetesEnvironment

@task
def get_data():
    return [1, 2, 3, 4, 5]

@task
def print_data(data):
    print(data)

env = DaskKubernetesEnvironment()
with Flow("file-based-flow", environment=env) as flow:
    data = get_data()
    print_data(data)

flow.storage = GitHub(
    repo="pheadra/prefect",                 # name of repo
    path="flows/my_flow.py",       # location of flow file in repo
    ref="main"
)
