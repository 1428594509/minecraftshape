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
        :param int x0:
            The x position of the start point.

        :param int y0:
            The y position of the start point.

        :param int z0:
            The z position of the start point.

        :param int length:
            The length of the x + -direction and z + -direction.
            
        :param int coefficience:
            The scale factor
              
        :param int blockType:
            The block id.

        :param int blockData:
            The block data value, defaults to ``0``.
        """

        for x in range(-length,length):
            for z in range(-length,length):
                y=(x*x+z*z)/coefficience
                self.mc.setBlock(x0+x,y0+y,z0+z,blockType,blockData)

    
    def drawCurve2(self, x0, y0, z0, length, coefficience, blockType, blockData=0):
        """
        :param int x0:
            The x position of the start point.

        :param int y0:
            The y position of the start point.

        :param int z0:
            The z position of the start point.

        :param int length:
            The length of the x + -direction and z + -direction.
            
        :param int coefficience:
            The scale factor
              
        :param int blockType:
            The block id.

        :param int blockData:
            The block data value, defaults to ``0``.
        """

        for x in range(-length,length):
            for z in range(-length,length):
                y=(x*x-z*z)/coefficience
                self.mc.setBlock(x0+x,y0+y,z0+z,blockType,blockData)
   
    def drawCurve3(self, x0, y0, z0, length, coefficience, blockType, blockData=0):
        """
        :param int x0:
            The x position of the start point.

        :param int y0:
            The y position of the start point.

        :param int z0:
            The z position of the start point.

        :param int length:
            The length of the x + -direction and z + -direction.
            
        :param int coefficience:
            The scale factor
              
        :param int blockType:
            The block id.

        :param int blockData:
            The block data value, defaults to ``0``.
        """

        for x in range(-length,length):
            for z in range(-length,length):
                if x!=0 and z!=0:
                    y=((x/z)**2+ (z/x)**2)/coefficience
                    self.mc.setBlock(x0+x,y0+y,z0+z,blockType,blockData)

    def drawCurve4(self, x0, y0, z0, length, coefficience, blockType, blockData=0):
        """
        :param int x0:
            The x position of the start point.

        :param int y0:
            The y position of the start point.

        :param int z0:
            The z position of the start point.

        :param int length:
            The length of the x + -direction and z + -direction.
            
        :param int coefficience:
            The scale factor
              
        :param int blockType:
            The block id.

        :param int blockData:
            The block data value, defaults to ``0``.
        """

        for x in range(-length,length):
            for z in range(-length,length):
                y=math.tan((x**2+z**2)*math.pi/180)/coefficience
                self.mc.setBlock(x0+x,y0+y,z0+z,blockType,blockData)

    def drawCurve5(self, x0, y0, z0, length, coefficience, blockType, blockData=0):
        """
        :param int x0:
            The x position of the start point.

        :param int y0:
            The y position of the start point.

        :param int z0:
            The z position of the start point.

        :param int length:
            The length of the x + -direction and z + -direction.
            
        :param int coefficience:
            The scale factor
              
        :param int blockType:
            The block id.

        :param int blockData:
            The block data value, defaults to ``0``.
        """

        for x in range(-length,length):
            for z in range(-length,length):
                if x!=0 or z!=0:
                    y=math.log10(x**2+z**2)*1000.0/coefficience
                    self.mc.setBlock(x0+x,y0+y,z0+z,blockType,blockData)

    
    def drawCurve6(self, x0, y0, z0, length, coefficience, blockType, blockData=0):
        """
        :param int x0:
            The x position of the start point.

        :param int y0:
            The y position of the start point.

        :param int z0:
            The z position of the start point.

        :param int length:
            The length of the x + -direction and z + -direction.
            
        :param int coefficience:
            The scale factor
              
        :param int blockType:
            The block id.

        :param int blockData:
            The block data value, defaults to ``0``.
        """

        for x in range(-length,length):
            for z in range(-length,length):
                if x!=0 or z!=0:
                    y=math.cos((x+z)*math.pi/180)*1000.0/coefficience
                    self.mc.setBlock(x0+x,y0+y,z0+z,blockType,blockData)
