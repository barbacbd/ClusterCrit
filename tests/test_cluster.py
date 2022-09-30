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


def testInvalidIntCriteria():
    '''Test that invalid criteria will yield no results
    '''


def testValidSingleIntCriteria():
    '''Test a single criteria with valid data calling
    the IntCriteria function.
    '''


def testValidMultipleIntCriteria():
    '''Test mulitple criteria with valid data calling
    the IntCriteria function.
    '''


def testOneValidOneInvalidIntCriteria():
    '''Test a single valid criteria and another invalid criteria
    with valid data calling the IntCriteria function.
    '''


def testMultValidMultInvalidIntCriteria():
    '''Test multiple valid criteria and multiple invalid criteria
    with valid data calling the IntCriteria function.
    '''


def testInvalidExtCriteria():
    '''Test that invalid criteria will yield no results
    '''
    

def testValidSingleExtCriteria():
    '''Test a single criteria with valid data calling
    the ExtCriteria function.
    '''


def testValidMultipleExtCriteria():
    '''Test mulitple criteria with valid data calling
    the ExtCriteria function.
    '''


def testOneValidOneInvalidExtCriteria():
    '''Test a single valid criteria and another invalid criteria
    with valid data calling the ExtCriteria function.
    '''


def testMultValidMultInvalidExtCriteria():
    '''Test multiple valid criteria and multiple invalid criteria
    with valid data calling the ExtCriteria function.
    '''
    

def testBestCriterionSingle():
    '''Test a single value with the best criterion. This
    should return the same value passed, so index = 0
    '''


def testBestCriterionEmpty():
    '''Test an empty set of data passed to the bestCriterion.
    This should return None
    '''


def testBestCriterionMult():
    '''Test several values passed to the best criterion function
    and make sure that the best one is always returned.
    '''
    
    