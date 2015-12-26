# K-Means Clustering

## Description
Matlab script testing clustering on set of images. 

## Summary Report

The following report talks through a few points and results found through experimentation with the script.

### Test Design

When testing an image, we tested both a large version and a small version. Then, we compared the results with an image with similar features, but highler complexity. For example, we took a picture of a buffalo and compared the results to that of a picture with multiple buffullo. This design would allows us to come up with a base case and compare across complexity.

### Computational Costs (CC)
	
#### CC of Size of Image

#### CC of Number of Clusters

### Different Solutions for Repeated k-means Runs

Different solutions for repeated k-means runs is normal. Since we are using Lloyd's algorithm, it may get stuck at a local minimizer. This is because it is an NP-hard problem. So the solution is simple, run the algorithm multiple times with different random starting centroids. By taking the best answer, or in some cases the only answer that computes, we can avoid the algorithm getting stuck. The way the program does this is by running parallel instances of the k-means algorithm. Each instance has different configurations. Therefore with different configurations, the k-means algorithm will find different solutions. 


### Trade-Off Between Clusters and Quality of Image

### Complexity of Image