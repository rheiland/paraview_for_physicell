# https://kitware.github.io/vtk-examples/site/Python/Filtering/Glyph3D/
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2

from vtk import *
# from vtkmodules.vtkCommonColor import vtkNamedColors
# from vtkmodules.vtkCommonCore import vtkPoints, vtkFloatArray
# from vtkmodules.vtkCommonDataModel import vtkPolyData,vtkUnsignedCharArray
# from vtkmodules.vtkFiltersCore import vtkGlyph3D
# from vtkmodules.vtkFiltersSources import vtkSphereSource
# from vtkmodules.vtkRenderingCore import (
#     vtkActor,
#     vtkPolyDataMapper,
#     vtkRenderWindow,
#     vtkRenderWindowInteractor,
#     vtkRenderer
# )

from pyMCDS_cells import pyMCDS_cells
from vtk.util import numpy_support
import numpy as np
import random

def main():
    argc = len(sys.argv)
    if argc < 2:
        print("   Missing argument: output<num>.xml\n")
        sys.exit(1)
    fname = sys.argv[1]
    # mcds = pyMCDS_cells('output00000032.xml', '.')  
    mcds = pyMCDS_cells(fname, '.')  
    print('time=', mcds.get_time())

    print(mcds.data['discrete_cells'].keys())

    ncells = len(mcds.data['discrete_cells']['ID'])
    print('ncells=', ncells)

    global xyz
    xyz = np.zeros((ncells, 3))
    xyz[:, 0] = mcds.data['discrete_cells']['position_x']
    xyz[:, 1] = mcds.data['discrete_cells']['position_y']
    xyz[:, 2] = mcds.data['discrete_cells']['position_z']
    #xyz = xyz[:1000]
    print("position_x = ",xyz[:,0])
    xmin = min(xyz[:,0])
    xmax = max(xyz[:,0])
    print("xmin = ",xmin)
    print("xmax = ",xmax)

    ymin = min(xyz[:,1])
    ymax = max(xyz[:,1])
    print("ymin = ",ymin)
    print("ymax = ",ymax)

    zmin = min(xyz[:,2])
    zmax = max(xyz[:,2])
    print("zmin = ",zmin)
    print("zmax = ",zmax)

    cell_type = mcds.data['discrete_cells']['cell_type']
    print(type(cell_type))
    print(cell_type)
    unique_cell_type = np.unique(cell_type)
    print("\nunique_cell_type = ",unique_cell_type )

    #------------
    colors = vtkNamedColors()

    points = vtkPoints()
    points.InsertNextPoint(0, 0, 0)
    points.InsertNextPoint(1, 1, 1)
    points.InsertNextPoint(2, 2, 2)
    cellID = vtkFloatArray()
    cellVolume = vtkFloatArray()
    num_cells = 0
    for idx in range(ncells):
        x= mcds.data['discrete_cells']['position_x'][idx]
        y= mcds.data['discrete_cells']['position_y'][idx]
        z= mcds.data['discrete_cells']['position_z'][idx]
        if z < 0:   # crop spatially to see inside
            num_cells += 1
            id = mcds.data['discrete_cells']['cell_type'][idx]
            points.InsertNextPoint(x, y, z)
            # cellVolume.InsertNextValue(30.0)
            cellID.InsertNextValue(id)

    print('after spatial cropping, num_cells=', num_cells)

    polydata = vtkPolyData()
    polydata.SetPoints(points)
    # polydata.GetPointData().SetScalars(cellVolume)
    polydata.GetPointData().SetScalars(cellID)

    cellID_color_dict = {}
    # for idx in range(ncells):
    random.seed(42)
    for utype in unique_cell_type:
        cellID_color_dict[utype] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
    # cellID_color_dict[0.0]=[255,255,0]  # yellow basement membrane
    print("color dict=",cellID_color_dict)

    colors = vtkUnsignedCharArray()
    colors.SetNumberOfComponents(3)
    colors.SetNumberOfTuples(polydata.GetNumberOfPoints())  # ncells

    # for idx in range(ncells):
    for idx in range(num_cells):
    # for idx in range(len(unique_cell_type)):
        # colors.InsertTuple3(idx, randint(0,255), randint(0,255), randint(0,255)) 
        # if idx < 5:
            # print(idx,cellID_color_dict[cell_type[idx]])
        # colors.InsertTuple3(idx, cellID_color_dict[cell_type[idx]][0], cellID_color_dict[cell_type[idx]][1], cellID_color_dict[cell_type[idx]][2])
        if mcds.data['discrete_cells']['current_phase'][idx] == 14.0:
            colors.InsertTuple3(idx, 255,255,0)
        else:
            colors.InsertTuple3(idx, 139,69,19)  # 250,138,38

    polydata.GetPointData().SetScalars(colors)

    sphereSource = vtkSphereSource()
    nres = 20
    sphereSource.SetPhiResolution(nres)
    sphereSource.SetThetaResolution(nres)
    sphereSource.SetRadius(0.03)

    glyph = vtkGlyph3D()
    glyph.SetSourceConnection(sphereSource.GetOutputPort())
    glyph.SetInputData(polydata)
    glyph.SetColorModeToColorByScalar()
    # glyph.SetScaleModeToDataScalingOff()
    # glyph.SetScaleModeToDataScalingOn()
    # glyph.ScalingOn()
    # glyph.SetScaleFactor(2)  # overall (multiplicative) scaling factor
    glyph.Update()


    # Visualize
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(glyph.GetOutputPort())

    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetInterpolationToPBR()
    # actor.GetProperty().SetColor(colors.GetColor3d('Salmon'))
    print("-- actor defaults:")
    print("-- diffuse:",actor.GetProperty().GetDiffuse())
    print("-- specular:",actor.GetProperty().GetSpecular())
    # print("-- roughness:",actor.GetProperty().GetCoatRoughness ())
    actor.GetProperty().SetDiffuse(0.7)
    # actor.GetProperty().SetSpecular(0.2)
    # actor.GetProperty().SetCoatRoughness (0.5)
    # actor.GetProperty().SetCoatRoughness (0.2)
    # actor.GetProperty().SetCoatRoughness (1.0)

    renderer = vtkRenderer()
    amval = 1.0  # default
    renderer.SetAmbient(amval, amval, amval)

    renderWindow = vtkRenderWindow()
    renderWindow.SetPosition(100,100)
    renderWindow.SetSize(1400,1200)
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    renderer.AddActor(actor)
    # renderer.SetBackground(colors.GetColor3d('SlateGray'))  # Background Slate Gray

    renderWindow.SetWindowName('PhysiCell model')
    renderWindow.Render()
    renderWindowInteractor.Start()


if __name__ == '__main__':
    main()
