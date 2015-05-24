'''
Created on May 24, 2015

@author: Jay
'''
import django
import os
import sys
sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "../")
))
os.environ['DJANGO_SETTINGS_MODULE'] = 'iot.settings'
from lock.lock_cmd import cmd_timeout

timeout = 60

if __name__ == '__main__':
    django.setup()
    print cmd_timeout(timeout=timeout)
