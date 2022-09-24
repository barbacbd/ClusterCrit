# Cluster Crit

The project is a python extension for the [cluster crit](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/viewer.html?pdfurl=https%3A%2F%2Fcran.r-project.org%2Fweb%2Fpackages%2FclusterCrit%2FclusterCrit.pdf&clen=129366&chunk=true) R package. The project also contains the ability to select the optimal results when running Cluster Criteria algorithms on any number of clusters. 

## Metrics

The following metrics were all taken from the [cluster crit](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/viewer.html?pdfurl=https%3A%2F%2Fcran.r-project.org%2Fweb%2Fpackages%2FclusterCrit%2FclusterCrit.pdf&clen=129366&chunk=true) package in `R` found [here](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/viewer.html?pdfurl=https%3A%2F%2Fcran.r-project.org%2Fweb%2Fpackages%2FclusterCrit%2FclusterCrit.pdf&clen=129366&chunk=true). To view more information about these algorithms see the [cluster crit documentation](./clusterCrit.pdf). 

| Cluster Crit Metric | Criteria to determine optimal cluster |
| ------------------- | ------------------------------------- |
| Ball_Hall | max diff |
| Banfeld_Raftery | min |
| C_index | min |
| Calinski_Harabasz | max |
| Davies_Bouldin | min |
| Det_Ratio | min diff |
| Dunn | max |
| Gamma | max |
| G_plus | min |
| Ksq_DetW | max diff |
| Log_Det_Ratio | min diff |
| Log_SS_Ratio | min diff |
| McClain_Rao | min |
| PBM | max |
| Ratkowsky_Lance | max |
| Ray_Turi | min |
| Scott_Symons | min |
| S_Dbw | min |
| Silhouette | max |
| Tau | max |
| Trace_W | max diff |
| Trace_WiB | max diff |
| Wemmert_Gancarski | max |
| Xie_Beni | min |

## Selection Algorithms

The following functions assume that one or more cluster criteria mertrics were executed by providing several different input cluster sizes (k clusters). 

### Min

Find the minimum value of the outputs when run against several cluster numbers. For example, using the same data set run a clustering algorithm so that the number of clusters created are two through `N`.
The optimal result would be the minimum value when running the same metric over each set of clusters.

### Max

Find the maximum value of the outputs when run against several cluster numbers. For example, using the same data set run a clustering algorithm so that the number of clusters created are two through `N`.
The optimal result would be the maximum value when running the same metric over each set of clusters.

### Min Diff

Find the minimum difference value of the outputs when run against several cluster numbers. For example, using the same data set run a clustering algorithm so that the number of clusters created are two through `N`. The optimal result would be the minimum difference between two adjacent values when running the same metric over each set of clusters.

### Max Diff

Find the maximum difference value of the outputs when run against several cluster numbers. For example, using the same data set run a clustering algorithm so that the number of clusters created are two through `N`. The optimal result would be the maximum difference between two adjacent values when running the same metric over each set of clusters.


# What does this all mean?

The user will select one or more algorithms above using the configuration. Each algorithm will be run on all 2 through `k` clusters. The second column above is the function that will be applied to the output when all clusters are created. To demonstrate, examine the example below. Take the following configuration variables 

- Metric = `Ball_Hall`
- K = `2-50`
- Clustering = `kmeans`

|    | k=2 | k=3 | k=4 | k=5 | k=6 | ... |
| -- | --- | --- | --- | --- | --- | --- |
| Ball Hall | 0.2342 | 1.23423 | 0.8924 | 1.20312 | 2.231 | ... |

The user supplies a file containing all values, and `kmeans` is run on the dataset for each value of `k` (2 to 50). A pandas dataframe is generated where the row corresponds to the metric and each value in the row is the result of executing that metric on each value of `k`. In this example for `Ball_Hall` the `max diff` for values of the row are calculated and the result is the value of `k` that best fit that metric.  In the table above (looking at only the values provided), when `k` is 6 the max diff is observed.

