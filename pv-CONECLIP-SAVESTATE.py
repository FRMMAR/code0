# state file generated using paraview version 5.7.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# trace generated using paraview version 5.7.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [395, 319]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraFocalDisk = 1.0
renderView1.Background = [0.32, 0.34, 0.43]
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [395, 319]
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.StereoType = 'Crystal Eyes'
renderView2.CameraPosition = [7.826440913553424, 0.0, 0.0]
renderView2.CameraFocalPoint = [-1e-20, 0.0, 0.0]
renderView2.CameraViewUp = [0.0, 0.0, 1.0]
renderView2.CameraFocalDisk = 1.0
renderView2.CameraParallelScale = 2.0256319637971973
renderView2.Background = [0.32, 0.34, 0.43]
renderView2.BackEnd = 'OSPRay raycaster'
renderView2.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.SplitHorizontal(0, 0.500000)
layout1.AssignView(1, renderView1)
layout1.AssignView(2, renderView2)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView2)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Cone'
cone1 = Cone()
cone1.Resolution = 16
cone1.Radius = 1.0

# create a new 'Clip'
clip1 = Clip(Input=cone1)
clip1.ClipType = 'Plane'
clip1.Scalars = ['POINTS', '']

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from clip1
clip1Display = Show(clip1, renderView2)

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['POINTS', '']
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'None'
clip1Display.ScaleFactor = 0.2
clip1Display.SelectScaleArray = 'None'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'None'
clip1Display.GaussianRadius = 0.01
clip1Display.SetScaleArray = ['POINTS', '']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', '']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityUnitDistance = 0.9243857090724148

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(clip1)
# ----------------------------------------------------------------