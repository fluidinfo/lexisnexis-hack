#!/usr/bin/env python

from json import dumps
import os
import sys

from fom.session import Fluid

fdb = Fluid()
fdb.login('lexisnexis.com', os.environ['FLUDINFO_LEXISNEXIS_PASSWORD'])

TAG = 'lexisnexis.com/posts'

datasets = [
    {
        'about': [
            'Audit',
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
        'data': [
            {
                'url': 'https://www.lexisnexis.com/uk/legal/docview/getDocForCuiReq?lni=5295-21X1-DYBR-30J2&csi=274640&oc=00240&perma=true&elb=t',
                'title': 'R (on the application of Veolia ES Nottinghamshire Ltd) v Nottinghamshire County Council (Dowen and another, interested parties)',
                'publicationDate': '29 October 2010'
            },
        ],
    },
    {
        'about': [
            'https://www.lexisnexis.com/uk/legal/docview/getDocForCuiReq?lni=5295-21X1-DYBR-30J2&csi=274640&oc=00240&perma=true&elb=t',
        ],
        'data': [
            {
                'url': 'http://www.monckton.com/docs/library/VEOLIA.pdf',
                'title': 'Veolia ES Nottinghamshire Ltd v Nottinghamshire County Council [2010] EWCA Civ 1214 (PDF)',
                'publicationDate': 'February 2011'
            },
            {
                'url': 'http://www.legalweeklaw.com/abstract/veolia-es-nottinghamshire-cc-sanctity-confidentiality-preserved-5839',
                'title': 'Veolia ES v Nottinghamshire CC: the sanctity of confidentiality preserved?',
                'publicationDate': '7 December 2010'
            },
            {
                'url': 'http://www.nabarro.com/Downloads/Projects-Veolia-ES-v-Nottinghamshire-CC.pdf',
                'title': 'Veolia ES v Nottinghamshire CC - the sanctity of confidentiality preserved?',
                'publicationDate': '6 December 2010'
            },
            {
                'url': 'http://www.guardian.co.uk/society/joepublic/2010/nov/08/transparency-local-government-finance',
                'title': 'Transparency in local government finance a step closer',
                'publicationDate': '8 November 2010'
            },
            {
                'url': 'http://www.orchardnews.com/veolegncc.htm',
                'title': 'The Veolia legal challenge to Notts County Council (2009/2010)',
                'publicationDate': '29 October 2010'
            },
            {
                'url': 'http://www.bailii.org/ew/cases/EWCA/Civ/2010/1214.html',
                'title': 'Veolia ES Nottinghamshire Ltd v Nottinghamshire County Council & Ors [2010] EWCA Civ 1214',
                'publicationDate': '29 October 2010'
            },
            {
                'url': 'http://www.mrw.co.uk/news/veolia-appeals-against-nottinghamshire-county-council-information-ruling/8603088.article',
                'title': 'Veolia appeals against Nottinghamshire County Council information ruling',
                'publicationDate': '13 July 2010'
            },
            {
                'url': 'http://www.burges-salmon.com/Practices/commercial/Publications/Veolia_and_confidentiality_clauses_in_local_authority_contracst_an_update.pdf',
                'title': 'Veolia client update: Protecting commercially sensitive information in local authority contracts: a lifeline from the Court of Appeal (PDF)',
                'publicationDate': '2010'
            },
            {
                'url': 'http://safewasteshrewsbury.blogspot.co.uk/2009/10/revealed-what-veolia-wanted-to-be-kept.html',
                'title': 'Revealed: What Veolia wanted to be kept secret',
                'publicationDate': '6 October 2009'
            },
            {
                'url': 'http://www.monckton.com/newsitem/323/r-(veolia-es-ltd)-v-nottinghamshire-county-council-(audit-commission-and-shlomo-dowen-(represented-by-friends-of-the-earth))-as-interested-parties',
                'title': 'R (Veolia ES Ltd) v Nottinghamshire County Council (Audit Commission and Shlomo Dowen (represented by Friends of the Earth)) as Interested Parties',
                'publicationDate': '6 October 2009'
            },
            {
                'url': 'http://www.letsrecycle.com/news/latest-news/councils/veolia-loses-notts-contract-disclosure-dispute',
                'title': 'Veolia loses Notts contract disclosure dispute',
                'publicationDate': '1 October 2009'
            },
        ],
    },
    {
        'about': [
            'rix lj',
        ],
        'data': [
            {
                'url': 'https://www.lexisnexis.com/uk/legal/docview/getDocForCuiReq?lni=55RS-3W51-DYBR-34B3&csi=274640&oc=00240&perma=true&elb=t',
                'title': 'R (on the application of De Whalley) v Norfolk County Council (Cory Environmental Management Ltd, interested party)',
                'publicationDate': '8 December 2011'
            },
            {
                'url': 'https://www.lexisnexis.com/uk/legal/docview/getDocForCuiReq?lni=557G-8GP1-DYBR-3522&csi=274640&oc=00240&perma=true&elb=t',
                'title': 'Rochdale Metropolitan Borough Council v Dixon',
                'publicationDate': '20 October 2011'
            },
            {
                'url': 'https://www.lexisnexis.com/uk/legal/docview/getDocForCuiReq?lni=551H-8MS1-DYBR-3215&csi=274640&oc=00240&perma=true&elb=t',
                'title': 'R (on the application of O) v East Riding of Yorkshire County Council (Secretary of State for Education intervening) - [2012] LGR 171',
                'publicationDate': '2 March 2011'
            },
            {
                'url': 'https://www.lexisnexis.com/uk/legal/docview/getDocForCuiReq?lni=52FV-W5M1-DYBR-33F3&csi=274640&oc=00240&perma=true&elb=t',
                'title': 'R (on the application of McDonald) v Kensington and Chelsea Royal London Borough Council',
                'publicationDate': '13 October 2010'
            },
        ],
    },
    {
        'about': [
            'inspection rights',
        ],
        'data': [
            {
                'url': 'https://www.lexisnexis.com/uk/legal/docview/getDocForCuiReq?lni=7X2F-J0S0-Y96Y-H3F8&csi=274665&oc=00240&perma=true&elb=t',
                'title': 'HHR Pascal B.V. v W2005 Puppet II B.V',
                'publicationDate': '5 November 2009'
            },
            {
                'url': 'https://www.lexisnexis.com/uk/legal/docview/getDocForCuiReq?lni=5295-21X1-DYBR-30J2&csi=274640&oc=00240&perma=true&elb=t',
                'title': 'R (on the application of Veolia ES Nottinghamshire Ltd) v Nottinghamshire County Council (Dowen and another, interested parties)',
                'publicationDate': '29 October 2010'
            },
            {
                'url': 'https://www.lexisnexis.com/uk/legal/docview/getDocForCuiReq?lni=52DB-KR91-DYBP-P1CY&csi=274662&oc=00240&perma=true&elb=t',
                'title': 'R (on the application of Betting Shop Services Ltd) v Southend-on-Sea Borough Council',
                'publicationDate': '14 January 2008'
            },
            {
                'url': 'https://www.lexisnexis.com/uk/legal/docview/getDocForCuiReq?lni=52DB-KRH1-DYBP-P424&csi=274662&oc=00240&perma=true&elb=t',
                'title': 'Centrica plc and another v Premier Power Ltd',
                'publicationDate': '27 November 2007'
            },
            {
                'url': 'https://www.lexisnexis.com/uk/legal/docview/getDocForCuiReq?lni=4CRN-PP20-TWP1-61G6&csi=274668&oc=00240&perma=true&elb=t',
                'title': 'Grove v Eastern Gas Board',
                'publicationDate': '19 November 1951'
            },
        ],
    },
    {
        'about': [
            'Nicholas Gibson'
        ],
        'data': [
            {
                'url': 'http://lexisweb.co.uk/users/nicholas-gibson',
                'title': 'LexisWeb Biography',
                'publicationDate': ''
            },
            {
                'url': 'http://www.matrixlaw.co.uk/Members/117/Nicholas%20Gibson.aspx',
                'title': 'Matrix Chambers profile',
                'publicationDate': 'Undated'
            },
            {
                'url': 'http://eutopialaw.com/tag/nicholas-gibson/',
                'title': 'Knowing your limits: Uniplex delimited',
                'publicationDate': '3 November 2011'
            },
            {
                'url': 'http://www.linkedin.com/pub/nicholas-gibson/18/75b/2a9',
                'title': 'LinkedIn profile',
                'publicationDate': '2010'
            },
        ],
    },
    # {
    #     'about': [
    #     ],
    #     'data': [
    #         {
    #             'url': '',
    #             'title': '',
    #             'publicationDate': ''
    #         },
    #     ],
    # },
]

def checkData():
    """Check that there are no about value duplicates in the data."""
    error = False
    seenAbout = {}

    # Check that no about value is used more than once (if it is we would be
    # overwriting its value with later data, which is clearly an error).
    for dataset in datasets:
        for about in dataset['about']:
            if about in seenAbout:
                print >>sys.stderr, (
                    'About value %r appears multiple times in the input data!'
                    % about)
                error = True
            else:
                seenAbout[about] = None

    if error:
        print >>sys.stderr, 'Exiting due to duplicate about value errors.'
        sys.exit(1)


def importData():
    """Import the data to Fluidinfo."""
    for dataset in datasets:
        for about in dataset['about']:
            count = len(dataset['data'])
            print 'Adding %d URL%s to %r' % (
                count, ('' if count == 1 else 's'), about)
            fdb.about[about.lower()][TAG].put(dumps(dataset['data']))


if __name__ == '__main__':
    checkData()
    importData()
