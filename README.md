<h1 align="center">
  <br>Cluster Criteria</br>
</h1>

<h2 align="center">

[![Build](https://github.com/barbacbd/ClusterCrit/actions/workflows/python-package.yml/badge.svg)](https://github.com/barbacbd/ClusterCrit/actions/workflows/python-package.yml)
[![PyPI version fury.io](https://badge.fury.io/py/cluster-crit.svg)](https://pypi.python.org/pypi/cluster-crit/)


## Description

The project is a python extension for the [cluster crit](https://cran.r-project.org/web/packages/clusterCrit/index.html) `R` package. The project also contains the ability to select the optimal results when running Cluster Criteria algorithms on any number of clusters.

## External Dependencies

The R programming language is a dependency of this project, and it **must** be installed prior to installing this project. Please visit the [R Downloads Page](https://www.r-project.org/).


## Internal Criteria

The function intCriteria calculates internal clustering indices. The list of all internal criteria can be found in [criteria.py](https://github.com/barbacbd/ClusterCrit/blob/main/cluster_crit/criteria.py).

## External Criteria

The function extCriteria calculates external clustering indices in order to compare two partitions. The list of all external criteria can be found in [criteria.py](https://github.com/barbacbd/ClusterCrit/blob/main/cluster_crit/criteria.py).

## Best Criterion

Given a vector of several clustering quality index values computed with a given criterion, the function bestCriterion returns the index of the "best" one in the sense of the specified criterion.
Typically, a set of data has been clusterized several times (using different algorithms or specifying a different number of clusters) and a clustering index has been calculated each
time. The bestCriterion function determines which value is considered the best according to the given clustering index. For instance, if one uses the Calinski_Harabasz index, the best
value is the largest one. A list of all the supported criteria can be obtained with the getCriteriaNames function. The criterion name (crit argument) is case insensitive and can be abbreviated.

## Get Criteria Names

Get a list of Criteria Names.

- The user can return Internal vs External Criteria Names by setting the `internal` variable to `True` vs `False` respectively.
- When retrieving Internal Criteria, the user can set `includeGCI` to `False` to skip returning any criteria with GDI-XXX as the name.
- The user can also control the return type by setting `returnEnumerations` to `True` (return Enumerations) or `False` to return the string representations of the criteria.

## Examples

The following sections are a set of brief/simple examples of this library. To setup/initialize these tests, you can use the following steps:

1. Install All External Dependencies (see external dependencies above).
2. Install `kmeans1d`: `python -m pip install kmeans1d`
3. Create the original set of data (this is a sample taken from a large data set).

```python
original = [
    -0.018, -0.03, 0.025, -0.073, -0.007, 0.052, -0.042, -0.025, -0.056, 0.005,
    0.131, 0.059, 0.15, 0.157, 0.036, 0.096, -0.027, -0.002, 0.069, 0.099,
    0.067, 0.101, 0.105, 0.115, 0.108, -0.036, -0.109, -0.133, -0.061, -0.045,
    -0.058, 0.017, 0.007, -0.093, 0.077, 0.085, 0.1, -0.005, 0.009, 0.16
]
```

**Note**: _It is advised that you convert this data when it is a 1-D data set like above_.

```python
import numpy as np

original = np.asarray([
    -0.018, -0.03, 0.025, -0.073, -0.007, 0.052, -0.042, -0.025, -0.056, 0.005,
    0.131, 0.059, 0.15, 0.157, 0.036, 0.096, -0.027, -0.002, 0.069, 0.099,
    0.067, 0.101, 0.105, 0.115, 0.108, -0.036, -0.109, -0.133, -0.061, -0.045,
    -0.058, 0.017, 0.007, -0.093, 0.077, 0.085, 0.1, -0.005, 0.009, 0.16
])
original = original.reshape(-1, 1)
```

4. Create a wrapper for `kmeans` so that we can generate the clusters for the above data set.

```python
def k_means_wrapper(data_set, k):
    matching_clusters, centroids = kmeans1dc(data_set, k)
    # R uses values 1-N not 0-N-1, so let's update here
    matching_clusters = [x+1 for x in matching_clusters]
    return matching_clusters
```

5. Cluster the data using values of K = 2,3,4,5,6 ...

```python
clusters = [
    k_means_wrapper(original, 2),
    k_means_wrapper(original, 3),
    k_means_wrapper(original, 4),
    k_means_wrapper(original, 5),
    k_means_wrapper(original, 6)
]
```

You should now have values similar to the following:

```python
clusters = [
    [1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 2],
    [2, 2, 2, 1, 2, 3, 1, 2, 1, 2, 3, 3, 3, 3, 2, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 2, 1, 1, 1, 1, 1, 2, 2, 1, 3, 3, 3, 2, 2, 3],
    [2, 2, 2, 1, 2, 3, 1, 2, 1, 2, 4, 3, 4, 4, 2, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 2, 1, 1, 1, 1, 1, 2, 2, 1, 3, 3, 3, 2, 2, 4],
    [2, 2, 3, 2, 3, 4, 2, 2, 2, 3, 5, 4, 5, 5, 3, 4, 2, 3, 4, 4, 4, 4, 4, 4, 4, 2, 1, 1, 2, 2, 2, 3, 3, 1, 4, 4, 4, 3, 3, 5],
    [3, 2, 3, 2, 3, 4, 2, 2, 2, 3, 6, 4, 6, 6, 4, 5, 2, 3, 4, 5, 4, 5, 5, 5, 5, 2, 1, 1, 2, 2, 2, 3, 3, 1, 4, 5, 5, 3, 3, 6],
]
```

These clusters can be used as parameters to IntCriteria. Follow similar steps to produce data for ExtCriteria.


### Internal Criteria

The following will receive the results of the clusters with the `Dunn` Criteria on cluster numbers two through six.

```python
criteria = CriteriaInternal.Dunn

values = []
for cluster in clusters:
    output = intCriteria(original, cluster, [criteria])
    values.append(output[criteria.name])
```

### External Criteria

```python
from random import randint

# generate two artificial partitions
part1 = [randint(1,3) for _ in range(150)]
part2 = [randint(1,5) for _ in range(150)]

output = extCriteria(part1, part2, [CriteriaExternal.Czekanowski_Dice])
```

### Best Criterion

Continuing with the IntCriteria example above, the following will print the index of the best cluster size given the
outputs of the Internal Crtieria evaluation.

```python
crit = np.asarray(values)
print(bestCriterion(crit, criteria.name))
```

### Get Criteria Names

The example will get all InternalCriteria, excluding `GDI-XXX` criteria, and the values will be returned as enumerations.

```python
criteria = getCriteriaNames(True, False, True)
```

The provided parameters are defaults, and they do **not** need to be specified. 
