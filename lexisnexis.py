#!/usr/bin/env python

from json import dumps
import os

from fom.session import Fluid

fdb = Fluid()
fdb.login('lexisnexis.com', os.environ['FLUDINFO_LEXISNEXIS_PASSWORD'])

datasets = [
    {
        'about': [
            'Audit',
            'Inspection rights',
            'Confidentiality',
            'Audit Commission Act 1998, s 15(1)',
            'European Convention for the Protection of Human Rights and Fundamental Freedoms 1950',
            'European Convention for the Protection of Human Rights and Fundamental Freedoms 1950, First Protocol, art 1.',
            'RIX LJ',
            'ETHERTON LJ',
            'JACKSON LJ',
            'Philip Coppel QC',
            'Clive Lewis QC',
            'Timothy Pitt-Payne QC',
            'Peter Oldham QC',
        ],
        'data': dumps(
            [
                {
                    'url': 'https://www.lexisnexis.com/uk/legal/results/enhdocview.do?docLinkInd=true&ersKey=23_T15049499852&format=GNBFULL&startDocNo=1&resultsUrlKey=0_T15049512934&backKey=20_T15049512935&csi=274640&docNo=5&scrollToPosition=693',
                    'title': 'R (on the application of Veolia ES Nottinghamshire Ltd) v Nottinghamshire County Council (Dowen and another, interested parties)',
                    'publicationDate': '23 April 1998'
                },
            ]
        ),
    },
    # {
    #     'about': [
    #     ],
    #     'data': dumps(
    #         [
    #             {
    #                 'url': '',
    #                 'title': '',
    #                 'publicationDate': ''
    #             },
    #         ]
    #     ),
    # },
]

for dataset in datasets:
    for about in dataset['about']:
        fdb.about[about.lower()]['lexisnexis.com/posts'].put(dataset['data'])
