import random
import math

learning_rate = 0.1
def sigmoid(x):
	return math.tanh(x)
def dsigmoid(y):
	return 1 - y**2

# todo bias / momentum
class Net:
	def __init__(self, num_inputs, num_hidden, num_outputs):
		self.num_inputs = num_inputs + 1
		self.num_hidden = num_hidden
		self.num_outputs = num_outputs
		# Init output values
		self.input_layer = [1.0] * self.num_inputs
		self.hidden_layer = [1.0] * self.num_hidden
		self.output_layer = [1.0] * self.num_outputs
		# Weights
		self.in_to_hidden = [[random.uniform(0.0, 1.0) for w in xrange(self.num_hidden)] for j in xrange(self.num_inputs)]
		self.hidden_to_out = [[random.uniform(0.0, 1.0) for w in xrange(self.num_outputs)] for j in xrange(self.num_hidden)]
	def run(self, inputs):
		if len(inputs) != self.num_inputs - 1:
			print "inputs length don't match"

		for i in range(self.num_inputs - 1):
			self.input_layer[i] = inputs[i]
		
		# Input -> Hidden
		for j in range(self.num_hidden):
			sum = 0.0
			for i in range(self.num_inputs):
				sum += self.input_layer[i] * self.in_to_hidden[i][j]
			self.hidden_layer[j] = sigmoid(sum)

		# Hidden -> Output
		for k in range(self.num_outputs):
			sum = 0.0
			for j in range(self.num_hidden):
				sum += self.hidden_layer[j] * self.hidden_to_out[j][k]
			self.output_layer[k] = sigmoid(sum)
		return self.output_layer

	def backPropogate(self, targets, N):
		# calc output deltas
		output_deltas = [0.0] * self.num_outputs
		for k in range(self.num_outputs):
			error = targets[k] - self.output_layer[k]
			output_deltas[k] = error * dsigmoid(self.output_layer[k])
		
		# update output weights
		for j in range(self.num_hidden):
			for k in range(self.num_outputs):
				change = output_deltas[k] * self.hidden_layer[j]
				self.hidden_to_out[j][k] += N * change
		
		# calc hidden deltas
		hidden_deltas = [0.0] * self.num_hidden
		for j in range(self.num_hidden):
			error = 0.0
			for k in range(self.num_outputs):
				error += output_deltas[k] *  self.hidden_to_out[j][k]
			hidden_deltas[j] = error * dsigmoid(self.hidden_layer[j])
		
		# update input weights
		for i in range(self.num_inputs):
			for j in range(self.num_hidden):
				change = hidden_deltas[j] * self.input_layer[i]
				self.in_to_hidden[i][j] += N * change

		# calc combined error
		error = 0.0
		for k in range(len(targets)):
			error += 0.5 * (targets[k] - self.output_layer[k])**2
		return error
	def test(self, patterns):
		for p in patterns:
			inputs = p[0]
			print self.run(inputs)
	def train(self, patterns, max_iterations = 1000, N=0.5):
		for i in range(max_iterations):
			for p in patterns:
				inputs = p[0]
				targets = p[1]
				self.run(inputs)
				error = self.backPropogate(targets, N)
			if i % 50 == 0:
				print 'Combined Error ', error
# nn = Net(2, 2, 1)
# patterns = [
# 	[[0, 0], [1]],
# 	[[0, 1], [1]],
# 	[[1, 0], [1]],
# 	[[1, 1], [0]],
# ]
# nn.train(patterns)
# nn.test(patterns)