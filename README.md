# Model-Evaluation-BDD100K

This repository contains code for evaluating performances of deep learning models on a custom BDD100K dataset containing only images from the night time. 

### Run inferences on GPU:
```bash
CUDA_VISIBLE_DEVICES=2 python ./test.py /data/BDD100K/bdd100k/configs/deeplabv3+_r50-d8_512x1024_80k_drivable_bdd100k.py --format-only --format-dir /data/BDD100K/bdd100k/output_masks/deeplabv3+ [--options]
```
