'''
Created on Mar 20, 2015

@summary: some utilities in the system.
@author: Jay <smile665@gmail.com>
'''
security_key = '*_*jayiot2015*_*'


def key_validation(key):
    '''
    @summary: validate the key used by the clients.
    '''
    ret = False
    if key.lower() == security_key:
        ret = True
    else:
        ret = False
    return ret


if __name__ == '__main__':
    print key_validation('haha')
    print key_validation(security_key)