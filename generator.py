'''
Created on 20.04.2013

@author: maweki
'''

import random
import json

probability = 0.005
amount = 5000

def getAny():
    return random.random() + random.random() - 1

def getX():
    return getAny()

def getY():
    return getAny()

def getZ():
    return getAny()

def getState():
    return (random.random() <= probability)

if __name__ == '__main__':
    for _ in range(amount):
        print json.dumps({'x': getX(), 'y': getY(), 'z': getZ(), 'a': getState()})