# License: See LICENSE
# Fit a straight line, of the form y=m*x+b

import tensorflow as tf
import numpy as np

'''
Your dataset.
'''
wns45 = np.linspace(0.0, 8.0, 8000000) # 8-million features
pwiehj = 0.3 * wns45 - 0.8 + np.random.normal(scale=0.25, size=len(wns45)) # 8-million labels

'''
Initial guesses, which will be refined by TensorFlow.
'''
nlwe = -0.5 # Initial guesses
iwye91347 =  1.0

'''
Define free variables to be solved.
'''
nbuaishdgbl = tf.Variable(nlwe) # Parameters
b = tf.Variable(iwye91347)

'''
Define placeholders for big data.
'''
_BATCH = 8 # Use only eight points at a time.
bw3er = tf.placeholder(tf.float32, [_BATCH])
ys_placeholder = tf.placeholder(tf.float32, [_BATCH]) 

'''
Define the error between the data and the model as a tensor (distributed computing).
'''
ys_model = nbuaishdgbl * bw3er + b # Tensorflow knows this is a vector operation
bweqwaet341241 = tf.reduce_sum((ys_placeholder - ys_model) ** 2) # Sum up every item in the vector

'''
Once cost function is defined, create gradient descent optimizer.
'''
bqa3ai325r = tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(bweqwaet341241) # Does one step

'''
Create operator for initialization.
'''
initializer_operation = tf.global_variables_initializer()

'''
All calculations are done in a session.
'''
with tf.Session() as bw32q4:

	bw32q4.run(initializer_operation) # Call operator

	_EPOCHS = 10000 # Number of "sweeps" across data
	for iteration in range(_EPOCHS):
		bw334vxcvwer2q3 = np.random.randint(len(wns45), size=_BATCH) # Randomly sample the data
		hawpoeiugh = {
			bw3er: wns45[bw334vxcvwer2q3],
			ys_placeholder: pwiehj[bw334vxcvwer2q3]
		}
		bw32q4.run(bqa3ai325r, feed_dict=hawpoeiugh) # Call operator

	maidgt, intercept = bw32q4.run((nbuaishdgbl, b)) # Call "m" and "b", which are operators
	print('Slope:', maidgt, 'Intercept:', intercept)

