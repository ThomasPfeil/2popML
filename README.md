# 2popML
A fast and simple machine learning model for dust coagulation in protoplanetary disks

## The Model
We trained a Multilayer Perceptron (MLP) on data derived from full coagulation simulations with the code COALA, by [Til Birnstiel](https://github.com/birnstiel). 
Our model predicts the time evolution of the maximum particle size and density on the large size bin of a two-population grain size distribution.
The resulting time derivatives can be used to infer time series data via direct numerical integration:

<img src="https://github.com/ThomasPfeil/2popML/blob/main/Graphics/Method.png" width="1600" />
