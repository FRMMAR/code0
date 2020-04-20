# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 11:34:29 2019

@author: 1
"""

import os 
import re
import numpy as np
from scipy.spatial import Delaunay
from scipy.spatial import ConvexHull

if __name__ == '__main__':

    def openstl(oFileName = "aa.stl"):
        with open(oFileName) as ofin:
            lines = ofin.readlines()
        for line in lines:
            if re.match(mat, line):
                line = re.sub(mat,'',line)
                line = line.split()
                a = [float(x) for x in line]
                a = tuple(a)
                l.append(a)
                ll = set(l)
                lll = list(ll)
                lla = [list(x) for x in lll]
                global llb
                llb = np.array(lla)
    
    def convexBody(x = llb):
        hull = ConvexHull(x)
        indices = hull.simplices
        global v
        v = str(llb[indices])
        
    def writeXyz():
        with open("z0", 'w') as z:
            z.write(v)
        
    def writeAll():
        with open("z0", 'r') as zz:
            lines = zz.read()
        for line in lines:
            lines = lines.replace('[[[', 'solid\nfacet\nouter loop\nvertex ')
            lines = lines.replace(']]]', '\nendloop\nendfacet\nendsolid')
            lines = lines.replace('\n [[', 'endloop\nendfacet\nfacet\nouter loop\nvertex ')
            lines = lines.replace('  [', 'vertex ')
            lines = lines.replace(']', '')
        with open("zz", 'w') as z:
            lines = z.write(lines)
            print(lines)
            
    os.getcwd()
    mat = r'vertex\s'
    l = []
    openstl('L16-01-nomesherror.stl')
    convexBody()
    writeXyz()
    writeAll()