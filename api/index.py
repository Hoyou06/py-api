# from http.server import BaseHTTPRequestHandler
 
 
# class handler(BaseHTTPRequestHandler):
 
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('Content-type', 'text/plain')
#         self.end_headers()
#         self.wfile.write("DearXuan's API by python!".encode())
#         return
import flask,json
@api.route('/article',methods=['post']) 
def article():
  #url格式参数?id=12589&name='lishi'
  id = flask.request.args.get('id')
    
  if id:
    if id == '12589':
      ren = {'msg':'成功访问文章','msg_code':200}
    else:
      ren = {'msg':'找不到文章','msg_code':400}
  else:
    ren = {'msg':'请输入文章id参数','msg_code':-1}
  return json.dumps(ren,ensure_ascii=False)
