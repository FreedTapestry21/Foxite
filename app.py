#!/bin/python3

#
# Foxite Launcher v1.1.0
# Copyright (c) 2022 FreedTapstry21
#

import sys

try: import foxite
except: print("Error: Unable to locate the Foxite module!"); sys.exit()

try: foxite.app().run()
except KeyboardInterrupt: print(); print("Info: Server stopped."); sys.exit()
except Exception as err: print(); print("Info: An internal error occured and the Foxite server had to shut down. \nError: " + str(err)); sys.exit()

print(); print("Info: Server stopped."); sys.exit()

#
# End of file
#
