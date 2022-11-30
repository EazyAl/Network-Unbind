import meraki
import pprint
import sys

# Get API Key and Network Name

print("Enter your API_KEY and press Enter")
API_KEY = input()

# Check if API Key is valid

try:

    dashboard = meraki.DashboardAPI(API_KEY)
    orgs = dashboard.organizations.getOrganizations()

except meraki.APIError as e:

    print("Invalid API key entered. Terminating script")
    sys.exit()

print("Enter the EXACT Name of the organization you would like to work with")

org_name = input()

#Find org ID based on name

org_id = '1'

for o in orgs:

    if o['name'] == org_name:

        org_id = o['id']

if org_id == '1':

    print("Org with this name not found. Cancelling operation")
    sys.exit()

networks = dashboard.organizations.getOrganizationNetworks(
    org_id, total_pages = 'all'
)

finished = False

# This loop unbinds the network by finding the network ID based on name
# The use is then asked if they would like to continue unbinding more networks
# Each iteration of this loop is one unbind

while finished == False:

    print("Enter the EXACT Name of the network you would like to unbind")
    network_name = input()

    network_id = '1'

    for n in networks:

        if n['name'] == network_name:

            network_id = n['id']

    if network_id != '1':

        response = dashboard.networks.unbindNetwork(network_id, retainConfigs=True)

        print(response)

    else:

        print("Network with given name not found")

    print("Would you like to unbind another network?")
    print("Type Y/N")

    answer = input()

    if answer.lower() == 'n':

        finished = True

print("Operation finished. Please review results on Meraki dashboard")
