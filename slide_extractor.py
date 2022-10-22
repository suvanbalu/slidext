#importing necessary libraries

import cv2
import numpy as np
import os
from PIL import Image
import imagehash
import time

def framing(ti,cap,const_threshold):
    # Collecting frame from video with a time interval ti
    frames=[]  #to save diiferent frames
    thresholds=[]
    fps=cap.get(cv2.CAP_PROP_FPS) #FPS of the video
    fr = cap.get(cv2.CAP_PROP_FRAME_COUNT) #Total Frame count of the video
    total_duration = fr/fps #Total Duration
    #print(total_duration)
    start=0
    prev_frame = None
    while start<=total_duration-ti: #Iterating through the video till the final duration
        print(f"Frame {start} of {total_duration} completed")
        fid = fps*start   #frame at particular time
        cap.set(cv2.CAP_PROP_POS_FRAMES,fid) #Setting the video cursor at the particular time
        ret, frame = cap.read()   #Reading the frame
        #print(fid,ret)
        if start>total_duration-(2*ti):   #For the last 2 seconds of the video
            frames.append(frame)
        if prev_frame is None:        #For the first frame
            prev_frame = frame
            frames.append(frame)
        else:
            dif,thresh=filter_diff(prev_frame,frame,const_threshold)  #Filtering out the frames
            if dif:
                frames.append(prev_frame)
                prev_frame=frame
                thresholds.append(thresh)
        start+=ti
    return frames,thresholds   #returning frames of the video as a numpy array with values 0-255

def diff(path1,path2): 
    #Testing Function, Not used in main program
    f1 = cv2.imread(path1)
    f2 = cv2.imread(path2)
    diff = cv2.absdiff(f1, f2)
    non_zero_count = np.count_nonzero(diff)
    print(non_zero_count)

# path1="test6/photo0.png"
# #cv2.imshow(path1)
# path2="test6/photo1.png"
# diff(path1,path2)

def similar(i,testname):    #second level filter
    #Checking whether the previous image and the current image are similar or not
    
    hash0 = imagehash.average_hash(Image.open(f'{testname}/photo{i-1}.png')) 
    hash1 = imagehash.average_hash(Image.open(f'{testname}/photo{i}.png')) 
    #print(int(hash0),int(hash1))
    cutoff = 5 
    if hash0 - hash1 < cutoff:
        return True
    else:
        return False

def checkblack(i,testname):   #Checking whether the image is black or not
    #Checking for any slides with majority values as black
    threshold=1033203
    img = cv2.imread(f'{testname}/photo{i}.png',0) #read img as b/w as an numpy array
    unique, counts = np.unique(img, return_counts=True)
    mapColorCounts = dict(zip(unique, counts))
    if 0 not in mapColorCounts:
        return False
    if mapColorCounts[0]>=threshold:
        return True 
    return False

def saveframes(frames,testname):
    #Saving the frames as image 
    if not os.path.exists(testname): #Creating the test folder if its not present
        os.mkdir(f"{testname}")
    cv2.imwrite(f"{testname}/photo{0}.png",frames[0])
    idx=1
    for frame in frames[1:-1]:
        cv2.imwrite(f"{testname}/photo{idx}.png",frame) 
        if similar(idx,testname) or checkblack(idx,testname):
            os.remove(f"{testname}/photo{idx}.png")
        else:
            idx+=1
    cv2.imwrite(f"{testname}/photo{idx}.png",frames[-1])
    if similar(idx,testname) or checkblack(idx,testname):
        os.remove(f"{testname}/photo{idx-1}.png")
    

def filter_diff(prev,current,const_threshold):  #1st level filter
    #First Stage of filtering out using opencv absdiff and count_nonzero method
    difference=cv2.absdiff(prev,current)
    value = np.count_nonzero(difference)
    if value>const_threshold:
        return True,value
    return False,value


def main(video_path,testname,const_thresh,ti): 
    # const_thresh = 520000 #Threshold for the first stage of filtering
    ti=float(ti)
    print(video_path)
    now = time.time()
    cap = cv2.VideoCapture(video_path) 
    frames,thresholds=framing(ti,cap,const_thresh)
    saveframes(frames,testname)
    saveend=time.time()
    return saveend-now,thresholds

# print(main("test_videos/test1.mp4","test7")[0])

#testname -> destination path