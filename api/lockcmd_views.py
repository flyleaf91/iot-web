'''
Created on May 16, 2015

@author: Jay <smile665@gmail.com>
'''

import copy
from django.views.decorators.csrf import csrf_exempt
from rest_framework.request import Request
from lib.response import JSONResponse
from lib.utility import key_validation
from lock.lock_cmd import add_cmd, get_lockcmd


@csrf_exempt
def add_lockcmd(request):
    '''
    @summary: add a lock cmd.
    '''
    if request.method == 'POST':
        req = Request(request)
        thekey = req.DATA.get('thekey', default='123')
        if key_validation(thekey):
            cmd_data = {'device_id': req.DATA.get('device_id'),
                        'command': req.DATA.get('command'),
                        'status': 'initialized'}
            if add_cmd(cmd_data):
                print 'hello4'
                data = {'status': 0, 'detail': 'cmd is added'}
            else:
                data = {'status': 1, 'detail': 'cmd is NOT added'}
        else:
            data = {'status': 1, 'detail': 'security key error.'}
        return JSONResponse(data=data, status=200)
    else:
        data = {'status': 1, 'detail': 'only support HTTP POST method'}
        return JSONResponse(data=data, status=200)


def get_latest_cmd(request):
    '''
    @summary: get the latest cmd.
    '''
    if request.method == 'GET':
        req = Request(request)
        thekey = req.QUERY_PARAMS.get('thekey', default='123')
        if key_validation(thekey):
            cmd_data = copy.copy(req.QUERY_PARAMS)
            print cmd_data
            cmd_data.pop('thekey')
            dev_id = cmd_data.get('dev_id')
            status = 'initialized'
            lock_cmd_data = get_lockcmd(dev_id, status)
            if lock_cmd_data:
                data = {'status': 0, 'detail': lock_cmd_data['command']}
            else:
                data = {'status': 0, 'detail': 'no cmd.'}
        else:
            data = {'status': 1, 'detail': 'security key error.'}
        return JSONResponse(data=data, status=200)
    else:
        data = {'status': 1, 'detail': 'only support HTTP GET method'}
        return JSONResponse(data=data, status=200)
