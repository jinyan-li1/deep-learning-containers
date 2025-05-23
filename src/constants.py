"""
Copyright 2019-2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License"). You
may not use this file except in compliance with the License. A copy of
the License is located at

    http://aws.amazon.com/apache2.0/

or in the "license" file accompanying this file. This file is
distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
ANY KIND, either express or implied. See the License for the specific
language governing permissions and limitations under the License.
"""

import os

# Environment settings
FRAMEWORKS = {
    "mxnet",
    "tensorflow",
    "pytorch",
    "huggingface_tensorflow",
    "huggingface_pytorch",
    "autogluon",
    "stabilityai_pytorch",
    "base",
}
DEVICE_TYPES = {"cpu", "gpu", "hpu", "eia", "inf", "neuron", "neuronx"}
IMAGE_TYPES = {"training", "inference"}
PYTHON_VERSIONS = {"py2", "py3", "py36"}
ALL = "all"

# Function Status Codes
SUCCESS = 0
FAIL = 1
NOT_BUILT = -1
FAIL_IMAGE_SIZE_LIMIT = 2

# Left and right padding between text and margins in output
PADDING = 1

# Docker build stages
PRE_PUSH_STAGE = "pre_push"
COMMON_STAGE = "common"

# Docker connections
DOCKER_URL = "unix://var/run/docker.sock"

STATUS_MESSAGE = {
    SUCCESS: "Success",
    FAIL: "Failed",
    NOT_BUILT: "Not Built",
    FAIL_IMAGE_SIZE_LIMIT: "Build with invalid image size",
}

BUILD_CONTEXT = os.environ.get("BUILD_CONTEXT", "DEV")

METRICS_NAMESPACE = "dlc-metrics"

# Logging level
INFO = 1
ERROR = 2
DEBUG = 3

# Repository prefix
MAINLINE_REPO_PREFIX = "beta-"
NIGHTLY_REPO_PREFIX = "nightly-"
PR_REPO_PREFIX = "pr-"
AUTOPATCH_REPO_PREFIX = "autopatch-"

# Env variables for the code build PR jobs
JOB_FRAMEWORK = os.environ.get("FRAMEWORK")
JOB_FRAMEWORK_VERSION = os.environ.get("VERSION")

# Test environment file
TEST_ENV_PATH = os.path.join(os.path.expanduser("~"), "testenv.json")
# Test images for all test types (sm,ecs,eks,ec2) to pass on to code build jobs
TEST_TYPE_IMAGES_PATH = os.path.join(os.path.expanduser("~"), "test_type_images.json")

# Types of binary links accepted:
LINK_TYPE = ["s3", "pypi"]

ARTIFACT_DOWNLOAD_PATH = os.path.join(os.sep, "docker", "build_artifacts")

# Test types for running code build test jobs
SAGEMAKER_REMOTE_TESTS = "sagemaker"
SAGEMAKER_EFA_TESTS = "sagemaker-efa"
SAGEMAKER_RC_TESTS = "sagemaker-rc"
SAGEMAKER_BENCHMARK_TESTS = "sagemaker-benchmark"
SANITY_TESTS = "sanity"
SECURITY_TESTS = "security"
EC2_TESTS = "ec2"
EC2_BENCHMARK_TESTS = "ec2-benchmark"
ECS_TESTS = "ecs"
EKS_TESTS = "eks"
ALL_TESTS = ["sagemaker", "ec2", "eks", "ecs"]

# Timeout in seconds for Docker API client.
API_CLIENT_TIMEOUT = 600
MAX_WORKER_COUNT_FOR_PUSHING_IMAGES = 3

PATCHING_INFO_PATH_WITHIN_DLC = "/opt/aws/dlc/patching-info"

## TODO: Make this account specific: pr-creation-data-helper-<12_digit_account_id>
PR_CREATION_DATA_HELPER_BUCKET = "pr-creation-data-helper"

PUBLIC_DLC_REGISTRY = "763104351884"
