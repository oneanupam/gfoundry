"""This sample code demosnstrates how to list all the VPC networks
in a given GCP project using the google cloud python sdk.
"""

# Standard library imports
import os

# Third party imports
from google.cloud import compute_v1


def logger(func):

    def wrapper(project_id, client):
        print(f"[INFO]: function {func.__name__} execution started...")
        result = func(project_id, client)
        print("[INFO]: function execution completed.")
        return result

    return wrapper


def list_vpc_networks(project_id: str, client) -> list:
    """This functions lists all the VPC networks in a given gcp project.

    Args:
        project_id (str): the id of the project to list the networks from.

    Returns:
        list: a list of VPC network names.
    """
    network_name_list = []
    response = client.list(project=project_id)
    for network in response:
        network_name_list.append(network.name)
    return network_name_list


GCP_PROJECT_ID = "extended-ward-500913-i6"
client = compute_v1.NetworksClient()
list_vpc_networks = logger(list_vpc_networks)
print(list_vpc_networks(GCP_PROJECT_ID, client))

# if __name__ == "__main__":
#     client = compute_v1.NetworksClient()
#     GCP_PROJECT_ID = "extended-ward-500913-i6"
#     print(f"List of networks: {logger(list_vpc_networks(GCP_PROJECT_ID, client))}")
