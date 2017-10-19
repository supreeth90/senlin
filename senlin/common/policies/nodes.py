# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


from oslo_policy import policy

from senlin.common.policies import base

rules = [
    policy.DocumentedRuleDefault(
        name="nodes:index",
        check_str=base.UNPROTECTED,
        description="List nodes",
        operations=[
            {
                'path': '/v1/nodes',
                'method': 'GET'
            }
        ]
    ),
    policy.DocumentedRuleDefault(
        name="nodes:create",
        check_str=base.UNPROTECTED,
        description="Create node",
        operations=[
            {
                'path': '/v1/nodes',
                'method': 'GET'
            }
        ]
    ),
    policy.DocumentedRuleDefault(
        name="nodes:adopt",
        check_str=base.UNPROTECTED,
        description="Adopt node",
        operations=[
            {
                'path': '/v1/nodes/adopt',
                'method': 'POST'
            }
        ]
    ),
    policy.DocumentedRuleDefault(
        name="nodes:adopt_preview",
        check_str=base.UNPROTECTED,
        description="Adopt node (preview)",
        operations=[
            {
                'path': '/v1/nodes/adopt-preview',
                'method': 'POST'
            }
        ]
    ),
    policy.DocumentedRuleDefault(
        name="nodes:get",
        check_str=base.UNPROTECTED,
        description="Show node details",
        operations=[
            {
                'path': '/v1/nodes/{node_id}',
                'method': 'GET'
            }
        ]
    ),
    policy.DocumentedRuleDefault(
        name="nodes:action",
        check_str=base.UNPROTECTED,
        description="Perform specified action on a Node.",
        operations=[
            {
                'path': '/v1/nodes/{node_id}/actions',
                'method': 'POST'
            }
        ]
    ),
    policy.DocumentedRuleDefault(
        name="nodes:update",
        check_str=base.UNPROTECTED,
        description="Update node",
        operations=[
            {
                'path': '/v1/nodes/{node_id}',
                'method': 'PATCH'
            }
        ]
    ),
    policy.DocumentedRuleDefault(
        name="nodes:delete",
        check_str=base.UNPROTECTED,
        description="Delete node",
        operations=[
            {
                'path': '/v1/nodes/{node_id}',
                'method': 'DELETE'
            }
        ]
    ),
    policy.DocumentedRuleDefault(
        name="nodes:operation",
        check_str=base.UNPROTECTED,
        description="Perform an Operation on a Node",
        operations=[
            {
                'path': '/v1/nodes/{node_id}/ops',
                'method': 'POST'
            }
        ]
    )
]


def list_rules():
    return rules
