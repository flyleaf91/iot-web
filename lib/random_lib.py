'''
Created on May 18, 2015

@author: Jay
'''

import string
import random


def id_generator(size=20, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


if __name__ == '__main__':
    print id_generator()
