#Author: Jennifer Cafiero
#Date: May 5 2017
#HackerRank Python - XML: Find the Score

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    n = len(node.items())
    for i in node.getchildren():
        if len(i.getchildren()) == 0:
            n += len(i.items())
        else:
            n += get_attr_number(i)
    return n


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
