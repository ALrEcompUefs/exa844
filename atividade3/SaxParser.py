import xml.sax
import time
class Listener(xml.sax.ContentHandler):
  def __init__(self):
    self.currentData = []
    self.Tag = ""
    self.cont =0
    self.estb = False

  def startElement(self, tag, attributes):    
    if tag == "node":
        self.Tag = "node"
        self.currentData.append(attributes.get("lat"))
        self.currentData.append( attributes.get("lon") )
    if tag == "tag" and self.Tag == "node":
        if attributes.get("k") == "amenity":
          self.estb= True
          self.currentData.append(attributes.get("v"))
          self.cont+=1
        elif attributes.get("k")== "name":
          self.currentData.append(attributes.get("v"))
      
  def endElement(self, tag):    
    if tag =="node":
      self.Tag=""
      if self.estb:
        print(self.currentData)	
        self.estb = False
      self.currentData= []
      #print("Nome:", self.currentData) 
      #print("id:", self.clientId) 

  def characters(self, content):	
    pass

start_time = time.time()
parser =  xml.sax.make_parser()

Handler = Listener()
parser.setContentHandler(Handler)

print("Starting SAX Parser...")
parser.parse("map.osm")
print("--- %s seconds ---" % (time.time() - start_time))
print(Handler.cont)