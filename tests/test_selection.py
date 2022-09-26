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
import pytest
# import values not covered in base cluster_crit
from cluster_crit.selection import df_min_diff, df_max_diff, df_min, df_max
# import values from cluster_crit
from cluster_crit import select, CriteriaInternal


def testDFMinDiffSingle():
    '''Test finding the min difference in a row with a single occurence of min
    distance between values.
    '''
    df = pd.DataFrame([[1, 2, 11, 6, 3]], columns=["2", "3", "4", "5", "6"])

    # differnce between 1 and 2
    expected_result = 1
    result = df_min_diff(df.iloc[0])

    assert result == expected_result


def testDFMinDiffMultiple():
    '''Test finding the min difference in a row with multiple occurences of min
    distance between values.
    '''
    df = pd.DataFrame([[1, 2, 11, 6, 5]], columns=["2", "3", "4", "5", "6"])

    expected_result = 1
    result = df_min_diff(df.iloc[0])

    assert result == expected_result


def testDFMinDiffEmpty():
    '''Test finding the min difference in a row with a no occurences of min
    distance between values.
    '''
    df = pd.DataFrame(columns=["2", "3", "4", "5", "6"])
    df.loc[df.shape[0]] = [None, None, None, None, None]

    result = df_min_diff(df.iloc[0])
    expected_result = None

    assert result == expected_result


def testDFMaxDiffSingle():
    '''Test finding the max difference in a row with a single occurence of max
    distance between values.
    '''
    df = pd.DataFrame([[1, 2, 11, 6, 3]], columns=["2", "3", "4", "5", "6"])

    # differnce between 2, 11
    expected_result = 2
    result = df_max_diff(df.iloc[0])

    assert result == expected_result


def testDFMaxDiffMultiple():
    '''Test finding the max difference in a row with multiple occurences of max
    distance between values.
    '''
    df = pd.DataFrame([[1, 2, 11, 2, 5]], columns=["2", "3", "4", "5", "6"])

    expected_result = 2
    result = df_max_diff(df.iloc[0])

    assert result == expected_result


def testDFMaxDiffEmpty():
    '''Test finding the max difference in a row with a no occurences of max
    distance between values.
    '''
    df = pd.DataFrame(columns=["2", "3", "4", "5", "6"])
    df.loc[df.shape[0]] = [None, None, None, None, None]

    result = df_max_diff(df.iloc[0])
    expected_result = None

    assert result == expected_result


def testDFMinSingle():
    '''Find the single smallest value in the dataframe
    '''
    df = pd.DataFrame([[1, 2, 11, 6, 3]], columns=["2", "3", "4", "5", "6"])

    expected_result = 0
    result = df_min(df.iloc[0])

    assert result == expected_result


def testDFMinMultiple():
    '''Find first instance of the smallest value in the dataframe
    '''
    df = pd.DataFrame([[1, 2, 11, 6, 1]], columns=["2", "3", "4", "5", "6"])

    expected_result = 0
    result = df_min(df.iloc[0])

    assert result == expected_result


def testDFMinEmpty():
    '''Find mine which is None when the row is empty
    '''
    df = pd.DataFrame(columns=["2", "3", "4", "5", "6"])
    df.loc[df.shape[0]] = [None, None, None, None, None]

    result = df_min(df.iloc[0])
    expected_result = None

    assert result == expected_result


def testDFMaxSingle():
    '''Find the single largest value in the row of the dataframe
    '''
    df = pd.DataFrame([[1, 2, 11, 2, 5]], columns=["2", "3", "4", "5", "6"])

    expected_result = 2
    result = df_max(df.iloc[0])

    assert result == expected_result


def testDFMaxMultiple():
    '''Find the first instance of the largest value in the row of the
    dataframe
    '''
    df = pd.DataFrame([[1, 2, 11, 11, 5]], columns=["2", "3", "4", "5", "6"])

    expected_result = 2
    result = df_max_diff(df.iloc[0])

    assert result == expected_result



def testDFMaxEmpty():
    '''Find the largest value which is None in an empty row of a
    dataframe
    '''
    df = pd.DataFrame(columns=["2", "3", "4", "5", "6"])
    df.loc[df.shape[0]] = [None, None, None, None, None]

    result = df_max(df.iloc[0])
    expected_result = None

    assert result == expected_result


def testSelectEmpty():
    '''Selection should contain nothing when the the row contains no matching
    data.
    '''
    df = pd.DataFrame(columns=["2", "3", "4", "5", "6"])
    df.loc[df.shape[0]] = [None, None, None, None, None]

    result = select(df)
    expected_result = {}

    assert result == expected_result



def testSelectSingleCriteria():
    '''Select a valid value from the row containing real data.
    '''
    df = pd.DataFrame(columns=["2", "3", "4", "5", "6"])

    row = pd.Series({"2": 1, "3": 2, "4": 11, "5": 11, "6": 5}, name=CriteriaInternal.Dunn.name)
    df = df.append(row)

    expected_result = {CriteriaInternal.Dunn.name: 2}
    result = select(df)

    assert result == expected_result


def testSelectMultipleCriteria():
    '''Select a set of valid values from several rows (criteria).
    '''
    df = pd.DataFrame(columns=["2", "3", "4", "5", "6"])

    row = pd.Series({"2": 1, "3": 2, "4": 11, "5": 11, "6": 5}, name=CriteriaInternal.Dunn.name)
    df = df.append(row)

    row = pd.Series({"2": 1, "3": 2, "4": 11, "5": 11, "6": 5}, name=CriteriaInternal.Xie_Beni.name)
    df = df.append(row)

    expected_result = {CriteriaInternal.Dunn.name: 2, CriteriaInternal.Xie_Beni.name: 0}
    result = select(df)

    assert result == expected_result
