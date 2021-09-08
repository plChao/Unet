# Unet
## 初始步驟

1. clone github
2. cp original image to './data/raw_data/'
3. run './1_img_resize.ipynb' to resize data

## Task_1 take out validation
1. cp label image to visul_label
2. run './2_create_label_for_train.ipynb' to create image in './label/label_for_train/'
3. run './4_train_val_split.ipynb' to create image in './label/train_label' and './label/val_label/'
4. run './3_train_model_Unet.ipynb' to create weight
5. run './3_test_model_Unet.ipynb' to create visual_label image in './result/seg_raw/' 
6. run './5_get_predict_IOU.ipynb' using './label/val_label/' and './result/seg_raw/' to count IOU of the image
## Task_2 save experiment result
1. run './record_result.ipynb' to copy './result/seg_raw' to './record/EXPERIMENT_NAME' folder