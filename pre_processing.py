import cv2
import glob
import numpy as np

# Path dataset
DIRECTORY_DATASET = ""

# Path cartella dove salvare le immagini
DIRECTORY_TARGET = ""

# Scorriamo tutte le immagini
for filename in glob.glob(DIRECTORY_DATASET):

    # Estraiamo il nome dell'immagine letta dal path completo
    img_name = filename.split('\\')[len(filename.split('\\')) - 1]

    # Leggiamo l'immagine
    img = cv2.imread(filename, 1)

    # Creazione del kernel
    kernel = np.ones((10, 10), np.uint8)

    # Operazione di closing
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

    # Operazione di filtering usando un filtro mediano
    median = cv2.medianBlur(closing, 7)
    # gaussian = cv2.GaussianBlur(closing, (3,3), 0) Prova col gaussiano

    # RGB to GRAY
    img_gray = cv2.cvtColor(median, cv2.COLOR_RGB2GRAY)

    # Creazione e disegno dei contorni della lesione cutanea
    ret, thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(median, contours, -1, (0, 250, 0), 1)

    # Sovrapponiamo la maschera all'immagine pulita
    median_matrix = np.asarray(median)
    mask_rgb = cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB)
    mask_rgb_matrix = np.asarray(mask_rgb)
    for i in range(mask_rgb_matrix.shape[0]):
        for j in range(mask_rgb_matrix.shape[1]):
            if (mask_rgb_matrix[i][j][0] == 255 and mask_rgb_matrix[i][j][1] == 255 and mask_rgb_matrix[i][j][2] == 255):
                mask_rgb_matrix[i][j] = median_matrix[i][j]

    # Resize dell'immagine
    dim = (300, 225)
    resized = cv2.resize(mask_rgb, dim, interpolation=cv2.INTER_AREA)

    # Salvataggio dell'immagine
    cv2.imwrite(DIRECTORY_TARGET + '\\' + img_name, resized)
    cv2.waitKey(0)