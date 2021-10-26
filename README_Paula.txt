Author: Paula Wilhelm
Date: 26.10.2021
Sources: https://github.com/luyanger1799/Amazing-Semantic-Segmentation, https://github.com/bonlime/keras-deeplab-v3-plus


# TRAINING #

- dataset must comply with the following structure

    |-- dataset
    |  |-- train
    |  |  |-- images
    |  |  |-- labels
    |  |-- valid
    |  |  |-- images
    |  |  |-- labels
    |  |-- test
    |  |  |-- images
    |  |  |-- labels
    |  |-- class_dict.csv
    |  |-- evaluated_classes.txt

- data prepocessing: data_preprocessing.ipynb
    - images will be divided as in the study work by Leo Misera
    - resolution of all images will be reduced to 512x512
    - creation of the augmented data sets with imgaug

- use train.py 
- set parameters (lines 25-59)
- specify model definition (line 71):
    weights:        'pascal_voc' / 'cityscapes' / None
    input_tensor:   optional Keras tensor (i.e. output of 'layers.Input()') to use as image input for the model
    classes:        already set by num_classes
    backbone:       'xception' / 'mobilenetv2'
    activation:     'softmax' / 'sigmoid' / None
    OS:             8 / 16
    alpha:          1 as default (refers to mobiletv2 as backbone)
- use docker (optimistic_wilson) to perform training on the GPU 
- model is stored in the folder "weights" (this contains for example DMN2_OS8, which was used for this study)
- plots are stored in the folder "plots" (referring to miou and loss over epochs)


# TESTING #

- use test.py 
- set parameters (lines 23-29)
- output: MeanIoU, Precision, Sensitivity


# PREDICTION / PREDICTION WITH INCLUDING EROSION #

- use predict.py resp. predic_erode.py
- execute file via terminal 
- Parameters:
    --model:            DeepLabV3Plus
    --base_model:       MobileNetV2
    --csv_file:         The path of colour code csv file
    --num_classes:      The number of classes to be segmented
    --crop_height:      The height to crop the image
    --crop_width:       The width to crop the image
    --weights:          The path of weights to be loaded
    --image_path:       The path of predicted image
    --color_encode':    Whether to colour encode the prediction
- example command:  python predict.py --model DeepLabV3Plus --base_model MobileNetV2 
                    --csv_file /app/shared/dataset/class_dict.csv --num_classes 2 
                    --weights /app/shared/Amazing-Semantic-Segmentation/weights/DMN2_OS8.h5 
                    --image_path /app/shared/dataset/test/images_ua/resized_0015.jpg 
- predictions are stored in the folder "predicitions" resp. "eroded_predictions"


# EVALUATION #

- use evaluate.py 
- evaluate already predicted images 
- set parameters (lines 18-21)
- output: MeanIoU, Precision, Sensitivity of the classes specified in evaluated_classes.txt (see dataset structure)


# RUNTIME #

- is calculated in predict.py and predict_erode.py
- time from loading the image to segmentation is stored for each image in duration.txt
- IMPORTANT: delete first line in duration.txt (since libraries are opened for the first image, this value is incorrect)
- for average running time of the images: mean_duration.py









