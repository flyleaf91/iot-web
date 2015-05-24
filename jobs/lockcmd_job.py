'''
Created on May 24, 2015

@author: Jay
'''
import django
from lock.lock_cmd import cmd_timeout

timeout = 60

if __name__ == '__main__':
    django.setup()
    print cmd_timeout(timeout=timeout)
