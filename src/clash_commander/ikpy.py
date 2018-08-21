from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
# from typing import *

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import ikpy
from ikpy import plot_utils
from ikpy import geometry_utils
from ikpy.chain import Chain
from ikpy.link import OriginLink, URDFLink, Link, DHLink


# robot base link: clash_hand__body
# clash_hand__thumb_body_base 
# clash_hand__left_body_proximal 
# clash_hand__right_body_proximal

# link name="clash_hand__body
# link name="clash_hand__left_proximal
# link name="clash_hand__left_distal
# link name="clash_hand__right_proximal
# link name="clash_hand__right_distal
# link name="clash_hand__thumb_base
# link name="clash_hand__thumb_proximal
# link name="clash_hand__thumb_distal
# joint name="clash_hand__left_body_proximal" type="revolute
# joint name="clash_hand__left_proximal_distal" type="revolute
# joint name="clash_hand__right_body_proximal" type="revolute
# joint name="clash_hand__right_proximal_distal" type="revolute
# joint name="clash_hand__thumb_body_base" type="revolute
# joint name="clash_hand__thumb_base_proximal" type="revolute
# joint name="clash_hand__thumb_proximal_distal" type="revolute

urdf = os.getenv("mod_handconvert_root") +'/adaptedURDF/model.urdf'
leftChain = Chain.from_urdf_file(urdf,
                                 name='left finger',
                                 base_elements=['clash_hand__body', 'clash_hand__left_body_proximal'])
rightChain = Chain.from_urdf_file(urdf,
                                  name='right finger',
                                  base_elements=['clash_hand__body', 'clash_hand__right_body_proximal'])
thumbChain = Chain.from_urdf_file(urdf,
                                  name='thumb',
                                  base_elements=['clash_hand__body', 'clash_hand__thumb_body_base'])

# chain = Chain.from_urdf_file(urdf,
#                              base_elements=['clash_hand__body', 'clash_hand__thumb_base'],
#                              name='clash_urdf')
# chain = Chain.from_urdf_file(urdf, name='clash_urdf')

def trav(chain):
    """traverses a chain object and prints it

    :param Chain chain: the chain
    :rtype: None

    """
    print('--------------------------')
    print('### Chain: %s' % chain)
    print('--------------------------')
    for chain_elem in chain.links: # type: ikpy.link.Link
        print(chain_elem)

trav(thumbChain)
# trav(leftChain)
# trav(rightChain)


fig = plt.figure() # type: plt.Figure
ax = fig.add_subplot(111, projection='3d')
thumbChain.plot([0, 0, 0, 0], ax)
leftChain.plot([0, 0, 0], ax)
rightChain.plot([0, 0, 0], ax)
plt.show()

exit()
# matplotlib.pyplot.show()

# def chain_with_base_at(z):
#     return Chain(name='finger', links=[
#     OriginLink(),
#     URDFLink(
#       name="base",
#       translation_vector=[0, 0, z],
#       orientation=[0, 0, 0],
#       rotation=[0, 1, 0],
#     ),
#     URDFLink(
#       name="middle",
#       translation_vector=[6, 0, 0],
#       orientation=[0, 0, 0],
#       rotation=[0, 1, 0],
#     ),
#     URDFLink(
#       name="distal",
#       translation_vector=[3, 0, 0],
#       orientation=[0, 0, 0],
#       rotation=[0, 1, 0],
#     ),
#     URDFLink(
#       name="tip",
#       translation_vector=[1, 0, 0],
#       orientation=[0, 0, 0],
#       rotation=[0, 1, 0],
#     )
# ])


# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# fig=plt.figure(figsize=(10, 10))
# ax = fig.add_subplot(121, projection='3d')

# # configuring finger target
# target=[9, 0, 4]
# target_orient=np.eye(3)

# tM=geometry_utils.to_transformation_matrix(target, target_orient)

# print("target:")
# print(tM)

# my_chain=chain_with_base_at(2)
# # my_chain=chain_with_base_at(1)

# ikin_solution=my_chain.inverse_kinematics(tM)
# print("jointspace solution")
# print(ikin_solution)

# my_chain.plot(ikin_solution, ax)


# ax2 = fig.add_subplot(122, projection='3d')

# my_chain2=chain_with_base_at(3)

# ikin_solution2=my_chain2.inverse_kinematics(tM)
# print("jointspace solution")
# print(ikin_solution2)

# my_chain2.plot(ikin_solution2, ax2)


# # plotting
# ax.autoscale()
# ax2.autoscale()
# ax.set_xticks(np.arange(0, 11, 1.0))
# ax.set_yticks(np.arange(0, 11, 1.0))
# ax2.set_zticks(np.arange(0, 11, 1.0))
# ax2.set_xticks(np.arange(0, 11, 1.0))
# ax2.set_yticks(np.arange(0, 11, 1.0))
# ax.set_zticks(np.arange(0, 11, 1.0))
# ax.view_init(0, 270)
# ax2.view_init(0, 270)
# plt.show()

