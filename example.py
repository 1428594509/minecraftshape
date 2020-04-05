import mcpi.minecraft as minecraft
import mcpi.block as block
#from minecraftshape import MinecraftMath3DShape
from minecraftshape import MinecraftMath2DShape
import time
 

 
# 连接到游戏
 
mc = minecraft.Minecraft.create()

#mathshape = MinecraftMath3DShape(mc)
mathshape = MinecraftMath2DShape(mc)

 
Middle = mc.player.getTilePos()


LENGTH=5
mathshape.drawPeach(Middle.x, Middle.y, Middle.z,LENGTH, 1,block.DIAMOND_BLOCK.id)
#mathshape.drawPeach(Middle.x, Middle.y, Middle.z,LENGTH, 1,block.AIR.id)



#LENGTH=50
#mathshape.drawCurve1(Middle.x, Middle.y, Middle.z,LENGTH, 100,block.DIAMOND_BLOCK.id)
#mathshape.drawCurve1(Middle.x, Middle.y, Middle.z,LENGTH, 100,block.AIR.id)

#LENGTH=50
#mathshape.drawCurve2(Middle.x, Middle.y+20, Middle.z,LENGTH, 100,block.DIAMOND_BLOCK.id)
#mathshape.drawCurve2(Middle.x, Middle.y+20, Middle.z,LENGTH, 100,block.AIR.id)

#LENGTH=50
#mathshape.drawCurve3(Middle.x, Middle.y+20, Middle.z,LENGTH, 100,block.DIAMOND_BLOCK.id)
#mathshape.drawCurve3(Middle.x, Middle.y+20, Middle.z,LENGTH, 100,block.AIR.id)

#LENGTH=50
#mathshape.drawCurve4(Middle.x, Middle.y+50, Middle.z,LENGTH, 100,block.DIAMOND_BLOCK.id)
#mathshape.drawCurve4(Middle.x, Middle.y+50, Middle.z,LENGTH, 100,block.AIR.id)

#LENGTH=50
#mathshape.drawCurve5(Middle.x, Middle.y, Middle.z,LENGTH, 100,block.DIAMOND_BLOCK.id)
#mathshape.drawCurve5(Middle.x, Middle.y, Middle.z,LENGTH, 100,block.AIR.id)

#LENGTH=50
#mathshape.drawCurve6(Middle.x, Middle.y, Middle.z,LENGTH, 100,block.DIAMOND_BLOCK.id)
#mathshape.drawCurve6(Middle.x, Middle.y, Middle.z,LENGTH, 100,block.AIR.id)

#LENGTH=50
#mathshape.drawCurve7(Middle.x, Middle.y, Middle.z,LENGTH, 100,block.DIAMOND_BLOCK.id)
#mathshape.drawCurve7(Middle.x, Middle.y, Middle.z,LENGTH, 100,block.AIR.id)

#WIDTH=5
#mathshape.drawMobius(Middle.x, Middle.y, Middle.z,WIDTH, 100,block.DIAMOND_BLOCK.id)
#mathshape.drawMobius(Middle.x, Middle.y, Middle.z,WIDTH, 100,block.AIR.id)

#LENGTH=100
#mathshape.drawSphere1(Middle.x, Middle.y, Middle.z,LENGTH, 1,block.DIAMOND_BLOCK.id)
#mathshape.drawSphere1(Middle.x, Middle.y, Middle.z,LENGTH, 1,block.AIR.id)


#if buried,just shuttle
#mc.player.setTilePos(Middle.x+400,Middle.y,Middle.z+400)
