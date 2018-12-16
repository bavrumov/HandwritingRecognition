'''

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