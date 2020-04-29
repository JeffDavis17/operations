import numpy as np
import math as m
import pandas as pd

'''
This is a function library that applies  transformations to Northing and Easting coordinates, when used in a Numpy array [[N1,E1],[N2,E2]]
'''


# ROTATE
'''
- Rotates all points in the counterclock direction by the angle specified: angle
- About the point specified by indice: pt_indice
- Using data inputed: l
'''
def rotate(angle,pt_indice,l):
    angle = m.radians(angle)
    a = m.cos(angle)
    b = m.sin(angle)
    M = np.array([[a,-b],
    [b,a]])

    new_pts = (M@l.T).T
    t = l[pt_indice] - new_pts[pt_indice]
    new_pts += t
    return new_pts



# TRANSLATE
'''
- Translates in Northing direction by amount: tN
- Translates in Easting direction by amount: tE
- Applied to all points entered: l
'''
def translate(tN,tE,l):
    l += [tN,tE]
    return l



# SCALE
'''
- Applies a scale factor s
- Applies in the outward direction from point indice specified: pt_indice
- Applied to each point entered: l
'''
def scale(s,pt_indice,l):
    new_pts = l*s
    t = l[pt_indice] - new_pts[pt_indice]
    new_pts += t
    return new_pts



# CONFORMAL
'''
- Applies Rotation: angle
- Applies Scale Factor: s
- Done in a certain direction about the specified point, by point indice: pt_indice
- Done to all points l
'''

def conformal(angle,s,pt_indice,l):
    # rotation
    angle = m.radians(angle)
    a = s*m.cos(angle)
    b = s*m.sin(angle)
    M = np.array([[a,-b],
    [b,a]])    

    new_pts = (M@l.T).T
    t = l[pt_indice] - new_pts[pt_indice]
    new_pts += t
    return new_pts


# INVERSE
'''
Provides the distance and Azimuth between 2 points [dist,az] = inverse(args)
'''
def inverse(pt1,pt2):
    dist = m.sqrt((pt2[1] - pt1[1])**2 + (pt2[0] - pt1[0])**2)
    az = m.atan2((pt2[1] - pt1[1])/(pt2[0] - pt1[0]))




# Bearing
'''
Converts Azimuth to Bearing
'''



# Azimuth
'''
Converts Bearning to Azimuth
'''
