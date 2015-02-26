#!/usr/bin/python
import os
import pprint
import novaclient.v1_1.client as novaclient
pp = pprint.PrettyPrinter(indent=4)

def p(value):
    """Shortcut for pretty printing"""
    pp.pprint(value)

def print_title(title):
    """Print title of things"""
    print "\n"+"#"*32+"\n# "+title+"\n"+"#"*32+"\n"

def get_creds():
    """Retrieve creds from environment"""
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['api_key'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['project_id'] = os.environ['OS_TENANT_NAME']
    return d

def main():
    creds = get_creds()
    nova = novaclient.Client(**creds)

    #print_title("servers list")
    #servers = nova.servers.list()
    #p(servers)

    #sprout = nova.servers.find(name='Sprout')
    #p(sprout.__dict__)

    f = nova.flavors.find(name = 'instantserver-small')
    i = nova.images.find(name = 'Ubuntu 14.10 64b')
    n = nova.networks.find(label = 'instantserver')
    k = "idrsa-sansmotdepasse"
    u = "#cloud-config\npassword: moutarde\nchpasswd: { expire: False }\nssh_pwauth: True"

    new_server = nova.servers.create(
        name = "instantserver-1", 
        flavor = f,
        image = i,
        nics = [{"net-id": n.id}],
        key_name = k,
        userdata = u,
        security_groups = ["Tout-Autorise-Entrant-Sortant"]
    )

if __name__ == '__main__':
    main()
