
print("\n>importing tensorflow, input data sets")

import tensorflow as tf
import keras
import numpy 
import matplotlib.pyplot as plot
from matplotlib import rcParams
import math
from mlxtend.data import loadlocal_mnist
import random

training_images, training_labels = loadlocal_mnist(
    images_path='./data/train-images-idx3-ubyte',
    labels_path='./data/train-labels-idx1-ubyte')
testing_images, testing_labels = loadlocal_mnist(
    images_path='./data/t10k-images-idx3-ubyte',
    labels_path='./data/t10k-labels-idx1-ubyte')

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

#Scaling Values from 0-255 to 0-1.0
training_images = training_images / 255.0
testing_images = testing_images / 255.0


item_num = numpy.arange(100)
for x in range(0,100):
    item_num[x] = random.randint(0,60000)

#Plot Preferences

#plot.imshow(training_images[item_num])
#plot.colorbar()
#plot.grid(False)

#plot.tick_params(axis='both', which='major', labelsize=6)
rcParams.update({'figure.autolayout': True})
plot.figure(figsize=(50,300))
for i in range(100):
    plot.subplot(20, 5, i+1)
    plot.grid(False)
    #plot.yticks(numpy.arange(0, 28, 1.0))
    #plot.xticks(numpy.arange(0, 28, 1.0))
    plot.xticks([])
    plot.yticks([])
    plot.imshow(training_images[item_num[i]])
    plot.xlabel(training_labels[item_num[i]], fontsize=200)
plot.savefig("pleasework.png")




#print(training_images[1])


#for label in numpy.bincount(training_labels):
#    print(round(label/60000, 5)*100)
#print(training_labels)

#print(testing_labels)








'''
print(training_images[0])
input()
print(training_images[1])
input()
print(training_images[2])
input()
print(training_images[59997])
input()
print(training_images[59998])
input()
print(training_images[59999])












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
