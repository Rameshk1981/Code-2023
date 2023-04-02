"""  
#******************************************************************************************************** 

Inclusion: Creates 32 CIRCULAR Inclusions 
#******************************************************************************************************** 
"""  


#Import Abaqus-related (Python) Object files 
from abaqus import * 
from abaqusConstants import * 
import __main__ 
import section 
import regionToolset 
import displayGroupMdbToolset as dgm 
import part 
import material 
import assembly 
import step 
import interaction 
import load 
import mesh 
import job 
import sketch 
import visualization 
import xyPlot 
import displayGroupOdbToolset as dgo 
import connectorBehavior 

#**************************************************** 
# CREATE MATRIX AND FIBRE MATERIALS/SECTIONS HERE 
#**************************************************** 
mdb.models['Model-1'].Material(name='matrix') 
mdb.models['Model-1'].Material(name='fibre') 
mdb.models['Model-1'].HomogeneousSolidSection(name='matrixSection', material='matrix', thickness=None) 
mdb.models['Model-1'].HomogeneousSolidSection(name='fibreSection', material='fibre', thickness=None) 

#Create Viewport 
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF) 
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(meshTechnique=OFF) 

s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=450) 
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints 
s.setPrimaryObject(option=STANDALONE) 
session.viewports['Viewport: 1'].view.setValues(width=30, height=15) 

#**************************************************** 
# REINFORCING INCLUSIONS SECTION 
#**************************************************** 

# ------------------------------------------------------------------- 
#Create Fibre circles at specified centre coordinates(XYAll) and defined radius, R 
s.CircleByCenterPerimeter(center=(104.6673, 10.0801), point1=(114.6673, 10.0801)) 
s.CircleByCenterPerimeter(center=(27.2639, 34.2161), point1=(37.2639, 34.2161)) 
s.CircleByCenterPerimeter(center=(38.4317, 66.067), point1=(48.4317, 66.067)) 
s.CircleByCenterPerimeter(center=(37.7476, 119.321), point1=(47.7476, 119.321)) 
s.CircleByCenterPerimeter(center=(118.509, 138.4279), point1=(128.509, 138.4279)) 
s.CircleByCenterPerimeter(center=(103.7407, 82.2336), point1=(113.7407, 82.2336)) 
s.CircleByCenterPerimeter(center=(140.4172, 90.8105), point1=(150.4172, 90.8105)) 
s.CircleByCenterPerimeter(center=(73.6163, 132.8073), point1=(83.6163, 132.8073)) 
s.CircleByCenterPerimeter(center=(15.6715, 0.11908), point1=(25.6715, 0.11908)) 
s.CircleByCenterPerimeter(center=(114.3922, 35.5202), point1=(124.3922, 35.5202)) 
s.CircleByCenterPerimeter(center=(11.1224, 126.778), point1=(21.1224, 126.778)) 
s.CircleByCenterPerimeter(center=(10.2029, 76.8641), point1=(20.2029, 76.8641)) 
s.CircleByCenterPerimeter(center=(50.5286, 94.8265), point1=(60.5286, 94.8265)) 
s.CircleByCenterPerimeter(center=(149.234, 44.3692), point1=(159.234, 44.3692)) 
s.CircleByCenterPerimeter(center=(50.6339, 21.7286), point1=(60.6339, 21.7286)) 
s.CircleByCenterPerimeter(center=(68.1863, 53.3984), point1=(78.1863, 53.3984)) 
s.CircleByCenterPerimeter(center=(82.1922, 22.3271), point1=(92.1922, 22.3271)) 
s.CircleByCenterPerimeter(center=(127.801, 17.1184), point1=(137.801, 17.1184)) 
s.CircleByCenterPerimeter(center=(83.2922, 110.9396), point1=(93.2922, 110.9396)) 
s.CircleByCenterPerimeter(center=(131.8298, 113.9221), point1=(141.8298, 113.9221)) 
s.CircleByCenterPerimeter(center=(45.4653, 149.5157), point1=(55.4653, 149.5157)) 
s.CircleByCenterPerimeter(center=(118.1219, 62.716), point1=(128.1219, 62.716)) 
s.CircleByCenterPerimeter(center=(95.465, 49.5245), point1=(105.465, 49.5245)) 
s.CircleByCenterPerimeter(center=(109.0645, 111.1388), point1=(119.0645, 111.1388)) 
s.CircleByCenterPerimeter(center=(140.9756, 146.6579), point1=(150.9756, 146.6579)) 
s.CircleByCenterPerimeter(center=(-9.5828, 90.8105), point1=(0.41715, 90.8105)) 
s.CircleByCenterPerimeter(center=(-0.76601, 44.3692), point1=(9.234, 44.3692)) 
s.CircleByCenterPerimeter(center=(-9.0244, 146.6579), point1=(0.97561, 146.6579)) 
s.CircleByCenterPerimeter(center=(15.6715, 150.1191), point1=(25.6715, 150.1191)) 
s.CircleByCenterPerimeter(center=(45.4653, -0.48429), point1=(55.4653, -0.48429)) 
s.CircleByCenterPerimeter(center=(140.9756, -3.3421), point1=(150.9756, -3.3421)) 
s.CircleByCenterPerimeter(center=(-9.0244, -3.3421), point1=(0.97561, -3.3421)) 
# ------------------------------------------------------------------- 
 
