import xml.dom.minidom as minidom


xml_file = open('currency.xml', 'r')
xml_data = xml_file.read()

dom = minidom.parseString(xml_data)
dom.normalize()

elements = dom.getElementsByTagName('Valute')
values_dict = {}

for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'Value':
                if child.firstChild.nodeType == 3:
                    value = str(child.firstChild.data)
                    if ',' in value:
                        value = value.replace(',','.')
                    value = float(value)
            if child.tagName == 'Name':
                if child.firstChild.nodeType == 3:
                    name = child.firstChild.data
    values_dict[name] = value



print(values_dict)


xml_file.close()