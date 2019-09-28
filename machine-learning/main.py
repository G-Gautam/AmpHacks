import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten
from keras.utils import to_categorical
import warnings
import os
from keras.models import load_model


warnings.filterwarnings('ignore')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

data = np.load('./training/data.npy')
labels = np.load('./training/labels.npy')


X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

#y_train = to_categorical(y_train)
#y_test = to_categorical(y_test)

#create model
model = Sequential()
#add model layers
model.add(Conv2D(8, kernel_size=5, activation='relu', input_shape=(200,200,3)))
model.add(Conv2D(8, kernel_size=5, activation='relu'))
model.add(Flatten())
model.add(Dense(1, activation='softmax'))

#compile model using accuracy to measure model performance
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mse'])

model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=20)

model.save('cnn_model.h5')  # creates a HDF5 file 'my_model.h5'

