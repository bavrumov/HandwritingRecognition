from tensorflow.examples.tutorials.mnist import input_data
#from pip._vendor.distlib.compat import raw_input


print("importing tensorflow, input data sets")

import tensorflow as tf
#import keras
mnist = input_data.read_data_sets('./data/', one_hot=True)
#mnist = input_data.read_data_sets(raw_input(), raw_input(), raw_input())


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

