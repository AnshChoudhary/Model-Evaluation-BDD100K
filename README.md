# Model-Evaluation-BDD100K

This repository contains code for evaluating performances of deep learning models on a custom BDD100K dataset containing only images from the night time. 

## Breakdown of the BDD100K dataset:
Total images = 100,000
Image Split (train : validation : test) = (70 : 10 : 20)

Within the train and test images,
- Time of Day
  - Daytime images: 41,986
  - Nighttime images: 31,900
  - Dawn/Dusk: 5,805
- Weather
  - Clear: 42,690
  - Overcast: 10,009
  - Undefined: 9,276
  - Snowy: 6,318
  - Rainy: 5,808
  - Partly Cloudy: 5,619
  - Foggy: 143

## Run inferences on GPU:
```bash
CUDA_VISIBLE_DEVICES=2 python ./test.py /data/BDD100K/bdd100k/configs/deeplabv3+_r50-d8_512x1024_80k_drivable_bdd100k.py --format-only --format-dir /data/BDD100K/bdd100k/output_masks/deeplabv3+ [--options]
```

## Model Performance on Night-time Images:
Total Images = 3,929

### FCN (fcn_r50-d8_769x769_40k_drivable_bdd100k): 
Mean IoU score: 0.9630112426345298

### DeepLabv3+ (deeplabv3_r50-d8_512x1024_80k_drivable_bdd100k):
Mean IoU score: 0.973638637519474

### DNLNet (dnl_r50-d8_512x1024_80k_drivable_bdd100k):
Mean IoU score: 0.9747568580854796
