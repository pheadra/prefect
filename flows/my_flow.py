# flows/my_flow.py

from prefect import task, Flow
from prefect.executors.dask import DaskExecutor
from prefect.storage import GitHub
from prefect.run_configs import KubernetesRun


@task
def get_data():
    return [1, 2, 3, 4, 5]


@task
def print_data(data):
    print(data)


with Flow("file-based-flow",
          executor=DaskExecutor("tcp://dask-scheduler:8786"),
          run_config=KubernetesRun(),
          storage=GitHub(
                  repo="pheadra/prefect",  # name of repo
                  path="flows/my_flow.py",  # location of flow file in repo
                  ref="main"
          )) as flow:
    data = get_data()
    print_data(data)
