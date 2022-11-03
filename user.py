import time
import os

while True:
    # Capture user input with prompt
    user_input = input("Type 1 to view preset options, press 2 to close software:\n")
    # Run program if input is 1
    if int(user_input) == 1:
        # Check whether a preset is available
        f = open('preset.txt','r')
        read_text = f.readline()
        while read_text:
            print(read_text)
            read_text = f.readline()
        f.close() 
        number = input("Choose one of the following presets:")
        if int(number) == 1 or 2 or 3:
            f = open('display.txt','w')
            f.write(number) 
            f.close()
            time.sleep(2)
            f = open('display.txt','r+')
            print(f.read())
        else:
            print("Invalid Option")
            pass
        f = open('display.txt','w')
        f.truncate(0)
        f.close()
        # Enter 2 to close program
    elif int(user_input) == 2:
        break
    else:
        print("Invalid option")