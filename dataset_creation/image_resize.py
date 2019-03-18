import cv2
import numpy as np
import os
import xml.etree.ElementTree as ET
from xml.dom import minidom


width_float = 640.0


def create_dirs(path):
    try:
        os.makedirs('resized_dataset')
    except FileExistsError as e:
        print(e)
    loop_files(path)


def loop_files(path):
    file_folder = 'Dataset/'
    files = os.listdir(file_folder)
    for file in files:
        _filename, file_extension = os.path.splitext(file)
        if file_extension == '.jpg':
            change_img_size(file)
        elif file_extension == '.xml':
            change_xml_size(file)
            update_path(file)


def change_xml_size(xml_file):
    tree = ET.parse('Dataset/' + xml_file)
    root = tree.getroot()
    a = root.findall('.//bndbox/*')

    for b in a:
        b.text = str(int(int(b.text) * 0.125))

    size = root.findall('.//size/*')
    for s in size:
        if s.tag == 'width' or s.tag == 'height':
            s.text = str(int(int(s.text) * 0.125))

    tree.write('resized_dataset/' + xml_file)


def change_img_size(image_name):
    # Load in image
    image = cv2.imread('Dataset/' + image_name)
    # Calculate aspect ratio
    r = width_float / image.shape[1]
    dim = (640, int(image.shape[0] * r))
    # Resize image
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    # Save image
    cv2.imwrite('resized_dataset/' + image_name, resized)


def update_path(xml_file):
    filename, _ = os.path.splitext(xml_file)
    tree = ET.parse('resized_dataset/' + xml_file)
    tree.find('path').text = '/resized_dataset/' + filename + '.jpg'
    tree.write('resized_dataset/' + xml_file)


# if __name__ == "__main__":
#     create_dirs(os.getcwd())
