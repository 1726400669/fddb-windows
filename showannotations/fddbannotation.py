import os,cv2
from math import *
import numpy as np
rootdir="E:/Face/Datasets/fddb"
origimagedir=rootdir+"/origimages"
imagesdir=rootdir+"/images"
annotationdir=rootdir+"/FDDB-folds"
labelsdir=rootdir+"/labels"
conver2rects=True

def show_annotations():
    for i in range(10):
        annotationfilepath=annotationdir+"/FDDB-fold-%0*d-ellipseList.txt"%(2,i+1)
        annotationfile=open(annotationfilepath)
        while(True):
            filename=annotationfile.readline()[:-1]+".jpg"
            if not filename:
                break
            line=annotationfile.readline()
            if not line:
                break
            print filename
            facenum=(int)(line)
            img=cv2.imread(origimagedir+"/"+filename)
            filename=filename.replace('/','_')
            cv2.imwrite(imagesdir+"/"+filename,img)
            w = img.shape[1]
            h = img.shape[0] 
            labelpath=labelsdir+"/"+filename.replace('/','_')[:-3]+"txt"
            labelfile=open(labelpath,'w')   
            for j in range(facenum):
                line=annotationfile.readline().strip().split()
                major_axis_radius=(float)(line[0])
                minor_axis_radius=(float)(line[1])
                angle=(float)(line[2])
                center_x=(float)(line[3])
                center_y=(float)(line[4])
                score=(float)(line[5])
                angle = angle / 3.1415926*180
                cv2.ellipse(img, ((int)(center_x), (int)(center_y)), ((int)(major_axis_radius), (int)(minor_axis_radius)), angle, 0., 360.,(255, 0, 0)) 
                if conver2rects:
                    mask=np.zeros((img.shape[0],img.shape[1]),dtype=np.uint8)
                    cv2.ellipse(mask, ((int)(center_x), (int)(center_y)), ((int)(major_axis_radius), (int)(minor_axis_radius)), angle, 0., 360.,(255, 255, 255))
                    #cv2.imshow("mask",mask) 
                    contours=cv2.findContours(mask,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
                    for k in range(len(contours)-2):
                        r=cv2.boundingRect(contours[k])
                        x_min=r[0]
                        y_min=r[1]
                        x_max=r[0]+r[2]
                        y_max=r[1]+r[3]
                        xcenter=r[0]+r[2]/2
                        ycenter=r[1]+r[3]/2
                        labelline="0"+"\t"+str(xcenter*1.0/w) + '\t' + str(ycenter*1.0/h) + '\t' + str(r[2]*1.0/w) + '\t' + str(r[3]*1.0/h)	+ '\n'
                        labelfile.write(labelline)
                        cv2.rectangle(img,(int(x_min),int(y_min)),(int(x_max),int(y_max)),(0,0,255))
            labelfile.close()
            cv2.imshow("img",img)
            cv2.waitKey(1)

if __name__=="__main__":
    show_annotations()