import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

training_inputs = np.array([[0,0,1],
                            [1,1,1],
                            [1,0,1],
                            [0,1,1]])

training_outpust = np.array([[0,1,1,0]]).T

np.random.seed(1)

synaptic_weights = 2 * np.random.random((3,1)) - 1

print('Случайные инициализирующие веса:')
print(synaptic_weights)

#метод обратного распространения
for i in range(20000):
    input_layer = training_inputs
    outputs = sigmoid( np.dot(input_layer, synaptic_weights))

    err = training_outpust - outputs
    adjustments = np.dot( input_layer.T, err * (outputs * (1 - outputs)) )

    synaptic_weights += adjustments

print('Веса после обучения: ')
print(synaptic_weights)


print('Результат после обучения: ')
print(outputs)

#TEST

new_inputs = np.array([1,1,0])
output = sigmoid( np.dot( new_inputs, synaptic_weights ))

print('New situation: ')
print(output)