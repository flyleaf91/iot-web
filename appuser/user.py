# -*- coding: utf-8 -*-
'''
Created on May 17, 2015

@author: Jay
'''

import django
from appuser.models import User
from appuser.models import Login
from appuser.serializers import UserSerializer
from appuser.serializers import LoginSerializer
from datetime import datetime


def add_user(data):
    '''
    @summary: add (if no) or update a user record.
    @parm data: a dict data for the User's serializer.
    @return: True (if added), False (if not added).
    '''
    try:
        user = User.objects.get(user=data['user'])
        user_se = UserSerializer(user, data=data, partial=True)
    except User.DoesNotExist:
        user_se = UserSerializer(data=data)
    if user_se.is_valid():
        user_se.save()
        return True
    else:
        return False


def get_user(username):
    '''
    @summary: get user info by username.
    @param username: the username.
    @return: username and reg_time;  None (if no user found).
    '''
    ret = None
    try:
        user = User.objects.get(user=username)
        user_se = UserSerializer(user)
        user_se.data.pop('password')
        ret = user_se.data
    except User.DoesNotExist:
        ret = None
    return ret


if __name__ == '__main__':
    django.setup()
    user = 'Jay'
    password = '1234'
    email = 'smile665@gmail.com'
    user_data = {'user': user, 'password': password, 'email': email}
    print add_user(user_data)
    print get_user('Jay')
    print get_user('Not')
