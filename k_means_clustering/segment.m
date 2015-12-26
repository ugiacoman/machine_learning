%% Image segmentation using k-means clustering.
%
% The goal of image segmentation is to break up an image into subregions.  Typically the subregions 
% represent significant features of the image.  For instance, given a picture of a car, one might wish
% to segment the image into the part that is the car and the part that is the background.  
%
% Image segementation is one of those tasks that humans are very good at but which is hard to do 
% automatically in a reliable way.  Clustering algorithms are one simple approach to image segmentation.
% In this exercise you will use k-means clustering to segment some images of animals.
%
% You will read in images and manipulate the pixels using their red-green-blue (RGB) color values.
% The RGB values of a pixel allow us to view the pixel as a point in three-dimensional space.  We
% can then cluster the pixels into a specificed number of clusters.  Now replace the RGB values of 
% all the pixels in a cluster with the mean value (the cluster center).  This has the effect of 
% breaking the image up into subregions.  
%
% This approach can also be used for a crude form of image compression.  For instance, if we use 
% 16 clusters, then we can replace the RGB values of each pixel, which requires 24 bits per pixel, 
% with an index into a table of 16 colors, which requires 4 bits per pixel.
%
% One real-world image segmentation problem to which machine learning techniques have been applied 
% comes from histology (the study of cells and tissues).  The microscopic examination of tissue samples 
% is an important step in thed diagnosis of many diseases, including cancer.  As part of this process, 
% tissue samples are stained with special dyes.  For example, a common technique involves staining tissue
% samples with the chemicals haematoxylin and eosin (H&E staining).  In the stained sample, cell nuclei 
% show up as purple, while connective tissue is pink.  Here are a couple of references concerning ML
% and histological image analysis:
%   <http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3678749/>
%   <http://www.nec.com/en/global/prod/epathologist/images/e-Pathologist_HE.pdf>

close all;
clear all;

%% Read and display the original image (e.g., panda_small.jpg).

filename = input('Enter the file name: ', 's');
% filename = 'panda_small.jpg';
P = imread(filename);

% Shrinking the image may makes things easier.
% P = imresize(P, 0.1);

figure('Name', 'Original image', 'NumberTitle', 'off');
imshow(P);
title('Original image', 'FontSize', 18); 
shg;

%% Prompt for the number of clusters (which corresponds to the number of colors in the processed image).
ncolors = input('Enter the desired number of clusters: ');
% ncolors = 8;

%% Convert the image into a set of points in $\boldmath{R^{3}}$.
% The original image is m * n with k colors.  This is turned into an (m * n) * k array of k-vectors.
[m, n, k] = size(P);
X = double(reshape(P, m*n, k));

%% The star of our show: k-means clustering.
% When applying k-means clustering, it's a good idea to run it multiple times with different random starting
% centroids.  Lloyd's algorithm may get stuck at a local minimizer (it's an NP-hard problem); running k-means 
% from multiple starting configurations and taking the best answer seen helps ameliorate the problem.  This
% is done with the optional argument 'Replicates' below.
%
% The replicated runs of k-means exhibits *embarassing parallelism*---we are running multiple, independent instances 
% of the same k-means algorithm, just with different starting configurations.  If we have a multi-CPU or 
% multi-core system, we can try running them on different processing units.  This is also sometimes called
% *single program, multiple data (SPMD) parallelism*.

% Fire up a pool of parallel workers (this may take a second if no pool is active).  On my four-core machine 
% at home, this leads to a pool of 4.  YMMV.
pp = gcp;

% Turn on the 'UseParallel' option for kmeans().  
opts = statset('Display', 'final', 'UseParallel', true);

%% Release the Kraken!  
% *For your own personal edification, try running with 'UseParallel' set to false and see if there is*
% *any difference in the runtime of kmeans().*

% tic and toc will give us the elapsed time.
fprintf('Calling kmeans()...\n');
tic;
[cluster_labels, centers, sumd] = kmeans(X, ncolors, 'Replicates', 3, 'Options', opts);
toc;

%% Look at the results.
% At this point we have clustered our pixels into clusters 1, 2, ..., ncolors.  Now let's look at just
% the pixels in each cluster, setting the rest to black.  
%
% Large areas of roughly homogeneous color are clustered together.
%
% You should also be able to see the outlines of various subsets we can use as image segments.
%
% For an image with relatively few colors and high contrast (e.g., buffalo.jpg), the result can
% be quite striking.  Try buffalo.jpg with 2 clusters.

% Convert the cluster centroids, which are double precision numbers, to 8-bit integer RGB values.
qcolors = uint8(centers);

% Reshape the cluster labels into an m * n * k array.
pixel_labels = reshape(cluster_labels, m, n);

% Plot the image as grayscale, where each pixel value corresponds to its cluster number.
figure('Name', 'Grayscale image with pixels labeled by cluster number', 'NumberTitle', 'off');
imshow(pixel_labels, []);
title('Grayscale image with pixels labeled by cluster number', 'FontSize', 18);
disp('Hit any key to continue - ');
pause;

% For each cluster, mask the pixels that are not in the cluster and plot the result.
rgb_labels = repmat(pixel_labels, [1 1 k]);
for i = 1:ncolors
  R = P;
  R(rgb_labels ~= i) = 0;
  figure('Name', sprintf('Features in cluster %d', i), 'NumberTitle', 'off');
  imshow(R);
  title(sprintf('Features in cluster %d', i), 'FontSize', 18);
  shg;
 disp('Hit any key to continue - ');
 pause;
end

%% The image with quantized colors.
% Let's also take a look at the image that results if we replace each pixel by the color of the centroid 
% of the cluster the pixel belongs to.
Q = P;
labels = repmat(pixel_labels, [1 1 k]);
for i = 1:ncolors
  color = repmat(centers(i,:), [m*n 1]);
  Q(labels == i) = color(labels == i);
end
figure('Name', sprintf('Quantized image using %d colors (cluster centers)', ncolors), 'NumberTitle', 'off');
imshow(Q);
title(sprintf('Quantized image using %d colors (cluster centers)', ncolors), 'FontSize', 18);
shg;

%% Silhouette analysis of the clustering.
% For large inputs, we compute a silhouette plot on a random sample of the data---computing all the silhouette 
% values for $N$ points is an $N^{2}$ operation, since for each point we compute the distance from the point to 
% all the other points.

% Display the silhouette plot.
fprintf('Preparing the silhouette plot...\n');
m = size(X,1); % Number of rows in X.
sample_size = 12000;
if (m > sample_size) 
  I = randi(m, sample_size, 1);
  figure('Name', sprintf('Silhouette plot of %d point sample',  sample_size), 'NumberTitle', 'off');
  [S, H] = silhouette(X(I,:), cluster_labels(I));
  title({sprintf('Silhouette plot of %d point sample', sample_size),
         sprintf('average silhouette value: %f', mean(S))}, 'FontSize', 18);
else
  figure('Name', 'Silhouette plot', 'NumberTitle', 'off');
  [S, H] = silhouette(X, cluster_labels);  
  title(sprintf('Silhouette plot (average silhouette value: %f)', mean(S)), 'FontSize', 18);
end
xlabel('');
ylabel('Cluster', 'FontSize', 18);
shg;

