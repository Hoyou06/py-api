from http.server import BaseHTTPRequestHandler
 
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        id=id+1
        self.wfile.write("DearXuan's API by python!".encode())
        return (id)
