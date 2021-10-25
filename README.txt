Author: Paula Wilhelm
Date: 25.10.2021
Sources: https://github.com/luyanger1799/Amazing-Semantic-Segmentation, https://github.com/bonlime/keras-deeplab-v3-plus

# TRAINING #

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
- model is stored in the folder "weights" (this contains for example DMN2_OS8, which was used for the study)
- plots are stored in the folder "plots" (referring to miou and loss over epochs)

# TEST #

- use test.py 
- set parameters (lines 20-28)
- output: MeanIoU, Precision, Sensitivity


# PREDICTION / PREDICITON WITH INCLUDING EROSION #

- use predict.py resp. predic_erode.py
- execute file via terminal 
- Parameters:
    --model:            DeepLabV3Plus
    --base_model:       MobileNetV2
    --csv_file:         The path of colour code csv file
    --num_classes':     The number of classes to be segmented
    --crop_height':     The height to crop the image
    --crop_width':      The width to crop the image
    --weights':         The path of weights to be loaded
    --image_path':      The path of predicted image
    --color_encode':    Whether to colour encode the prediction
- example command:  python predict.py --model DeepLabV3Plus --base_model MobileNetV2 
                    --csv_file /app/shared/dataset/class_dict.csv --num_classes 2 
                    --weights /app/shared/Amazing-Semantic-Segmentation/weights/DMN2_OS8.h5 
                    --image_path /app/shared/dataset/test/images_ua/resized_0015.jpg 

# EVALUATE #

- use evaluate.py 
- evaluate already predicted images 
- set parameters (lines 18-21)
- output: MeanIoU, Precision, Sensitivity

# RUNTIME

- is calculated in predict.py and predict_erode.py
- time from loading the image to segmentation is stored for each image in duration.txt
- IMPORTANT: delete first line in duration.txt
- for average running time of the images: mean_duration.py









