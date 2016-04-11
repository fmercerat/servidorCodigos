from BaseHTTPServer import BaseHTTPRequestHandler
import json
import keyboard
import urlparse
import socket


class PostHandler(BaseHTTPRequestHandler):
    
    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        content_len = int(self.headers.getheader('content-length', 0))
        post_body = self.rfile.read(content_len)
        #print post_body
        par = urlparse.parse_qs(post_body)
        cod = par['codigo'][0]
        #print cod
        resp = "{0}\n\r".format(cod)
        keyboard.EmulaPistola(resp, 100)

        return
    
def PresionaTeclas(data_json):
    res = json.loads(data_json)
    cadena = res['codigo']
    keyboard.Write(cadena, 100)

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('', 8088), PostHandler)
    hostname = socket.gethostbyname(socket.gethostname())
    print 'Iniciando servidor de teclado en {0}:8088\nUse <Ctrl-C> para apagar'.format(hostname)
    server.serve_forever()