#!/usr/bin/env python

## Program:   VMTK
## Module:    $RCSfile: vmtksurfacetomesh.py,v $
## Language:  Python
## Date:      $Date: 2005/09/14 09:49:59 $
## Version:   $Revision: 1.7 $

##   Copyright (c) Luca Antiga, David Steinman. All rights reserved.
##   See LICENCE file for details.

##      This software is distributed WITHOUT ANY WARRANTY; without even 
##      the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR 
##      PURPOSE.  See the above copyright notices for more information.


import vtk
import vtkvmtk
import sys

import pypes

vmtksurfacetomesh = 'vmtkSurfaceToMesh'

class vmtkSurfaceToMesh(pypes.pypeScript):

    def __init__(self):

        pypes.pypeScript.__init__(self)
        
        self.Surface = None
        self.Mesh = None
        self.CleanInput = 1

        self.SetScriptName('vmtksurfacetomesh')
        self.SetScriptDoc('convert surface to a mesh')
        self.SetInputMembers([
            ['Surface','i','vtkPolyData',1,'','the input surface','vmtksurfacereader'],
            ['CleanInput','cleaninput','bool',1,'','clean unused points in the input']
            ])
        self.SetOutputMembers([
            ['Mesh','o','vtkUnstructuredGrid',1,'','the output mesh','vmtkmeshwriter']])

    def Execute(self):

        if self.Surface == None:
            self.PrintError('Error: No input surface.')

        if self.CleanInput == 1:
            cleaner = vtk.vtkCleanPolyData()
            cleaner.SetInputData(self.Surface)
            cleaner.Update()
            self.Surface = cleaner.GetOutput()

        surfaceToMeshFilter = vtkvmtk.vtkvmtkPolyDataToUnstructuredGridFilter()
        surfaceToMeshFilter.SetInputData(self.Surface)
        surfaceToMeshFilter.Update()

        self.Mesh = surfaceToMeshFilter.GetOutput()


if __name__=='__main__':

    main = pypes.pypeMain()
    main.Arguments = sys.argv
    main.Execute()
