# Research Project
Project aim is to use data augmentation techniques to improve detection score for a deep learning model. The first step will involve traditional data augmentation and transformation and the second step will involve the use of synthetic data generated by DCGAN.

## GAN images
Below is a sample image generated by DCGAN

<img width="860" alt="1" src="https://github.com/ljr97/research-project/blob/master/output/output_gan.jpg">

## Data
Link to all images with corresponding xml annotations -
[Images-with-xml](https://drive.google.com/open?id=1O-Yv8JHo4jM2JDpx7pMyhLPHJY1KAH4q
)

## COCO Format

XML files converted into COCO JSON format can be found here: [coco_format](https://github.com/ljr97/research-project/tree/master/coco_annotations)
These JSON represent data that had been split into train, test, and val sets.

Directory Structure for COCO Format:

* Dataset
  * annotations
    * Contains all JSON annotations
    * (project_train.json,  project_test.json,  project_val.json)
  * project_train
    * Contains all JPGs for project_train.json
  * project_test
    * Contains all JPGs for project_test.json
  * project_val
    * Contains all JPGs for project_val.json

## Class Names

* Halomonas cupida square  
* Idiomarina abyssalis dumbell  
* idiomarina baltica circle
* idiomarina baltic dumbell  
* idiomarina loihensis circle  
* idiomarina loihensis dumbell  
* idiomarina salinarum circle  
* idiomarina salinarum dumbell
* idiomarina sediminum circle  
* idiomarina sediminum dumbell  
* idiomarina sediminum triangle  
* idiomarina zobellii circle  
* idiomarina zobellii dumbell

## Sample Images

| | | 
|:-------------------------:|:-------------------------:|
|<img width="1604" alt="1" src="https://github.com/ljr97/research-project/blob/master/sample_images/107.jpg?raw=true"> Idiomarina abyssalis | <img width="1604" alt="2" src="https://github.com/ljr97/research-project/blob/master/sample_images/111.jpg?raw=true"> Idiomarina abyssalis
| <img width="1604" alt="3" src="https://github.com/ljr97/research-project/blob/master/sample_images/407.jpg?raw=true"> Idiomarina salinarum | <img width="1604" alt="4" src="https://github.com/ljr97/research-project/blob/master/sample_images/408.jpg?raw=true"> Idiomarina salinarum |
<img width="1604" alt="5" src="https://github.com/ljr97/research-project/blob/master/sample_images/508.jpg?raw=true"> Idiomarina sediminum | <img width="1604" alt="6" src="https://github.com/ljr97/research-project/blob/master/sample_images/516.jpg?raw=true"> Idiomarina sediminum |

# Dataset Preperation

# Preprocessing

# Changes from baseline Detectron
cutsom config file located here: [config](https://github.com/ljr97/research-project/blob/master/configs/halomonas_4.yaml)

```yaml
MODEL: 
    TYPE: generalized_rcnn
    CONV_BODY: FPN.add_fpn_ResNet101_conv5_body
    NUM_CLASSES: 15
    FASTER_RCNN: True
NUM_GPUS: 1
SOLVER:
    WEIGHT_DECAY: 0.0001
    LR_POLICY: steps_with_decay
    BASE_LR: 0.0025
    GAMMA: 0.1
    MAX_ITER: 60000
    STEPS: [0, 30000, 40000]
FPN:
    FPN_ON: True
    MULTILEVEL_ROIS: True
    MULTILEVEL_RPN: True
FAST_RCNN:
    ROI_BOX_HEAD: fast_rcnn_heads.add_roi_2mlp_head
    ROI_XFORM_METHOD: RoIAlign
    ROI_XFORM_RESOLUTION: 7
    ROI_XFORM_SAMPLING_RATIO: 2
TRAIN:
    WEIGHTS: https://dl.fbaipublicfiles.com/detectron/ImageNetPretrained/MSRA/R-101.pkl
    DATASETS: ('project_train', 'project_val)
    SCALES: (500,)
    MAX_SIZE: 833
    BATCH_SIZE_PER_IM: 256
    RPN_PRE_NMS_TOP_N: 2000  # Per FPN level
TEST:
    DATASETS: ('project_test',)
    SCALE: 500
    MAX_SIZE: 833
    NMS: 0.5
    RPN_PRE_NMS_TOP_N: 1000  # Per FPN level
    RPN_POST_NMS_TOP_N: 1000
    FORCE_JSON_DATASET_EVAL: True
    OUTPUT_DIR: .
```

# Output

Results from training including model can be found here: [model](https://drive.google.com/open?id=1e4BQjOmhHJrA0eVT7SA230n6XyxBSmpG)

All output pdfs located here: [pdf-output](https://github.com/ljr97/research-project/tree/master/output/pdfs)</p>

Bounding box text size small at the moment, will update soon.

<img width="1604" alt="Idiomarina abyssalis" src="https://github.com/ljr97/research-project/blob/master/output/207.jpg?raw=true">

<img width="1604" alt="Idiomarina abyssalis" src="https://github.com/ljr97/research-project/blob/master/output/212.jpg?raw=true">

<img width="1604" alt="Idiomarina abyssalis" src="https://github.com/ljr97/research-project/blob/master/output/216.jpg?raw=true">

<img width="1604" alt="Idiomarina abyssalis" src="https://github.com/ljr97/research-project/blob/master/output/6.jpg?raw=true">

<img width="1604" alt="Idiomarina abyssalis" src="https://github.com/ljr97/research-project/blob/master/output/616.jpg?raw=true">
