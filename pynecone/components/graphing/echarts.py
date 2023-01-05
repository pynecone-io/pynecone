# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from pynecone.components.component import Component
from pynecone.var import Var
from typing import Any, Dict

class Echarts(Component):
    """A component that wraps echarts-for-react.
    - echarts: https://echarts.apache.org/examples/en/index.html
    - echarts-for-react: https://github.com/hustcc/echarts-for-react
    """

    library = "echarts-for-react"
    tag = "EchartsForReact"

    #
    option: Var[Dict]#Var[dict] = {}

    theme: Var[str]

    notMerge: Var[bool]

    lazyUpdate: Var[bool]

    opts: Var[Dict]
    
    onEvents: Var[Dict]

    # onChartReady: Var



    def _get_imports(self):
        return {}

    def _get_custom_code(self) -> str:
        return f'import {self.tag} from "{self.library}"'