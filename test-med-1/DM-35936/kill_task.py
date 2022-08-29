#!/usr/bin/env python
import argparse

from pandatools import Client

parser = argparse.ArgumentParser()
parser.add_argument('--taskid', dest='taskid', action='store', help='Task to kill', required=True)
results = parser.parse_args()
print(Client.killTask(results.taskid))

