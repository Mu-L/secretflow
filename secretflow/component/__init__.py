# Copyright 2023 Ant Group Co., Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import os

from secretflow_spec import load_component_modules


def _import_all_submodules():
    root_path = os.path.dirname(__file__)
    load_component_modules(
        root_path,
        "secretflow.component",
        ignore_dirs=["core", "test_framework", "storage"],
        ignore_keys=["/core/", "_utils/"],
        ignore_root_files=True,
    )


_import_all_submodules()
