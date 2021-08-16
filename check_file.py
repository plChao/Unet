import os
import glob

label_image_list = glob.glob("label/image/*PNG")
label_image_name_list = [os.path.basename(x) for x in label_image_list]

raw_image_list = glob.glob("data/raw_data/*PNG")
raw_image_name_list = [os.path.basename(x) for x in raw_image_list]
not_in_raw = (set(label_image_name_list) - (set(label_image_name_list) & set(raw_image_name_list)))
print(len(not_in_raw))