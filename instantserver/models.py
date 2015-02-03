from django.db import models

# Instant server models

class VirtualMachine(models.Model):
    """VirtualMachine
    
    This represent a Virtual Machine
    """
    ip_address = models.GenericIPAddressField(protocol='ipv4')
    creation_date = models.DateTimeField()
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    
    def __str__(self):
        return "{} ({} / {}) created on {}".format(self.ip_address, self.login, self.password, self.creation_date)
