from flask import Flask

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello(path: str):
    print(path)
    if(path.startswith('api')):
        return 'api call'

    return "catch all"


if __name__ == '__main__':
    app.run()
