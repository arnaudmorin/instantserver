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

    print_title("servers list")
    pp.pprint(nova.servers.list())

    print_title("images list")
    pp.pprint(nova.images.list())

    #sprout = nova.servers.find(name='Sprout')
    #pp.pprint(sprout.__dict__)

    f = nova.flavors.find(name = 'm1.tiny')
    i = nova.images.find(name = 'Ubuntu 14.04.1 LTS')
    n = nova.networks.find(label = 's_Cld4Net_internal_net')
    #pp.pprint(f.__dict__)

    #nova.servers.create(
    #    name = "tutu-server", 
    #    flavor = f,
    #    image = i,
    #    nics = [{"net-id": n.id}],
    #    key_name = "id-rsa-sans-mot-de-passe"
    #)

if __name__ == '__main__':
    main()
