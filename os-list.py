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
    servers = nova.servers.list()
    pp.pprint(servers)

    print_title("Fabm Server")
    server = get_server(get_nova_creds(), "fabm")
    pp.pprint(server.networks)

    print_title("Servers IP by network")
    dns_records={'externe':{}}
    for srv in servers:
        name = str(srv.name.replace(' ','_'))
        for net,ips in srv.networks.items():
            if(len(ips)>1):
                dns_records['externe'][name]=str(ips[1])
            if(not dns_records.has_key(net)):
                dns_records[str(net)]={}
            dns_records[net][name]=str(ips[0])
    pp.pprint(dns_records)
    
    print_title("Externe DNS db")
    for node,ip in dns_records['externe'].items():
        print "%-40sIN\tA\t%s" % ( node, ip )
            
    #~ (fixed_ip, floating_ip) = server.networks[netname]
    # Remove existing key, if any
    #~ remove_hostkey(floating_ip)
    #~ output = server.get_console_output()
    #~ key = get_hostkey_from_console(output)
    #~ with open(os.path.expanduser("~/.ssh/known_hosts"), 'a') as f:
        #~ f.write("{0} {1}\n".format(floating_ip, key))


if __name__ == '__main__':
    main()
