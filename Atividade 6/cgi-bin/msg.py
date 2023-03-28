#!/usr/bin/env python
import os, cgi
form = cgi.FieldStorage()
var = form["mensagem"].value

arquivo = open("mensagens.txt",'w')

print(form["REMOTE_HOST"])
print ("Content-type: text/html;charset=utf-8")
print("")
print ("<html><head><title>Mensagens</title></head><body>")
print ("Nome: "+ var + "<br>")
print ("CONTENT_LENGTH=" +os.environ['CONTENT_LENGTH'] )
print ("</body></html>")
