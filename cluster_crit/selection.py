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
from numpy import inf, nan
from math import fabs
from .criteria import CriteriaInternal as CI


def df_min_diff(row):
    '''The function is applied to columns start + 1 - n

    For instance columns 2 to 50 would apply the data to

    3 - 50 as the function is the minimum difference
    between columns n and n-1 for the row.

    :param df: Pandas Dataframe row
    :return: Column number where the value contains the min difference
    '''
    local_min_idx = None
    local_min_value = None

    for i in range(1, len(row.values.tolist()), 1):
        if row[i] in (-inf, inf, nan) or row[i-1] in (-inf, inf, nan):
            continue

        if local_min_value is None or fabs(row[i] - row[i-1]) < local_min_value:
            local_min_value = fabs(row[i] - row[i-1])
            local_min_idx = i

    return local_min_idx  # column containing min diff


def df_max_diff(row):
    '''The function is applied to columns start + 1 - n

    For instance columns 2 to 50 would apply the data to

    3 - 50 as the function is the maximum difference
    between columns n and n-1 for the row.

    :param df: Pandas Dataframe row
    :return: Column number where the value contains the max difference
    '''
    local_max_idx = None
    local_max_value = None

    for i in range(1, len(row.values.tolist()), 1):
        if row[i] in (-inf, inf, nan) or row[i-1] in (-inf, inf, nan):
            continue

        if local_max_value is None or fabs(row[i] - row[i-1]) > local_max_value:
            local_max_value = fabs(row[i] - row[i-1])
            local_max_idx = i

    return local_max_idx  # column containing max diff


def df_min(row):
    '''Find the min in the Dataframe row

    :param row: Pandas dataframe row
    :return: column name of the min value in the row
    '''
    return row.idxmin()


def df_max(row):
    '''Find the max in the dataframe row

    :poaram row: Pandas dataframe row
    :return: Column name of the max value in the row
    '''
    return row.idxmax()

# The dictionary of Algorithms with the name/kind of function
# that should be applied to the entire set of outcomes for
# clusters k (Ex: k = 2 ... 50)
MetricChoices = {
    CI.Ball_Hall.name: df_max_diff,
    CI.Banfeld_Raftery.name: df_min,
    CI.C_index.name: df_min,
    CI.Calinski_Harabasz.name: df_max,
    CI.Davies_Bouldin.name: df_min,
    CI.Det_Ratio.name: df_min_diff,
    CI.Dunn.name: df_max,
    CI.GDI11.name: df_max,
    CI.GDI12.name: df_max,
    CI.GDI13.name: df_max,
    CI.GDI21.name: df_max,
    CI.GDI22.name: df_max,
    CI.GDI23.name: df_max,
    CI.GDI31.name: df_max,
    CI.GDI32.name: df_max,
    CI.GDI33.name: df_max,
    CI.GDI41.name: df_max,
    CI.GDI42.name: df_max,
    CI.GDI43.name: df_max,
    CI.GDI51.name: df_max,
    CI.GDI52.name: df_max,
    CI.GDI53.name: df_max,
    CI.Gamma.name: df_max,
    CI.G_plus.name: df_min,
    CI.Ksq_DetW.name: df_max_diff,
    CI.Log_Det_Ratio.name: df_min_diff,
    CI.Log_SS_Ratio.name: df_min_diff,
    CI.McClain_Rao.name: df_min,
    CI.PBM.name: df_max,
    CI.Point_Biserial.name: df_max,
    CI.Ratkowsky_Lance.name: df_max,
    CI.Ray_Turi.name: df_min,
    CI.Scott_Symons.name: df_min,
    CI.SD_Scat.name: df_min,
    CI.SD_Dis.name: df_min,
    CI.S_Dbw.name: df_min,
    CI.Silhouette.name: df_max,
    CI.Tau.name: df_max,
    CI.Trace_W.name: df_max_diff,
    CI.Trace_WiB.name: df_max_diff,
    CI.Wemmert_Gancarski.name: df_max,
    CI.Xie_Beni.name: df_min
}


def select(df):
    '''For each algorithm in `MetricChoices` run the function
    that should be applied for the algorithm on the row in the dataframe.
    The column that is the result of the function is saved and the
    dictionary of the algorithm with the column name (cluster) is returned.

    :param df: Pandas dataframe containing the metrics as the index from the
    `MetricChoices`.

    :return: dictionary of algorithms (key) to their resulting column (cluster).
    It is possible for `None` to be in the resultant value field.
    '''

    # don't modify the supplied dataframe
    df_copy = df.copy(deep=True)

    # modify the copy by removing all infinite values and replacing with NaN
    # this will allow us to not include them in the comparisons in the selection functions
    df_copy.replace([-inf, inf], nan, inplace=True)

    # result
    selections = {}

    # create a reference list of all column names to be looked
    # up later (this isn't required, but it makes it easier for later)
    ref_cols = df_copy.columns.values.tolist()

    for idx, row in df_copy.iterrows():
        # Get the function associated with the row (algorithm)
        # if this is a function and not some mistake, run the function
        # and store the result.
        func = MetricChoices.get(idx, None)

        if callable(func):
            ret = func(row)

            # get the column name as the max diff and min diff functions return
            # integers instead of column names. Turn it into a column name
            if isinstance(ret, int):
                ret = ref_cols[ret]

            selections[idx] = ret

    return selections
