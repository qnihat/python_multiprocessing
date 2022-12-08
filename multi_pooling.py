import multiprocessing
from upload_to_s3 import save_to_s3_
import os
import cv2
import time

data_folder='faces/'

p=multiprocessing.Pool(10)

array_of_images_with_uuid_names=[]
for file in os.listdir(data_folder):
    file_=data_folder+file
    image_as_arr=cv2.imread(file_)
    array_of_images_with_uuid_names.append([image_as_arr,file])

start=time.time()

p.map(save_to_s3_,array_of_images_with_uuid_names)
print('total time: ',time.time()-start)