from gasFees import *
from time import sleep
import logging

logFileName = "./log/index.log"

logging.basicConfig(filename=logFileName, level=logging.DEBUG)

gasFeesIns = GasFees()

while 1:
    gasFeesIns.updateInstance()
    print(gasFeesIns.lastCacheUpdate)
    sleep(3)