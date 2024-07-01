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

| Metric         | FCN                 | DeepLabv3+         | DNLNet              | UPerNet            |
|----------------|---------------------|--------------------|---------------------|--------------------|
| Mean IoU Score | 0.9630              | 0.9736             | 0.9748              | 0.9715             |
| Mean Accuracy  | 0.9676              | 0.9771             | 0.9781              | 0.9753             |
| Mean F1 Score  | 0.9808              | 0.9863             | 0.9868              | 0.9852             |

