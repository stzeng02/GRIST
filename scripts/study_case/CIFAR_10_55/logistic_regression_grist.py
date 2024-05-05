# -*- encoding=utf-8 -*-
import tensorflow as tf
import numpy as np
import sys
import scripts.study_case.CIFAR_10_3.input_data as input_data

sys.path.append("/data")
mnist = input_data.read_data_sets(one_hot=True)

learnin_rate = 0.1
trainin_epochs = 25
batch_size = 100
display_step = 1

X = tf.placeholder(tf.float32, [None, 1024]) 
Y = tf.placeholder(tf.float32, [None, 10])

W = tf.Variable(tf.zeros([1024, 10]))
b = tf.Variable(tf.zeros([10]))

pred = tf.nn.softmax(tf.matmul(X, W) + b)


def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                          strides=[1, 2, 2, 1], padding='SAME')


W_conv1 = weight_variable([5, 5, 1, 32])
b_conv1 = bias_variable([32])

x_image = tf.reshape(X, [-1, 32, 32, 1])  # 28 * 28

h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)  # output size: 28 * 28 * 32
h_pool1 = max_pool_2x2(h_conv1)  # output size: 14 * 14 * 32

W_conv2 = weight_variable([5, 5, 32, 64])
b_conv2 = bias_variable([64])

h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)  # output size: 14 * 14 * 64
h_pool2 = max_pool_2x2(h_conv2)  # output size: 7 * 7 * 64

W_fc1 = weight_variable([4096, 1024])
b_fc1 = bias_variable([1024])

h_pool2_flat = tf.reshape(h_pool2, [-1, 4096])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

keep_prob = tf.placeholder("float")
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])

prediction = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

obj_var = prediction
cross_entropy = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(prediction), reduction_indices=1))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

correct_prediction = tf.equal(tf.argmax(prediction, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

sess = tf.InteractiveSession()
sess.run(tf.initialize_all_variables())

"""insert code"""
from scripts.utils.tf_utils import GradientSearcher
gradient_search = GradientSearcher(name="practice.logistic_regression_grist")
obj_function = tf.reduce_min(tf.abs(obj_var))
obj_grads = tf.gradients(obj_function, X)[0]
batch = mnist.train.next_batch(50)
batch_xs, batch_ys = batch[0], batch[1]
max_val, min_val = np.max(batch_xs), np.min(batch_xs)
gradient_search.build(batch_size=50, min_val=min_val, max_val=max_val)
"""insert code"""

with tf.Session() as session:
    session.run(tf.global_variables_initializer())
    while True:
        """inserted code"""
        monitor_vars = {'loss': cross_entropy, 'obj_function': obj_function, 'obj_grad': obj_grads}
        feed_dict = {X: batch_xs, Y: batch_ys, keep_prob: 0.5}
        batch_xs, scores_rank = gradient_search.update_batch_data(session=sess, monitor_var=monitor_vars,
                                                                  feed_dict=feed_dict, input_data=batch_xs, )
        """inserted code"""

        _, loss = sess.run([train_step, cross_entropy], feed_dict=feed_dict)

        """inserted code"""
        new_batch = mnist.train.next_batch(50)
        new_batch_xs, new_batch_ys = new_batch[0], new_batch[1]
        new_data_dict = {'x': new_batch_xs, 'y': new_batch_ys}
        old_data_dict = {'x': batch_xs, 'y': batch_ys}
        batch_xs, batch_ys = gradient_search.switch_new_data(new_data_dict=new_data_dict,
                                                             old_data_dict=old_data_dict,
                                                             scores_rank=scores_rank)
        gradient_search.check_time()
        """inserted code"""
