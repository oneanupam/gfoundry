"""Module for retrieving Google Service Accounts from a GCP project.

This module provides functionality to list all service accounts in a given
Google Cloud Platform (GCP) project using the Google Cloud IAM Admin API.
"""

import logging
from typing import List

from google.cloud import iam_admin_v1
from google.api_core import exceptions

# Module-level logger following Python best practices
logger = logging.getLogger(__name__)

# Constants (if needed)
DEFAULT_PROJECT_TEMPLATE = "projects/{}"


def get_gsa_list(
    client: iam_admin_v1.IAMClient,
    project_id: str,
) -> List[str]:
    """Retrieve all Google Service Accounts in a GCP project.

    Lists all service accounts available in the specified Google Cloud
    Platform project. This function is a thin wrapper around the GCP
    IAM Admin API.

    Args:
        client: An initialized IAMClient instance for making API calls.
        project_id: The ID of the Google Cloud Platform project.

    Returns:
        A list of service account email addresses.

    Raises:
        google.api_core.exceptions.NotFound: If the project doesn't exist.
        google.api_core.exceptions.PermissionDenied: If lacking permissions.
        google.api_core.exceptions.GoogleAPICallError: On API errors.

    Example:
        >>> from google.cloud import iam_admin_v1
        >>> client = iam_admin_v1.IAMClient()
        >>> accounts = get_gsa_list(client, "my-project-id")
        >>> print(accounts)
        ['sa1@my-project-id.iam.gserviceaccount.com', ...]
    """
    # DEBUG: Function entry point with parameters
    logger.debug(f"Fetching service accounts for project: {project_id}")

    gsa_list: list[str] = []

    try:
        # DEBUG: API call details
        logger.debug(f"Calling IAM API: list_service_accounts(projects/{project_id})")

        # Make API request
        response = client.list_service_accounts(
            request={"name": DEFAULT_PROJECT_TEMPLATE.format(project_id)}
        )

        # Process response
        for account in response.accounts:
            logger.debug(f"Found service account: {account.email}")
            gsa_list.append(account.email)

        # INFO: Operation result (what matters to users)
        logger.info(
            f"Retrieved {len(gsa_list)} service accounts from project {project_id}"
        )

    except exceptions.NotFound:
        logger.error(f"Project '{project_id}' not found or does not exist")
        raise

    except exceptions.PermissionDenied:
        logger.error(
            f"Permission denied: Unable to list service accounts in {project_id}"
        )
        raise

    except exceptions.GoogleAPICallError as e:
        logger.error(f"GCP API error while listing service accounts: {str(e)}")
        raise

    except Exception as e:
        logger.error(
            f"Unexpected error while listing service accounts: {str(e)}", exc_info=True
        )
        raise

    return gsa_list


def main() -> None:
    """CLI entry point for testing (when running module directly).

    This allows the module to be executed directly for testing:
        python -m gcp_tools.gcp_compute.get_gsa
    """
    import sys

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    if len(sys.argv) < 2:
        print("Usage: python -m gcp_tools.gcp_compute.get_gsa <project_id>")
        sys.exit(1)

    project_id = sys.argv[1]

    try:
        client = iam_admin_v1.IAMClient()
        accounts = get_gsa_list(client, project_id)
        print(f"\nService Accounts in {project_id}:")
        for account in accounts:
            print(f"  - {account}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
