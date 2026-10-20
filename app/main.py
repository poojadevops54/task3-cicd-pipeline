
from http.server import BaseHTTPRequestHandler, HTTPServer


def greet():
    return "Hello! CI/CD Pipeline is working."


class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Application is healthy")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), HealthCheckHandler)
    print("Application running on port 8000")
    server.serve_forever()
