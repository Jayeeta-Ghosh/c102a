from os import access
from tracemalloc import start
import cv2

import dropbox
import time
import random

start_time=time.time()
def snapshot():
    number=random.randint(0,100)
    videoCapture = cv2.VideoCapture(0)
    result=True
    while (result):
        ret,frame=videoCapture.read()
        image_name="pic"+str(number)+".png"
        cv2.imwrite(image_name,frame)
        start_time=time.time
        result=False
    return image_name    
    videoCapture.release()
    cv2.destroyAllWindows() 

def uploadFile(image):
    accessToken="sl.BKGeg1e8cc_f9M2A14QgFcPDhpn99oDFeeu7R8SAvOV2_r8M1a2PfOe2Qlp9mkfG_K5T_G2r3_3q-VsmVVcAM_xmHPWXTxDOvFCJG_gbpmHKzjQ0U85IZp3Z0w5_GeN45Wim4_baNiUo"
    file=image
    file_from=file
    file_to="/mypic/"+(image)
    dbx=dropbox.Dropbox(accessToken)
    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=60):
            name=snapshot()
            uploadFile(name)

main()
