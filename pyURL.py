import os
import sys
import pyshorteners 
# pip install pyshorteners


# ASCII logo banner
bannerShortUrl = '''

______                 _   _ ______  _     
| ___ \               | | | || ___ \| |    
| |_/ / _   _  ______ | | | || |_/ /| |    
|  __/ | | | ||______|| | | ||    / | |    
| |    | |_| |        | |_| || |\ \ | |____
\_|     \__, |         \___/ \_| \_|\_____/
         __/ |                             
        |___/                              

'''

print(bannerShortUrl)

# define main script 
# as a start for looping
def start(): 
     	url = input("\nEnter your url :~# ")
     	print(" ↓ URL\n",pyshorteners.Shortener().tinyurl.short(url))

start()

# option for re-run script or exit
ask = input("\nWanna create a new one? y/n : ")

if ask == "y" or "yes":
   start()
elif ask == "n" or "no":
   sys.exit(0)


    
# u/ MrRobot
# v/ 1.0.2
    
# ---------------
# T H E  E N D .
# ---------------
    
