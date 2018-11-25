from tensorflow.examples.tutorials.mnist import input_data
from _random import Random
from mlxtend.data.local_mnist import loadlocal_mnist
#from pip._vendor.distlib.compat import raw_input

print("importing tensorflow, input data sets")

import tensorflow as tf
import keras
import numpy 
import matplotlib.pyplot
from mlxtend.data import loadlocal_mnist

training_images, training_labels = loadlocal_mnist(
    images_path='./data/train-images-idx3-ubyte',
    labels_path='./data/train-labels-idx1-ubyte')

print('\nTraining Dataset')
print('Dimensions of Images: ', training_images.shape[0], ' x ', training_images.shape[1])
print('Number of Labels: ', len(training_labels))
#print(training_labels)

testing_images, testing_labels = loadlocal_mnist(
    images_path='./data/t10k-images-idx3-ubyte',
    labels_path='./data/t10k-labels-idx1-ubyte')

print('\nTesting Dataset')
print('Dimensions of Images: ', testing_images.shape[0], ' x ', testing_images.shape[1])
print('Number of Labels: ', len(testing_labels))
#print(testing_labels)





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
