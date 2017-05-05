#Author: Jennifer Cafiero
#Date: May 5 2017
#HackerRank Python - XML: Find the Maximum Depth

import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    for x in elem.getchildren():
        depth(x, level)
    maxdepth = level if level > maxdepth else maxdepth
    return maxdepth - 1


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
