import getpass
import glob
import tempfile
import uuid
import os
import sys
from os.path import realpath
from posixpath import basename

from fabric.contrib import files
from fabric.api import *

sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.curdir)))

def clean():
    print('Removing all .pyc files')
    local("find . -name \"*.pyc\" -exec rm '{}' ';'")


def brunch_compile():
    brunch_paths = ('client/',)

    for pth in brunch_paths:
        with lcd(pth):
            local('npm install')
            local('brunch b')


def local_update():
    #local('git pull origin master')
    #local('git submodule update --init')
    local('pip install -r requirements.txt')
    brunch_compile()
    #migrate()
    clean()



def local_compile():
    brunch_compile()