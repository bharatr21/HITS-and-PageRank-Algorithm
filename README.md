# HITS-and-PageRank-Algorithm
A very basic implementation of the HITS (HyperLink Induced Topic Search) and the PageRank Algorithms

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

The PageRank Score of any node in an iteration is given by: \
![equation](https://latex.codecogs.com/gif.latex?%5Cforall%20i%2C%20%5C%3A%20%5C%3A%20PageRank%28i%29%20%3D%20%5Csum_%7Bp%20%5Cin%20Neighbors%28i%29%7D%20%5Cfrac%7BPageRank%28p%29%7D%7BL%28p%29%7D) \
where ![equation](https://latex.codecogs.com/gif.latex?L%28p%29) is the number of outbound links (in this case, just the number of links since graph is undirected) of node ![equation](https://latex.codecogs.com/gif.latex?p) and ![equation](https://latex.codecogs.com/gif.latex?PageRank%28p%29) is the PageRank of nodes in the previous iteration.

This also takes into account the damping parameter ![equation](https://latex.codecogs.com/gif.latex?%5Calpha) where ![equation](https://latex.codecogs.com/gif.latex?%5Calpha%20%5Cin%20%5B0%2C%201%5D) with a default of 0.85,  in order to take into account the user's patience while surfing the web. \
![equation](https://latex.codecogs.com/gif.latex?%5Cforall%20p%2C%20%5C%3A%5C%3A%20PageRank%28p%29%20%3D%20%5Cfrac%7B1%20-%20%5Calpha%7D%7BN%7D%5C%3A%20&plus;%20%5C%3A%5Calpha%5C%3A*%5C%3APageRank%28p%29) \
where ![equation](https://latex.codecogs.com/gif.latex?N) is the total number of documents/webpages in consideration, in this case, the total number of Nodes. 

To use this implementation, please clone this repository first and use the `hits.py` or `pagerank.py` file: \
`git clone https://github.com/Bharat123rox/HITS-and-PageRank-Algorithm.git` \
To use the Algos:
```python
    c = HITS(G=Graph) or HITS(file='graph.txt') 
    hubs, authorities = c.compute_hits()
```
```python
    c = PageRank(G=Graph) or PageRank(file='graph.txt')
    pagerank = c.compute_pagerank()
```
