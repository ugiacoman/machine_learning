# K-Means Clustering

## Description
Matlab script testing clustering on set of images. 

## Summary Report

The following report talks through a few points and results found through experimentation with the script.

### Test Design

When testing an image, we tested both a large version and a small version. Then, we compared the results with an image with similar features, but highler complexity. For example, we took a picture of a buffalo and compared the results to that of a picture with multiple buffullo. This design would allows us to come up with a base case and compare across complexity.

### Computational Costs (CC)

The problem is compuationaly NP-hard. However, by using Lloyd's algorithm as well as running several instances we can converge on better local optimum. 
	
#### CC of Size of Image

The script reads the images and manipulates the pixels using their red-green-blue (RGB) color values. The RGB values give us a representation of the pixel in the three-dimensional space. The pixels can then be converted into clusters. We then replace the clusters with the mean value of the pixels (RGB). This will break up the image into subregions of clusters. The larger the image, the more pixels and potentionally more clusters. However, if we take the same image, both a large and a small version. The ideal number of clusters should be around the same. However, there will be less pixels to compute from. Therefore, by choosing a smaller version of an image, with less pixels, we should be able to lower the computational cost. 

#### CC of Number of Clusters

Running a fixed number i of iterations of the standard algorithm for a number of k clusters takes only O(iknd) for n points in d dimensions. So for every extra cluster computed, this will increase the complexity by k + 1.

### Different Solutions for Repeated k-means Runs

Different solutions for repeated k-means runs is normal. Since we are using Lloyd's algorithm, it may get stuck at a local minimizer. This is because it is an NP-hard problem. So the solution is simple, run the algorithm multiple times with different random starting centroids. By taking the best answer, or in some cases the only answer that computes, we can avoid the algorithm getting stuck. The way the program does this is by running parallel instances of the k-means algorithm. Each instance has different configurations. Therefore with different configurations, the k-means algorithm will find different solutions. 


### Trade-Off Between Clusters and Quality of Image

The less pixels, the less will be used to compute the mean value of the cluster center. Therefore the mean value may be more accurate with a higher number of pixels. If the mean value is more accurate, subregions of clusters may also be more accurate.

### Complexity of Image