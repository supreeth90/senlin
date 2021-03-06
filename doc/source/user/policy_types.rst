..
  Licensed under the Apache License, Version 2.0 (the "License"); you may
  not use this file except in compliance with the License. You may obtain
  a copy of the License at

          http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
  License for the specific language governing permissions and limitations
  under the License.


.. _ref-policy-types:

============
Policy Types
============

Concept
~~~~~~~

A :term:`Policy Type` is an abstract specification of the rules to be checked
and/or enforced when certain :term:`Action` is performed on a cluster that
contains nodes of certain :term:`Profile Type`.

A registry of policy types is built in memory when the Senlin engine
(:program:`senlin-engine`) is started. In future, Senlin will allow users to
provide additional policy type implementations as plug-ins to be loaded
dynamically.

A policy type implementation dictates which fields are required, which fields
are optional and sometimes the constraints on field values. When a
:term:`policy` is created by referencing this policy type, the fields are
assigned with concrete values. For example, a policy type
``senlin.policy.deletion`` conceptually specifies the properties required::

  criteria: String # valid values - OLDEST_FIRST, YOUNGEST_FIRST, RANDOM
  destroy_after_deletion: Boolean
  grace_period: Integer
  reduce_desired_capacity: Boolean

The specification of a policy object of this policy type may look like
following::

  type: senlin.policy.deletion
  version: 1.0
  properties:
    criteria: OLDEST_FIRST
    destroy_after_deletion: True
    grace_period: 120
    reduce_desired_capacity: True


Listing Policy Types
~~~~~~~~~~~~~~~~~~~~

Senlin server comes with some built-in policy types. You can check the list
of policy types using the following command::

  $ openstack cluster policy type list
  +--------------------------------+---------+----------------------------+
  | name                           | version | support_status             |
  +--------------------------------+---------+----------------------------+
  | senlin.policy.affinity         | 1.0     | SUPPORTED since 2016.10    |
  | senlin.policy.batch            | 1.0     | EXPERIMENTAL since 2017.02 |
  | senlin.policy.deletion         | 1.0     | SUPPORTED since 2016.04    |
  | senlin.policy.deletion         | 1.1     | SUPPORTED since 2018.01    |
  | senlin.policy.health           | 1.0     | EXPERIMENTAL since 2017.02 |
  | senlin.policy.loadbalance      | 1.0     | SUPPORTED since 2016.04    |
  | senlin.policy.loadbalance      | 1.1     | SUPPORTED since 2018.01    |
  | senlin.policy.region_placement | 1.0     | EXPERIMENTAL since 2016.04 |
  |                                |         | SUPPORTED since 2016.10    |
  | senlin.policy.scaling          | 1.0     | SUPPORTED since 2016.04    |
  | senlin.policy.zone_placement   | 1.0     | EXPERIMENTAL since 2016.04 |
  |                                |         | SUPPORTED since 2016.10    |
  +--------------------------------+---------+----------------------------+


The output is a list of policy types supported by the Senlin server.


Showing Policy Details
~~~~~~~~~~~~~~~~~~~~~~

Each :term:`Policy Type` has a schema for its *spec* (i.e. specification)
that describes the names and types of the properties that can be accepted. To
show the schema of a specific policy type along with other properties, you can
use the following command::

  $ openstack cluster policy type show senlin.policy.deletion-1.1
  support_status:
    '1.0':
    - since: '2016.04'
      status: SUPPORTED
    '1.1':
    - since: '2018.01'
      status: SUPPORTED
  id: senlin.policy.deletion-1.1
  location: null
  name: senlin.policy.deletion-1.1
  schema:
    criteria:
      constraints:
      - constraint:
        - OLDEST_FIRST
        - OLDEST_PROFILE_FIRST
        - YOUNGEST_FIRST
        - RANDOM
        type: AllowedValues
      default: RANDOM
      description: Criteria used in selecting candidates for deletion
      required: false
      type: String
      updatable: false
    destroy_after_deletion:
      default: true
      description: Whether a node should be completely destroyed after deletion. Default
        to True
      required: false
      type: Boolean
      updatable: false
    grace_period:
      default: 0
      description: Number of seconds before real deletion happens.
      required: false
      type: Integer
      updatable: false
    hooks:
      default: {}
      description: Lifecycle hook properties
      required: false
      schema:
        params:
          default: {}
          required: false
          schema:
            queue:
              default: ''
              description: Zaqar queue to receive lifecycle hook message
              required: false
              type: String
              updatable: false
            url:
              default: ''
              description: Url sink to which to send lifecycle hook message
              required: false
              type: String
              updatable: false
          type: Map
          updatable: false
        timeout:
          default: 0
          description: Number of seconds before actual deletion happens.
          required: false
          type: Integer
          updatable: false
        type:
          constraints:
          - constraint:
            - zaqar
            - webhook
            type: AllowedValues
          default: zaqar
          description: Type of lifecycle hook
          required: false
          type: String
          updatable: false
      type: Map
      updatable: false
    reduce_desired_capacity:
      default: true
      description: Whether the desired capacity of the cluster should be reduced along
        the deletion. Default to True.
      required: false
      type: Boolean
      updatable: false

Here, each property has the following attributes:

- ``default``: the default value for a property when not explicitly specified;
- ``description``: a textual description of the use of a property;
- ``required``: whether the property must be specified. Such kind of a
  property usually doesn't have a ``default`` value;
- ``type``: one of ``String``, ``Integer``, ``Boolean``, ``Map`` or ``List``;
- ``updatable``: a boolean indicating whether a property is updatable.

The default output from the :command:`policy-type-show` command is in YAML
format. You can choose to show the spec schema in JSON format by specifying
the :option:`-f json` option as shown below::

  $ openstack cluster policy type show -f json senlin.policy.deletion-1.0

For information on how to manage the relationship between a policy and a
cluster, please refer to :ref:`ref-bindings`.


See Also
~~~~~~~~

Check the list below for documents related to the creation and usage of
:term:`Policy` objects.

* :doc:`Creating Your Own Policy Objects <policies>`
* :doc:`Managing the Binding between Cluster and Policy <bindings>`
* :doc:`Examining Actions <events>`
* :doc:`Browsing Events <events>`
