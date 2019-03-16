./Dataset contains all images and corresponding xml files with ground truths.

Download Dataset from https://drive.google.com/drive/folders/1O-Yv8JHo4jM2JDpx7pMyhLPHJY1KAH4q
and put into this current folder.

If any changes to the xml annotations, run voc2coco.py file. This updates/converts any
changes and outputs dataset.json (COCO format).

To generate a random train, val, and test set, run dataset_creator.py.
This splits the dataset.json file into 3 files:
 - halomonas_train.json 
 - halomonas_val.json
 - halomonas_test.json
These files are saved to the 'annotations' folder in the 'coco' directory.

The corresponding images are also copied into the relevant directory.
(proejct_train, project_val, project_test)

The final directory tree for the dataset is as follows:
    - coco 
        - annotations
            Relevant JSON file for train, val, and test images
        - project_train
            All training images
        - project_val
            All validation images
        - project_test
            All test images

