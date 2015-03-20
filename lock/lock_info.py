# -*- coding: utf-8 -*-
'''
Created on Mar 19, 2015

@author: jay
'''

import django
from lock.models import LockInfo
from lock.serializers import LockInfoSerializer
from datetime import datetime


def add(data):
    '''
    @summary: add (if no) or update a lock_info record.
    @parm data: a dict for the LockInfo's serializer.
    @return: None.
    '''
    lockinfo_se = LockInfoSerializer(data=data)
    if lockinfo_se.is_valid():
        lockinfo_se.save()
        return True
    else:
        return False


def get_lockinfo(dev_id, evt_type=0, start=None, end=None):
    '''
    @summary: get lock info by device and time.
    @param dev_id: the id of the device.
    @param evt_type: the event type.
    @param start: the start time.
    @param end: the end time.
    '''
    ret = None
    try:
        lockinfo = LockInfo.objects.filter(device_id=dev_id, 
                                           event_type=evt_type)
        lockinfo_se = LockInfoSerializer(lockinfo, many=True)
        ret = lockinfo_se.data
    except LockInfo.DoesNotExist:
        pass
    return ret


if __name__ == '__main__':
    django.setup()
    device_id = 'hello123'
    event_type = 0
    event_time = datetime.today()
    data = {'device_id': device_id, 'event_type': event_type,
            'event_time': event_time}
#    add(data)
    print get_lockinfo(dev_id=device_id)