import itertools
from collections import OrderedDict

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
from PIL import Image



class Model(object):
    kerasModel = keras.models.Sequential()
    label_names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D',
                   'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                   'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                   'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # GRAPHING TO LOOK AT FULL CHANNEL SET
    # def plotter(self, predictions_arr, img):
    #     plot.grid(True)
    #     plot.xticks([])
    #     plot.yticks([])
    #     plot.imshow(img) #cmap=plot.cm.binary
    #     predicted_label = numpy.argmax(predictions_arr)
    #     color = 'blue'
    #
    #     plot.xlabel("{} {:2.0f}% ({})".format(self.label_names[predicted_label],
    #                                           100 * numpy.max(predictions_arr),
    #                                           self.label_names[predicted_label]),
    #                 color=color)
    #
    # def plot_value_array(self, predictions_arr):
    #     plot.grid(False)
    #     plot.xticks([])
    #     plot.yticks([])
    #
    #     thisplot = plot.bar(range(62), predictions_arr, color="#777777")
    #     plot.ylim([0, 1])
    #     predicted_label = numpy.argmax(predictions_arr)
    #
    #     thisplot[predicted_label].set_color('blue')
    #     #thisplot[correct_label].set_color('green')

    def plotter(self, i, predictions_array, img):
        # plot.figure(figsize=(50, 10))
        # plot.autoscale(False)
        # plot.rcParams["figure.figsize"] = [16, 9]
        predictions_array, img = predictions_array[i], img[i]

        plot.grid(True)
        plot.xticks([])
        plot.yticks([])

        plot.imshow(img) #cmap=plot.cm.binary)

        # plot.figure(figsize=(50, 10))
        predicted_label = numpy.argmax(predictions_array)

        color = "green"

        plot.xlabel("{:2.0f}% ({})".format(100 * numpy.max(predictions_array),
                                           self.label_names[predicted_label]),
                            color=color)

    def plot_value_array(self, i, predictions_array):
        plot.figure(figsize=(20, 10))
        plot.tight_layout()
        predictions_array = predictions_array[i]
        plot.grid(True)
        plot.xticks([])
        _ = plot.xticks(range(62), self.label_names)
        plot.yticks([])
        thisplot = plot.bar(range(62), predictions_array, color="#777777")
        plot.ylim([0, 1])
        predicted_label = numpy.argmax(predictions_array)

        thisplot[predicted_label].set_color('blue')


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
        #tfjs.converters.save_keras_model(self.kerasModel, './tfjs_model')

    def load(self):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, 'digitizer.h5')

        self.kerasModel = load_model(my_file)
        #self.kerasModel.summary()

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

        # predictions = self.kerasModel.predict(predict_image)



        img = predict_image[0]

        print(img.shape)

        img = (numpy.expand_dims(img, 0))

        print(img.shape)

        predictions = self.kerasModel.predict(img)

        print(predictions)

        print(predict_image)
        #
        # for i in range(1):
        #     plot.subplot(1, 2 * 1, 2 * i + 1)
        #     self.plotter(i, predictions, predict_image)
        #     plot.subplot(1, 2 * 1, 2 * i + 2)
        #     self.plot_value_array(i, predictions)

        # self.plotter(0, predictions, predict_image)
        # self.plot_value_array(0, predictions)

        self.plotter(0, predictions, predict_image)
        plot.savefig('justPicture.png')

        self.plot_value_array(0, predictions)
        plot.savefig('justArray.png')


        # print(self.label_names[numpy.argmax(predictions)])
        print(predictions)
        return self.label_names[numpy.argmax(predictions)]

    def test_predicts_metrics(self):
        testing_images, testing_labels = loadlocal_mnist(
            images_path='./data/emnist-byclass-test-images-idx3-ubyte',
            labels_path='./data/emnist-byclass-test-labels-idx1-ubyte')

        with open('./data/emnist-byclass-test-images-idx3-ubyte', 'rb') as imgpath:
            magic, num, rows, cols = struct.unpack(">IIII",
                                                   imgpath.read(16))
            images = numpy.fromfile(imgpath,
                                 dtype=numpy.uint8).reshape(116323, 784)
            testing_images = images

        gridSize = int(math.sqrt(testing_images.shape[1]))

        testing_images = numpy.expand_dims(testing_images, axis=2)

        testing_images = numpy.reshape(testing_images, (testing_images.shape[0], gridSize, gridSize))

        testing_images = keras.utils.normalize(testing_images, axis=1)

        predictions = self.kerasModel.predict(testing_images)

        totalimgs = 116323
        numcorrect = 0
        wrong_guesses = [[0 for x in range(62)] for y in range(62)]
        wrong_sums = [0 for x in range(62)]

        # COUNTING WRONG GUESSES FOR EACH CHAR
        for i in range (totalimgs):
            guessed_label = numpy.argmax(predictions[i])
            if str(self.label_names[guessed_label]) == str(self.label_names[testing_labels[i]]):
                numcorrect = numcorrect + 1
            else:
                wrong_guesses[testing_labels[i]][guessed_label] = wrong_guesses[testing_labels[i]][guessed_label] + 1
                wrong_sums[testing_labels[i]] = wrong_sums[testing_labels[i]] + 1
        accuracy = numcorrect/totalimgs

        wrong_guesses_topped = [{} for i in range(62)]
        for character in range(62):
            for i in range(62):
                if wrong_guesses[character][i] != 0:
                    wrong_guesses_topped[character].update({self.label_names[i]:int(wrong_guesses[character][i])})

        # SORTING
        wrong_guesses_topped_sorted = [{} for i in range(62)]
        guesses_dict_array = [dict() for i in range(62)]
        for i in range(62):
            wrong_guesses_topped_sorted[i] = sorted(wrong_guesses_topped[i].items(), key=lambda kv: kv[1], reverse=True)
            guesses_dict_array[i] = dict(wrong_guesses_topped_sorted[i])
            guesses_dict_array[i] = OrderedDict(itertools.islice(guesses_dict_array[i].items(), 5))
            #print(self.label_names[i] + "\t" + str(guesses_dict_array[i]))

        centeringwidth = 15
        # COUNTING IMAGES OF EACH CHAR
        imgcounts = [0 for i in range(62)]
        for imgnum in range(totalimgs):
            imgcounts[testing_labels[imgnum]] = imgcounts[testing_labels[imgnum]] + 1

        key_array = [guesses_dict_array[i].keys() for i in range(62)]
        val_array = [guesses_dict_array[i].values() for i in range(62)]




        chars_and_accuracies = {}
        for i in range(62):
            if imgcounts[i]-wrong_sums[i] != 0:
                chars_and_accuracies.update({self.label_names[i]: ((imgcounts[i]-wrong_sums[i])/imgcounts[i])*100})

        chars_and_accuracies_sorted = dict(sorted(chars_and_accuracies.items(), key=lambda kv: kv[1], reverse=True))
        chars_and_accuracies_sorted_topped = OrderedDict(itertools.islice(chars_and_accuracies_sorted.items(), 20))

        chars_accuracies_key_array = list(chars_and_accuracies_sorted_topped.keys())# for i in range(20)]
        chars_accuracies_val_array = list(chars_and_accuracies_sorted_topped.values())# for i in range(20)]




        print("\n\n+ Model Accuracy: \n")
        print("\t{:.2f}".format(accuracy*100) + "%")


        print("\n\n+ Most Accurately Predicted Characters: \n")
        print(str("  Char").rjust(centeringwidth-10) + str("Accuracy").rjust(centeringwidth))
        print(str("  ----").rjust(centeringwidth-10) + str("--------").rjust(centeringwidth))
        for i in range(13):
            localval = chars_accuracies_val_array[i]
            print(str(chars_accuracies_key_array[i]).rjust(centeringwidth-10) + str(f'{localval:.2f}' + "%").rjust(centeringwidth))


        print("\n\n+ Categorical Accuracy: \n")

        print(str("  Char").rjust(centeringwidth-10) + str("Accuracy").rjust(centeringwidth) + str("\t\t\tShare of Top Incorrect Guesses").rjust(centeringwidth)) #+ str("Total").rjust(centeringwidth) + str("Correct").rjust(centeringwidth) + str("Wrong").rjust(centeringwidth))
        print(str("  ----").rjust(centeringwidth-10) + str("--------").rjust(centeringwidth) + str("\t\t\t----- -- --- --------- -------").rjust(centeringwidth)) #+ str("-----").rjust(centeringwidth) + str("-------").rjust(centeringwidth) + str("-----").rjust(centeringwidth))
        for i in range(62):
            print(str(self.label_names[i]).rjust(centeringwidth-10) + "" + str("{:.2f}".format(((imgcounts[i]-wrong_sums[i])/imgcounts[i])*100) + "%").rjust(centeringwidth), end = "\t") #+ str(imgcounts[i]).rjust(centeringwidth) + str(imgcounts[i]-wrong_sums[i]).rjust(centeringwidth) + str(wrong_sums[i]).rjust(centeringwidth), end="\t")
            for k in range(5):
                print("\t\t" + list(key_array[i])[k], end="")
                print("  " + str(int(((list(val_array[i])[k])/wrong_sums[i])*100)) + "%", end = "")
            print("")










