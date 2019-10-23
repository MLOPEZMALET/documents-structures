#!/usr/bin/env python

from lxml import etree

xmlfile = "Duchn-etiquetage.txt.xml"
tree = etree.parse(xmlfile)
root = tree.getroot()

# Extraire les déterminants
determinants = set()
for element in root.iter("element"):
    # 'element' contient toujours trois fils
    if (element[0].text)[:3] == "DET":
        determinants.add(element[2].text)

# Les patrons DET-NOM
elements = [_ for _ in root.iter("element")]
for i in range(0, len(elements)-1):
    child = elements[i]
    child_next = elements[i+1]
    if (child[0].text)[:3] == 'DET' and child_next[0].text == 'NOM':
        #print(child[2].text, child_next[2].text)
        pass

# Reconstruire les phrases
sentences = []
sent = []
for child in elements: 
    sent.append(child[2].text)
    if child[0].text == "SENT":
        sentences.append(sent)
        sent = []

# Affichage token/pos/lemme
for child in elements:
    print(f"{child[2].text}/{child[0].text}/{child[1].text}")
