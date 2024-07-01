import os
import numpy as np
from PIL import Image

def calculate_iou(image1, image2):
    arr1 = np.array(image1)
    arr2 = np.array(image2)
    
    arr1 = (arr1 != 0).astype(np.uint8)
    arr2 = (arr2 != 0).astype(np.uint8)
    
    intersection = np.logical_and(arr1, arr2)
    union = np.logical_or(arr1, arr2)
    
    union_sum = np.sum(union)
    if union_sum == 0:
        return 0.0
    
    iou_score = np.sum(intersection) / union_sum
    return iou_score

def calculate_mean_iou(gt_folder, prd_folder):
    iou_scores = []
    
    # Get list of files in gt_folder
    gt_files = os.listdir(gt_folder)
    
    for filename in gt_files:
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):  # Add more extensions if needed
            gt_path = os.path.join(gt_folder, filename)
            prd_path = os.path.join(prd_folder, filename)
            
            # Check if the file exists in prd_folder
            if os.path.exists(prd_path):
                gt_img = Image.open(gt_path).convert('L')
                prd_img = Image.open(prd_path).convert('L')
                
                iou = calculate_iou(gt_img, prd_img)
                iou_scores.append(iou)
                print(f"IoU for {filename}: {iou}")
            else:
                print(f"Warning: {filename} not found in prediction folder")
    
    if iou_scores:
        mean_iou = np.mean(iou_scores)
        return mean_iou
    else:
        return 0.0

# Specify the paths to your ground truth and prediction folders
gt_folder = '/data/BDD100K/bdd100k/night/masks'
prd_folder = '/data/BDD100K/bdd100k/DNLNet/night'

mean_iou = calculate_mean_iou(gt_folder, prd_folder)
print(f"Mean IoU score: {mean_iou}")