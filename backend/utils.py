
def get_dictionary_from_cli_args(argv):
    '''
        Args: sys.argv

        Returns:
        A dictionary with the following structure:
        dict = {
            "named": {
                <key>: <value>
            },
            "unnamed": [
                <value>
            ]
        }

        where named are any arguments passed in that are in the format: <key>=<value> and unnamed are just: <value>
    '''

    dictionary = {
        "named": dict(),
        "unnamed": []
    }

    # skip first item as it is the file name that has been run
    argv = argv[1:]

    for arg in argv:
        if '=' in arg:
            # named param
            splitted = arg.split('=')
            dictionary["named"][splitted[0]] = splitted[1]
        else:
            # unnamed param
            dictionary["unnamed"].append(arg)

    return dictionary
