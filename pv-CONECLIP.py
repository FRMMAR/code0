# trace generated using paraview version 5.7.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Cone'
cone1 = Cone()

# Properties modified on cone1
cone1.Resolution = 16
cone1.Radius = 1.0

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraFocalDisk = 1.0
renderView1.Background = [0.32, 0.34, 0.43]
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1
# uncomment following to set a specific view size
# renderView1.ViewSize = [400, 400]

# show data in view
cone1Display = Show(cone1, renderView1)

# trace defaults for the display properties.
cone1Display.Representation = 'Surface'
cone1Display.ColorArrayName = [None, '']
cone1Display.OSPRayScaleFunction = 'PiecewiseFunction'
cone1Display.SelectOrientationVectors = 'None'
cone1Display.ScaleFactor = 0.2
cone1Display.SelectScaleArray = 'None'
cone1Display.GlyphType = 'Arrow'
cone1Display.GlyphTableIndexArray = 'None'
cone1Display.GaussianRadius = 0.01
cone1Display.SetScaleArray = [None, '']
cone1Display.ScaleTransferFunction = 'PiecewiseFunction'
cone1Display.OpacityArray = [None, '']
cone1Display.OpacityTransferFunction = 'PiecewiseFunction'
cone1Display.DataAxesGrid = 'GridAxesRepresentation'
cone1Display.PolarAxes = 'PolarAxesRepresentation'

# add view to a layout so it's visible in UI
AssignViewToLayout(view=renderView1, layout=None, hint=0)

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Clip'
clip1 = Clip(Input=cone1)
clip1.ClipType = 'Plane'
clip1.Scalars = [None, '']

# Properties modified on clip1
clip1.Scalars = ['POINTS', '']

# show data in view
clip1Display = Show(clip1, renderView1)

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = [None, '']
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'None'
clip1Display.ScaleFactor = 0.2
clip1Display.SelectScaleArray = 'None'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'None'
clip1Display.GaussianRadius = 0.01
clip1Display.SetScaleArray = [None, '']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = [None, '']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityUnitDistance = 0.9243857090724148

# hide data in view
Hide(cone1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [7.826440913553424, 0.0, 0.0]
renderView1.CameraFocalPoint = [-1e-20, 0.0, 0.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 2.0256319637971973

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).