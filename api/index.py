from http.server import BaseHTTPRequestHandler
 
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        return("123")
        self.wfile.write("DearXuan's API by python!".encode())
        return
