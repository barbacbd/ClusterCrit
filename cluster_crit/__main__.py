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
import argparse
from .cluster import clusterCrit
from .criteria import CriteriaInternal
from os.path import exists


def main():
    '''Main entry point for the ClusterCrit software bridge between
    python and R.
    '''
    clusterCritAlgorithms = ['clusterCrit']

    parser = argparse.ArgumentParser(prog='ClusterCrit')
    parser.add_argument('file', help='Input file containing the original data set, '
                        'cluster algorithms, and the cluster that each data point '
                        'is associated with when run against each cluster algorithm.'
    )
    parser.add_argument('-c', '--command', help='Command to execute',
                        choices=clusterCritAlgorithms, default='clusterCrit')
    parser.add_argument('-d', '--dir', default='.',
                        help='Directory where the executable will run. '
                        'This directory will contain any input files as well as '
                        'the artifact files output by this executable.'
    )
    parser.add_argument('-k', '--clusters', dest='k', type=int, default=2,
                        help='Number of clusters that were expected when the original '
                        'data set was run through a clustering algorithm.'
    )

    criteriaOptions = [x.name for x in CriteriaInternal]
    parser.add_argument('-a', '--criteria', nargs='+', choices=criteriaOptions, default=CriteriaInternal.ALL.name)
    parser.add_argument('--skip_gdi', action='store_false')
    parser.set_defaults(skip_gdi=True)

    args = parser.parse_args()

    if not exists(args.dir):
        # Error out when the directory does not exist
        exit(1)

    criteria = args.criteria
    if CriteriaInternal.ALL.name in criteria:
        criteria = criteriaOptions
        criteria.remove(CriteriaInternal.ALL.name)

    if args.skip_gdi:
        criteria = [c for c in criteria if "GDI" not in c]

    '''
    dataset: original dataset
    labels: matching cluster number for the dataset
    '''
    clusterCrit(dataset, labels, criteria, args.k)

if __name__ == '__main__':
    main()
