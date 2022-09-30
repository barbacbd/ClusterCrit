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
from .criteria import CriteriaInternal, CriteriaExternal


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
    rIntCriteria <- function(dataset, labels, criteria) {
        ccData <- clusterCrit::intCriteria(dataset, unlist(labels), unlist(criteria))
        return(ccData)
    }
    
    rExtCriteria <- function(part1, part2, criteria) {
        ccData <- clusterCrit::extCriteria(unlist(part1), unlist(part2), unlist(criteria))
        return(ccData)
    }
    
    rBestCriterion <- function(x, crit) {
        ccData <- clusterCrit::bestCriterion(x, crit)
    }
    '''
)


def intCriteria(traj, part, crit):
    '''Expose the clusterCrit::intCriteria funcion (initially created in R)
    to all users. intCriteria calculates various internal clustering
    validation or quality criteria. The list of all the supported criteria
    can be obtained with the `getCriteriaNames`.

    :param traj [matrix] : the matrix of observations (trajectories).
    :param part [vector] : the partition vector.
    :param crit [vector] : a list containing CriteriaInternal indices to compute

    :return: Map of the criteria to the value
    '''
    _criteria = []
    for c in crit:
        if  isinstance(c, CriteriaInternal):
            _criteria.append(c)

    if not _criteria:
        return None

    indices = [x.name for x in _criteria]
    numpy2ri.activate()
    if 'rIntCriteria' not in robjects.globalenv:
        return None

    applied_data = robjects.globalenv['rIntCriteria'](traj, part, indices)
    numpy2ri.deactivate()
    return dict(zip(indices, applied_data))


def extCriteria(part1, part2, crit):
    '''Expose the clusterCrit::extCriteria funcion (initially created in R)
    to all users. intCriteria calculates external clustering indices in order
    to compare two partitions. The list of all the supported criteria
    can be obtained with the `getCriteriaNames`.

    :param part1 [vector] : the first partition vector.
    :param part2 [vector] : the second partition vector.
    :param crit [vector]  : a list containing CriteriaExternal indices to compute

    :return: Map of the criteria to the value
    '''
    _criteria = []
    for c in crit:
        if  isinstance(c, CriteriaExternal):
            _criteria.append(c)

    if not _criteria:
        return None

    indices = [x.name for x in _criteria]
    numpy2ri.activate()
    if 'rExtCriteria' not in robjects.globalenv:
        return None

    applied_data = robjects.globalenv['rExtCriteria'](part1, part2, indices)
    numpy2ri.deactivate()
    return dict(zip(indices, applied_data))


def bestCriterion(x, crit):
    '''Expose the clusterCrit::bestCriterionn function (initially created in R)
    to all users. `bestCriterion` returns the best index value according to a 
    specified criterion. Given a vector of several clustering quality index values
    computed with a given criterion, the function `bestCriterion` returns the index
    of the "best" one in the sense of the specified criterio
    
    :param x [matrix]    : a numeric vector of quality index values.
    :param crit [string] : a string specifying the name of the criterion which 
    was used to compute the quality indices
    
    :return: The index in vector x of the best value according to the criterion
    specified by the crit argument.
    '''
    
    numpy2ri.activate()
    if 'rBestCriterion' not in robjects.globalenv:
        return None

    index = robjects.globalenv['rBestCriterion'](x, crit)
    numpy2ri.deactivate()
    return index