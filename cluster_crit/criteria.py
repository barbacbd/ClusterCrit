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
from enum import Enum


class CriteriaInternal(Enum):
    '''All possible values that the Cran (R) package Cluster Crit can receive
    for the intCriteria. The `ALL` type is handled slightly differently as
    it should be the extension of only the valid values in this enumeration
    rather than `ALL` in cluster crit.
    '''
    ALL = 0
    Ball_Hall = 1
    Banfeld_Raftery = 2
    C_index = 3
    Calinski_Harabasz = 4
    Davies_Bouldin = 5
    Det_Ratio = 6
    Dunn = 7
    Gamma = 8
    G_plus = 9
    GDI11 = 10
    GDI12 = 11
    GDI13 = 12
    GDI21 = 13
    GDI22 = 14
    GDI23 = 15
    GDI31 = 16
    GDI32 = 17
    GDI33 = 18
    GDI41 = 19
    GDI42 = 20
    GDI43 = 21
    GDI51 = 22
    GDI52 = 23
    GDI53 = 24
    Ksq_DetW = 25
    Log_Det_Ratio = 26
    Log_SS_Ratio = 27
    McClain_Rao = 28
    PBM = 29
    Point_Biserial = 30
    Ray_Turi = 31
    Ratkowsky_Lance = 32
    Scott_Symons = 33
    SD_Scat = 34
    SD_Dis = 35
    S_Dbw = 36
    Silhouette = 37
    Tau = 38
    Trace_W = 39
    Trace_WiB = 40
    Wemmert_Gancarski = 41
    Xie_Beni = 42


def getCriteriaNames(includeGDI=False, returnEnumerations=True):
    '''Get a list of the available internal clustering indices.

    :param includeGDI: When true the GDI indices are included
    :param returnEnumeration: When true, return the list of
    enumerations, otherwise strings are returned.

    :return: available clustering criteria names
    '''
    critNames = []

    for ci in CriteriaInternal:
        if ci != CriteriaInternal.ALL:
            if includeGDI or (not includeGDI and not ci.name.beginswith("GDI")):
                critNames.append(ci)

    if not returnEnumeration:
        critNames = [x.name for x in critNames]

    return critNames
