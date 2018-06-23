import sys
from math import sqrt
class HITS():
    '''
    @class HITS: The base class for the HITS Algorithm.
    @param G: The graph on which the HITS Algorithm shall be performed. 
    Has to be a 0-1 adjacency matrix format as space separated values.
    @param file(required if Graph not provided): File containing Adjacency Matrix
    Either file or Graph HAS to be provided.
    @param initial: Initialize the hubbiness and authority values to 1, 1/sqrt(n) or 1/(n) 
    for values 1, 2, 3 respectively where n->Number of nodes (1 by default)
    @param max_iter: Maximum number of iterations the algorithm performs, if the algorithm has not converged earlier.
    @param tol: The error difference (tolerance) between two iterations for which 
    the algorithm is declared converged and terminates (0.000001 by default)
    @return hub, auth
    The Array of Hubbiness scores for each node and the Array of Authority scores for each node respectively.
    Other Keyword Arguments are simply discarded.
    '''
    def __init__(self, G=None, file=None, initial=1, max_iter=100000, tol=1e-6, **kwargs):
        if not G and not files:
            sys.exit('Exited the program because no graph was provided.')
        self.G = G if G else read_from_file(file)
        self.max_iter = max_iter
        self.tol = tol
        self.n = len(self.G)
        self.initial = initial
        if self.initial == 2:
            self.hubs = [1.0/sqrt(self.n) for i in range(self.n)]
            self.auth = [1.0/sqrt(self.n) for i in range(self.n)]
        elif self.initial == 3:
            self.hubs = [1.0/self.n for i in range(self.n)]
            self.auth = [1.0/self.n for i in range(self.n)] 
        else:
            self.initial = 1
            self.hubs = [1 for i in range(self.n)]
            self.auth=  [1 for i in range(self.n)]
    def compute_hits(self):
    	#Actual Computation of Hubbiness and Authority
        sanity_check(self.G)
        prevhubs = [0 for i in range(self.n)]
        prevauth = [0 for i in range(self.n)]
        for i in range(self.max_iter):
            prevhubs = sum(self.hubs)
            prevauth = sum(self.auth)
            self.auth = [0 for i in range(self.n)]
            #Authority Update Round
            for i in range(self.n):
                for j in range(self.n):
                    if self.G[i][j] == 1:
                        self.auth[i] += self.hubs[j]
            auth_scale = sqrt(sum([x**2 for x in self.auth]))
            #Hub Update Round
            self.hubs = [0 for i in range(self.n)]
            for i in range(self.n):
                for j in range(self.n):
                    if self.G[i][j] == 1:
                        self.hubs[i] += self.auth[j]
            hubs_scale = sqrt(sum([x**2 for x in self.hubs]))
            #Scaling Authorities and Hubs
            self.auth = [x / auth_scale for x in self.auth]
            self.hubs = [x / hubs_scale for x in self.hubs]
            #Check for Convergence
            if abs(sum(self.hubs) - prevhubs) < self.n*self.tol or abs(sum(self.auth) - prevauth) < self.n*self.tol:
                break
        return self.hubs, self.auth
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
                    raise ValueError('Only a square matrix processed for HITS Algorithm to be properly defined.')
                if G[i][j] == 0 or G[i][j] == 1:
                    pass
                else:
                    raise ValueError('Only a 0-1 Adjacency Matrix shall be processed')
            except IndexError:
                raise ValueError('Not a valid Adjacency Matrix')