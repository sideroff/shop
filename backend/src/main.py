from flask import Flask, json, request
from werkzeug.routing import Rule, BaseConverter

from config import config
from services import hub
from messages import internal_server_error

app = Flask(config.get('name'))


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def request_handler(path: str):
    try:
        # handle file calls
        # handle all other calls => index.html

        # handle api calls
        if path.strip('/') == 'api':
            data = request.json

            method = data.get('method')
            params = data.get('params', dict())

            return handle_api_call(method, params)
    except Exception as e:
        # return full exception in development mode
        if config.get('mode') == 'development':
            raise e
        return json.dumps(internal_server_error)

        print('exception happened ' + e.with_traceback(None))

    return path + ' ' + request.method


def handle_api_call(method: str, params: dict):
    [service_provider, service_name] = method.split('.')

    return hub.execute_request(service_provider, service_name, params)
    # response = app.response_class()
    # response.status_code = 215
    # response.response = json.dumps({"test": True})


if __name__ == '__main__':
    if config.get('mode') == 'development':
        app.debug = True

    app.env = config.get('mode', 'production')
    app.run()
