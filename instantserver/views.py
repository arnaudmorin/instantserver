from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.utils import timezone
from instantserver.models import VirtualMachine
import json
import random
import string

def index(request):
	"""Index page"""
	context = {}
	return render(request, 'instantserver/index.html', context)

def vm_list(request):
	"""List all VM"""
	if request.method == 'POST':
		virtual_machine = VirtualMachine()
		
		# Temporary hack to return a valid machine
		# TODO: make request over opensteak API
		virtual_machine.ip_address = "192.168.1.{}".format(random.randrange(2, 254))
		virtual_machine.creation_date = timezone.now()
		virtual_machine.login = "ubuntu"
		virtual_machine.password = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])
		
		# Create json object from VM
		json_object = {	'ip_address': virtual_machine.ip_address,
						'creation_date': str(virtual_machine.creation_date),
						'login': virtual_machine.login,
						'password': virtual_machine.password
					  }
		return HttpResponse(json.dumps(json_object), content_type="application/json")
	else:
		virtual_machines = VirtualMachine.objects.all()
		context = {'virtual_machines': virtual_machines}
		return render(request, 'instantserver/vm_list.html', context)
	

def vm_id(request, vm_id):
	"""Detail of one VM"""
	virtual_machine = get_object_or_404(VirtualMachine, pk=vm_id)
	context = {'vm': virtual_machine}
	return render(request, 'instantserver/vm.html', context)

def vm_ip(request, vm_ip):
	"""Detail of one VM"""
	virtual_machine = get_object_or_404(VirtualMachine, ip_address=vm_ip)
	context = {'vm': virtual_machine}
	return render(request, 'instantserver/vm.html', context)
