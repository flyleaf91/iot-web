'''
Created on Mar 20, 2015

@author: Jay <smile665@gmail.com>
'''

from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from rest_framework.request import Request
from lib.response import JSONResponse
from lib.utility import key_validation
import lock.lock_info as lockinfo


@csrf_exempt
def list_lockinfo(request):
    '''
    @summary: get a list of lock_info.
    '''
    if request.method == 'GET':
        req = Request(request)
        thekey = req.QUERY_PARAMS.get('thekey', default='123')
        if key_validation(thekey):
            dev_id = req.QUERY_PARAMS.get('dev_id', default='123')
            evt_type = int(req.QUERY_PARAMS.get('evt_type', default=0))
            data = {'status': 0,
                    'detail': lockinfo.get_lockinfo(dev_id, evt_type)}
        else:
            data = {'status': 1, 'detail': 'security key error.'}
        return JSONResponse(data=data, status=200)
    else:
        data = {'status': 1, 'detail': 'only support HTTP GET method'}
        return JSONResponse(data=data, status=200)


@csrf_exempt
def add_lockinfo(request):
    '''
    @summary: add a lockinfo record.
    '''
    if request.method == 'GET':
        default_dev_id = '123'
        req = Request(request)
        thekey = req.QUERY_PARAMS.get('thekey', default=default_dev_id)
        if key_validation(thekey):
            dev_id = req.QUERY_PARAMS.get('dev_id', default='123')
            evt_type = int(req.QUERY_PARAMS.get('evt_type', default=0))
            evt_time = datetime.today()
            li_data = {'device_id': dev_id, 'event_type': evt_type,
                       'event_time': evt_time}
            if dev_id == default_dev_id:
                msg = 'invalid device id: %s' % dev_id
                data = {'status': 1, 'detail': msg}
            elif lockinfo.add(li_data):
                msg = 'added event for %s' % dev_id
                data = {'status': 0, 'detail': msg}
            else:
                msg = 'invalid lock info data.'
                data = {'status': 1, 'detail': msg}
        else:
            data = {'status': 1, 'detail': 'security key error.'}
        return JSONResponse(data=data, status=200)
    else:
        data = {'status': 1, 'detail': 'only support HTTP GET method'}
        return JSONResponse(data=data, status=200)