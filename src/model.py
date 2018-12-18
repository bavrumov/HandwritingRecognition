import tensorflow as tf
#import tensorflowjs as tfjs
import keras
import keras.backend as kbe
from keras.models import load_model
from keras import metrics
import numpy
import matplotlib.pyplot as plot
from matplotlib import rcParams
import math
from mlxtend.data import loadlocal_mnist
import random
import struct
import os



class Model(object):
    kerasModel = keras.models.Sequential()
    label_names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D',
                   'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                   'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                   'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # GRAPHING TO LOOK AT FULL CHANNEL SET
    def plotter(self, predictions_arr, img):
        plot.grid(False)
        plot.xticks([])
        plot.yticks([])

        plot.imshow(img) #cmap=plot.cm.binary
        predicted_label = numpy.argmax(predictions_arr)
        color = 'blue'

        plot.xlabel("{} {:2.0f}% ({})".format(self.label_names[predicted_label],
                                              100 * numpy.max(predictions_arr)),
                    color=color)

    def plot_value_array(predictions_arr):
        plot.grid(False)
        plot.xticks([])
        plot.yticks([])

        thisplot = plot.bar(range(62), predictions_arr, color="#777777")
        plot.ylim([0, 1])
        predicted_label = numpy.argmax(predictions_arr)

        thisplot[predicted_label].set_color('blue')
        #thisplot[correct_label].set_color('green')

    def build(self):
        self.kerasModel.add(keras.layers.Flatten(input_shape=(28, 28)))  # Brings our 28x28 array back into a flat 1d aray
        self.kerasModel.add(keras.layers.Dense(128, activation=tf.nn.relu,
                                     bias_initializer='zeros'))  # Rectified Linear Unit - max(x,0)
        self.kerasModel.add(keras.layers.Dense(128, activation=tf.nn.relu,
                                     bias_initializer='zeros'))  # Rectified Linear Unit - max(x,0)
        self.kerasModel.add(keras.layers.Dense(62, activation=tf.nn.softmax,
                                     bias_initializer='zeros'))  # Multiclass Probabalistic Output

        self.kerasModel.compile(optimizer=keras.optimizers.Adam(lr=1e-5),  # RMSprop w/ momentum
                      loss='sparse_categorical_crossentropy',
                      metrics=[keras.metrics.mae]
                      )
        self.kerasModel.summary()

    def train(self, numOfEpochs):
        training_images, training_labels = loadlocal_mnist(
            images_path = './data/emnist-byclass-train-images-idx3-ubyte',
            labels_path = './data/emnist-byclass-train-labels-idx1-ubyte')

        #numpy.set_printoptions(linewidth=1800)
        gridSize = int (math.sqrt(training_images.shape[1]))

        training_images = numpy.expand_dims(training_images, axis=2)
        training_images = numpy.reshape(training_images, (training_images.shape[0], gridSize, gridSize))
        training_images = keras.utils.normalize(training_images, axis=1)

        self.kerasModel.fit(training_images, training_labels, epochs=numOfEpochs) # Arbitrary Epoch Cutoff

    def test(self):
        testing_images, testing_labels = loadlocal_mnist(
            images_path='./data/emnist-byclass-test-images-idx3-ubyte',
            labels_path='./data/emnist-byclass-test-labels-idx1-ubyte')

        gridSize = int(math.sqrt(testing_images.shape[1]))

        testing_images = numpy.expand_dims(testing_images, axis=2)

        testing_images = numpy.reshape(testing_images, (testing_images.shape[0], gridSize, gridSize))

        testing_images = keras.utils.normalize(testing_images, axis=1)

        val_loss, val_acc = self.kerasModel.evaluate(testing_images, testing_labels)

    def save(self):
        self.kerasModel.save(('digitizer.h5'))
        tfjs.converters.save_keras_model(self.kerasModel, './tfjs_model')

    def load(self):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, 'digitizer.h5')

        self.kerasModel = load_model(my_file)
        self.kerasModel.summary()

    def predict(self):
        with open('inputdata-images-idx3-ubyte', 'rb') as imgpath:
            magic, num, rows, cols = struct.unpack(">IIII",
                                                   imgpath.read(16))
            images = numpy.fromfile(imgpath,
                                 dtype=numpy.uint8).reshape(1, 784)
            predict_image = images


        gridSize = int(math.sqrt(predict_image.shape[1]))

        predict_image = numpy.expand_dims(predict_image, axis=2)

        predict_image = numpy.reshape(predict_image, (predict_image.shape[0], gridSize, gridSize))

        predict_image = keras.utils.normalize(predict_image, axis=1)

        #predictions = self.kerasModel.predict(predict_image) #this will work on user input data yay

        predictions = self.kerasModel.predict([predict_image])

        self.plotter(predictions, predict_image)
        self.plot_value_array(predictions, predict_image)
        plot.savefig('testMaster.png')

        print(self.label_names[numpy.argmax(predictions)])
        print(predictions)
        return self.label_names[numpy.argmax(predictions)]















