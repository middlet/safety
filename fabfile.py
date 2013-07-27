#!/usr/bin/env python

from fabric.api import *
from fabric.contrib import files

# globals
env.project_name = "safetytron"

# environment
def dev():
    """
    use the local development server
    """
    env.hosts = ['192.168.0.53']
    # get vagrant key
    result = local('vagrant ssh-config | grep IdentityFile', capture=True)
    env.key_filename = result.split()[1].strip('"')
    env.user = 'vagrant'
    env.code_root = '/vagrant/'+env.project_name
    env.tile_root = '/vagrant'
    
# tasks
def runserver(port=31337):
    """
    start the server running on the remote machine
    """
    with cd(env.code_root):
        run('python ./manage.py runserver 0.0.0.0:%s' % port)
        
def syncdb():
    """
    run syncdb on the server
    """
    with cd(env.code_root):
        run('python ./manage.py syncdb --noinput')
        
def resetdb():
    """
    flush the db and resync it
    """
    with cd(env.code_root):
        run('python ./manage.py flush --noinput')
        run('python ./manage.py syncdb --noinput')
        
def test():
    """
    test the application
    """
    with cd(env.code_root):
        run('python ./manage.py test safety')
    
