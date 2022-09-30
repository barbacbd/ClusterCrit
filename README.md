# Cluster Crit

The project is a python extension for the [cluster crit](https://cran.r-project.org/web/packages/clusterCrit/index.html) `R` package. The project also contains the ability to select the optimal results when running Cluster Criteria algorithms on any number of clusters. 

## Metrics

The following metrics were all taken from the [cluster crit](https://cran.r-project.org/web/packages/clusterCrit/index.html) package in `R`. To view more information about these algorithms see the [cluster crit documentation](https://github.com/barbacbd/ClusterCrit/blob/main/clusterCrit.pdf). 

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


## Executable

The package provides an executable to the installer, [ClusterCrit](https://github.com/barbacbd/ClusterCrit/blob/main/cluster_crit/__main__.py). The executable exposes the library as a managed application for easier use. The following options are provided:

- `file` - The file is a **required** argument. _Please see below in `Input Data Format` for the expected file format_.

- `dir` - The directory where output files will be located. _Default_ is set to `.`.

- `criteria` - A _list_ of criteria. _Please see [CriteriaInternal](https://github.com/barbacbd/ClusterCrit/blob/main/cluster_crit/criteria.py#L27) for more information_.

- `skip_gdi` - A Boolean. When present, this flag indicates that any criteria with `GDI` in the name will be skipped.


## Input Data Format

The user is required to input a file when using the exectuable. The user can also take advantage of the [file parsing](Add data here) function in the library to split a file manually when they wish to directly interact with the Cluster Crit library.

_The expected file type is a `json` file_. The file requires the following tags:

- `dataset` - A list of all data points. If the points are multi-dimensional use a list to represent each point (please do not include any labels, ex: "x", "y").

- `clusters` - A list (same length as the number of data points) that contains the cluster number from 1 to k that the data point belongs to. The order **must** be the same as the order of the data set.

- `k` - An integer representing the value of K used for clustering. Generally, this is the number of clusters that were generated.


_If any of the above tags are missing, the data will be considered corrupt and will not be used_.
