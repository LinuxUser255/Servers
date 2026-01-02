import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

"""Basic HTTP Server in Python"""


# Create a simple HTTP server handler class
class SimpleHandler(BaseHTTPRequestHandler):

    # Create a method to Handle GET Requests, creating endpoints for different paths
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('web/index.html', 'rb') as f:
                self.wfile.write(f.read())

        elif self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            response = {
                'status': 'ok',
                'message': 'Python server is running',
                'port': 8000
            }
            self.wfile.write(json.dumps(response).encode())

        elif self.path.startswith('/css/'):
            try:
                file_path = 'web' + self.path
                self.send_response(200)
                self.send_header('Content-type', 'text/css')
                self.end_headers()
                with open(file_path, 'rb') as f:
                    self.wfile.write(f.read())
            except FileNotFoundError:
                self.send_error(404, 'File not found')

        elif self.path.startswith('/js/'):
            try:
                file_path = 'web' + self.path
                self.send_response(200)
                self.send_header('Content-type', 'application/javascript')
                self.end_headers()
                with open(file_path, 'rb') as f:
                    self.wfile.write(f.read())
            except FileNotFoundError:
                self.send_error(404, 'File not found')

        else:
            self.send_error(404, 'File not found')

    # Create a method to Handle Post Requests
    def do_POST(self):
        if self.path == '/api/echo':
            length = int(self.headers['Content-Length'])
            body = self.rfile.read(length).decode()
            self.send_json({"received": body})

    # Create helper methods: Send text and JSON responses
    def send_text(self, message):
        """sending a plain text response and headers"""
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())

    # sending a json response
    def send_json(self, data):
        """sending a json response of the response code and headers"""
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        # write the json data to the response
        self.wfile.write(json.dumps(data).encode())

    # Tie in index.html file to serve static files
    def serve_html(self):
        try:
            file_path = os.path.join(os.path.dirname(__file__), 'web', 'index.html')
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(content.encode())
        except FileNotFoundError:
            self.send_error(404, "index.html not found")

    def serve_static_file(self):
        """serve static files from the web directory"""
        try:
            file_path = self.path[5:]  # remove '/web/'
            full_path = os.path.join(os.path.dirname(__file__), 'web', file_path)

            # determine the content type based on the file extension
            if file_path.endswith('.js'):
                content_type = 'application/javascript'
            elif file_path.endswith('.css'):
                content_type = 'text/css'
            else:
                content_type = 'text/plain'

            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()

            self.send_response(200)
            self.send_header('Content-Type', content_type)
            self.end_headers()
            self.wfile.write(content.encode())
        except FileNotFoundError:
            self.send_error(404, f"File not found: {self.path}")


# main function called from main.py, and thus not to be run directly from here
def main():
    """Start the server and listen for incoming connections."""
    port = 8000
    # Create a Server object and bind it to the specified port number
    server = HTTPServer(('', port), SimpleHandler)

    print(f"Server running at http://localhost:{port}")
    print("Press Ctrl+C to stop")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\nServer stopped.")
        server.shutdown()

#if __name__ == '__main__':
#    main()
