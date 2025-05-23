# Copyright 2018-2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.
from __future__ import absolute_import

import os

import pytest
from sagemaker import utils
from sagemaker.pytorch import PyTorch

from ...integration import resources_path, DEFAULT_TIMEOUT
from ...integration.sagemaker.timeout import timeout

from test.test_utils import get_framework_and_version_from_tag, get_cuda_version_from_tag
from packaging.version import Version
from packaging.specifiers import SpecifierSet
from .... import invoke_pytorch_helper_function


DGL_DATA_PATH = os.path.join(resources_path, "dgl-gcn")
DGL_LT_09x_SCRIPT_PATH = os.path.join(DGL_DATA_PATH, "train_dgl_lt_09x.py")
DGL_SCRIPT_PATH = os.path.join(DGL_DATA_PATH, "train.py")
inductor_instance_types = ["ml.g5.12xlarge", "ml.g5.12xlarge", "ml.g4dn.12xlarge"]


@pytest.mark.skip_dgl_test
@pytest.mark.skip_gpu
@pytest.mark.skip_py2_containers
@pytest.mark.skip_inductor_test
@pytest.mark.integration("dgl")
@pytest.mark.processor("cpu")
@pytest.mark.model("gcn")
@pytest.mark.team("dgl")
def test_dgl_gcn_training_cpu(ecr_image, sagemaker_regions, instance_type):
    instance_type = instance_type or "ml.c5.xlarge"
    function_args = {
        "instance_type": instance_type,
    }
    invoke_pytorch_helper_function(ecr_image, sagemaker_regions, _test_dgl_training, function_args)


@pytest.mark.skip_dgl_test
@pytest.mark.skip_cpu
@pytest.mark.skip_py2_containers
@pytest.mark.skip_inductor_test
@pytest.mark.integration("dgl")
@pytest.mark.processor("gpu")
@pytest.mark.model("gcn")
@pytest.mark.team("dgl")
@pytest.mark.parametrize("instance_type", inductor_instance_types, indirect=True)
def test_dgl_gcn_training_gpu(ecr_image, sagemaker_regions, instance_type):
    instance_type = instance_type or "ml.g5.8xlarge"
    function_args = {
        "instance_type": instance_type,
    }

    invoke_pytorch_helper_function(ecr_image, sagemaker_regions, _test_dgl_training, function_args)


def _test_dgl_training(ecr_image, sagemaker_session, instance_type):
    dgl = PyTorch(
        entry_point=DGL_SCRIPT_PATH,
        role="SageMakerRole",
        instance_count=1,
        instance_type=instance_type,
        sagemaker_session=sagemaker_session,
        image_uri=ecr_image,
        hyperparameters={"inductor": 1},
    )
    with timeout(minutes=DEFAULT_TIMEOUT):
        job_name = utils.unique_name_from_base("test-pytorch-dgl-image")
        dgl.fit(job_name=job_name)
