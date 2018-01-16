import cv2

def save_image(img,name):
    cv2.imwrite('./output_images/' + name + '.png', img)
