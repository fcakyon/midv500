import os
import cv2
import json
import argparse
import numpy as np
from tqdm import tqdm
from utils import list_annotation_paths_recursively, get_bbox_inside_image, create_dir

def convert(root_dir, export_dir):
    """
    Walks inside root_dir (should oly contain original midv500 dataset folders), 
    reads all annotations, and creates coco styled annotation file 
    named as midv500_coco.json saved to export_dir.
    Sample inputs:
        root_dir: ~/data/midv500/
        export_dir: ~/data/
    """
    
    # raise error if export_dir is given as a json file path
    if "json" in export_dir:
        raise ValueError('export_dir should be a directory, not a file path!')
        
    # create export_dir if not present
    create_dir(export_dir)
    
    # init coco vars
    images = []
    annotations = []
    
    annotation_paths = list_annotation_paths_recursively(root_dir)
    print("Converting to coco.")
    for ind, rel_annotation_path in enumerate(tqdm(annotation_paths)):
        # get image path
        rel_image_path = rel_annotation_path.replace("ground_truth","images")
        rel_image_path = rel_image_path.replace("json","tif")
        
        # load image
        abs_image_path = os.path.join(root_dir, rel_image_path)
        image = cv2.imread(abs_image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # prepare image info
        image_dict = dict()
        image_dict["file_name"] = rel_image_path
        image_dict['height'] = image.shape[0]
        image_dict['width'] = image.shape[1]
        image_dict['id'] = ind
        # add image info
        images.append(image_dict)
        
        # form image regions
        image_xmin = 0
        image_xmax = image.shape[1]
        image_ymin = 0
        image_ymax = image.shape[0]
        image_bbox = [image_xmin, image_ymin, image_xmax, image_ymax]
        
        # load mask coords
        abs_annotation_path = os.path.join(root_dir, rel_annotation_path)
        quad = json.load(open(abs_annotation_path, 'r'))
        mask_coords = quad['quad']
        
        # create mask from poly coords
        mask = np.zeros(image.shape, dtype=np.uint8)
        mask_coords_np = np.array(mask_coords, dtype=np.int32)
        cv2.fillPoly(mask, mask_coords_np.reshape(-1, 4, 2), color=(255,255,255))
        mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
        mask = cv2.threshold(mask, 0,255, cv2.THRESH_BINARY)[1]
        
        # get voc style bounding box coordinates [minx, miny, maxx, maxy] of the mask
        label_xmin = min([pos[0] for pos in mask_coords])
        label_xmax = max([pos[0] for pos in mask_coords])
        label_ymin = min([pos[1] for pos in mask_coords])
        label_ymax = max([pos[1] for pos in mask_coords])
        label_bbox = [label_xmin, label_ymin, label_xmax, label_ymax]
        label_bbox = get_bbox_inside_image(label_bbox, image_bbox)
        
        # calculate coco style bbox coords [minx, miny, width, height] and area
        label_area = int((label_bbox[2]-label_bbox[0]) * (label_bbox[3]-label_bbox[1]))
        label_bbox = [label_bbox[0], label_bbox[1], label_bbox[2]-label_bbox[0], label_bbox[3]-label_bbox[1]]
        
        # prepare annotation info
        annotation_dict = dict()
        annotation_dict["iscrowd"] = 0
        annotation_dict["image_id"] = image_dict['id']
        annotation_dict['category_id'] = 1 # id card
        annotation_dict['ignore'] = 0
        annotation_dict['id'] = ind
        
        annotation_dict['bbox'] = label_bbox
        annotation_dict['area'] = label_area
        annotation_dict['segmentation'] = [[single_coord for coord_pair in mask_coords for single_coord in coord_pair]]
        # add annotation info
        annotations.append(annotation_dict)
        
    # combine lists and form coco dict
    coco_dict = dict()
    coco_dict["images"] = images
    coco_dict["annotations"] = annotations
    coco_dict["categories"] = [{'name': 'id_card', 'id': 1}]
    
    # export coco dict
    export_path = os.path.join(export_dir, "midv500_coco.json")
    with open(export_path, 'w') as f:
        json.dump(coco_dict, f)
        
if __name__ == '__main__':
    # construct the argument parser
    ap = argparse.ArgumentParser()
    
    # add the arguments to the parser
    ap.add_argument("root_dir", default="data/", help="Directory of the downloaded MIDV-500 dataset.")
    ap.add_argument("export_dir", default="coco/", help="Directory for coco file to be exported.")
    args = vars(ap.parse_args())
    
    # convert dataset
    convert(args['root_dir'], args['export_dir'])