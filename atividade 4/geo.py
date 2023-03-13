from xml.dom.minidom import parse
import time
import json

start_time = time.time()
BancoDocument = parse('map.osm')
print("--- %s seconds ---" % (time.time() - start_time))
dim = dict()
# cria json das features
dim["type"] ="FeatureCollection"
# array para as features
colecao = []
propriedades = dict()
#iniciliza propriedades
propriedades["nome"]="nome"
propriedades["tipo"]="tipo"
feature = dict()
#inicializa feature
feature["type"]="Feature"
#feature["geometry"]
#feature["properties"]
ponto = dict()
#inicializa ponto
ponto["type"]= "Point"
ponto["coordinates"]=[]
ok = False
print("Iniciando extração do aquivo")
for c in BancoDocument.getElementsByTagName("node"):
	

	propriedades["nome"]="name"
	for sub_Element in c.getElementsByTagName("tag"):
		#print(c.getAttribute("k"))
		if sub_Element.getAttribute("k") == "amenity":
			ok = True
			coords =[]
			coords.append(c.getAttribute("lon"))
			coords.append(c.getAttribute("lat"))
			ponto["coordinates"]=coords
			propriedades["tipo"]= sub_Element.getAttribute("v")

			#print("latitude: ",c.getAttribute("lat"))
			#print("longitude: ",c.getAttribute("lon"))
			#print("Tipo:", sub_Element.getAttribute("v"))
			feature["geometry"]=ponto
		if sub_Element.getAttribute("k") == "name" and ok:
			propriedades["nome"]=sub_Element.getAttribute("v")
			feature["properties"]=propriedades
			colecao.append(feature)
			#print(feature)
			print("\n")
			#print("Nome:",sub_Element.getAttribute("v"),"\n")
			ok = False
			coords.clear()
#print(len(colecao))
dim["features"]= colecao
jsonStr = json.dumps(dim, indent=4, ensure_ascii=False)
arquivo = open("data.json","w")
arquivo.write(jsonStr)
print(jsonStr)