# Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
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

import unittest
import paddle
import os


class TestFleetRuntime(unittest.TestCase):
    def test_fleet_runtime_base(self):
        import paddle.fleet.runtime
        base = paddle.fleet.runtime.runtime_base.RuntimeBase()
        base._run_worker()
        base._init_server()
        base._run_server()
        base._stop_worker()

    def test_fleet_collective_runtime(self):
        import paddle.fleet.runtime
        collective_runtime = paddle.fleet.runtime.CollectiveRuntime()
        collective_runtime._init_worker()
        collective_runtime._run_worker()
        collective_runtime._init_worker()
        collective_runtime._run_server()
        collective_runtime._stop_worker()


if __name__ == "__main__":
    unittest.main()
