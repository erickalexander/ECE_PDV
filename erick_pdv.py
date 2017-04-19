#Gamepad controller 710
#Make sure to install kernel interpreter evdev
        ##  Check for gamepad information   ##

from evdev import InputDevice, categorize, ecodes
gamepad = InputDevice('/dev/input/event0')
print gamepad


        ##  Recognizes when button pressed  ##

from evdev import InputDevice, categorize, ecodes
gamepad = InputDevice('/dev/input/event0')
for event in gamepad.readloop():
    print event


                    #sample output#

## event at 1432

##
