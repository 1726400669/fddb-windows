import os,cv2
from math import *
rootdir="E:/Face/Datasets/fddb"
imagesdir=rootdir+"/images"
annotationdir=rootdir+"/FDDB-folds"
labelsdir=rootdir+"/labels"

def filterCoordinate(c,m):
	if c < 0:
		return 0
	elif c > m:
		return m
	else:
		return c

def show_annotations():
    for i in range(10):
        annotationfilepath=annotationdir+"/FDDB-fold-0%d-ellipseList.txt"%(i+1)
        annotationfile=open(annotationfilepath)
        while(True):
            filename=annotationfile.readline()[:-1]+".jpg"
            print filename
            if not filename:
                break
            facenum=(int)(annotationfile.readline())
            img=cv2.imread(imagesdir+"/"+filename)
            w = img.shape[1]
            h = img.shape[0] 
            labelpath=labelsdir+"/"+filename.replace('/','_')[:-3]+"txt"
            labelfile=open(labelpath,'w')
            for j in range(facenum):
                line =annotationfile.readline().strip().split()
                major_axis_radius=(float)(line[0])
                minor_axis_radius=(float)(line[1])
                angle=(float)(line[2])
                center_x=(float)(line[3])
                center_y=(float)(line[4])
                score=(float)(line[5])
                angle = angle / 3.1415926*180.
                cv2.ellipse(img, ((int)(center_x), (int)(center_y)), ((int)(major_axis_radius), (int)(minor_axis_radius)), angle, 0., 360.,(255, 0, 0))
                
                a=major_axis_radius
                b=minor_axis_radius
                tan_t = -(b/a)*tan(angle)
                t = atan(tan_t)
                x1 = center_x + (a*cos(t)*cos(angle) - b*sin(t)*sin(angle))
                x2 = center_x + (a*cos(t+pi)*cos(angle) - b*sin(t+pi)*sin(angle))
                x_max = filterCoordinate(max(x1,x2),w)
                x_min = filterCoordinate(min(x1,x2),w)
                if tan(angle) != 0:
                    tan_t = (b/a)*(1/tan(angle))
                else:
                    tan_t = (b/a)*(1/(tan(angle)+0.0001))
                t = atan(tan_t)
                y1 = center_y + (b*sin(t)*cos(angle) + a*cos(t)*sin(angle))
                y2 = center_y + (b*sin(t+pi)*cos(angle) + a*cos(t+pi)*sin(angle))
                y_max = filterCoordinate(max(y1,y2),h)
                y_min = filterCoordinate(min(y1,y2),h)
                cv2.rectangle(img,(int(x_min),int(y_min)),(int(x_max),int(y_max)),(0,0,255))
                labelline="0"+","+str(x_min) + ',' + str(y_min) + ',' + str(x_max) + ',' + str(y_max)	+ '\n'
                labelfile.write(labelline)
            labelfile.close()
            cv2.imshow("img",img)
            cv2.waitKey()

if __name__=="__main__":
    show_annotations()