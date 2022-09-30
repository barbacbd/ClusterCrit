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
import pytest
from cluster_crit.criteria import getCriteriaNames, CriteriaInternal, CriteriaExternal


def testGetCriteriaNamesBaseInt(subtests):
    '''getCriteriaNames:
          internal=True
          includeGDI=False
          returnEnumeration=True

    This should skip all GDI values and the return value
    will be a list of enumerations (CriteriaInternal).
    '''
    expected = [
        x for x in CriteriaInternal
        if not x.name.startswith("GDI") and x != CriteriaInternal.ALL
    ]

    output = getCriteriaNames()

    assert len(expected) == len(output)

    for o in output:
        with subtests.test(o=o, expected=expected):
            assert o in expected


def testGetCriteriaNamesIncludeGDIInt(subtests):
    '''getCriteriaNames:
          internal=True
          includeGDI=True
          returnEnumeration=True

    This should contain ALL GDI values and the return value
    will be a list of enumerations (CriteriaInternal).
    '''
    expected = [x for x in CriteriaInternal if x != CriteriaInternal.ALL]

    output = getCriteriaNames(True, True, True)

    assert len(expected) == len(output)

    for o in output:
        with subtests.test(o=o, expected=expected):
            assert o in expected


def testGetCriteriaNamesStringsNoGDIInt(subtests):
    '''getCriteriaNames:
          internal=True
          includeGDI=False
          returnEnumeration=False

    This should skip all GDI values and the return value
    will be a list of strings.
    '''
    expected = [
        x.name for x in CriteriaInternal
        if not x.name.startswith("GDI") and x != CriteriaInternal.ALL
    ]

    output = getCriteriaNames(True, False, False)

    assert len(expected) == len(output)

    for o in output:
        with subtests.test(o=o, expected=expected):
            assert o in expected


def testGetCriteriaNamesStringsWithGDIInt(subtests):
    '''getCriteriaNames:
          internal=True
          includeGDI=True
          returnEnumeration=False

    This should contain ALL GDI values and the return value
    will be a list of strings.
    '''
    expected = [x.name for x in CriteriaInternal if x != CriteriaInternal.ALL]

    output = getCriteriaNames(True, True, False)

    assert len(expected) == len(output)

    for o in output:
        with subtests.test(o=o, expected=expected):
            assert o in expected


def testGetCriteriaNamesBaseExt(subtests):
    '''getCriteriaNames:
          internal=False
          includeGDI=False
          returnEnumeration=True

    This should skip all GDI values and the return value
    will be a list of enumerations (CriteriaExternal).
    '''
    expected = [x for x in CriteriaExternal if x != CriteriaExternal.ALL]

    output = getCriteriaNames(False, False, True)

    assert len(expected) == len(output)

    for o in output:
        with subtests.test(o=o, expected=expected):
            assert o in expected


def testGetCriteriaNamesStringsExt(subtests):
    '''getCriteriaNames:
          internal=False
          includeGDI=False
          returnEnumeration=False

    This should skip all GDI values and the return value
    will be a list of strings.
    '''
    expected = [x.name for x in CriteriaExternal if x != CriteriaExternal.ALL]

    output = getCriteriaNames(False, False, False)

    assert len(expected) == len(output)

    for o in output:
        with subtests.test(o=o, expected=expected):
            assert o in expected
