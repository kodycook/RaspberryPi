# This file acts as the primary conduit for all local node fucntions of the Pi

version = 0.1
MasterIp = '10.1.1.1'
NodeIp = '10.1.1.10'
NasIp = '10.1.1.3'

class Main:
    def subMainFunction():
        print("SUB")


def init():
    print("TEST")

init()
Main.subMainFunction()
