# -*- coding: utf-8 -*-
'''
Created on May 16, 2015

@author: Jay
'''

import django
from lock.models import LockCmd
from lock.serializers import LockCmdSerializer
from datetime import datetime, timedelta


def add_cmd(data):
    '''
    @summary: add (if no) or update a lock_cmd record.
    @parm data: a dict data for the LockCmd's serializer.
    @return: None.
    '''
    lockcmd_se = LockCmdSerializer(data=data)
    if lockcmd_se.is_valid():
        lockcmd_se.save()
        return True
    else:
        return False


def get_lockcmd(dev_id, status):
    '''
    @summary: get the latest lock cmd by device and status.
    @param dev_id: the id of the device.
    @param status: the event type.
    @return: the lock cmd info; or None (if no info found).
    '''
    ret = None
    lockcmd = LockCmd.objects.filter(device_id=dev_id,
                                     status=status).order_by('-create_time')
    lockcmd_se = LockCmdSerializer(lockcmd, many=True)
    if len(lockcmd_se.data) >= 1:
        ret = lockcmd_se.data[0]
    else:
        pass
    return ret


def cmd_timeout(timeout):
    '''
    @summary: change some lockcmd to 'timeout' status.
    @param timeout: the time (in seconds) a cmd should timeout.
    @return: the number of timeouted records.
    '''
    invalid_time = datetime.now() - timedelta(seconds=timeout)
    status_list = ['initialized', 'processing']
    ret = LockCmd.objects.filter(status__in=status_list).\
                              filter(create_time__lt=invalid_time).\
                              update(status='timeout')
    return ret


if __name__ == '__main__':
    django.setup()
    cmd_data = {'device_id': 'hello123', 'command': 'unlock',
                'user': 'smile', 'status': 'initialized'}
    print add_cmd(cmd_data)
    print get_lockcmd(dev_id='hello123', status='initialized')
    print cmd_timeout(timeout=60)
