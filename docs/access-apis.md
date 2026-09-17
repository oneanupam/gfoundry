# Accessing Cloud APIs

You can access Cloud APIs using client libraries available for many popular programming languages While you can use Google Cloud APIs directly by making raw requests to the server, client libraries provide simplifications that significantly reduce the amount of code you need to write.

1. Cloud Client Libraries are the recommended option for accessing Cloud APIs programmatically, where available. Cloud Client Libraries use the latest client library model.
   [NEW - Recommended Way] https://github.com/googleapis/google-cloud-python

2. A few Google Cloud APIs don't have Cloud Client Libraries available in all languages. If you want to use one of these APIs and there is no Cloud Client Library for your preferred language, you can still use the previous style of client library, called Google API Client Libraries.
   [OLD - Not Recommended] https://github.com/googleapis/google-api-python-client

**Note:** It is recommended to use Cloud Client Libraries for Python, where possible, for new code development due to the following reasons:

With Cloud Client Libraries for Python:

- There is a separate client library for each API, so you can choose which client libraries to download. Whereas, google-api-python-client is a single client library for all APIs. As a result, the total package size for google-api-python-client exceeds 50MB.
- There are stricter controls for breaking changes to the underlying APIs as each client library is focused on a specific API.
- There are more features in these Cloud Client Libraries as each library is focused on a specific API, and in some cases, the libraries are owned by team who specialized in that API.

## References

- https://cloud.google.com/python/docs/setup
- https://cloud.google.com/apis/docs/overview
- https://cloud.google.com/apis/docs/client-libraries-explained
- https://cloud.google.com/apis/docs/cloud-client-libraries
- [NEW] https://cloud.google.com/python/docs/reference
- [OLD] https://developers.google.com/api-client-library/
- https://cloud.google.com/docs/samples
- https://cloud.google.com/compute/docs/samples
- https://github.com/googleapis/google-cloud-python
- https://github.com/googleapis/python-compute
- https://github.com/GoogleCloudPlatform/python-docs-samples
