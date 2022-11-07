# Welcome
Hey there. 
This here is Foxite, an open-source web server made with Python.

## Get Foxite
You can get the most up-to-date stable release under `Releases`.
However you can also get the latest version by cloning the repository. You can do this using git (`git clone https://github.com/FreedTapstry21/Foxite.git`).

## Run Foxite
First, you will need to have Python 3 installed on your system.
To run the program you will have to open python and import the app.py file. On Unix based systems (like Linux or MacOS) you can just run ./app.py in your terminal.

# Troubleshooting
Here are the most common problems and how to solve them.

- Failed to bind to port:
Try to run Foxite as a Administrator (or on unix based systems, as root) otherwise Foxite won't have permissions to access the required port, if that fails then it may be a issue with your firewall or the port is already in use.

- Unable to locate the Foxite module:
app.py was unable to import the foxite.py file. Please dubble check if foxite.py exists in your current working directory.

- Server terminated without error:
There was an internal error and the server could not recover. Please try restarting Foxite.

# License
Go to the LICENSE file for more information about the license that Foxite is using.
