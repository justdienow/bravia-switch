"""
Date: Sunday 15th September 2019
Developer: justdienow
Mentions: Photonios at https://github.com/Photonios
GitHub repos used: https://github.com/Photonios/py-sony-bravia-remote
Notes:
This is a proof of concept being a simple command line remote control to turn a Sony Bravia TV 
on and off if you didn't have the actual TV remote near by! This is handy if you were streaming 
to the TV that has a built in chromecast and you suddenly stream to the wrong TV - happens to me.

I plan on porting this to micropython to make an ESP32 button to have in my bedroom - this is where
idea stems from.

Keep in mind that you might want to assign a static IP to your TV and change the name from "ItsThere"
to something else.

Have fun!
"""
from sonybraviaremote import TV, TVConfig

def on_auth():
    return input('Pincode as seen on TV: ')

config = TVConfig('192.168.0.2', 'ItsThere')
tv = TV.connect(config, on_auth)

#print("Is TV on?: " + str(tv.is_on()) + "\n")

userIn = " "
print("Welcome to the Sony Bravia TV remote.\nPlease make a selection of the following:\n   TV On -- i\n   TV off - o\n   Quit --- q") 

while userIn != "q":
    userIn = input()
    if userIn == "i":
        if tv.is_on():
            print("TV is already on!")
        else:
            print("Turning TV On!")
            tv.wake_up()
    elif userIn == "o":
        if not tv.is_on():
            print("TV is already off!")
        else:
            print("Turning TV Off!")
            tv.power_off()
    elif userIn == "q":
        # Dirty work around for having to use a while instead of a do-while
        print("Quiting!")
    else:
        print("Incorrect input!\nPlease make a selection of the following:\n   TV On -- i\n   TV off - o\n   Quit --- q")
