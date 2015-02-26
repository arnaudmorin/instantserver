#!/usr/bin/python
import os
import pprint
import novaclient.v1_1.client as nvclient
pp = pprint.PrettyPrinter(indent=4)

def get_keystone_creds():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['password'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['tenant_name'] = os.environ['OS_TENANT_NAME']
    return d
    
def get_nova_creds():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['api_key'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['project_id'] = os.environ['OS_TENANT_NAME']
    return d

def get_server(creds, servername):
    nova = nvclient.Client(**creds)
    return nova.servers.find(name=servername)

def remove_hostkey(ip):
    subprocess.call(["ssh-keygen", "-R", ip])

def get_hostkey_from_console(text):
    lines = text.split('\n')
    start = '-----BEGIN SSH HOST KEY KEYS-----\r'
    end = '-----END SSH HOST KEY KEYS-----\r'
    start_ind = lines.index(start)
    end_ind = lines.index(end)
    for i in range(start_ind+1, end_ind):
        key = lines[i].rstrip()
        if key.startswith('ssh-rsa'):
            return key
    raise KeyError("ssh host key not found")

def print_title(title):
    print "\n"+"#"*32+"\n# "+title+"\n"+"#"*32+"\n"
    
def main():
    creds = get_nova_creds()
    nova = nvclient.Client(**creds)

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
