#imports
import pandas as pd
from collections import defaultdict
import xml.etree.ElementTree as xml
from xml.dom import minidom

#using pandas in order to explore the data
df = pd.read_csv("/home/mlopezmalet/MLOPEZMALET/m2/documents-structures/tournagesdefilmsparis2011.csv", sep=";")
df.info()

#replacing incompatible characters (spaces in attributes)
df["Type de tournage"] = df["Type de tournage"].str.replace("LONG METRAGE", "LONG_METRAGE").str.replace("SERIE TELEVISEE", "SERIE_TELEVISEE")

#filling NaN values
df = df.fillna("0")

#from DataFrame to dictionnary
data = []
for i in range(1,2805):
    data.append(list(df.iloc[i].to_dict().values()))

#filling a dictionnary with one particular column as key
dict_arr = defaultdict(list)
for row in data:
    dict_arr[str(row[5])].append(row)

#creating the XML tree
root = xml.Element("Arrondissements")
for i in dict_arr:
    for k in dict_arr[i]:
        arr = xml.SubElement(root,"Arrondissement")
        arr.text = i
        tournage = xml.SubElement(arr, "Tournage")
        tournage.attrib = {"type": k[4]}
        titre = xml.SubElement(tournage, "Titre")
        titre.text = k[0]
        realisateur = xml.SubElement(tournage, "Realisateur")
        realisateur.text = k[1]
        orga = xml.SubElement(tournage, "Organisme_demandeur")
        orga.text = k[3]
        adresse = xml.SubElement(tournage, "Adresse")
        adresse.text = k[2]
        adresse.attrib = {"date_debut": k[6], "date_fin": k[7],"coordonnees": k[8]}

# checking the tree is fine before writing data: print(xml.tostring(root))

# setting more readable indentations (pretty-print)
def prettify(elem):
    rough_string = xml.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

#creating an xml file
with open("devoir-01MLM.xml", "w+") as f:
    f.write(prettify(root))
