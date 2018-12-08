
print("\n>importing tensorflow, input data sets")

import tensorflow as tf
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


label_names = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


'''
# METRIC REDEFINITION
def get_categorical_accuracy_keras(y_true, y_pred):
    return kbe.mean(kbe.equal(kbe.argmax(y_true, axis=1), kbe.argmax(y_pred, axis=1)))


# GRAPHING TO LOOK AT FULL CHANNEL SET
def plotter(i, predictions_arr, correct_label, img):
    predictions_arr, correct_label, img = predictions_arr[i], correct_label[i], img[i]
    plot.grid(False)
    plot.xticks([])
    plot.yticks([])

    plot.imshow(img) #cmap=plot.cm.binary
    predicted_label = numpy.argmax(predictions_arr)
    if predicted_label == correct_label:
        color = 'green'
    else:
        color = 'red'

    plot.xlabel("{} {:2.0f}% ({})".format(label_names[predicted_label],
                                          100 * numpy.max(predictions_arr),
                                          label_names[correct_label]),
                color=color)

def plot_value_array(i, predictions_arr, correct_label):
    predictions_arr, correct_label = predictions_arr[i], correct_label[i]
    plot.grid(False)
    plot.xticks([])
    plot.yticks([])

    thisplot = plot.bar(range(62), predictions_arr, color="#777777")
    plot.ylim([0, 1])
    predicted_label = numpy.argmax(predictions_arr)

    thisplot[predicted_label].set_color('red')
    thisplot[correct_label].set_color('green')



# training_images, training_labels = loadlocal_mnist(
#     images_path='./data/train-images-idx3-ubyte',
#     labels_path='./data/train-labels-idx1-ubyte')
# testing_images, testing_labels = loadlocal_mnist(
#     images_path='./data/t10k-images-idx3-ubyte',
#     labels_path='./data/t10k-labels-idx1-ubyte')

training_images, training_labels = loadlocal_mnist(
    images_path='./data/emnist-byclass-train-images-idx3-ubyte',
    labels_path='./data/emnist-byclass-train-labels-idx1-ubyte')
testing_images, testing_labels = loadlocal_mnist(
    images_path='./data/emnist-byclass-test-images-idx3-ubyte',
    labels_path='./data/emnist-byclass-test-labels-idx1-ubyte')

numpy.set_printoptions(linewidth=1800)
gridSize = int(math.sqrt(training_images.shape[1]))


print('\n------------------------------\n')
print('ORIGINALS:')
print('Training: ', training_images.shape)
print('Testing:  ', testing_images.shape)

training_images = numpy.expand_dims(training_images, axis=2)
testing_images = numpy.expand_dims(testing_images, axis=2)
print('\nADDED DIMENSIONS:')
print('Training: ', training_images.shape)
print('Testing:  ', testing_images.shape)

training_images = numpy.reshape(training_images, (training_images.shape[0], gridSize, gridSize))
testing_images = numpy.reshape(testing_images, (testing_images.shape[0], gridSize, gridSize))
print('\nRESHAPED:')
print('Training: ', training_images.shape)
print('Testing:  ', testing_images.shape)
print('\n------------------------------\n')

print('\nTraining Dataset')
print('Images: ', training_images.shape[0], '  x  ', training_images[1].shape)
print('Labels: ', len(training_labels))
print('Label distribution: ', numpy.bincount(training_labels))
print('       percentages: ')

print('\nTesting Dataset')
print('Images: ', testing_images.shape[0], '  x  ', testing_images[1].shape)
print('Labels: ', len(testing_labels))
print('Label distribution: ', numpy.bincount(testing_labels))

training_images = keras.utils.normalize(training_images, axis=1)
testing_images = keras.utils.normalize(testing_images, axis=1)

model = keras.models.Sequential()
model.add(keras.layers.Flatten(input_shape=(28,28)))                                    # Brings our 28x28 array back into a flat 1d aray
model.add(keras.layers.Dense(128, activation=tf.nn.relu, bias_initializer='zeros'))     # Rectified Linear Unit - max(x,0)
model.add(keras.layers.Dense(128, activation=tf.nn.relu, bias_initializer='zeros'))     # Rectified Linear Unit - max(x,0)
model.add(keras.layers.Dense(62, activation=tf.nn.softmax, bias_initializer='zeros' ))  # Multiclass Probabalistic Output

model.compile(optimizer=keras.optimizers.Adam(lr=1e-5),                                 # RMSprop w/ momentum
              loss='sparse_categorical_crossentropy',
              metrics=[keras.metrics.mae]
              )

model.summary()

model.fit(training_images, training_labels, epochs=1)                                   # Arbitrary Epoch Cutoff
model.save('digitizer.h5')

del model
'''
model = load_model('digitizer.h5')
model.summary()


'''
val_loss, val_acc = model.evaluate(testing_images, testing_labels)
print(val_loss, val_acc)

predictions = model.predict([testing_images])
num_rows = 50
num_cols = 1
num_images = num_rows*num_cols
plot.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
  plot.subplot(num_rows, 2*num_cols, 2*i+1)
  plotter(i, predictions, testing_labels, testing_images)
  plot.subplot(num_rows, 2*num_cols, 2*i+2)
  plot_value_array(i, predictions, testing_labels)
  plot.savefig('testMaster.png')

'''


















'''
for i in range(100):
    print("\n\n\n+++++", numpy.argmax(predictions[i]), "+++++\n")
    for j in range(28):
        for k in range(28):
            testing_images[i][j][k] = math.ceil(testing_images[i][j][k])
            if testing_images[i][j][k] == 1:
                testing_images[i][j][k] = 4.4
    print(testing_images[i])
'''





'''
print("initializing x, W, b, y, y_")

x = tf.placeholder(tf.float32, [None, 784])

W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros(10))

y = tf.matmul(x,W) + b
y_ = tf.placeholder(tf.float32, [None,10])

print('initialized')


print("cross entropy, training")

cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels = y_, logits = y))
train_step = tf.train.GradientDescentOptimizer(0,4).minimize(cross_entropy)


print("setting up session")

init = tf.initialize_all_variables()

sess = tf.Session


print("running session")

sess.run(init)

for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys})


print("results")

result = sess.run(tf.arg_max(y,1), feed_dict={x:mnist.validation.images})
print (" ".join(map(str,result)))
'''