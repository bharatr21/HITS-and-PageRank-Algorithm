import sys
from math import sqrt
class PageRank():
    '''
    @class PageRank: The base class for the PageRank Algorithm.
    @param G: The graph on which the PageRank Algorithm shall be performed. 
    Has to be a 0-1 adjacency matrix format as space separated values.
    @param file(required if Graph not provided): File containing Adjacency Matrix
    Either file or Graph HAS to be provided.
    Initialize the pagerank values to 1/(n)
    @param alpha: Damping Factor/Parameter for PageRank (0.85 by default)
    @param max_iter: Maximum number of iterations the algorithm performs, if the algorithm has not converged earlier.
    @param tol: The error difference (tolerance) between two iterations for which
    the algorithm is declared converged and terminates (0.001 by default)
    @return pagerank
    The Array of PageRank scores for each node respectively.
    Other Keyword Arguments are simply discarded.
    '''
    def __init__(self, G=None, file=None, alpha=0.85, max_iter=100000, tol=1e-3, **kwargs):
        if not G and not file:
            sys.exit('Exited the program because no graph was provided.')
        self.G = G if G else read_from_file(file)
        self.max_iter = max_iter
        self.tol = tol
        self.n = len(self.G)
        self.alpha = alpha
        self.pagerank = [1.0/self.n for i in range(self.n)]
        self.L = [0 for i in range(self.n)]
    def compute_pagerank(self):
        #Actual Computation of PageRank
        sanity_check(self.G)
        prevpagerank = [0 for i in range(self.n)]
        #Find number of outbound links (One-time Process)
        for i in range(self.n):
                for j in range(self.n):
                    self.L[i] += self.G[i][j]
        for i in range(self.max_iter):
            prevpagerank = sum(self.pagerank)
            #Calculate current iteration of PageRank
            for i in range(self.n):
                self.pagerank[i] = 0
                for j in range(self.n):
                    if self.G[i][j] == 1:
                        self.pagerank[i] = self.pagerank[i] + 1.0 * self.pagerank[j] / self.L[j] if self.L[j] else 1.0/self.n
            #Incorporate damping factor alpha
            self.pagerank[i] = ((1 - self.alpha) * 1.0)/self.n + self.alpha * (self.pagerank[i])
            #Condition for convergence of PageRank
            if abs(sum(self.pagerank) - prevpagerank) < self.n * self.tol:
                break
        return self.pagerank
def read_from_file(files):
    G = []
    lis = []
    with open(files) as f:
        for line in f:
            lis = line.split()
            try:
                lis = [int(i) for i in lis]
            except (ValueError, TypeError):
                raise TypeError('Cannot convert to integer in the adjacency matrix')
            G.append(lis)
    #Convert to 0-1 adjacency matrix (binarization, here edge weights are discarded and only presence is considered)
    G = [[1 if i else 0 for i in group] for group in G] 
    return G
def check_square_matrix(matrix):
    return all(len(row) == len(matrix) for row in matrix)
def sanity_check(G):
    #Basic check for a 0-1 Adjacency Matrix
    n = len(G)
    for i in range(n):
        for j in range(n):
            try:
                if not check_square_matrix(G):
                    raise ValueError('Only a square matrix processed for PageRank to be properly defined.')
                if G[i][j] == 0 or G[i][j] == 1:
                    pass
                else:
                    raise ValueError('Only a 0-1 Adjacency Matrix shall be processed')
            except IndexError:
                raise ValueError('Not a valid Adjacency Matrix')