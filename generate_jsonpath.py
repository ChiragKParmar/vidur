#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import sys
import pprint

def recur_dict(
        accum,
        value,
        parent = None,
        list_idx = None,
    ):
    list_idx = list_idx or 0
    parent = parent or '$'

    if isinstance(value, dict):
        for (k, v) in value.items():
            fmt_k = "['{}']".format(k)
            parent_path = (''.join([parent, fmt_k]) if parent != '' else fmt_k)
            if isinstance(v, (list, dict)):
                recur_dict(accum, v, parent_path, list_idx = list_idx)
            else :
                accum.add(parent_path)
    elif isinstance(value, list):
        accum.add(''.join([parent, '[{}]'.format(str(list_idx))]))
        return accum
    return accum


with open(sys.argv[1]) as data_file:
    data = json.load(data_file)

paths_set = recur_dict(set(), data, list_idx = None)
paths_list = list(paths_set)
paths_list.sort()

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(paths_list)

#return {"jsonpaths": paths_list}