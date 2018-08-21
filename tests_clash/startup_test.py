from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
# from typing import *

import unittest
import clash_commander.sim as sim

print('helloworld')

class PlannerTest(unittest.TestCase):

    def setUp(self):
        self.abc = 'test'

    def testBla(self):
        print('hello test %s' % self.abc)
        sim.importtest()
        # raise 'BOOM'


# Typing:
# def trav(chain):
#     """traverses a chain object and prints it

#     :param Chain chain: the chain
#     :rtype: None
# fig = plt.figure() # type: plt.Figure
# for chain_elem in chain.links: # type: ikpy.link.Link
