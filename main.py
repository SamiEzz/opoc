from gasFees import *
from time import sleep

gasFeesIns = GasFees()

while 1:
    gasFeesIns.updateInstance()
    print(gasFeesIns.lastCacheUpdate)
    sleep(3)