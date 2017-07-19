#imports
import arcpy
from arcpy import env
from arcpy.sa import *

#set workspace
env.workspace   = "C:/sapyexamples/data"
# Get the input feature class name.
#
InRaster        =   arcpy.GetParameter(0)
saveLoc         =   arcpy.GetParameterAsText(1)
Filled          =   Fill(InRaster)
flowDir         =   FlowDirection(Filled)
flowAcc         =   FlowAccumulation(flowDir)
StrmOrd         =   StreamOrder(flowAcc,flowDir)

#featrCla        =   arcpy.CreateFeatureclass_management("C:/sapyexamples/output", "streams.shp", "POLYLINE")

#StrmFeat        =   StreamToFeature(flowAcc,flowDir,"C:/sapyexamples/output/streams02.shp")

arcpy.AddMessage(flowDir)
arcpy.AddMessage("The name of the raster is {0}".format(InRaster))



flowAcc.save("C:/sapyexamples/output/flowAcc")
flowDir.save("C:/sapyexamples/output/flowDir")





