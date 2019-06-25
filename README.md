# SOMMD
Self Organizing Map for Melanoma Detection

The project, developed in Python, involves the use of unsupervised SOM neural networks for the classification of melanomas, i.e. extremely dangerous and deadly skin cancers.

The structures present in the project will be described below.

The dataset folder has two subfolders, AG_HAM_240x180 and AG_HAM_300x225, which contain preprocessed and augmented images of melanomas and non-melanomas.
AG_HAM_240x180 contains 8000 images of 240x180 size, 50% of which are melanomas and the remaining 50% are non-melanomas.
AG_HAM_300x225 contains 7000 images of 300x225 size, 50% of which are melanomas and the remaining 50% are non-melanomas.
In both cases, the reference images were taken from the HAM10000 dataset, which was made available by the University of Harvard.
There is also a csv file, AGHAM_metadata, which contains information about the images, including the corresponding labels.

The file melanoma_classification.py loads the dataset from the above mentioned directory and normalizes and binaries the dataset in order to transform the images into a monodimensional vector with values in the range [0,1]; after that, it divides the data into two main sets,  i. e. the one of melanomas and non melanomas.
After that the SOM network with the specified hyperparameters is built, it is trained on the dataset and finally tested and validated, respectively, on the test set and on the validation set

Finally, the U-Matrix is displayed to allow the subdivision of neurons of the trained SOM network to be displayed.
