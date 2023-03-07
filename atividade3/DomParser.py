from xml.dom.minidom import parse
import time

start_time = time.time()
BancoDocument = parse('map.osm')
print("--- %s seconds ---" % (time.time() - start_time))
ok = False
print("Iniciando extração do aquivo")
for c in BancoDocument.getElementsByTagName("node"):
	for sub_Element in c.getElementsByTagName("tag"):
		
		#print(c.getAttribute("k"))
		if sub_Element.getAttribute("k") == "amenity":
			ok = True
			print("latitude: ",c.getAttribute("lat"))
			print("longitude: ",c.getAttribute("lon"))
			print("Tipo:", sub_Element.getAttribute("v"))
		if sub_Element.getAttribute("k") == "name" and ok:
			print("Nome:",sub_Element.getAttribute("v"),"\n")
			ok = False
	