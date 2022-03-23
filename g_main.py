# g_main.py

from graphics.g_global import Flags, ViewParams, SceneParams, OpenGLParams
import graphics.g_scene as g_scene
import graphics.ogl_renderer as ogl_renderer

def getPauseFlag():
	return Flags.pause

def initGraphics( layerIn, layer ):
	assemblies = SceneParams.assemblies

	ogl_renderer.init()
	initOrthogonalProjection()
	g_scene.initScene( layerIn, layer )

	meshList = assemblies[0].polygons[0].mesh

	positionList = []
	for assembly in assemblies:
		for polygon in assembly.polygons:
			positionList += polygon.position

	ogl_renderer.updateUniformMatrix( OpenGLParams.shaderProjectionMatrixLocation,
                                      ViewParams.projectionMatrix )

	ogl_renderer.updateVBO( OpenGLParams.shaderMeshLocation,
                            OpenGLParams.meshBuffer,
                            meshList,
                            2 )

	ogl_renderer.updateVBO( OpenGLParams.shaderPositionLocation,
                            OpenGLParams.positionBuffer,
                            positionList,
                            2, )

def updateGraphics( layerIn, layer ):
	assemblies = SceneParams.assemblies

	updateView()
	g_scene.updateScene( layerIn, layer )

	colorList = []
	for assembly in assemblies:
		for polygon in assembly.polygons:
			colorList += polygon.color

	ogl_renderer.updateUniformMatrix( OpenGLParams.shaderViewMatrixLocation,
                                      ViewParams.viewMatrix )

	ogl_renderer.updateVBO( OpenGLParams.shaderColorLocation,
                            OpenGLParams.colorBuffer,
                            colorList,
                            3 )

	numPolygons = int( len( colorList ) / 3 )
	ogl_renderer.draw( "triangles", numPolygons )
#	ogl_renderer.draw( "line_strip", numPolygons )

	Flags.pause = True

	if Flags.cleanGraphics == True: cleanGraphics()

def cleanGraphics():
	ogl_renderer.cleanup( OpenGLParams.shaderMeshLocation,
                          OpenGLParams.meshBuffer )

	ogl_renderer.cleanup( OpenGLParams.shaderPositionLocation,
                          OpenGLParams.positionBuffer )

	ogl_renderer.cleanup( OpenGLParams.shaderColorLocation,
                          OpenGLParams.colorBuffer )

	ogl_renderer.exit( OpenGLParams.shaderID,
                       OpenGLParams.windowID )

def initOrthogonalProjection():
	"""2D projection with top left pixel as the origin"""
	projectionMatrix = ViewParams.projectionMatrix

	xmin = 0.0
	xmax = ViewParams.viewportWidth

	ymin = ViewParams.viewportHeight
	ymax = 0.0

	znear = 1.0
	zfar = -1.0

	width = xmax - xmin
	height = ymax - ymin
	depth = zfar - znear

	projectionMatrix[0] = 2.0 / width
	projectionMatrix[4] = 0.0
	projectionMatrix[8] = 0.0
	projectionMatrix[12] = -( xmax + xmin ) / width

	projectionMatrix[1] = 0.0
	projectionMatrix[5] = 2.0 / height
	projectionMatrix[9] = 0.0
	projectionMatrix[13] = -( ymax + ymin ) / height

	projectionMatrix[2] = 0.0
	projectionMatrix[6] = 0.0
	projectionMatrix[10] = -2.0 / depth
	projectionMatrix[14] = -( zfar + znear ) / depth

	projectionMatrix[3] = 0.0
	projectionMatrix[7] = 0.0
	projectionMatrix[11] = 0.0
	projectionMatrix[15] = 1.0

def updateView():
	viewMatrix = ViewParams.viewMatrix

	viewMatrix[12] = ViewParams.viewX
	viewMatrix[13] = ViewParams.viewY
	viewMatrix[14] = ViewParams.viewZ
