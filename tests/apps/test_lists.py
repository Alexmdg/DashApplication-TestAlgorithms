import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(0,parentdir)

print(currentdir, parentdir)

from AlgoWebSite.DashApps.Apps.lists import *
# from AlgoWebSite.DashApps.toolbox.lists_data import *

class TestCallbacksFunctions:
    data_set = DataSet()

    def test_newList(self):
        bttn_input = 1
        list_len = 10
        results=newList(bttn_input, list_len)
        errors=[]
        if len(results) != 2:
            errors.append('number of value returned error')
        elif type(results[0]) is not list() :
            errors.append(f'error saving list: {type(results[0])}')
        elif len(results[0]) != 10:
            errors.append(f'list length error: {len(results[0])}')

