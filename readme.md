# Preset Microservice

### Description: Returns a Preset from text file. The microservice will be incorporated locally.

## Basic Instructions
### Input 1 to use presets
### OR
### input 2 to close program

### ---------------------------

### Input 1 for preset 1
### OR
### Input 2 for preset 2
### OR
### Input 3 for preset 3

## Detailed Instructions
### To request the data: User will be prompted whether they want to use the a preset. The choices will be printed and the user will send a number to be printed to display.py. 

### Receive Data: Micro.py will then read text file of display.py, save the preset choice and wipe display.py. It will open preset.txt and print based off of (nubmer - 1) to get the specific index of what the user chose. It will then be saved to display.py and send back to the user.

![UML](micro.png)