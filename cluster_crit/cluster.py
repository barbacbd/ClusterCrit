"""
MIT License

Copyright (c) 2022 Brent Barbachem

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import pandas as pd
from rpy2 import robjects
from rpy2.robjects.packages import importr, isinstalled
from rpy2.robjects import numpy2ri
from rpy2.robjects.vectors import StrVector
from .criteria import CriteriaInternal


PackageNameR = 'clusterCrit'

# Initialize the R environment, including the Cluster Crit requirements
utils = importr('utils')
utils.chooseCRANmirror(ind=1)

# install the packages inside of the R environment, if the packages are not
# already installed
if not isinstalled(PackageNameR):
    utils.install_packages(StrVector((PackageNameR,)))

# define the R function that this script will use
robjects.r(
    '''
    crit <- function(dataset, labels, criteria) {
        ccData <- clusterCrit::intCriteria(dataset, unlist(labels), unlist(criteria))
        return(ccData)
    }
    '''
)


def clusterCrit(dataSet, labels, criteria, k):
    '''Expose the clusterCrit::intCriteria funcion (initially created in R)
    to all users. intCriteria calculates various internal clustering
    validation or quality criteria. The list of all the supported criteria
    can be obtained with the `getCriteriaNames`.

    The following is the original set of parameters for intCriteria:

    traj [matrix] : the matrix of observations (trajectories).
    part [vector] : the partition vector.
    crit [vector] : a vector containing the names of the indices to compute

    :param dataSet: The matrix of observations
    :param labels: The partition vector
    :param criteria: a vector containing the names of the indices to compute, see `getCriteriaNames`
    :param k: The number of clusters

    :return: Pandas Dataframe where the column is the number k (provided) and the rows
    are the algorithms run within the cluster crit package
    '''
    _criteria = []
    for c in criteria:
        if  isinstance(c, CritSelection):
            _criteria.append(c)

    if not _criteria:
        return None

    indices = [x.name for x in _criteria]
    numpy2ri.activate()
    if 'crit' not in robjects.globalenv:
        return None

    applied_data = robjects.globalenv['crit'](dataSet, labels, indices)
    numpy2ri.deactivate()
    return pd.DataFrame(applied_data, index=indices, columns=[str(k)])
