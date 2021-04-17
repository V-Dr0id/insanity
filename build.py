import subprocess, sys

if len(sys.argv[2]) != 0:
    ip = sys.argv[2]
else:
    print("\x1b[1;95mIncorrect Usage!\x1b[0m")
    exit(1) #elliot can you fix this pls

bot = sys.argv[1]
SpaceMan= raw_input("\x1b[1;95mReady To Install Cross Compilers? (Press Enter): \x1b[0m")
if SpaceMan.lower() == "":
    get_arch = True
else:
    get_arch = False
#start
