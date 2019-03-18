import cv2
import numpy as np
import os
import xml.etree.ElementTree as ET
from xml.dom import minidom


def loop_files(path):
    y_min_index = 0
    y_max_index = 0

    for file in os.listdir(path + '/resized_dataset/'):
        filename, file_extension = os.path.splitext(file)
        if file_extension == '.jpg':
            horizontal_flip(filename, file_extension)
        elif file_extension == '.xml':
            update_xml(filename, file_extension, y_min_index, y_max_index)


def horizontal_flip(filename, file_extension):
    # Load in image
    image = cv2.imread('resized_dataset/' + filename + file_extension)
    # Flip image horizontally
    horizontal_image = cv2.flip(image, 0)
    new_jpg_name = 'resized_dataset/' + filename + '000' + file_extension
    cv2.imwrite(new_jpg_name, horizontal_image)


def update_xml(filename, file_extension, y_min_index, y_max_index):
    tree = ET.parse('resized_dataset/' + filename + file_extension)
    root = tree.getroot()
    a = root.findall('.//bndbox/*')

    ymin = []
    ymax = []

    for b in a:
        if b.tag == 'ymin':
            ymin.append(b.text)
        elif b.tag == 'ymax':
            ymax.append(b.text)

    for b in a:
        if b.tag == 'ymin':
            b.text = str(int(480 - int(ymax[y_max_index]) - 1 ))
            y_max_index += 1
        elif b.tag == 'ymax':
            b.text = str(int(480 - int(ymin[y_min_index]) - 1 ))
            y_min_index += 1

    new_xml_name = filename + '000' + file_extension
    tree.write('resized_dataset/' + new_xml_name)
    update_path(new_xml_name)


def update_path(new_xml_name):
    filename, _ = os.path.splitext(new_xml_name)
    tree = ET.parse('resized_dataset/' + new_xml_name)
    tree.find('path').text = '/resized_dataset/' + filename + '.jpg'
    tree.write('resized_dataset/' + new_xml_name)
    update_file_name(new_xml_name)


def update_file_name(new_xml_name):
    filename, _ = os.path.splitext(new_xml_name)
    tree = ET.parse('resized_dataset/' + new_xml_name)
    tree.find('filename').text = filename + '.jpg'
    tree.write('resized_dataset/' + new_xml_name)