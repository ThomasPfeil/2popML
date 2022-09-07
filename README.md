# 2popML
### A fast and simple machine learning model for two-population dust coagulation in protoplanetary disks.

The following link will open a jupyter notebook and run it on Google Colab which allows you to test and evaluate the already trained model. For this, a subset of the test dataset is provided, which can be loaded and processed through the model.
GPU support is not required. 
To learn more about the model and how it is used, see the description below.

<div align="center">

| **colab** | 
|---|
|[![Colab](https://img.shields.io/badge/colab-notebook-yellow)](https://colab.research.google.com/github/ThomasPfeil/2popML/blob/main/EvaluateMLModel.ipynb)|

</div>

## The 2pop Approach to Dust Coagulation

We are currently developing an approach in which the dust size distribution is described by a truncated power law, instead of a discretized distribution with hundreds of size bins. Our goal is to make the modeling of dust coagulation on top of large scale hydrodynamic simulations more feasible.
For a given total dust column density $\sigma_\text{tot}$, and a minimum particle size $a_\text{min}=10^{-5}$ cm, this simplified distribution can be described by only two parameters:

$$
\begin{align}
    a_\text{max}: \quad &\text{The size of the largest particles (truncation size of the power law)} \\ 
    \sigma_1: \quad &\text{The column density of particles larger than $a_\text{int}=\sqrt{a_\text{max}a_\text{min}}$}
\end{align}
$$

It can be shown that the exponent of the power law size distribution $\sigma(a)\propto a^{p+4}$ is then given by $p = \frac{\log{\left(\sigma_1/\sigma_0\right)}}{\log{\left(a_\text{max}/a_\text{int}\right)}} - 4$,
where $\sigma_0= \sigma_\text{tot}-\sigma_1$ is the column density of particles smaller than $a_\text{int}$.

In contrast to other approximate models like two-pop-py ([Birnstiel et al., 2012](https://ui.adsabs.harvard.edu/abs/2012A%26A...539A.148B/abstract)), this approach makes it possible to retain information about the overall shape of the size distribution.
It is, however, not trivial to find a mathematical description for the time evolution of the power law distribution without making strongly simplifying assumptions. 

Here, we present a machine learning aided two-population model, which predicts the time evolution of the simplified distribution.

## The Model
We trained a Multilayer Perceptron (MLP) on data derived from full coagulation simulations with the code COALA, by [Til Birnstiel](https://github.com/birnstiel). 
Our neural network's output are the size distribution parameter's respective time derivatives $\partial_t a_\text{max}$ and $\partial_t \sigma_1$, which are then used as source terms for a standard numerical integration in time.
The input of our neural network are $a_\text{max}$, $\sigma_1$, and parameters of the protoplanetary disk environment, like gas temperature, gas density, distance to the central star, etc. 
Our model is set up and trained with PyTorch Lightning. Our MLP consists of 3 hidden layers, each with 100 nodes, 14 nodes in the input layer, and two nodes in the output layer, fully connected with ReLU activation functions.

<img src="https://github.com/ThomasPfeil/2popML/blob/main/Graphics/Method.png" width="1600" />

### Model Input:
Input parameters are: the logarithm of density of large particles $\text{log}\left(\frac{\sigma_1}{\sigma_\text{tot}}\right)$, the logorithm of the maximum particle size $a_\text{max}$, the power law index $p$, the stellar mass $M_\*$, the stellar temperature $T_\*$, the disk gas mass $M_\text{disk}$, the turbulence parameter $\alpha_\text{turb}$, the distance to the central star $R$, the lokal gas temperature $T_\text{gas}$, the local gas column density $\Sigma_\text{gas}$, the dust-to-gas ratio $\epsilon$, the fragmentation size $a_\text{frag}$, the local Keplerian frequency $\Omega_\text{K}$, and the local monodisperse dust growth time scale $t_\text{gr}$

<img src="https://github.com/ThomasPfeil/2popML/blob/main/Graphics/Input.png" width="1600" />

### Model Output:
The first model output is the tenth root of the gradient of $a_\text{max}$, multiplied by the sign of the gradient. The second output the tenth root of the gradient of $\sigma_1$, multiplied by the sign of the gradient.

<img src="https://github.com/ThomasPfeil/2popML/blob/main/Graphics/output.png" width="300" />
