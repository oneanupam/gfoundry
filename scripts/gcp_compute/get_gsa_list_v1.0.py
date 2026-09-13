"""Module for retrieving Google Service Accounts from a GCP project.

This module provides functionality to list all service accounts in a given
Google Cloud Platform (GCP) project using the Google Cloud IAM Admin API.
"""

import json
from pathlib import Path
import yaml
from pprint import pprint

# # Third party packages
# from google.cloud import iam_admin_v1

# # Constants (if needed)
# DEFAULT_PROJECT_TEMPLATE = "projects/{}"


# def get_gsa_list(
#     client,
#     project_id: str,
# ) -> list[str]:
#     """Retrieve all Google Service Accounts in a GCP project.

#     Args:
#         client: An initialized IAMClient instance for making API calls.
#         project_id: The ID of the Google Cloud Platform project.

#     Returns:
#         A list of service account email addresses.

#     Raises:
#         exception, if error occurs.
#     """

#     gsa_list: list[str] = []

#     try:
#         # Make API request
#         response = client.list_service_accounts(
#             request={"name": DEFAULT_PROJECT_TEMPLATE.format(project_id)}
#         )

#         # Process response
#         for account in response.accounts:
#             gsa_list.append(account.email)
#     except Exception as e:
#         print(f"Unexpected error while listing service accounts: {e}")
#         sys.exit(1)

#     return gsa_list


# def get_project(file_name: str) -> str:
# """Retrieve the project ID from a file.

# Args:
#     file_name: The name of the file containing the project ID.

# Returns:
#     The project ID as a string.
# """

# An idiomatic way of working with the current module’s location as the path is using __file__
# You may want to get the parent directory with .parent and you can join multiple paths using .joinpath()
# current_script_path = Path(__file__)
# config_file_path = current_script_path.parent.parent.parent.joinpath(
#     "config", "dev.yaml"
# )

# with open(config_file_path, "r") as reader_obj:
#     data = yaml.safe_load(reader_obj)
#     print(type(data))
#     pprint(data)
#     gcp_project_id = data["dev"]["foundations"]["project_id"]
#     print(gcp_project_id)

# print(yaml.dump(data, sort_keys=False))

current_script_path = Path(__file__)
config_folder = current_script_path.parent.parent.parent.joinpath("config")

# List all files and directories in the config folder using os.scandir()
for entry in os.scandir(config_folder):
    print(entry.name)

# List all files and directories in the config folder using pathlib.Path.iterdir()
for entry in Path(config_folder).iterdir():
    print(entry.name)

# Check if dev.yaml or dev.json exists in the config folder
if Path.exists(config_folder.joinpath("dev.yaml")):
    print("dev.yaml exists")
elif Path.exists(config_folder.joinpath("dev.json")):
    print("dev.json exists")
else:
    print("No config file found")

# PyYAML's safe_load() accepts a stream or string, while Python's built-in json module provides separate APIs for a file-like object and a string.
# Both yaml.safe_load() and json.load() convert data from a file into Python objects. Most commonly, that object is a dict.
# yaml.dump() without a file → returns YAML as a string. yaml.dump() with a file → writes to that file

# current_script_path = Path(__file__)
# config_file_path = current_script_path.parent.parent.parent.joinpath(
#     "config", "dev.json"
# )

# with open(config_file_path, "r") as reader_obj:
#     data = json.load(reader_obj)
#     print(type(data))  # a dict object
#     pprint(data)  # pretty print the dict object
#     gcp_project_id = data.get("dev").get("foundations").get("project_id")
#     print(gcp_project_id)

# # json.dump() writes to a file. json.dumps() returns a string.
# # json.dumps() with sort_keys=False → preserves the order of keys in the dictionary
# print(json.dumps(data, sort_keys=False))


# def main() -> None:
#     """Entry point for testing (when running module directly).

#     This allows the module to be executed directly for testing:
#         python -m gcp_tools.gcp_compute.get_gsa
#     """

#     try:
#         client = iam_admin_v1.IAMClient()
#         accounts = get_gsa_list(client, project_id)
#         print(f"\nService Accounts in {project_id}:")
#         for account in accounts:
#             print(f"  - {account}")
#     except Exception as e:
#         print(f"Error: {e}", file=sys.stderr)
#         sys.exit(1)


# if __name__ == "__main__":
#     main()
