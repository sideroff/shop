import sys

from utils import get_dictionary_from_cli_args

argv_dictionary = get_dictionary_from_cli_args(sys.argv)

config = {
    'name': __name__,
    'mode': argv_dictionary['named'].get('mode', 'development'),
    'argv': argv_dictionary,
    'server': {
        'methods': ['GET', 'POST', 'PUT', 'PATCH', "DELETE"],
        'api_methods': ['GET', 'POST']
    }
}
