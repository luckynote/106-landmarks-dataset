"""
Image visualization result for 106 landmarks
Created by Jacky LUO
Usage: python vis.py 
"""
import os
import cv2
import numpy as np

base_path = '../data/'

if __name__ == '__main__':
    with open("../box_landmark.txt") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split()
            # image_path, box, 106-landmarks
            image_path = line[0]
            b_box = line[1: 5]
            landmarks = line[5:]

            # visualization
            img = cv2.imread(os.path.join(base_path, image_path))
            cv2.rectangle(img, (int(b_box[2]), int(b_box[1])),
                          (int(b_box[0])+int(b_box[2]), int(b_box[1])+int(b_box[3])), (0, 0, 255), 2)
            landmarks = np.reshape(landmarks, (-1, 2))
            for (x, y) in landmarks:
                cv2.circle(img, (int(x), int(y)), 2, (255, 0, 0), -1)
            cv2.imshow("image", img)
            cv2.waitKey(0)
