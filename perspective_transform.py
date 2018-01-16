import pickle
import cv2
import glob
import numpy as np
from math import *
import matplotlib.pyplot as plt

def convertBinary(img):
    img = np.copy(img)
    imgHLS = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    imgSbinary = imgHLS[:,:,2]
    sobelx = cv2.Sobel(imgSbinary, cv2.CV_64F, 0, 1, ksize=3)
    sobely = cv2.Sobel(imgSbinary, cv2.CV_64F, 1, 0, ksize=3)
    sobelxy = np.sqrt(sobelx**2 + sobely**2)
    _, sxybinary = cv2.threshold(sobelxy.astype('uint8'), 100, 255, cv2.THRESH_BINARY)

    return sxybinary

def mask(binary):
    masked_binary = np.copy(binary)
    masked_binary[:binary.shape[0]*6//10,:] = 0
    return masked_binary

def warp(img):
    img = np.copy(img)
    src = np.float32([[ 585, 460 ],
                      [ 700, 460 ],
                      [ 1130, 720 ],
                      [ 200, 720 ]])
    img_size = (img.shape[1], img.shape[0])
    offset = 200
    dst = np.float32([[ offset, 0],
                      [ img_size[0] - offset,0],
                      [ img_size[0] - offset, img_size[1]],
                      [ offset, img_size[1]]])

    # Use cv2.getPerspectiveTransform() to get M, the transform matrix
    M = cv2.getPerspectiveTransform(src, dst)
    Minv = cv2.getPerspectiveTransform(dst, src)
    # use cv2.warpPerspective() to warp your image to a top-down view
    warped = cv2.warpPerspective(img, M, img_size)

    return warped, Minv
