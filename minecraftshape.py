#https://github.com/1428594509/minecraftshape
#Raspberry Pi, Minecraft - Minecraft mathshape

try:
    import mcpi.minecraft as minecraft
    import mcpi.block as block
    import mcpi.util as util
except ImportError:
    import minecraft
    import block
    import util

import time
import math

class MinecraftMath3DShape:
    """
    MinecraftShape - a class of complexed shape functions

    :param mcpi.minecraft.Minecraft mc:
        A Minecraft object which is connected to a world. 
    """
    def __init__(self, mc):
        self.mc = mc
   
    def drawCurve1(self, x0, y0, z0, length, coefficience, blockType, blockData=0):
        """
        draws a circle in the Y plane (i.e. vertically)

        :param int x0:
            The x position of the start point.

        :param int y0:
            The y position of the start point.

        :param int z:
            The z position of the start point.

        :param int length:
            The length of the x direction and z direction.
            
        :param int coefficience:
            The scale factor
              
        :param int blockType:
            The block id.

        :param int blockData:
            The block data value, defaults to ``0``.
        """

        for x in range(0,length):
            for z in range(0,length):
                y=(x*x+z*z)/coefficience
                self.mc.setBlock(x0+x,y0+y,z0+z,blockType,blockData)
         
     def drawCurve2(self, x0, y0, z0, length, coefficience, blockType, blockData=0):
        """
        draws a circle in the Y plane (i.e. vertically)

        :param int x0:
            The x position of the start point.

        :param int y0:
            The y position of the start point.

        :param int z:
            The z position of the start point.

        :param int length:
            The length of the x direction and z direction.
            
        :param int coefficience:
            The scale factor
              
        :param int blockType:
            The block id.

        :param int blockData:
            The block data value, defaults to ``0``.
        """

        for x in range(0,length):
            for z in range(0,length):
                y=(x*x-z*z)/coefficience
                self.mc.setBlock(x0+x,y0+y,z0+z,blockType,blockData)   
     
