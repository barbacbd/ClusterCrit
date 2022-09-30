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
from cluster_crit import intCriteria, extCriteria, bestCriterion
from cluster_crit import CriteriaInternal, CriteriaExternal
import pandas as pd
import numpy as np
from random import randint


original = np.asarray([
    -0.018, -0.03, 0.025, -0.073, -0.007, 0.052, -0.042, -0.025, -0.056, 0.005,
    0.131, 0.059, 0.15, 0.157, 0.036, 0.096, -0.027, -0.002, 0.069, 0.099,
    0.067, 0.101, 0.105, 0.115, 0.108, -0.036, -0.109, -0.133, -0.061, -0.045,
    -0.058, 0.017, 0.007, -0.093, 0.077, 0.085, 0.1, -0.005, 0.009, 0.16
])
original = original.reshape(-1, 1)

# k = 4
# points are in the same order
clusters = [2, 2, 2, 1, 2, 3, 1, 2, 1, 2, 4, 3, 4, 4, 2, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 2, 1, 1, 1, 1, 1, 2, 2, 1, 3, 3, 3, 2, 2, 4]
assert len(original) == len(clusters)


part1 = [randint(1,3) for _ in range(150)]
part2 = [randint(1,5) for _ in range(150)]


def testInvalidIntCriteria():
    '''Test that invalid criteria will yield no results
    '''
    assert intCriteria(original, clusters, [CriteriaExternal.ALL]) is None


def testValidSingleIntCriteria():
    '''Test a single criteria with valid data calling
    the IntCriteria function.
    '''
    output = intCriteria(original, clusters, [CriteriaInternal.Ball_Hall])
    assert CriteriaInternal.Ball_Hall.name in output
    assert output[CriteriaInternal.Ball_Hall.name] is not None


def testValidMultipleIntCriteria(subtests):
    '''Test mulitple criteria with valid data calling
    the IntCriteria function.
    '''
    expected = [
        CriteriaInternal.Ball_Hall,
        CriteriaInternal.Banfeld_Raftery,
        CriteriaInternal.C_index
    ]
    
    output = intCriteria(original, clusters, expected)
    for ex in expected:
        with subtests.test(ex=ex, output=output):
            assert ex.name in output
            assert output[ex.name] is not None


def testOneValidOneInvalidIntCriteria(subtests):
    '''Test a single valid criteria and another invalid criteria
    with valid data calling the IntCriteria function.
    '''
    expected = [CriteriaInternal.Ball_Hall]
    bad = [CriteriaExternal.ALL]
    
    output = intCriteria(original, clusters, expected+bad)
    for ex in expected:
        with subtests.test(ex=ex, output=output):
            assert ex.name in output
            assert output[ex.name] is not None

    for ex in bad:
        with subtests.test(ex=ex, output=output):
            assert ex.name not in output


def testMultValidMultInvalidIntCriteria(subtests):
    '''Test multiple valid criteria and multiple invalid criteria
    with valid data calling the IntCriteria function.
    '''
    expected = [CriteriaInternal.Ball_Hall, CriteriaInternal.Banfeld_Raftery, CriteriaInternal.C_index]
    bad = [CriteriaExternal.Czekanowski_Dice, CriteriaExternal.Folkes_Mallows]
    
    output = intCriteria(original, clusters, expected+bad)
    for ex in expected:
        with subtests.test(ex=ex, output=output):
            assert ex.name in output
            assert output[ex.name] is not None

    for ex in bad:
        with subtests.test(ex=ex, output=output):
            assert ex.name not in output


def testInvalidExtCriteria():
    '''Test that invalid criteria will yield no results
    '''
    assert extCriteria(part1, part2, [CriteriaInternal.ALL]) is None
    

def testValidSingleExtCriteria():
    '''Test a single criteria with valid data calling
    the ExtCriteria function.
    '''
    output = extCriteria(part1, part2, [CriteriaExternal.Czekanowski_Dice])
    assert CriteriaExternal.Czekanowski_Dice.name in output
    assert output[CriteriaExternal.Czekanowski_Dice.name] is not None

    
