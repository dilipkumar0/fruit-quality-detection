#from pymongo import MongoClient
#from bson.objectid import ObjectId
from flask import Flask,render_template,jsonify,json,request
#from fabric.api import *


import base64


from PIL import Image
import os, os.path
import cv2
import glob
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics


application = Flask(__name__)




aList=[];
count=0;
index=0;
state=1;
def labels() :
    count=0;
    index=0;
    state=1;
    
    for x in range(0,60) :
        if count == 9 :
            if state == 0 :
                aList.append( int(state) );
                state=1;
                count=0;
            else :
                aList.append( int(state) );
                state=0;
                count=0;
        else :
             aList.append( int(state) );
             count=count+1;

labels();

def convertGrayScale(path) :
    img_2d_list = [];
    for img in glob.glob(path):
        origi_img = cv2.imread(img)
        oriimage = cv2.resize(origi_img,(50,50))
        gray_img = cv2.cvtColor(oriimage, cv2.COLOR_BGR2GRAY)
        img_2d_list.append(gray_img)
    train_data = []
    for img_2d in img_2d_list:
        flatten_img = img_2d.flatten()
        flatten_img_list = list(flatten_img)
        train_data.append(flatten_img_list)
    return train_data;        

train_data=[];
train_data=convertGrayScale("/home/iiitg/PythonFlaskRemoteApp-master/mixed/*.jpg");
np_train_data = np.array(train_data)

model = LogisticRegression()
model.fit(np_train_data, aList)


@application.route("/showData",methods=['GET'])
def get() :
    print 'i got a request'
    fileHandle = open ( 'fruitStatus.txt',"r" )
    lineList = fileHandle. readlines()
    fileHandle. close()
    ll=lineList[len(lineList)-1]
    arr = ll.split(' ');
    
    imageName=arr[0];
    print imageName;
    with open("/home/iiitg/PythonFlaskRemoteApp-master/test_data/"+imageName, "rb") as f:
        data = f.read()
        encodingData=data.encode("base64")
        result = {"status" : arr[6] , "base64" : encodingData}
        return jsonify(result)

@application.route("/lastFive",methods=['GET'])
def five() :
    fileHandle = open ( 'fruitStatus.txt',"r" )
    lineList = fileHandle. readlines()
    fileHandle. close()
    ll=lineList[-5:]
    result={};
    c=0;
    x={}
    #x['hi']=1
    #x['byer']=2
    for x in ll:
        arr = x.split(' ');
        imageName=arr[0];
        with open("/home/iiitg/PythonFlaskRemoteApp-master/test_data/"+imageName, "rb") as f:
            data = f.read()
            encodingData=data.encode("base64")
            result[str(c)]= {"status" : arr[6] , "base64" : encodingData}
            c=c+1;
    return jsonify(result)


    


@application.route("/sendimage",methods=['GET'])
def sendimage() :
    with open("/home/iiitg/PythonFlaskRemoteApp-master/test_data/image_0.jpg", "rb") as f:
        data = f.read()
        encodingData=data.encode("base64")
        print encodingData
        return jsonify(encodingData)


#client = MongoClient('localhost:27017')
#db = client.MachineData

@application.route("/addMachine",methods=['GET'])
def addMachine():
    data = {"x" : 1}
    return jsonify(status='OK',message='inserted successfully')

    
@application.route('/')
def showMachineList():
    return render_template('list.html')



if __name__ == "__main__":
    application.run(host='0.0.0.0')
