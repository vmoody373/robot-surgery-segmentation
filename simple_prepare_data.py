#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 02:29:19 2019

@author: vmoody
"""

from tqdm import tqdm
import cv2
from pathlib import Path

data_path = Path('data')

train_path = data_path / 'train'

cropped_path = data_path / 'cropped_train'

if __name__ == '__main__':
    for file_name in train_path.glob('*.jpg'):
        img = cv2.imread(str(file_name))
        print(file_name)
        
        img = cv2.resize(img, (864, 800)) # img[h_start: h_start + height, w_start: w_start + width]
        cv2.imwrite(str(cropped_path / (file_name.stem + '.jpg')), img,
                        [cv2.IMWRITE_JPEG_QUALITY, 100])