#Name the part model and associate it 
p = mdb.models['Model-1'].Part(name='RVE2DFibre', dimensionality=TWO_D_PLANAR, type=DEFORMABLE_BODY) 
p = mdb.models['Model-1'].parts['RVE2DFibre'] 
 
#Fibre Extrusion 
p.BaseShell(sketch=s) 
s.unsetPrimaryObject() 
p = mdb.models['Model-1'].parts['RVE2DFibre'] 
session.viewports['Viewport: 1'].setValues(displayedObject=p) 
del mdb.models['Model-1'].sketches['__profile__'] 
 
#**************************************************** 
# MATRIX SECTION 
#**************************************************** 

#Create Viewport 
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF) 
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(meshTechnique=OFF) 

s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=450) 
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints 
s1.setPrimaryObject(option=STANDALONE) 
session.viewports['Viewport: 1'].view.setValues(width=30, height=15) 

#Sketch RVE Rectangle 
s1.rectangle(point1=(0.0,0.0), point2=(150, 150)) 
 
#Name the part model and associate it 
p = mdb.models['Model-1'].Part(name='RVE2DMatrix', dimensionality=TWO_D_PLANAR, type=DEFORMABLE_BODY) 
p = mdb.models['Model-1'].parts['RVE2DMatrix'] 
 
#Matrix Extrusion 
p.BaseShell(sketch=s1)  
s1.unsetPrimaryObject() 
p = mdb.models['Model-1'].parts['RVE2DMatrix'] 
session.viewports['Viewport: 1'].setValues(displayedObject=p) 
del mdb.models['Model-1'].sketches['__profile__'] 
 
#**************************************************** 
#ASSEMBLY INSTANCES AND MERGE THE TWO INSTANCES 
#**************************************************** 
a = mdb.models['Model-1'].rootAssembly 
a.DatumCsysByDefault(CARTESIAN) 
p = mdb.models['Model-1'].parts['RVE2DFibre'] 
a.Instance(name='RVE2DFibre-1', part=p, dependent=ON) 
p = mdb.models['Model-1'].parts['RVE2DMatrix'] 
a.Instance(name='RVE2DMatrix-1', part=p, dependent=ON) 
a = mdb.models['Model-1'].rootAssembly 
a.InstanceFromBooleanMerge(name='RVE2DComposite', instances=( 
    a.instances['RVE2DFibre-1'], a.instances['RVE2DMatrix-1'], ), 
    keepIntersections=ON, originalInstances=SUPPRESS, domain=GEOMETRY) 
mdb.models['Model-1'].rootAssembly.features.changeKey( 
    fromName='RVE2DComposite-1', toName='RVE2DComposite') 
 
#**************************************************** 
# EXTRUDE-CUT SECTION TO TRIM BOUNDARY FIBRES 
#**************************************************** 
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF,engineeringFeatures=OFF) 
p1 = mdb.models['Model-1'].parts['RVE2DComposite'] 
session.viewports['Viewport: 1'].setValues(displayedObject=p1) 
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=450) 
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints 
s.setPrimaryObject(option=SUPERIMPOSE) 
p = mdb.models['Model-1'].parts['RVE2DComposite'] 
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES) 
s.rectangle(point1=(0 ,0), point2=(150 ,150)) 
s.rectangle(point1=(-300 ,-300), point2=(300 ,300)) 
session.viewports['Viewport: 1'].view.fitView() 
p = mdb.models['Model-1'].parts['RVE2DComposite'] 
p.Cut(sketch=s) 
s.unsetPrimaryObject() 
mdb.models.changeKey(fromName='Model-1', toName='RandomUDComposite' )
session.viewports['Viewport: 1'].setValues(displayedObject=None) 
 
mdb.Model(name='Model-1') 
#************************************************************************ 
#                               END OF SCRIPT                             
#************************************************************************ 
# ------------------------------------------------------------------- 
