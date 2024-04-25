'''
Copy existing structure from ID_3 over, but adjust which dataset we are using
from MNIST -> CIFAR-10

INFO: Iter: 480 Current Time cost:0:00:01.364792 Loss: nan Object function value: 0.0 Change step: 0.15
FINAL RESULTS: #ghips9_grist# Success to find NaN!  Iteration: <480> Time cost: <0:00:01.364792>.

INFO: Iter: 480 Current Time cost:0:00:01.354379 Loss: nan Object function value: 0.0 Change step: 0.15
FINAL RESULTS: #ghips9_grist# Success to find NaN!  Iteration: <480> Time cost: <0:00:01.355379>.

Author: Aymeric Damien
Project: https://github.com/aymericdamien/TensorFlow-Examples/
'''
from __future__ import print_function
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from keras.utils import plot_model
from keras.utils import to_categorical

import scripts.study_case.CIFAR_10.input_data as input_data
mnist = input_data.read_data_sets(one_hot=True)

# Parameters
learning_rate = 0.005
training_epochs = 25
batch_size = 100
display_step = 1

# tf Graph Input
x = tf.placeholder("float", [None, 1024]) # CIFAR-10 data image of shape 32*32=1024
y = tf.placeholder("float", [None, 10]) # 10 classes of labels

# Create model

# Set model weights
W = tf.Variable(tf.zeros([1024, 10]))
b = tf.Variable(tf.zeros([10]))

# Construct model
activation = tf.nn.softmax(tf.matmul(x, W) + b) # Softmax

# Minimize error using cross entropy
#MUTATION#
cost = -tf.reduce_sum(y*tf.log(activation)) # Cross entropy
optimizer = tf.train.AdamOptimizer(learning_rate).minimize(cost) # Gradient Descent


# Initializing the variables
init = tf.initialize_all_variables()


"""insert code"""
from scripts.utils.tf_utils import GradientSearcher
gradient_search = GradientSearcher(name="ghips9_grist")
obj_function = tf.reduce_min(tf.abs(activation))
obj_grads = tf.gradients(obj_function,x)[0]
batch_xs, batch_ys = mnist.train.next_batch(batch_size)
max_val, min_val = np.max(batch_xs), np.min(batch_xs)
gradient_search.build(batch_size=batch_size,min_val=min_val,max_val=max_val)
"""insert code"""


# Launch the graph
with tf.Session() as sess:
    sess.run(init)

    # Training cycle
    while True:
        avg_cost = 0.
        total_batch = int(mnist.train.num_examples/batch_size)
        # Loop over all batches

        """inserted code"""
        monitor_vars = {'loss': cost, 'obj_function': obj_function, 'obj_grad': obj_grads}
        feed_dict={x: batch_xs, y: batch_ys}
        batch_xs, scores_rank = gradient_search.update_batch_data(session=sess, monitor_var=monitor_vars,
                                                                  feed_dict=feed_dict,input_data=batch_xs,)
        """inserted code"""

        # Fit training using batch data
        sess.run(optimizer, feed_dict={x: batch_xs, y: batch_ys})
        # Compute average loss

        """inserted code"""
        new_batch_xs, new_batch_ys = mnist.train.next_batch(batch_size)
        new_data_dict = {'x': new_batch_xs, 'y': new_batch_ys}
        old_data_dict = {'x': batch_xs, 'y': batch_ys}
        batch_xs, batch_ys = gradient_search.switch_new_data(new_data_dict=new_data_dict, old_data_dict=old_data_dict,
                                                             scores_rank=scores_rank)
        gradient_search.check_time()
        """inserted code"""
