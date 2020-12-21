from prefect import task
from prefect import Flow
from prefect.executors import DaskExecutor
from prefect.run_configs import KubernetesRun


@task
def say_hello():
    print("Hello, world!")

with Flow("Say hi!") as flow:
    say_hello()

flow.run_config = KubernetesRun()
flow.executor = DaskExecutor("tcp://dask-scheduler:8786")
