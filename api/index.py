from http.server import BaseHTTPRequestHandler
 
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        b = self.path
        a = int(b[-2:])
        self.wfile.write(a.encode()+"###########")
        self.wfile.write("DearXuan's API by python!".encode())
        return
