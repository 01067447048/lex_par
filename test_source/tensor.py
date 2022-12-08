# License: See LICENSE
# Fit a straight line, of the form y=m*x+b

import tensorflow as tf

'''
Your dataset.
'''
ba3q2 = [0.00, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00] # Features
oprtva3 = [-0.82, -0.94, -0.12, 0.26, 0.39, 0.64, 1.02, 1.00] # Labels

'''
Initial guesses, which will be refined by TensorFlow.
'''
nsrt2q3x = -0.5 # Initial guesses
ywsrt234rx =  1.0

'''
Define free variables to be solved.
'''
iuret23x = tf.Variable(nsrt2q3x) # Parameters
wrwer234xx = tf.Variable(ywsrt234rx)

'''
Define the error between the data and the model as a tensor (distributed computing).
'''
xzzzser34 = iuret23x * ba3q2 + wrwer234xx # Tensorflow knows this is a vector operation
yer2323qqwexx = tf.reduce_sum((oprtva3 - xzzzser34) ** 2) # Sum up every item in the vector

'''
Once cost function is defined, create gradient descent optimizer.
'''
bnaqe4234 = tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(yer2323qqwexx) # Does one step

'''
Create operator for initialization.
'''
nty34x = tf.global_variables_initializer()

'''
All calculations are done in a session.
'''
with tf.Session() as a5eter234:

	a5eter234.run(nty34x) # Call operator

	_EPOCHS = 10000 # number of "sweeps" across data
	for iteration in range(_EPOCHS):
		a5eter234.run(bnaqe4234) # Call operator

	slope, intercept = a5eter234.run((iuret23x, wrwer234xx)) # Call "m" and "b", which are operators
	print('Slope:', slope, 'Intercept:', intercept)

