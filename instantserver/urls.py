from django.conf.urls import patterns, url
from instantserver import views

urlpatterns = patterns('',
    # Index
    url(r'^$', views.index, name='index'),
    
    # List all vm
    url(r'^vm/$', views.vm_list, name='vm_list'),
    
    # VM detail
    url(r'^vm/(?P<vm_id>\d+)/$', views.vm_id, name='vm_id'),
    
    # VM detail
    url(r'^vm/(?P<vm_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/$', views.vm_ip, name='vm_ip'),
)
