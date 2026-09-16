# GFoundry

GFoundry is a collection of Python utilities for routine Google Cloud Platform operations. The scripts are designed to support everyday tasks such as resource discovery, auditing, and administrative automation.

## Prerequisites

### Software Requirements

Install the required tools before contributing to this project:

- [Python 3](https://www.python.org/downloads/) >= 3.14.6
- [pip](https://pypi.org/project/pip/) >= 26.1.2
- [pre-commit](https://pre-commit.com/) >= 4.2.0

```bash
# Upgrade pip before installing project dependencies
python -m pip install --upgrade pip
```

> [!NOTE]
> To confirm your environment, run `python3 --version` or `python --version`, and `pip3 --version` or `pip --version`. See the [Python download page](https://www.python.org/downloads/) for installation instructions.

### Set Up a Virtual Environment

It is recommended to create an isolated virtual environment for this project to avoid dependency conflicts with other Python projects.

```bash
# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Windows
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

> [!NOTE]
> Activating the virtual environment updates your shell PATH so `python` and `pip` point to the environment for the current session. To leave the environment, run `deactivate`. Follow the [google article](https://cloud.google.com/python/docs/setup) to setup your Python development environment.

## Quick Start

If you want to quickly run and test the Python scripts without installing Python locally, the recommended approach is to use Cloud Shell.

Cloud Shell is a Compute Engine virtual machine with automatically provisioned service credentials, so there is no need to download or configure a service account key manually.

The Cloud Shell terminal comes preloaded with common tools and utilities, including Python, the `gcloud` CLI, `kubectl`, and more, helping you get started with minimal setup.

- [x] **Step 01:** Activate Cloud Shell from the Google Cloud Console.
- [x] **Step 02:** Clone this repository: `git clone https://github.com/oneanupam/gfoundry.git`
- [x] **Step 03:** Set up the Python virtual environment using [Set Up a Virtual Environment](#set-up-a-virtual-environment).

### Authentication and Authorization

This client library used in the python script supports authentication via Google Application Default Credentials, or by providing a JSON key file for a Service Account. Google Application Default Credentials (ADC) is the recommended way to authorize and authenticate clients.

## Run pre-commit
This repository already includes a `.pre-commit-config.yaml`. Run the following commands to install the hooks locally:

```bash
python -m pip install pre-commit
pre-commit install
pre-commit validate-config
```

This installs the hook into `.git/hooks/pre-commit`. Once installed, pre-commit runs automatically when you commit changes. By default, it checks only the files included in the commit.

To run all hooks manually, use:

```bash
pre-commit run --all-files
pre-commit run <hook_id>
```

## Contributing

Contributions and suggestions are welcome. Before opening an issue or pull request:

1. Review the [contribution guidelines](CONTRIBUTING.md).
2. Install the pre-commit hooks and run them against your changes.
3. Open an issue for bugs or ideas, or submit a pull request with a clear description of the change.

## License

This repository is under MIT License.

## References

- https://cloud.google.com/python/docs/setup
- [NEW] https://cloud.google.com/python/docs/reference
- [OLD] https://developers.google.com/api-client-library/
- https://cloud.google.com/docs/samples
