#!/usr/bin/env python

import argparse

import pandatools.idds_api
import idds.common.utils as idds_utils

parser = argparse.ArgumentParser()
parser.add_argument('--workflowid', dest='workflowid', action='store', help='Workflow to retry', required=True)
results = parser.parse_args()

c = pandatools.idds_api.get_api(idds_utils.json_dumps, idds_host='https://aipanda015.cern.ch:443/idds', compress=True, manager=True)
print(c.retry(request_id=results.workflowid))

