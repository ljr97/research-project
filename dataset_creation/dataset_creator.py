import sys
import os
import json
import xml.etree.ElementTree as ET
import random
from shutil import copyfile
import shutil

image_set = []
end_json = ['halomonas_train.json', 'halomonas_val.json', "halomonas_test.json"]

def create_dirs(path):
    coco_dir = 'coco'
    try:
        os.makedirs(coco_dir)    
    except FileExistsError as e:
        #print(e)
        pass
    dirs = ['annotations', 'project_train', 'project_val', 'project_test']
    for dir in dirs:
        try:
            os.makedirs(coco_dir + '/' + dir)    
        except FileExistsError:
            files = os.listdir(coco_dir + '/' + dir)
            for file in files:
                try:
                    os.unlink(coco_dir + '/' + dir + '/'  + file)
                except Exception as e:
                    print(e) 
    count_images(path)


def count_images(path):
    dataset_path = path + '/dataset.json'
    anno_path = path + '/' + 'coco' + '/' + 'annotations'
    num_images = 0
    with open(dataset_path, 'r') as f:
        data = json.load(f)
        images = data['images']
        for image in images:
            image_set.append(image['file_name'])
            num_images += 1
        split_data(dataset_path, num_images, image_set, anno_path)
        f.close()


def split_data(dataset_path, num_images, image_set, anno_path):
    train_num = int(num_images * 0.84)
    val_num = int(num_images * 0.11)
    test_num = int(num_images - train_num - val_num)
    random.shuffle(image_set)
    train_set = image_set[:train_num]
    image_set = image_set[train_num:]
    val_set = image_set[:val_num]
    image_set = image_set[val_num:]
    test_set = image_set[:test_num]
    filter_images(dataset_path, [train_set, val_set, test_set], anno_path)


def filter_images(dataset_path, data_split, anno_path):
    end_json_index = -1
    for dataset in data_split:
        end_json_index += 1
        filters2 = []
        image_id_list = []
        image_name_list = []
        filters2 = dataset

        with open(dataset_path, 'r') as f:
            data = json.load(f)
            images = data['images']
            images_new = [x for x in images if x['file_name'] in filters2]
            for image in images_new:
                image_id_list.append(image['id'])
                image_name_list.append(image['file_name'])

            data['images'] = images_new

            with open(anno_path + '/' + end_json[end_json_index], 'w') as f:
                json.dump(data, f)
            f.close()

            copy_image_files(image_name_list, end_json[end_json_index])
            filter_annotations(dataset_path, image_id_list, end_json_index, anno_path)


def filter_annotations(dataset_path, image_id_list, end_json_index, anno_path):
    with open(anno_path + '/' + end_json[end_json_index], 'r') as f:
        data = json.load(f)
        annotations = data['annotations']
        annotations_new = [
            x for x in annotations if x['image_id'] in image_id_list]
        
        category_list = []

        for anno in annotations_new:
            category_list.append(anno['category_id'])
        category_set = set(category_list)

        data['annotations'] = annotations_new

        with open(anno_path + '/' + end_json[end_json_index], 'w') as f:
            json.dump(data, f)
        f.close()

        filter_categories(dataset_path, category_set, end_json_index, anno_path)


def filter_categories(dataset_path, category_set, end_json_index, anno_path):
    with open(anno_path + '/' + end_json[end_json_index], 'r') as f:
        data = json.load(f)
        categories = data['categories']
        categories_new = [
            x for x in categories if x['id'] in category_set]

        data['categories'] = categories_new

        with open(anno_path + '/' + end_json[end_json_index], 'w') as f:
            json.dump(data, f)
        f.close()


def copy_image_files(image_name_list, img_set):
    img_path = 'Dataset/'

    if "val" in img_set:
        image_dir = "project_val/"
    elif "test" in img_set:
        image_dir = "project_test/"
    else:
        image_dir = "project_train/"

    files = os.listdir(img_path)

    for file in files:
        filename, file_extension = os.path.splitext(file)
        if file_extension == '.jpg':
            if file in image_name_list:
                shutil.copy2(img_path + file, 'coco/' + image_dir)
            pass


if __name__ == "__main__":
    if 'Dataset' in os.listdir(os.getcwd()):
        create_dirs(os.getcwd())
    else:
        print('Image directory could not be found')
