import pytest
import unittest

import unittest
import pytest
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))
parentdir2 = os.path.dirname(parentdir)
sys.path.insert(0,parentdir2)

from AlgoWebSite.DashApps.service.Dunod.list_sorting import *