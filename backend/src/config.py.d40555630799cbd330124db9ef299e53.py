import sys
import os
import socket

from utils import get_dictionary_from_cli_args

argv_dictionary = get_dictionary_from_cli_args(sys.argv)

DEVELOPMENT = 'development'

NAME = __name__

MODE = os.getenv('MODE', DEVELOPMENT)

ARGV = argv_dictionary

# SERVER config
HOST =os.getenv('HOST',socket.gethostbyname(socket.gethostname())),
HOST = 
