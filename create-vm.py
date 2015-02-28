#!/usr/bin/python
import os
import pprint
import novaclient.v1_1.client as novaclient
import cinderclient.v1.client as cinderclient
pp = pprint.PrettyPrinter(indent=4)

def p(value):
    """Shortcut for pretty printing"""
    pp.pprint(value)

def print_title(title):
    """Print title of things"""
    print "\n"+"#"*32+"\n# "+title+"\n"+"#"*32+"\n"

def get_credentials(service):
    """Returns a creds dictionary filled with the following keys:

    * username
    * password/api_key (depending on the service)
    * tenant_name/project_id (depending on the service)
    * auth_url

    :param service: a string indicating the name of the service
                    requesting the credentials.
    """

    creds = {}
    # Unfortunately, each of the openstack client will request slightly
    # different entries in their credentials dict.
    if service.lower() in ("nova", "cinder"):
        password = "api_key"
        tenant = "project_id"
    else:
        password = "password"
        tenant = "tenant_name"

    # The most common way to pass these info to your script is to do it through
    # your environment variables. Since we're `get`ing values from a
    # dict, it shouldn't be too difficult to set default values too.
    creds.update({
        "username": os.environ.get('OS_USERNAME', "demo"),
        password: os.environ.get("OS_PASSWORD", "password"),
        "auth_url": os.environ.get("OS_AUTH_URL",
                                   "http://192.168.0.10:5000/v2.0"),
        tenant: os.environ.get("OS_TENANT_NAME", "invisible_to_admin"),
    })

    return creds

def create_volume(c,i):
    """Create a volume from image"""
    return c.volumes.create(
        size = "10",
        display_name = "instantserver-1",
        display_description = "Volume for instantserver-1",
        imageRef = i
    )

def main():
    creds = get_credentials("nova")
    nova = novaclient.Client(**creds)
    cinder = cinderclient.Client(**creds)

    print_title("servers list")
    p(nova.servers.list())

    print_title("images list")
    p(nova.images.list())

    # Create a volume

    new_server = nova.servers.create(
        name = "instantserver-1", 
        flavor = f,
        image = i,
        nics = [{"net-id": n.id}],
        key_name = k,
        userdata = u,
        security_groups = s
    )

    # OpenWatt
    f = nova.flavors.find(name = 'm1.tiny')
    i = nova.images.find(name = 'Ubuntu 14.04.1 LTS')
    n = nova.networks.find(label = 's_Cld4Net_internal_net')
    u = "#cloud-config\npassword: moutarde\nchpasswd: { expire: False }\nssh_pwauth: True"
    k = "idrsa-sansmotdepasse"
    s = ["default"]

    # OpenSteak
    #f = nova.flavors.find(name = 'instantserver-small')
    #i = nova.images.find(name = 'Ubuntu 14.10 64b')
    #n = nova.networks.find(label = 'instantserver')
    #u = "#cloud-config\npassword: moutarde\nchpasswd: { expire: False }\nssh_pwauth: True"
    #k = "idrsa-sansmotdepasse"
    #s = ["Tout-Autorise-Entrant-Sortant"]
    #v = create_volume(cinder, i.id)

    # Do create
    new_server = nova.servers.create(
        name               = "instantserver-1", 
        flavor             = f,
        image              = i,
        nics               = [{"net-id": n.id}],
        key_name           = k,
        userdata           = u,
        security_groups    = s
    )

    p(new_server)

if __name__ == '__main__':
    main()
