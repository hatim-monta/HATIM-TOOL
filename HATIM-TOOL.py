#!/usr/bin/env python3
import sys
import socket
from datetime import datetime
import pyfiglet

def print_banner(text):
    font = pyfiglet.Figlet()
    ascii_art = font.renderText(text)
    print(ascii_art)

if len(sys.argv) != 2:
    print("Invalid number of arguments.")
    print("Syntax: python3 scanner.py <target>")
    sys.exit(1)

target = sys.argv[1]

# Add a pretty banner
print_banner("Hatim Tool")
print("-" * 50)
print("Scanning target: " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(50, 1000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))  # returns an error indicator - 0 if the port is open, otherwise 1
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit(1)

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit(1)

except socket.error:
    print("Could not connect to the server.")
    sys.exit(1)
