import glob
import cv2
import numpy as np
import imutils

DIRECTORY_DATASET = ""
DIRECTORY_TARGET = ""

melanoma_filename = []

def data_augmentation():

    i = 0

    for a in glob.glob(DIRECTORY_DATASET):

        img = cv2.imread(a, 1)

        # Flipping image
        flipped_img = np.fliplr(img)

        # Rotate flipped "
        rotated_flipped_180 = imutils.rotate(flipped_img, 180)
        # rotated_flipped_90 = imutils.rotate(flipped_img, 90)

        # Flipping rotated
        # flipped_img_90 = np.fliplr(rotated_flipped_90)

        # Vertical flip
        # vertical_flip_img = img[::-1,:]


        # Rotate 45 - 90
        # rotated_45 = imutils.rotate(img, 45)
        #rotated_inverse_45 = imutils.rotate(img, -45)

        # Save image
        cv2.imwrite(DIRECTORY_TARGET+ '\\' + i + ".jpg", flipped_img)
        i+=1
        cv2.imwrite(DIRECTORY_TARGET + '\\' + i + ".jpg", rotated_flipped_180)
        i+=1
        # FARLO PER TUTTE LE IMMAGINI CHE SI VUOLE SALVARE

data_augmentation()
