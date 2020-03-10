from os import getpid
import http.server
import socketserver

HOST = '127.0.0.1'
PORT = 8080

MAX_HEADERS_LENGTH = 8192
MAX_BODY_LENGTH = 16384

HTTP_VERSION = 'HTTP/1.1'
HTTP_CODES = {
    200: '200 OK',
    400: '400 Bad Request',
    413: '413 Payload Too Large',
    500: '500 Internal Server Error'
}


def serialize_response(http_code: int, headers: list = [], body: str = '') -> bytes:
    global HTTP_CODES
    # Status line
    response = f'{HTTP_VERSION} {HTTP_CODES[http_code] if HTTP_CODES[http_code] else HTTP_CODES[500]}'

    # Headers
    for header_name, header_value in headers:
        response += f'\r\n {header_name}: {header_value}'

    # Empty Line
    response += '\r\n\r\n'

    # Body
    response += body

    return bytes(response, encoding='utf-8')


def deserialize_request(request, max_headers_length=MAX_HEADERS_LENGTH, max_body_length=MAX_BODY_LENGTH):
    data = request.recv(max_headers_length)

    index_where_headers_end = data.find(b'\r\n\r\n')

    if index_where_headers_end == -1:
        print(f'Headers not found in first {max_headers_length} bytes, 413')
        request.sendall(serialize_response(http_code=413))
        return False

    print(f'Headers found in first {max_headers_length} bytes, 200')
    request.sendall(serialize_response(http_code=200))


class RequestHandler(socketserver.BaseRequestHandler):
    def setup(self):
        # self.cache = redis.get_or_create_cache()
        # self.db = db.get_or_create_connection()
        print('setup called')

    def handle(self):
        print('request received')
        deserialize_request(self.request)

    def finish(self):
        print('finish called')


with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
    print(f'server #{getpid()} running on port {HOST}:{PORT}')
    httpd.serve_forever()
