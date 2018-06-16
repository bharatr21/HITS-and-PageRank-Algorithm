# HITS-Algorithm
A very basic implementation of the HITS (HyperLink Induced Topic Search) algorithm

The Authority Score of any node is given by: \
\
![equation](http://latex.codecogs.com/gif.latex?%5Cforall%20i%2C%5C%3A%5C%3A%20Auth%28i%29%20%3D%20%5Csum_%7Bp%20%5Cin%20Neighbors%28i%29%7D%20Hubs%28p%29) \
The Hubbiness Score of any node is given by: \
\
![equation](http://latex.codecogs.com/gif.latex?%5Cforall%20i%2C%5C%3A%5C%3A%20Hubs%28i%29%20%3D%20%5Csum_%7Bp%20%5Cin%20Neighbors%28i%29%7D%20Auth%28p%29) \
And the algorithm is run for a certain number of iterations until it converges by the following steps:
1. Authority Update Round
2. Hub Update Round
3. Authority and Hub Scaling

The scaling is done by: \
![equation](http://latex.codecogs.com/gif.latex?%5Cforall%20i%20%5C%3A%5C%3A%20Hubs%28i%29%20%3D%20%5Cfrac%7BHubs%28i%29%7D%7B%5Csqrt%7B%5Csum_%7Bi%7D%5Cleft%20%5C%7C%20Hubs%28i%29%20%5Cright%20%5C%7C%5E2%7D%7D) \
![equation](http://latex.codecogs.com/gif.latex?%5Cforall%20i%20%5C%3A%5C%3A%20Auth%28i%29%20%3D%20%5Cfrac%7BAuth%28i%29%7D%7B%5Csqrt%7B%5Csum_%7Bi%7D%5Cleft%20%5C%7C%20Auth%28i%29%20%5Cright%20%5C%7C%5E2%7D%7D)
