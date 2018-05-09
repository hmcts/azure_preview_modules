#!/usr/bin/python
#
# Copyright (c) 2018 Calin Marina, <calin.marina@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = '''
---
module: azure_rm_appgw_facts
version_added: "2.6"
short_description: Get AppGw facts.
description:
    - Get facts of Application Gateway.

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    application_gateway_name:
        description:
            - The name of the Application Gateway.
        required: True

extends_documentation_fragment:
    - azure
'''

EXAMPLES = '''
  - name: Get instance of AppGw
    azure_rm_appgw_facts:
      resource_group: resource_group_name
      application_gateway_name: Application Gateway name
'''

RETURN = '''
todo: describe output
'''

from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.network import NetworkManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMApplicationGatewaysFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            application_gateway_name=dict(
                type='str',
                required=True
            )
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict()
        )
        self.mgmt_client = None
        self.resource_group = None
        self.application_gateway_name = None
        super(AzureRMApplicationGatewaysFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and self.application_gateway_name is not None):
            self.results['ansible_facts'] = self.get()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Application Gateway.

        :return: deserialized Application Gateway state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.application_gateways.get(resource_group_name=self.resource_group,
                                                                 application_gateway_name=self.application_gateway_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for Application Gateway.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results


def main():
    AzureRMApplicationGatewaysFacts()
if __name__ == '__main__':
    main()
