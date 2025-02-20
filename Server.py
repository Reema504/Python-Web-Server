import http.server
import socketserver

# Define the port number
PORT = 8080

# Set up the request handler
Handler = http.server.SimpleHTTPRequestHandler

# Start the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Web server is running on port {PORT}")
    print("Press Ctrl+C to stop the server")
    httpd.serve_forever()
