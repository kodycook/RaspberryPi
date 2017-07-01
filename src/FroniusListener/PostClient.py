#!/usr/bin/env python
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import socket

# HTTPRequestHandler class
from bs4 import BeautifulSoup


class PostClient(BaseHTTPRequestHandler):

    def __init__(self):
        run()

def run():
    print('Starting Fronius Listener')

    server = socket.socket()
    server.bind(('10.1.1.15', 40))
    server.listen(4)
    client_socket, client_address = server.accept()
    print(client_address, "has connected")
    while 1 == 1:
        recieved_data = client_socket.recv(1024)
        ConvertJson(recieved_data.decode("utf-8"))



def ConvertJson(text):
    # print(text)

    soup = BeautifulSoup(text, "lxml")
    # print(soup.prettify())
    print(soup.p)

    # print("Timestamp: {0}".format(data["Head"]["Timestamp"]))
    # print("Current Production: {0}{1}".format(data["Body"]["PAC"]["Values"]["1"],data["Body"]["PAC"]["Unit"]))
    # print("Today's Yeild: {0}{1}".format(data["Body"]["DAY_ENERGY"]["Values"]["1"],data["Body"]["DAY_ENERGY"]["Unit"]))
    #print(data[""])
    #print(data[""])