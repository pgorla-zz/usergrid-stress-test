#!/usr/bin/env python

from __future__ import print_function

import datetime
import random
import requests
import sys

from tokens import ACCESS_TOKEN

ORG = "myorg"
APP = "myapp"

path = "http://localhost:8080/%s/%s" % (ORG, APP)

headers = {
    "Authorization": "Bearer {}".format(ACCESS_TOKEN),
    "Content-Type": "application/json"
    }

def rand_inserts(inserts=100):
    success = 0
    for i in range(inserts):
        data = {i:random.random()}
        response = requests.post(path, data=data, headers=headers)
        if response.status_code == 200:
            success += 1
    return success


if __name__ == "__main__":
    try:
        inserts = int(sys.argv[1])
    except IndexError:
        inserts = 1000
    print("Testing %s inserts." % inserts)
    tstart = datetime.datetime.now()
    success = rand_inserts(inserts)
    tend = datetime.datetime.now()

    ttotal = tend - tstart

    print("Tested %s inserts with %s successes." % (inserts, success))
    print("Inserted %s inserts in %s seconds." % (success, ttotal.total_seconds()))
