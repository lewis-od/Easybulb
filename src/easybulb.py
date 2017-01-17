import socket
import struct

# Command codes
COMMAND_OFF = 0x41
COMMAND_ON = 0x42
COMMAND_WHITE = 0xC2
COMMAND_COLOUR = 0x40
COMMAND_BRIGHTNESS = 0x4E
COMMAND_DISCO = 0x4D
COMMAND_DISCO_FASTER = 0x44
COMMAND_DISCO_SLOWER = 0x43

class Easybulb:
    def __init__(self, ip_addr, port=8899):
        """
        :param ip_addr: The ip address of the Easybub hub
        :param port: The port to send the UDP packets to
        """
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__dest = (ip_addr, port)
        self.__packer = struct.Struct('i')

    # Helper method for brightness and colour commands
    def __concat_bytes(self, i1, i2):
        cmd_string = hex(i1) + hex(i2)[2:]
        cmd_int = int(cmd_string, 16)
        return cmd_int

    # Helper method for sending commands to the Easybulb hub via UDP
    def __send_cmd(self, cmd_int):
        cmd_bytes = self.__packer.pack(cmd_int)
        self.__sock.sendto(cmd_bytes, self.__dest)

    def on(self):
        """Turn all lights on"""
        self.__send_cmd(COMMAND_ON)

    def off(self):
        """Turn all lights off"""
        self.__send_cmd(COMMAND_OFF)

    def white(self):
        """Make all lights white"""
        self.__send_cmd(COMMAND_WHITE)

    def colour(self, i):
        """
        Set the colour of all lights
        :param i: A value between 0 and 255 indicating which colour to use
        """
        if i > 255 or i < 0:
            raise Exception("Colour must be between 0 and 255")
        cmd_int = self.__concat_bytes(i, COMMAND_COLOUR)
        self.__send_cmd(cmd_int)

    def brightness(self, i):
        """
        Set the brightness of all lights
        :param i: A value between 0 and 59
        """
        if i < 1 or i > 59:
            raise Exception("Brightness must be between 1 and 59. Got {}".format(i))
        cmd_int = self.__concat_bytes(i, COMMAND_BRIGHTNESS)
        self.__send_cmd(cmd_int)

    def disco(self):
        """Activate disco mode"""
        self.__send_cmd(COMMAND_DISCO)

    def disco_faster(self):
        """Speed up disco mode"""
        self.__send_cmd(COMMAND_DISCO_FASTER)

    def disco_slower(self):
        """Slow down disco mode"""
        self.__send_cmd(COMMAND_DISCO_SLOWER)