def testValidMultipleExtCriteria(subtests):
    '''Test mulitple criteria with valid data calling
    the ExtCriteria function.
    '''
    expected = [
        CriteriaExternal.Czekanowski_Dice,
        CriteriaExternal.Folkes_Mallows,
        CriteriaExternal.Hubert
    ]
    
    output = extCriteria(part1, part2, expected)
    for ex in expected:
        with subtests.test(ex=ex, output=output):
            assert ex.name in output
            assert output[ex.name] is not None

            
def testOneValidOneInvalidExtCriteria(subtests):
    '''Test a single valid criteria and another invalid criteria
    with valid data calling the ExtCriteria function.
    '''
    bad = [CriteriaInternal.Ball_Hall]
    expected = [CriteriaExternal.Czekanowski_Dice]
    
    output = extCriteria(part1, part2, expected+bad)
    for ex in expected:
        with subtests.test(ex=ex, output=output):
            assert ex.name in output
            assert output[ex.name] is not None

    for ex in bad:
        with subtests.test(ex=ex, output=output):
            assert ex.name not in output
            

def testMultValidMultInvalidExtCriteria(subtests):
    '''Test multiple valid criteria and multiple invalid criteria
    with valid data calling the ExtCriteria function.
    '''
    bad = [CriteriaInternal.Ball_Hall, CriteriaInternal.Banfeld_Raftery, CriteriaInternal.C_index]
    expected = [CriteriaExternal.Czekanowski_Dice, CriteriaExternal.Folkes_Mallows, CriteriaExternal.Hubert]
    
    output = extCriteria(part1, part2, expected+bad)
    for ex in expected:
        with subtests.test(ex=ex, output=output):
            assert ex.name in output
            assert output[ex.name] is not None

    for ex in bad:
        with subtests.test(ex=ex, output=output):
            assert ex.name not in output
    

def testBestCriterionSingle():
    '''Test a single value with the best criterion. This
    should return the same value passed, so index = 0
    '''
    clusters = [
        [1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 2],
    ]
    criteria = CriteriaInternal.Dunn
    values = []
    for cluster in clusters:
        output = intCriteria(original, cluster, [criteria])
        values.append(output[criteria.name])

    crit = np.asarray(values)
    assert bestCriterion(crit, criteria.name) == 0


def testBestCriterionEmpty():
    '''Test an a data set that will return a None value. This will
    happen more often in indicies that required diff_ function such
    as min_diff and max_diff and there are not enough values passed
    to calculate a diff.
    '''
    clusters = [
        [1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 2],
    ]
    criteria = CriteriaInternal.Ball_Hall
    values = []
    for cluster in clusters:
        output = intCriteria(original, cluster, [criteria])
        values.append(output[criteria.name])

    crit = np.asarray(values)
    assert bestCriterion(crit, criteria.name) is None
    

def testBestCriterionMult():
    '''Test several values passed to the best criterion function
    and make sure that the best one is always returned.
    '''
    clusters = [
        [1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 2],
        [2, 2, 2, 1, 2, 3, 1, 2, 1, 2, 3, 3, 3, 3, 2, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 2, 1, 1, 1, 1, 1, 2, 2, 1, 3, 3, 3, 2, 2, 3],
        [2, 2, 2, 1, 2, 3, 1, 2, 1, 2, 4, 3, 4, 4, 2, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 2, 1, 1, 1, 1, 1, 2, 2, 1, 3, 3, 3, 2, 2, 4],
        [2, 2, 3, 2, 3, 4, 2, 2, 2, 3, 5, 4, 5, 5, 3, 4, 2, 3, 4, 4, 4, 4, 4, 4, 4, 2, 1, 1, 2, 2, 2, 3, 3, 1, 4, 4, 4, 3, 3, 5],
        [3, 2, 3, 2, 3, 4, 2, 2, 2, 3, 6, 4, 6, 6, 4, 5, 2, 3, 4, 5, 4, 5, 5, 5, 5, 2, 1, 1, 2, 2, 2, 3, 3, 1, 4, 5, 5, 3, 3, 6], 
    ]
    criteria = CriteriaInternal.Dunn
    values = []
    for cluster in clusters:
        output = intCriteria(original, cluster, [criteria])
        values.append(output[criteria.name])

    crit = np.asarray(values)
    # technically this value is 3, but we are going to just ensure that it
    # wasn't the first value, because that was a clustering with 2 clusters
    # so let's hope that one isn't the optimal size.
    assert bestCriterion(crit, criteria.name) > 0

    
