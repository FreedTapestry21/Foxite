# Welcome
Hey there! Nice to see you here!
This here is Foxite, an open-source web server made with Python.

## Get Foxite
You can get the most up-to-date stable release under `Releases`.
However you can also get the latest unstable version by just cloning the repository. You can do this by downloading it or using a tool like git.

## Run Foxite
First, you will need to have Python 3 installed on your system.
Now to run the program, open python and import the app.py file, or if you're using a unix based system (like Linux or MacOS) you can just run ./app.py in your terminal.

# Troubleshooting
Here are the most common problems and how to solve them!

- Failed to bind to port:
Try to run Foxite as a Administrator (or on unix based systems, as root) otherwise Foxite won't have permissions to access the port, if that fails then it may be a issue with your firewall or the port is already in use.

- Unable to locate the Foxite module:
app.py was unable to import the foxite.py file. Please dubble check if foxite.py exists.

- Server terminated without error:
There was an internal error and the server could not recover. Please try restarting Foxite.

# License
Go to the LICENSE file for more information about the license that Foxite is using.
