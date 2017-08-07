# import json

# with open ('file.json') as var:
# 	doc= json.loads(var.read())

# print doc['glossary']['GlossDiv']['GlossList']

# var.close()

# d={'key':'value'}
# with open("file.json", 'w') as var:
# 	json.dump(d,var)


# d={'key':'value'}
# with open("file.json", 'a') as var:
# 	json.dump(d,var)

# import xmltodict

# with open("test.xml") as var:
# 	doc= xmltodict.parse(var.read())

# print doc['mydocument']['plus']['@a']

# for i in doc['mydocument']['and']['many']:
# 	print i

# import xml.etree.cElementTree as ET

# root = ET.Element("Element")
# doc = ET.SubElement(root, "doc")

# ET.SubElement(doc, "field1", name="blah").text = "some value1"
# ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"

# var = ET.ElementTree(root)
# var.write("test.xml")

#functional programming

#lambda

# a= lambda x,y:x*y
# print a('hello',3)

#filter

# a=[2,3,6,8,9,7]

# print filter(lambda x:x%2==0, a)

#map:
# a=[2,3,6,8,9,7]

# print map(lambda x:x*2, a)

#reduce
# a=[2,3,6,8,9,7]
# print reduce(lambda x,y:x+y, a)