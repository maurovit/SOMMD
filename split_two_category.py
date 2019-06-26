import pandas as pd
import cv2
import glob

def load_dataset():
    # all_labels è un dizionario dove come chiave abbiamo il nome dell'immagine (univoco) e come valore: 'mel' o 'not mel'
    all_labels = load_dataset_labels()

    # Inseriamo in filenames tutte le immagini da splittare del dataset
    filenames = glob.glob(DATASET_DIR + "*.jpg")

    for img_name in filenames:

        # Leggiamo l'immagine
        img = cv2.imread(img_name, cv2.IMREAD_COLOR)

        # Estraiamo dall'intero path, solo il nome dell'immagine
        key = img_name.split("\\")[1].split(".")[0]

        # Se è un melanoma allora la salviamo nella cartella predisposta
        if (all_labels[key] != 'mel'):
            cv2.imwrite(NOT_MELANOMA_DIR + key + ".jpg", img)
        else:

            # Se non è un melanoma allora la salviamo nella cartella predisposta
            if (all_labels[key] == 'mel'):
                cv2.imwrite(MELANOMA_DIR + key + ".jpg", img)

def load_dataset_labels():

    # Leggiamo il csv
    df = pd.read_csv(CSV_DATASET_PATH)
    lables_list = []

    # Per ogni nome dell'immagine (image_id) e lezione cutanea associata ad essa (dx)
    for im_id, label in zip(df['image_id'], df['dx']):
        # Aggiungiamo un elemento <nome_dell'immagine, lesione cutanea> alla lista
        lables_list.append((im_id, label))

    # Ritorniamo la lista trasformata in un dizionazio
    return dict(lables_list)


if __name__ == "__main__":

    # Inserire il path del file csv
    CSV_DATASET_PATH = ""

    # Inserire il path del dataset di immagini
    DATASET_DIR = 'dataset/HAM_240x180/'

    # Inserire il path della cartella dove salvare le immagini relative a lesioni cutanee di tipo melanoma
    MELANOMA_DIR = 'dataset/melanoma_images_240x180/'

    # Inserire il path della cartella dove salvare le immagini non relative a lezione cutanee di tipo melanoma
    NOT_MELANOMA_DIR = 'dataset/not_melanoma_images_240x180/'

    load_dataset()