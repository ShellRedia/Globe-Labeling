import os
import cv2
from func import *
import numpy as np

type_scene = "SceneColor"
type_base = "BaseColor"

src_dir = "sample"

images, masks = [], []

for img_path in os.listdir(src_dir):
    img_path = "{}/{}".format(src_dir, img_path)
    if type_base in img_path: masks.append(img_path)
    else: images.append(img_path)



for i, (img_path, mask_path) in enumerate(zip(sorted(images), sorted(masks[1:]))):
    if i <= 2: continue
    img, mask = cv2.imread(img_path), cv2.imread(mask_path)
    for j, x in enumerate(segment_mask(mask)):
        label = visualization(img, x)
        cv2.imwrite("temp/{:0>4}-{}.png".format(i, j), label)

