from flask import Flask, json

from config import config

print(f'Server starting in {config.get("mode")} mode')
app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello(path: str):
    print(path)
    if(path.startswith('api')):
        return handleApiCall

    return "catch all"


if __name__ == '__main__':
    app.run()


def handleApiCall(path: str):
    response = app.response_class()
    response.status_code = 215
    response.response = json.dumps({"test": True})
