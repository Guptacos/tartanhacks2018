from azure.cognitiveservices.vision.customvision.training import training_api
from azure.cognitiveservices.vision.customvision.training.models import ImageUrlCreateEntry


from azure.cognitiveservices.vision.customvision.prediction import prediction_endpoint

from azure.cognitiveservices.vision.customvision.prediction.prediction_endpoint import models

import os

import time

training_key = "6675bfa94aa949dd97d5025fed9f3d74"
prediction_key = "15c7f6bd782b4fab887295c83a608f42"

trainer = training_api.TrainingApi(training_key)

# Create a new project
print ("Creating project...")
project = trainer.create_project("Hacking")

and_tag = trainer.create_tag(project.id, "AND")
or_tag = trainer.create_tag(project.id, "OR")
not_tag = trainer.create_tag(project.id, "NOT")

and_dir = "Photos/TartanHacks/And"
or_dir = "Photos/TartanHacks/Or"
not_dir = "Photos/TartanHacks/Not"

for image in os.listdir(os.fsencode(and_dir)):
    with open(and_dir + "\\" + os.fsdecode(image), mode="rb") as img_data:
        trainer.create_images_from_data(project.id, img_data.read(), [and_tag.id])
        

for image in os.listdir(os.fsencode(or_dir)):
    with open(or_dir + "\\" + os.fsdecode(image), mode="rb") as img_data:
        trainer.create_images_from_data(project.id, img_data.read(), [or_tag.id])
        
for image in os.listdir(os.fsencode(not_dir)):
    with open(not_dir + "\\" + os.fsdecode(image), mode="rb") as img_data:
        trainer.create_images_from_data(project.id, img_data.read(), [not_tag.id])
        
#training time

print("Training...")

iteration = trainer.train_project(project.id)
while (iteration.status == "Training"):
    iteration = trainer.get_iteration(project.id, iteration.id)
    print("Training status: " + iteration.status)
    time.sleep(1)
        
        
trainer.update_iteration(project.id, iteration.id, is_default=True)
print("Done!")







