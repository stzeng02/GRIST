# Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================
import tensorflow as tf
tf.set_random_seed(20191215)
import numpy as np
import sys
sys.path.append("/data")
np.random.seed(0)
from scripts.study_case.ID_1.spatial_transformer import transformer
from scripts.study_case.ID_1.tf_utils import weight_variable, bias_variable, dense_to_one_hot
from datetime import datetime
import os

s1 = datetime.now()

# %% Load data
parent_dir = os.path.dirname(os.path.abspath(__file__))
# mnist_cluttered = np.load('./data/mnist_sequence1_sample_5distortions5x5.npz')
mnist_cluttered = np.load(os.path.join(parent_dir,'data/mnist_sequence1_sample_5distortions5x5.npz'))

X_train = mnist_cluttered['X_train']
y_train = mnist_cluttered['y_train']
X_valid = mnist_cluttered['X_valid']
y_valid = mnist_cluttered['y_valid']
X_test = mnist_cluttered['X_test']
y_test = mnist_cluttered['y_test']

# % turn from dense to one hot representation
Y_train = dense_to_one_hot(y_train, n_classes=10)
Y_valid = dense_to_one_hot(y_valid, n_classes=10)
Y_test = dense_to_one_hot(y_test, n_classes=10)

# %% Graph representation of our network

# %% Placeholders for 40x40 resolution
x = tf.placeholder(tf.float32, [None, 1600])
y = tf.placeholder(tf.float32, [None, 10])

# %% Since x is currently [batch, height*width], we need to reshape to a
# 4-D tensor to use it in a convolutional graph.  If one component of
# `shape` is the special value -1, the size of that dimension is
# computed so that the total size remains constant.  Since we haven't
# defined the batch dimension's shape yet, we use -1 to denote this
# dimension should not change size.
x_tensor = tf.reshape(x, [-1, 40, 40, 1])

# %% We'll setup the two-layer localisation network to figure out the
# %% parameters for an affine transformation of the input
# %% Create variables for fully connected layer
W_fc_loc1 = weight_variable([1600, 20])
b_fc_loc1 = bias_variable([20])

W_fc_loc2 = weight_variable([20, 6])
# Use identity transformation as starting point
initial = np.array([[1., 0, 0], [0, 1., 0]])
initial = initial.astype('float32')
initial = initial.flatten()
b_fc_loc2 = tf.Variable(initial_value=initial, name='b_fc_loc2')

# %% Define the two layer localisation network
h_fc_loc1 = tf.nn.tanh(tf.matmul(x, W_fc_loc1) + b_fc_loc1)
# %% We can add dropout for regularizing and to reduce overfitting like so:
keep_prob = tf.placeholder(tf.float32)
h_fc_loc1_drop = tf.nn.dropout(h_fc_loc1, keep_prob)
# %% Second layer
h_fc_loc2 = tf.nn.tanh(tf.matmul(h_fc_loc1_drop, W_fc_loc2) + b_fc_loc2)

# %% We'll create a spatial transformer module to identify discriminative
# %% patches
out_size = (40, 40)
h_trans = transformer(x_tensor, h_fc_loc2, out_size)

# %% We'll setup the first convolutional layer
# Weight matrix is [height x width x input_channels x output_channels]
filter_size = 3
n_filters_1 = 16
W_conv1 = weight_variable([filter_size, filter_size, 1, n_filters_1])

# %% Bias is [output_channels]
b_conv1 = bias_variable([n_filters_1])

# %% Now we can build a graph which does the first layer of convolution:
# we define our stride as batch x height x width x channels
# instead of pooling, we use strides of 2 and more layers
# with smaller filters.

h_conv1 = tf.nn.relu(
    tf.nn.conv2d(input=h_trans,
                 filter=W_conv1,
                 strides=[1, 2, 2, 1],
                 padding='SAME') +
    b_conv1)

# %% And just like the first layer, add additional layers to create
# a deep net
n_filters_2 = 16
W_conv2 = weight_variable([filter_size, filter_size, n_filters_1, n_filters_2])
b_conv2 = bias_variable([n_filters_2])
h_conv2 = tf.nn.relu(
    tf.nn.conv2d(input=h_conv1,
                 filter=W_conv2,
                 strides=[1, 2, 2, 1],
                 padding='SAME') +
    b_conv2)

# %% We'll now reshape so we can connect to a fully-connected layer:
h_conv2_flat = tf.reshape(h_conv2, [-1, 10 * 10 * n_filters_2])

# %% Create a fully-connected layer:
n_fc = 1024
W_fc1 = weight_variable([10 * 10 * n_filters_2, n_fc])
b_fc1 = bias_variable([n_fc])
h_fc1 = tf.nn.relu(tf.matmul(h_conv2_flat, W_fc1) + b_fc1)

h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

# %% And finally our softmax layer:
W_fc2 = weight_variable([n_fc, 10])
b_fc2 = bias_variable([10])
y_pred = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

# %% Define loss/eval/training functions
#MUTATION#
cross_entropy = -tf.reduce_sum(y * tf.log(y_pred))
opt = tf.train.AdamOptimizer()
optimizer = opt.minimize(cross_entropy)
grads = opt.compute_gradients(cross_entropy, [b_fc_loc2])

# %% Monitor accuracy
correct_prediction = tf.equal(tf.argmax(y_pred, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, 'float'))

# %% We now create a new session to actually perform the initialization the
# variables:
sess = tf.Session()
sess.run(tf.initialize_all_variables())


# %% We'll now train in minibatches and report accuracy, loss:
iter_per_epoch = 100
n_epochs = 500
train_size = 10000

indices = np.linspace(0, 10000 - 1, iter_per_epoch)
indices = indices.astype('int')
iter_i = 0

"""insert code"""
from scripts.utils.tf_utils import GradientSearcher
gradient_search = GradientSearcher(name="ghips1_grist")
batch_size = int(train_size/iter_per_epoch)
obj_function = tf.reduce_min(tf.abs(y_pred))
obj_grads = tf.gradients(obj_function,x)[0]

batch_xs = X_train[indices[iter_i]:indices[iter_i + 1]]
batch_ys = Y_train[indices[iter_i]:indices[iter_i + 1]]

max_val, min_val = np.max(batch_xs), np.min(batch_xs)
gradient_search.build(batch_size=batch_size,min_val=min_val,max_val=max_val)
"""insert code"""


while True:

    """inserted code"""
    monitor_vars = {'loss': cross_entropy, 'obj_function': obj_function, 'obj_grad': obj_grads}
    feed_dict = {x: batch_xs, y: batch_ys,keep_prob: 1.0}
    batch_xs, scores_rank = gradient_search.update_batch_data(session=sess, monitor_var=monitor_vars,
                                                              feed_dict=feed_dict,input_data=batch_xs,
                                                              )
    """inserted code"""

    sess.run(optimizer, feed_dict={
        x: batch_xs, y: batch_ys, keep_prob: 0.8})

    """inserted code"""
    iter_i = gradient_search.iter_count
    iter_i = iter_i % (indices.shape[0]-1)
    new_batch_xs = X_train[indices[iter_i]:indices[iter_i + 1]]
    new_batch_ys = Y_train[indices[iter_i]:indices[iter_i + 1]]
    new_data_dict = {'x': new_batch_xs, 'y': new_batch_ys}
    old_data_dict = {'x': batch_xs, 'y': batch_ys}
    batch_xs, batch_ys = gradient_search.switch_new_data(new_data_dict=new_data_dict, old_data_dict=old_data_dict,
                                                         scores_rank=scores_rank)
    gradient_search.check_time()
    """inserted code"""
