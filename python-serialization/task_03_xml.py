#!/usr/bin/python3
"""
This module is to explore serialization and deserialization using XML as an alternative
format to JSON.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    This function takes a Python dictionary and a filename,
    serializes the dictionary into XML format,
    and saves it to the given filename.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Create ElementTree object from the root
    tree = ET.ElementTree(root)

    # Write XML tree to the provided filename
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    This function takes a filename as
    its parameter, reads the XML data from that file,
    and returns a deserialized Python dictionary.
    """
    try:
        # read and parse the XML file
        tree = ET.parse(filename)

        # get the root element:
        root = tree.getroot()

        # read the child elements and reconstruct dictionary
        data_dict = {}
        for child in root:
            data_dict[child.tag] = child.text
        return data_dict

    except Exception:
        return {}
