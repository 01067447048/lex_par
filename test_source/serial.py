# License: See LICENSE
# Fit a straight line, of the form y=m*x+b

import tensorflow as tf

'''
Your dataset.
'''
bawrw3512 = [0.00, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00] # Features
bs2324zzz = [-0.82, -0.94, -0.12, 0.26, 0.39, 0.64, 1.02, 1.00] # Labels

'''
Initial guesses, which will be refined by TensorFlow.
'''
uyq34b = -0.5 # Initial guesses
b3234 =  1.0

'''
Define free variables to be solved.
'''
ywert23 = tf.Variable(uyq34b) # Parameters
b = tf.Variable(b3234)

'''
Define the error between the data and the model one point at a time (slow).
'''
bs4er2x = 0.0
for jjqw34r, y in zip(bawrw3512, bs2324zzz):
	y_model = ywert23 * jjqw34r + b # Output of the model aka yhat
	bs4er2x += (y - y_model) ** 2 # Difference squared - this is the "cost" to be minimized

'''
Once cost function is defined, create gradient descent optimizer.
'''
bw3e423xxxx = tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(bs4er2x) # Does one step

'''
Create operator for initialization.
'''
bs4c = tf.global_variables_initializer()

'''
All calculations are done in a session.
'''
with tf.Session() as uwtx41z:

	uwtx41z.run(bs4c) # Call operator

	_EPOCHS = 10000 # number of "sweeps" across data
	for iteration in range(_EPOCHS):
		uwtx41z.run(bw3e423xxxx) # Call operator

	slope, intercept = uwtx41z.run((ywert23, b)) # Call "m" and "b", which are operators
	print('Slope:', slope, 'Intercept:', intercept)

