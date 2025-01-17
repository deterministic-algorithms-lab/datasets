# coding=utf-8
# Copyright 2020 The HuggingFace Datasets Authors and the TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# flake8: noqa
# Lint as: python3
"""Util import."""

from . import logging
from .download_manager import DownloadManager, GenerateMode
from .file_utils import DownloadConfig, cached_path, hf_bucket_url, is_remote_url, temp_seed
from .mock_download_manager import MockDownloadManager
from .py_utils import (
    NonMutableDict,
    abstractclassmethod,
    classproperty,
    copyfunc,
    datasets_dir,
    dumps,
    flatten_nest_dict,
    get_datasets_path,
    has_sufficient_disk_space,
    is_notebook,
    map_nested,
    memoize,
    memoized_property,
    size_str,
    temporary_assignment,
    zip_dict,
    zip_nested,
)
from .tqdm_utils import async_tqdm, tqdm
from .version import Version
