import tensorflow as tf
from keras import layers, datasets,models
import numpy as np
import cv2
from keras import losses
from matplotlib import pyplot as plt
#Lets LOAD 

model = models.Sequential()
model.add(layers.Conv2D(32, (5, 5), activation='relu', input_shape=(224, 224, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (5, 5), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (5, 5), activation='relu'))

model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(4))
model.compile(optimizer='adam',
              loss=losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
model.summary()
# history = model.fit(train_images, train_labels, epochs=10, 
#                     validation_data=(test_images, test_labels))
#model.predict()