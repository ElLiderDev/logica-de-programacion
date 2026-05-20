import xml.etree.ElementTree as xml
import os
import json

"""

data={
    "name":"Willie Casimiro",
    "age":'25',
    "dob":"11-02-2000",
    "programming_languages":"Python"
}

xml_file = "ElLiderDev.xml"
#XML

def save_xml():
    root = xml.Element("data")

    for key,value in data.items():
        child = xml.SubElement(root,key)
        child.text = value

    tree = xml.ElementTree(root)
    tree.write(xml_file)

save_xml()

with open(xml_file) as xml_data:
    print(xml_data.read())

os.remove(xml_file)
"""
data={
    "name":"Willie Casimiro",
    "age":'25',
    "dob":"11-02-2000",
    "programming_languages":"Python"
}

json_file = "ElLiderDev.json"
#Json

with open(json_file,"w") as json_data:
    json.dump(data,json_data)

with open(json_file,"r") as json_data:
    print(json_data.read())

os.remove(json_file)