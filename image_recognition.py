from azure.cognitiveservices.vision.customvision.training import training_api
from azure.cognitiveservices.vision.customvision.training.models import ImageUrlCreateEntry

from azure.cognitiveservices.vision.customvision.prediction import prediction_endpoint

from azure.cognitiveservices.vision.customvision.prediction.prediction_endpoint import models

import os

import requests

#from create_recog import project
#from create_recog import iteration

training_key = "6675bfa94aa949dd97d5025fed9f3d74"
'''
body = "Photos/test_or.jpg"

url = "https://southcentralus.api.cognitive.microsoft.com/customvision/v1.1/Prediction/a7e5c237-2257-4451-88d7-8492de3e0b70/Photos/test_or.jpg"

imgurl = "https://southcentralus.api.cognitive.microsoft.com/customvision/v1.1/Prediction/a7e5c237-2257-4451-88d7-8492de3e0b70/"
response = requests.post(
    imgurl,
    body, headers = {
    'Prediction-Key': '15c7f6bd782b4fab887295c83a608f42',
    'Content-Type': 'application/octet-stream'})

print(response)



project = {'description': '', 'id': '69df6b7e-1b16-4676-84e5-8af5bead93fe', 'current_iteration_id': 'c7161559-6233-4c3c-a81e-3a7eb274d93c', 'last_modified': datetime.datetime(2018, 2, 10, 8, 14, 46, 724541, tzinfo=<isodate.tzinfo.Utc object at 0x064EB850>), 'name': 'Hacking', 'thumbnail_uri': None, 'created': datetime.datetime(2018, 2, 10, 8, 14, 46, 710000), 'settings': <azure.cognitiveservices.vision.customvision.training.models.project_settings.ProjectSettings object at 0x06629630>, 'additional_properties': {}}

iteration = {'project_id': '69df6b7e-1b16-4676-84e5-8af5bead93fe', 'exportable': False, 'id': 'c7161559-6233-4c3c-a81e-3a7eb274d93c', 'last_modified': datetime.datetime(2018, 2, 10, 8, 15, 29, 238923), 'name': 'Iteration 1', 'status': 'Completed', 'created': datetime.datetime(2018, 2, 10, 8, 14, 46, 709439), 'trained_at': datetime.datetime(2018, 2, 10, 8, 15, 29, 238923), 'is_default': False, 'domain_id': 'ee85a74c-405e-4adc-bb47-ffa8ca0c9f31', 'additional_properties': {}}
'''
def identify(image):
 #   print (project)
 #   print (iteration)
    predictor = prediction_endpoint.PredictionEndpoint("15c7f6bd782b4fab887295c83a608f42")
    with open(image, mode="rb") as test_data:
        results = predictor.predict_image("a7e5c237-2257-4451-88d7-8492de3e0b70", test_data.read())
    answer = None
    percent = 0
    #results = predictor.predict_image_url(project.id, iteration.id, image)
    for prediction in results.predictions:
        if answer == None:
            percent = prediction.probability
            answer = prediction.tag
        else:
            if prediction.probability > .5: return answer
            elif prediction.probability > percent:
                answer = prediction.tag
                percent = prediction.probability
        #print ("\t" + prediction.tag + ": {0:.2f}%".format(prediction.probability * 100))
    return answer
    
def images2Circ(photos):
    rows = 6
    cols = 8
    circuit = [[None for i in range(cols)] for j in range(rows)]
    listing = os.listdir(photos)
    length = len(listing)
    for i in range(rows):
        for j in range(cols):
            index = (i * (cols-1)) + j
            if index >= length: break
            pic = photos + listing[index]
            gate = identify(pic)
            circuit[i][j] = gate
    return circuit

print(images2Circ("Photos/TartanHacks/Test1/"))
        
        
