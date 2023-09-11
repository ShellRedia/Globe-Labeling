import numpy as np
import cv2
from collections import *

def visualization(image, mask):
    alpha = 0.5
    return cv2.addWeighted(image.astype(np.float32), 1 - alpha, mask.astype(np.float32), alpha, 0)

def segment_mask(mask)->list:
    g = defaultdict(set)
    h, w, c = mask.shape
    s = set()
    lmt = 20
    cv2.imwrite("test.png", mask)
    for x in range(h):
        for y in range(w):
            color = tuple(mask[x][y])
            for _color in s:
                if abs(sum(color) - sum(_color)) < lmt:
                    color = _color
                    break
            s.add(color)
            g[color].add((x, y))
    rnt = []
    for mt in g:
        mat = np.zeros((h, w, c), dtype=int)
        for v in g[mt]:
            mat[v] = mt
        rnt.append(mat)
    return rnt