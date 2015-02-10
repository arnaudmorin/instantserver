import os
from novaclient.client import Client

def get_nova_credentials_v2():
    d = {}
    d['version'] = '2'
    d['username'] = os.environ['OS_USERNAME']
    d['api_key'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['project_id'] = os.environ['OS_TENANT_NAME']
    return d


credentials = get_nova_credentials_v2()
c = Client(**credentials)

print(c_.servers.list())
print(c.flavors.list())

i = c.servers.create(
    name = "instantserver-1",
    image = c.images.find(name="Ubuntu 14.10 64b"),
    flavor = c.flavors.find(name="instantserver-small"),
    nics = [{'net-id': c.networks.find(label="instantserver").id}],
    userdata = "#cloud-config\npassword: motdepasse\nchpasswd: { expire: False }\nssh_pwauth: True")

# Add security group just after creation of the machine so that it will be able to contact
# the metadata services
i.add_security_group(c.security_groups.find(name='Tout-Autorise-Entrant-Sortant'))
