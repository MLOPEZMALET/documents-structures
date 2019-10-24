#!/usr/bin/env python

from lxml import etree


xmlfile = "valery_ame-et-danse_1921.xml"

TEI_NAMESPACE = "http://www.tei-c.org/ns/1.0"
TEI = "{%s}" % TEI_NAMESPACE

# Initialiser la lecture du fichier
tree = etree.parse(xmlfile)

# Le contenu en tant que string
#print(etree.tostring(tree))

# La racine
root = tree.getroot()

# Itérer à travers tout le document
#for element in root.iter():
#    print(element.tag, element.text)

# Obtenir le tag et valeur des enfants de <titleStmt>
for element in root.iter(TEI + 'edition'):
    print("edition : %s" %element.text)

for element in root.iter(TEI + 'licence'):
    print("licence : %s" %element.attrib.get('target'))
# Afficher les attributs (dictionnaire)
#print(root.attrib)

d = {}
for element in root.iter(TEI + 'label'):
    if element.attrib.get('type') == 'speaker':
        speaker = element.text
        d[speaker] = d.get(speaker, 0)+1
print("Speakers : ", d)
print("Speaker avec le plus de réplique : ", sorted(d.items(), key=lambda x: x[1], reverse=True)[0])


# Afficher un attribut particulier
#print(root.get('{http://www.w3.org/XML/1998/namespace}' + 'lang'))

# Ajouter un attribut
root.set('nouvel-attribut', 'documentsStructures')
#print(root.attrib)

# Ajouter un enfant
text = etree.SubElement(root, "text")
#text.text = "un texte"
#text.set("un-attribut", 'une-valeur')

