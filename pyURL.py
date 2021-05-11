import os
import sys
import pyshorteners




## author : MrRobot
## pyurl tool for shorten url.
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
url = input("Enter your url :~# ")

print(" ↓ URL\n",pyshorteners.Shortener().tinyurl.short(url))
