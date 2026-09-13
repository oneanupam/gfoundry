"""CLI entry point for GCP Tools."""

import argparse
import sys

from google.cloud import compute_v1, iam_admin_v1

from gcp_tools.gcp_compute.get_gsa import get_gsa_list
from gcp_tools.gcp_compute.get_vpc import list_vpc_networks


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser for the CLI."""
    parser = argparse.ArgumentParser(
        prog="gcp-tools",
        description="GCP Tools - Utilities for Google Cloud Platform operations",
        epilog="For more information, visit the project repository.",
    )

    subparsers = parser.add_subparsers(
        dest="command", required=True, help="Available commands"
    )

    # Subcommand: get-gsa
    gsa_parser = subparsers.add_parser(
        "get-gsa",
        help="List all Google Service Accounts in a GCP project",
    )
    gsa_parser.add_argument(
        "--project-id",
        type=str,
        required=True,
        help="The ID of the Google Cloud project",
    )

    # Subcommand: get-vpc
    vpc_parser = subparsers.add_parser(
        "get-vpc",
        help="List all VPC networks in a GCP project",
    )
    vpc_parser.add_argument(
        "--project-id",
        type=str,
        required=True,
        help="The ID of the Google Cloud project",
    )

    return parser


def main() -> None:
    """Main entry point for the CLI."""
    parser = build_parser()
    args = parser.parse_args()

    try:
        if args.command == "get-gsa":
            client = iam_admin_v1.IAMClient()
            result = get_gsa_list(client, args.project_id)
            print(f"Service Accounts: {result}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        if args.command == "get-vpc":
            client = compute_v1.NetworksClient()
            result = list_vpc_networks(client, args.project_id)
            print(f"VPC Networks in project {result}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
