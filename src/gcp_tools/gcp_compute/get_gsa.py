"""This module gets the list of all the Google Service Accounts in a google cloud project."""

# # Standard library imports
# import argparse

# # Third party packages
# from google.cloud import iam_admin_v1


# def get_gsa_list(client, project_id: str = "extended-ward-500913-i6") -> list[str]:
def get_gsa_list(client, project_id: str) -> list[str]:
    """Function to get the list of of the google service accounts in a project.

    Args:
        project_id (str): the id of the gcp project.

    Returns:
        list[str]: the list of the service account in the supplied project.
    """
    gsa_list = []
    response = client.list_service_accounts(request={"name": f"projects/{project_id}"})

    for result in response.accounts:
        # print(f"Service Account: {result.email}, Display Name: {result.display_name}")
        gsa_list.append(result.email)
    return gsa_list


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(
#         prog="Get GSA",
#         description="This utility lists the service accounts in a project.",
#         epilog="Thank you for using the utility.",
#     )
#     parser.add_argument(
#         "project_id", type=str, help="The id of the google cloud project"
#     )
#     args = parser.parse_args()

#     client = iam_admin_v1.IAMClient()
#     print(f"List of GSAs: {get_gsa_list(client, args.project_id)}")
