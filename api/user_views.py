'''
Created on May 16, 2015

@author: Jay <smile665@gmail.com>
'''

import copy
from django.views.decorators.csrf import csrf_exempt
from rest_framework.request import Request
from lib.response import JSONResponse
from lib.utility import key_validation
from appuser.user import add_user, get_user


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
