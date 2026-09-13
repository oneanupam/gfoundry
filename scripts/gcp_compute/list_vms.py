from google.cloud import compute_v1


def list_vms(project_id, instance_zone):
    """Prints all the google compute instances of a project"""

    # Empty list to store instance names
    instance_names = []

    # Create a client
    client = compute_v1.InstancesClient()

    # Initialize request argument(s)
    request = compute_v1.ListInstancesRequest(
        project=project_id,
        zone=instance_zone,
    )

    # Make the request
    page_result = client.list(request=request)

    # Handle the response
    for response in page_result:
        print(response.name)
        instance_names.append(response.name)

    return instance_names


if __name__ == "__main__":
    project_id = "tidal-outlook-488409-e6"
    instance_zone = "us-central1-c"
    list_vms(project_id, instance_zone)
