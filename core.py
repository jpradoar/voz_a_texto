#!/usr/bin/env python
import sys
import os
import datetime
import time
import subprocess



"""
comando = ""
i = 0
for arg in sys.argv:
 if i != 0:
  comando = comando + arg + " "
 i = i + 1
comando = comando[0:len(comando)-1]
"""


os.system("> socket")
while True:
	if os.stat("socket").st_size != 0:
		if "Prueba" in open('socket').read():
    			os.system("cat socket | festival --tts --language spanish")
    			time.sleep(0.5)
    			os.system("> socket")
    	if "Hola" in open('socket').read():
    			os.system("cat socket | festival --tts --language spanish")
    			time.sleep(0.5)
    			os.system("> socket")
    	if "Prender luces" in open('socket').read():
    			os.system("cat socket | festival --tts --language spanish")
    			time.sleep(0.5)
    			os.system("> socket")
    	if "IP" in open('socket').read():
    			os.system("ifconfig wlan0 | grep inet | grep -v inet6 | awk {'print $2'} | cut -d':' -f2 | festival --tts --language spanish")
    			time.sleep(0.5)
    			os.system("> socket")

	else:
		time.sleep(1)	
		print time.strftime("%Y-%m-%d %H:%M:%S")

