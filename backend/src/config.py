import sys
import os
import socket

from utils import get_dictionary_from_cli_args

ARGV = get_dictionary_from_cli_args(sys.argv)

DEVELOPMENT = 'development'

NAME = __name__

MODE = os.getenv('MODE', DEVELOPMENT)

# SERVER config
HOST = os.getenv('HOST', socket.gethostbyname(socket.gethostname()))
PORT = os.getenv('PORT', 8080)

