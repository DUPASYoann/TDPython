import cgitb; cgitb.enable()  # Permet d'afficher les logs CGI
import http.server
PORT = 8001
server_address = ('', PORT)
server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ['/']
print("Serveur actif sur le port :", PORT)
httpd = server(server_address, handler)
httpd.serve_forever()


