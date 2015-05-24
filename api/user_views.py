'''
Created on May 16, 2015

@author: Jay <smile665@gmail.com>
'''

import copy
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from rest_framework.request import Request
from lib.response import JSONResponse
from lib.utility import key_validation
from lib.random_lib import id_generator
from appuser.user import add_user, get_user, add_login


@csrf_exempt
def register(request):
    '''
    @summary: register a user.
    '''
    if request.method == 'POST':
        req = Request(request)
        thekey = req.DATA.get('thekey', default='123')
        if key_validation(thekey):
            user_data = copy.copy(req.DATA)
            user_data.pop('thekey')
            exist_user = get_user(username=user_data['user'])
            if not exist_user:
                if add_user(user_data):
                    data = {'status': 0,
                            'detail': 'user %s added' % user_data['user']}
                else:
                    data = {'status': 1,
                            'detail': 'user %s not added' % user_data['user']}
            else:
                data = {'status': 1,
                        'detail': '%s already exists' % user_data['user']}
        else:
            data = {'status': 1, 'detail': 'security key error.'}
        return JSONResponse(data=data, status=200)
    else:
        data = {'status': 1, 'detail': 'only support HTTP POST method'}
        return JSONResponse(data=data, status=200)


@csrf_exempt
def login(request):
    '''
    @summary: user login.
    '''
    if request.method == 'POST':
        req = Request(request)
        thekey = req.DATA.get('thekey', default='123')
        if key_validation(thekey):
            login_data = dict()
            login_data['user'] = req.DATA.get('user', default='abc')
            login_data['password'] = req.DATA.get('password', default='abc')
            login_data['login_key'] = id_generator(size=20)
            login_data['valid_end_time'] = datetime.now() + timedelta(days=30)
            if add_login(login_data):
                login_data.pop('password')
                login_data['valid_end_time'] = datetime.
                data = {'status': 0, 'detail': login_data}
            else:
                data = {'status': 1, 'detail': 'login failed.'}
        else:
            data = {'status': 1, 'detail': 'security key error.'}
        return JSONResponse(data=data, status=200)
    else:
        data = {'status': 1, 'detail': 'only support HTTP POST method'}
        return JSONResponse(data=data, status=200)
