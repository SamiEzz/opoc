import json
from typing import Dict
import requests
from datetime import datetime


class GasFees:
    fast: int
    fastest: int
    safe_low: int
    average: int
    block_time: float
    block_num: int
    speed: float
    safe_low_wait: float
    avg_wait: float
    fast_wait: float
    fastest_wait: float
    gas_price_range: Dict[str, float]
    # auxiliaires
    lastCacheUpdate: int
    cacheUpdateRate = 5000
    cachePath = "./ressources/gasFees.json"
    ethGasUrl = "https://ethgasstation.info/api/ethgasAPI.json?"

    def __init__(self):
        print("Initiating GasFees module ...")
        self.setConfig()
        self.updateInstance()
    
    def setConfig(self):
        self.lastCacheUpdate = self.getTimeMS()

    def getTimeMS(self):
        return int(datetime.now().timestamp()*1000)
    
    def updateCache(self):
        with  open(self.cachePath,"w") as gasF:
            r = requests.get(self.ethGasUrl)
            json.dump(r.json(),gasF,indent=4)
            self.lastCacheUpdate = self.getTimeMS()
        return 0

    def readCache(self):
        with open(self.cachePath) as gasF:
            data = json.load(gasF)
        return data
    
    def updateInstance(self):
        if self.getTimeMS() > self.lastCacheUpdate + self.cacheUpdateRate:
            self.updateCache()
        #self.updateInstance()
        data = self.readCache()
        self.fast = data['fast']
        self.fastest = data['fastest']
        self.safe_low = data['safeLow']
        self.average = data['average']
        self.block_time = data['block_time']
        self.block_num = data['blockNum']
        self.speed = data['speed']
        self.safe_low_wait = data['safeLowWait']
        self.avg_wait = data['avgWait']
        self.fast_wait = data['fastWait']
        self.fastest_wait = data['fastestWait']
        self.gas_price_range = data['gasPriceRange']

        
            
            
        
        