'''DAY 24 OF 100DAYS 
PYTHON PROJECT'''
import subprocess

output = subprocess.check_output(
    "netsh wlan show interfaces",
    shell=True
).decode()
print(output)