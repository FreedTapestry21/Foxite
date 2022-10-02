#!/bin/python3

#
# Foxite Server v1.0.0
# Copyright (c) 2022 FreedTapstry21
#

# Library imports
import socket, json, os, sys

# Startup message
STARTMSG = """
Welcome to Foxite Server!
Version 1.0.0
Copyright (c) 2022 FreedTapstry21
"""

# Database
database = {
    "version": "1.0.0",
    "license": "MIT",
    "author": "FreedTapstry21"
}

# notify class
# Used for logging info onto the Terminal display
class notify:
    def __init__(self):
        self.msg= []

    def clear(self):
        self.msg = []

    def info(self, msg):
        self.msg.append("[INFO] " + str(msg))

    def error(self, msg):
        self.msg.append("[ERROR] " + str(msg))

    def raw_print(self, msg):
        self.msg.append(str(msg))

    def print(self):
        for x in self.msg:
            print(x)
        self.clear()

# server class
# Used for starting the server
class server:
    def __init__(self):
        pass
    
    def get_url(self):
        # Waits untill client excepts
        self.client_sock, self.client_addr = self.sock.accept()
        request = self.client_sock.recv(1024).decode()

        # Checks if it's a HTTP GET request is, if not then closes the connection
        if request.split(' ')[0] != "GET":
            self.client_sock.close() 

        # Splits the headers
        headers = request.split('\n')
        url = headers[0].split()[1]
        adv_url = url.split("/")

        adv_url.pop(0)

        return url, adv_url

    def get_file(self, dir, url):
        found = False
        if found == False:
            try:
                file = open(dir + url + ".html", "r")
                found = True
            except:
                pass
        if found == False:
            try:
                file = open(dir + url, "r")
                found = True
            except:
                pass
        if found == False:
            file = open("404.html", "r")
            return 1, file.read()
        else:
            return 0, file.read()
    
    def get_settings(self):
        try:
            file = open("settings", "r")
            self.settings = json.load(file)
            Notify.raw_print("Settings: \n    Host: " + str(self.settings["host"]) + " \n    Port: " + str(self.settings["port"]) + " \n    Listeners: " + str(self.settings["listeners"]) + " \n    Web directory: " + str(self.settings["webdir"]) + " \n    api Link: " + str(self.settings["api_link"] + ""))
        except:
            Notify.info("Configuration file is missing or corrupt! Resetting configuration...")
            file = open("settings", "w")
            file.write("""{"host": "0.0.0.0", "port": 80, "listeners": 25, "webdir": "web", "api_link": "api"}""")
            file.close()
            self.settings = {"host": "0.0.0.0", "port": 80, "listeners": 25, "webdir": "web", "api_link": "api"}
            Notify.info("Done!")
        return 0

    def bind(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.bind((host, port))
        except:
            Notify.error("Failed to bind to port!")
            return 1
        self.sock.listen(self.settings["listeners"])
        return 0
                

# api class
# Usage: A separate api Server for api calls.
class api:
    def __init__(self):
        pass
    
    def detect(self, adv_url):
        if adv_url[0] == Server.settings["api_link"]:
            return "rest_api"
        else:
            return "web_api"

    def web_api(self, url):
        # Web
        if url == "/":
            url = "/index.html"
        
        status, data = Server.get_file(Server.settings["webdir"], url)

        if status == 0:
            Notify.info("[web] " + str(Server.client_addr) + " requested " + str(url))
        elif status == 1:
            Notify.info("[web] " + str(Server.client_addr) + " requested " + str(url) + " but the file was not found!")
        else:
            Notify.error("[web] " + str(Server.client_addr) + " requested " + str(url) + " but the get_file function returned an unknown status code.")
        
        response = data
        Server.client_sock.send(response.encode())

        return 0

    def rest_api(self, url, adv_url):
        adv_url.pop(0)

        req = adv_url[0]

        if req == "version": data = database["version"]; status = 0
        elif req == "license": data = database["license"]; status = 0
        elif req == "author": data = database["author"]; status = 0
        else: status = 1

        if status == 0: Notify.info("[api] " + str(Server.client_addr) + " requested " + str(url))
        elif status == 1: Notify.info("[api] " + str(Server.client_addr) + " requested " + str(url) + " but the server was unable to complete the api call.")
        else: Notify.error("[api] " + str(Server.client_addr) + " requested " + str(url) + " but the server returned an unknown status code.")

        response = data
        Server.client_sock.send(response.encode())

        return 0

# app class
# Usage: Starting and controlling the Server
class app:
    def __init__(self):
        pass
    def run(self):
        global Notify

        Notify = notify()

        Notify.raw_print(STARTMSG)
        Notify.info("Loading settings...")
        Notify.print()
        Notify.raw_print("")

        # Loads settings from JSON file, if fails make a new JSON file
        status = Server.get_settings()

        Notify.raw_print("")

        if status == 1: Notify.print(); return 1
        else: Notify.print()

        # Checks and setting variables
        current_dir = os.getcwd()
        
        try: os.chdir(Server.settings["webdir"]); os.chdir(current_dir)
        except: os.mkdir(Server.settings["webdir"])

        host = Server.settings["host"]
        port = Server.settings["port"]

        status = Server.bind(host, port)

        if status == 1: Notify.print(); return 1
        else: Notify.print()

        Notify.info("Now listening on " + str(host) + ":" + str(port))
        Notify.info("Press Ctrl+C to exit!")
        Notify.raw_print("")
        Notify.print()

        while True:
            url, adv_url = Server.get_url()
            type = Api.detect(adv_url)
            if type == "web_api":
                status = Api.web_api(url)
                Server.client_sock.close()
                Notify.print()
            elif type == "rest_api":
                status = Api.rest_api(url, adv_url)
                Server.client_sock.close()
                Notify.print()
            else:
                Server.client_sock.close()
                Notify.error(str(Server.client_addr) + " requested an unknown api call.")
                Notify.print()

# Define classes
Notify = notify()
Server = server()
Api = api()
App = app()

#
# End of file
#