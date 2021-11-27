| Initiate services
|+ log init
|+ Test connectivity to online providers

| Initiate multithreading

|| Thread 0
||+ Monitoring arbitrage opportunities
||+ refresh database

|| Thread 1
||+ Detect a wining arbitrage
||+ estimate gas fees

|| Thread 2
||+ Generate Solidity smart contract
||+ build .sol
||+ Deploy
