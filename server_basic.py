"""
Basic HTTP Server in Python

A minimal example demonstrating how HTTP servers work.
Run: python server.py
Test: curl http://localhost:8000
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class SimpleHandler(BaseHTTPRequestHandler):
    """Handle incoming HTTP requests."""

    def do_GET(self):
        """Handle GET requests."""
        if self.path == '/':
            self.send_text("Hello from Python!")

        elif self.path == '/health':
            self.send_json({"status": "ok"})

        else:
            self.send_error(404, "Not Found")

    def do_POST(self):
        """Handle POST requests."""
        if self.path == '/echo':
            # Read the request body
            length = int(self.headers['Content-Length'])
            body = self.rfile.read(length).decode()

            # Echo it back
            self.send_json({"received": body})

        else:
            self.send_error(404, "Not Found")

    # Helper methods
    def send_text(self, message):
        """Send a plain text response."""
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())

    def send_json(self, data):
        """Send a JSON response."""
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())


def main():
    port = 8000
    server = HTTPServer(('', port), SimpleHandler)

    print(f"Server running at http://localhost:{port}")
    print("Press Ctrl+C to stop")

    server.serve_forever()


if __name__ == '__main__':
    main()