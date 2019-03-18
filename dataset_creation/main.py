import image_resize
import voc2coco
import dataset_creator
import image_prep

import sys
import os


def main():
    if len(sys.argv) > 1:
        image_resize.width_float = float(sys.argv[1])

    path = os.getcwd()

    # Resize images and update path
    image_resize.create_dirs(path)

    # Flips images 
    image_prep.loop_files(path)

    # Convert new dataset to COCO JSON file
    voc2coco.get_xmls()

    # Split JSON file up and return ready COCO dataset
    dataset_creator.create_dirs(path)

if __name__ == "__main__":
    if 'Dataset' in os.listdir(os.getcwd()):
        main()
    else:
        print('Image directory could not be found')
        print('First download Dataset folder from https://drive.google.com/drive/folders/1O-Yv8JHo4jM2JDpx7pMyhLPHJY1KAH4q and put in /Dataset folder ')
