# TSP Approximation Algorithms in Python

Here are a some implementations of various approximation algorithms for the optimal Travelling Salesperson Tour in 2D Euclidean Space. Additionally there are some helper algorithms such as Kruskal's MST algorithm which solve related problems. I developed these as part of my work on a research paper, which I will link when it is done.

Every algorithm takes in as input a list of 2-tuples of floats.

Here is a list of the algorithms implemented here

## TSP Approximation Algorithms

### Nearest Neighbor

The nearest neighbor algorithm is a worst-case O(n^2) time algorithm for approximating the TSP tour. In order to implement this, rather than denote the vertices as objects with an visited attribute, I simply kept two lists, one of visited nodes to return as the tour and one of unvisited nodes to consider for adding. The additional space doesn't affect complexity, but increases the speed significantly.
More can be read about the algorithm in the Wikipedia article: https://en.wikipedia.org/wiki/Nearest_neighbour_algorithm

### Insertion-Type Algorithms

The insertion type algorithms for the Traveling Salesperson Tour, like other insertion-type algorithms, operate off inserting nodes successively into partial solutions until all nodes are incorporated. The only difference between each one is its selection heuristic, hence why my implementation makes use of a chasis function that takes in the selection heuristic as a parameter. They run in O(n^2) time, with the exception of cheapest which runs in O(n^2 log n) time.

More can be read about each version in the links from Georgia Tech as listed below:

Nearest Insertion: https://www2.isye.gatech.edu/~mgoetsch/cali/VEHICLE/TSP/TSP009__.HTM

Cheapest Insertion: https://www2.isye.gatech.edu/~mgoetsch/cali/VEHICLE/TSP/TSP011__.HTM

Random Insertion (this is essentially arbitrary insertion): https://www2.isye.gatech.edu/~mgoetsch/cali/VEHICLE/TSP/TSP013__.HTM

Farthest Insertion: https://www2.isye.gatech.edu/~mgoetsch/cali/VEHICLE/TSP/TSP015__.HTM

### Christofides

Christofides' algorithm is specific to metric space, unlike the previous algorithms which could be used on graphs which don't obey triangle equality. It first finds the minimum spanning tree of the nodes (which I have implemented as specified below), then in order to ensure even degree, finds a minimum cost perfect matching (for this I used the networkx library) of the nodes of odd degree and adds it to the graph. It then finds an Euler circuit (this implementation uses Hierholzer's Algorithm), which is then converted to a Hamiltonian circuit by removing multiple occurences of a vertex (hence why triangle equality is required). It runs in varying times depending on the implementations used for each step. In this case it runs in O(n^3) because the longest part is the minimum cost perfect matching.

More can be read about the algorithm in the Wikipedia article: https://en.wikipedia.org/wiki/Christofides_algorithm

## Helper Algorithms

### Kruskal's Algorithm for Minimum Spanning Tree

Kruskal's algorithm is a greedy algorithm for finding the Minimum Spanning Tree. It runs in O(E log V) time where E and V are the number of edges and vertices respectively. Since the MST is in Euclidean space, the number of edges is n^2 - n, which brings the time complexity to O(n^2 log n). There are two versions implemented, one which returns simply the length for use as a lower bound of comparison and another as an adjacency list.

More can be read about the algorithm in the Wikipedia article: https://en.wikipedia.org/wiki/Kruskal%27s_algorithm

### Hierholzer's Algorithm for finding Euler Circuits

Hierholzer's Algorithm is an O(E) time algorithm for finding the Euler Circuit of a given graph. For our purposes this translates to and O(n^2) time algorithm. It takes an adjacency list as a parameter (particularly a subset of the one returned by my implementation of Kruskal's algorithm), and returns the list of nodes visited by the Euler circuit it found in order with repeats. It rejects adjacency lists with no Euler circuit, returning an empty list.

More can be read about the algorithm in the Wikipedia article for Eulerian paths: https://en.wikipedia.org/wiki/Eulerian_path#Hierholzer's_algorithm 

My implementation is heavily influenced by the explanation and implentations described here: https://slaystudy.com/hierholzers-algorithm/
