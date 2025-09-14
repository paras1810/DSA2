import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

observations = 1000
xs=np.random.uniform(low=-10, high=10, size=(observations,1))
zs=np.random.uniform(-10, 10, (observations,1))
inputs = np.column_stack((xs, zs))
print(inputs.shape)
noise=np.random.uniform(-1,1,(observations,1))
targets = 2*xs-3*zs+5+noise
 
init_range = 0.1
weights = np.random.uniform(-init_range, init_range, size=(2,1))
biases = np.random.uniform(-init_range, init_range, size=1)

learning_rate=0.2

'''
Calculate outputs
Compare outputs to targets through the loss
Print the loss
Adjust weights and biases
'''
for i in range(100):
    outputs = np.dot(inputs, weights) + biases
    deltas = outputs - targets
    loss = np.sum(deltas**2)/2/observations
    print(loss)
    deltas_scaled=deltas/observations
    weights=weights-learning_rate*np.dot(inputs.T, deltas_scaled)
    biases = biases - learning_rate*np.sum(deltas_scaled)
print(weights, biases)
'''
Developed by Google NN, CNN, RNN
tensorflow 2.0
conda info --envs
conda create --name py3-TF2.0
conda install tensorflow
vs scikitlearn
    Tensorflow use CPU and GPU of system.
    Add TPU(Tensor processing Unit)
    SkLearn: For K-Means Clustering, Random Forest
Tensorflow1 vs Tensorflow2
    1 is very code intensive and not coder friendly to used.
    Pytorch and Keras
    TF2 is more likely keras
'''
import tensorflow as tf
print(tf.__version__) #2.0.0
generated_inputs = np.column_stack((xs, zs))
generated_targets = 2*xs-3*zs+5+noise
np.savez('TF_intro', inputs=generated_inputs, targets=generated_targets)

training_data = np.load('TF_intro.npz')
input_size=2
output_size=1
model = tf.keras.Sequential([
    tf.keras.layers.Dense(output_size)
])
model.compile(optimizer='sgd', loss='mean_squared_error')#
model.fit(training_data['inputs'], training_data['targets'], epochs=100, verbose=0)
weights = model.layers[0].get_weights()[0]
bias = model.layers[0].get_weights[1]
model.predict_on_batch(training_data['inputs'])
# Epoch--Iteration over the full dataset

custom_optimizer = tf.keras.optimizers.SGD(learning_rate=0.2)

#MNIST Dataset
import tensorflow_datasets as tfds
mnist_dataset = tfds.load(name='mnist', as_supervised=True, with_info=True)




