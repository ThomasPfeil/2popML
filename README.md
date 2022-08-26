# 2popML
A fast and simple machine learning model for two-population dust coagulation in protoplanetary disks

<div align="center">

| **colab** | 
|---|
|[![Colab](https://img.shields.io/badge/colab-notebook-yellow)](https://colab.research.google.com/github/ThomasPfeil/2popML/EvaluateMLModel.ipynb)|

</div>

## The Model
We trained a Multilayer Perceptron (MLP) on data derived from full coagulation simulations with the code COALA, by [Til Birnstiel](https://github.com/birnstiel). 
Our neural network's output are the size distribution parameter's respective time derivatives $\partial_t a_\text{max}$ and $\partial_t \sigma_1$, which are then used as source terms for a standard numerical integration in time.

The input of our neural network are $a_\text{max}$, $\sigma_1$, and parameters of the protoplanetary disk environment, like gas temperature, gas density, distance to the central star, etc. 
Our model is set up and trained with PyTorch Lightning. Our MLP consists of 3 hidden layers, each with 100 nodes, 14 nodes in the input layer, and two nodes in the output layer, fully connected with ReLU activation functions.

<img src="https://github.com/ThomasPfeil/2popML/blob/main/Graphics/Method.png" width="1600" />

