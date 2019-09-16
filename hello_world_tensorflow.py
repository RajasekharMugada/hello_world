# -*- coding: utf-8 -*-
"""
@author: Rajasekhar Mugada
@brief : Tensorflow basics
"""

import tensorflow as tf

#Tensorflow data types 

################## constants #########################################
'''
tf.constant(
    value,
    dtype=None,
    shape=None,
    name='Const'
)

Most used tensorflow dtype : 
    tf.int8/16/32/64, tf.uint8/16/32/64
    tf.bool, tf.string, tf.float16/32/64, tf.complex64/128
'''
c = tf.constant(value = 4.0, dtype= tf.float32, shape = [1,1] , name = 'c')

#############  place holders  #########################################
#place holders : Inputs that can be fed just before the execution
x = 

###########  variables: to solve ######################################
'''
w = tf.Variable(<initial-value>, name = <optional-name>)
To assign a new value to the variable use 'assign()'
w.assign(W + 1.0)
'''
w1 = tf.Variable(name = 'w1')
w2 = tf.Variable(name = 'w2')

  

#equation/graph to solve
y = w1*x^2 + w2*x + c


#Initialize the tensor graph

#Solve the tensor graph

#Print tensor graph




