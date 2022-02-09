import xml.etree.ElementTree as ET
filename = "../Analysis/analysis.xml"
tree = ET.parse(filename)
root= tree.getroot()


runda=int(root[0].text)
print(runda)
runda=runda+1
print(runda)
root[0].text=str(runda)

tree.write(filename)



