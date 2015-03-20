'''
Created on Mar 20, 2015

@author: Jay <smile665@gmail.com>
'''

import logging


class CarLogger:
    '''
    The common logger for iot-web project.
    '''

    logger = None

    def __init__(self, logfile='iot.log', level=logging.INFO, name='iot'):
        FORMAT = '%(asctime)-15s  %(message)s'
        logging.basicConfig(filename=logfile, format=FORMAT, level=level)
        self.logger = logging.getLogger(name=name)

    def getLogger(self):
        return self.logger


if __name__ == '__main__':
    mylogger = CarLogger().getLogger()
    mylogger.info('hello')
