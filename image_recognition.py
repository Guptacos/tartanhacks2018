from azure.cognitiveservices.vision.customvision.training import training_api
from azure.cognitiveservices.vision.customvision.training.models import ImageUrlCreateEntry

from azure.cognitiveservices.vision.customvision.prediction import prediction_endpoint

from azure.cognitiveservices.vision.customvision.prediction.prediction_endpoint import models

import os

import requests

import string

def identify(image):
 #   print (project)
 #   print (iteration)
    predictor = prediction_endpoint.PredictionEndpoint("15c7f6bd782b4fab887295c83a608f42")
    with open(image, mode="rb") as test_data:
        results = predictor.predict_image("ac4d0722-29ce-4116-b9d2-225b453a3df3", test_data.read())
    answer = None
    percent = 0
    #results = predictor.predict_image_url(project.id, iteration.id, image)
    for prediction in results.predictions:
        if prediction.probability > .5: 
            if (answer == None):
                answer = prediction.tag
            else:
                if prediction.probability > percent:
                    answer = prediction.tag
                    percent = prediction.probability
        #print ("\t" + prediction.tag + ": {0:.2f}%".format(prediction.probability * 100))
    return answer
    
def images2Circ(photos):
    rows = 6
    cols = 8
    circuit = [[None for i in range(cols)] for j in range(rows)]
    listing = os.listdir(photos)
    listing.sort()
    print(listing)
    length = len(listing)
    for i in range(rows):
        for j in range(cols):
            index = (i * (cols-1)) + j
            if index >= length: break
            pic = photos + listing[index]
            gate = identify(pic)
            circuit[i][j] = gate
    return circuit


print(images2Circ("Photos/t2/"))
        
        
