import time
import os

while True:
    time.sleep(1)
    # microservice status indicator
    print("micro.py is running...")
    # Initialize preset
    preset = None
    # Open display.txt
    f = open('display.txt','r+')
    read_txt = f.readline()
    if read_txt == "1":
        f.truncate(0)
        f.close()
        print("User Selected 1")
        g = open('preset.txt','r+')
        test = int(read_txt) - 1
        preset = g.readlines()
        f = open('display.txt','w')
        f.writelines(preset[test])
    elif read_txt == "2":   
        f.truncate(0)
        f.close()
        print("User Selected 2")
        g = open('preset.txt','r+')
        test = int(read_txt) - 1
        preset = g.readlines()
        f = open('display.txt','w')
        f.writelines(preset[test])
    elif read_txt == "3":
        f.truncate(0)
        f.close()
        print("User Selected 3")
        g = open('preset.txt','r+')
        test = int(read_txt) - 1
        preset = g.readlines()
        f = open('display.txt','w')
        f.writelines(preset[test])  
