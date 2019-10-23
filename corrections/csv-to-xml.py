#!/usr/bin/env python

import csv
import xml.etree.ElementTree as ET
import unicodedata

def remove_diacritic(string):
    '''
    http://code.activestate.com/recipes/576648-remove-diatrical-marks-including-accents-from-stri/
    Accept a unicode string, and return a normal string (bytes in Python 3)
    without any diacritical marks.
    '''
    return unicodedata.normalize('NFKD', string).encode('ASCII', 'ignore').decode('utf-8')


racine = ET.Element('tournages')
with open('petit-echantillon.csv', newline='') as csvfile:
    tournages = csv.reader(csvfile, delimiter=';', quotechar='"')

    mapping = {}
    header = next(tournages)
    for i, h in enumerate(header):
        mapping[i] = mapping.get(i, remove_diacritic(h).replace(' ', '-').lower())

    for tournage in tournages:

        attributs = {'date-debut': tournage[6],
                     'date-fin': tournage[7],}
        tournage_element = ET.SubElement(racine, "tournage", attributs)

        for i, info in enumerate(tournage[:5]):

            if mapping[i] == 'adresse':
                x, y = tournage[8].split(',')
                atts = {'arrondissement': tournage[5],
                        'x': x, 'y': y}
                tournage_info = ET.SubElement(tournage_element, mapping[i], atts)
            else:
                tournage_info = ET.SubElement(tournage_element, mapping[i])
            tournage_info.text = info.lower()

xmlfile = ET.tostring(racine)
with open("out.xml", 'w', encoding='utf-8') as fout:
    fout.write(xmlfile.decode('utf-8'))
