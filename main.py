import multiprocessing
import os
import cv2
from saving_to_s3 import save_to_s3_
import time

data_folder='faces/'
print('num of CPU cores: ',multiprocessing.cpu_count())


images_url=[]
img_arr=[]
for file in os.listdir(data_folder):
    file_=data_folder+file
    images_url.append(file)
    image_as_arr=cv2.imread(file_)
    img_arr.append(image_as_arr)



start=time.time()
pl1=multiprocessing.Process(target=save_to_s3_,args=(zip(img_arr[:130],images_url[:130]),))
pl2=multiprocessing.Process(target=save_to_s3_,args=(zip(img_arr[131:262],images_url[131:262]),))
pl3=multiprocessing.Process(target=save_to_s3_,args=(zip(img_arr[263:407],images_url[263:407]),))
pl1.start()
pl2.start()
pl3.start()

pl1.join()
pl2.join()
pl3.join()

print('time total: ',time.time()-start)
print('num of images: ',images_url)
