# minecraftshape
the interesting shape python function in minecraft

usage:
   from minecraftShape import MinecraftMath2DShape
   from minecraftShape import MinecraftMath3DShape

function index:
   MinecraftMath2DShape
1.drawPeach(self, x0, y0, z0, length, coefficience, blockType, blockData=0)
     param:
       x0-------------The x position of the start point.
       y0-------------The y position of the start point.
       z0-------------The z position of the start point.
       length---------- The length of the x + -direction, z + -direction.
       coefficience---The scale factor 
       blockType------The block id.
       blockData------The block data value, defaults to ``0``.
     Fomula:
       r= sin(theta)+  sin(theta)^3,(0< theta <2Pi)
       
       x=cos(theta) *length/coefficience
       z=sin(theta) *length/coefficience
      




   MinecraftMath3DShape
 1.drawCurve1(self, x0, y0, z0, length, coefficience, blockType, blockData=0)
     param:
       x0-------------The x position of the start point.
       y0-------------The y position of the start point.
       z0-------------The z position of the start point.
       length---------The length of the x direction and z direction.
       coefficience---The scale factor 
       blockType------The block id.
       blockData------The block data value, defaults to ``0``.
     Fomula:
       y=(x^2 + z^2)/coefficience

 2.drawCurve1(self, x0, y0, z0, length, coefficience, blockType, blockData=0)
     param:
       x0-------------The x position of the start point.
       y0-------------The y position of the start point.
       z0-------------The z position of the start point.
       length---------The length of the x direction and z direction.
       coefficience---The scale factor 
       blockType------The block id.
       blockData------The block data value, defaults to ``0``.
     Fomula:
       y=(x^2 - z^2)/coefficience

3.drawCurve3(self, x0, y0, z0, length, coefficience, blockType, blockData=0)
     param:
       x0-------------The x position of the start point.
       y0-------------The y position of the start point.
       z0-------------The z position of the start point.
       length---------The length of the x direction and z direction.
       coefficience---The scale factor 
       blockType------The block id.
       blockData------The block data value, defaults to ``0``.
     Fomula:
       y=((x/y)^2 + (y/x)^2)/coefficience

4.drawCurve4(self, x0, y0, z0, length, coefficience, blockType, blockData=0)
     param:
       x0-------------The x position of the start point.
       y0-------------The y position of the start point.
       z0-------------The z position of the start point.
       length---------The length of the x direction and z direction.
       coefficience---The scale factor 
       blockType------The block id.
       blockData------The block data value, defaults to ``0``.
     Fomula:
       y=tan((x^2 + y^2) *Pi/180) /coefficience

5.drawCurve5(self, x0, y0, z0, length, coefficience, blockType, blockData=0)
     param:
       x0-------------The x position of the start point.
       y0-------------The y position of the start point.
       z0-------------The z position of the start point.
       length---------The length of the x direction and z direction.
       coefficience---The scale factor 
       blockType------The block id.
       blockData------The block data value, defaults to ``0``.
     Fomula:
       y=log10(x^2 + y^2)*1000.0/coefficience

6.drawCurve6(self, x0, y0, z0, length, coefficience, blockType, blockData=0)
     param:
       x0-------------The x position of the start point.
       y0-------------The y position of the start point.
       z0-------------The z position of the start point.
       length---------The length of the x direction and z direction.
       coefficience---The scale factor 
       blockType------The block id.
       blockData------The block data value, defaults to ``0``.
     Fomula:
       y=cos(x + y)*1000.0/coefficience

7.drawCurve7(self, x0, y0, z0, length, coefficience, blockType, blockData=0)
     param:
       x0-------------The x position of the start point.
       y0-------------The y position of the start point.
       z0-------------The z position of the start point.
       length---------The length of the x direction and z direction.
       coefficience---The scale factor 
       blockType------The block id.
       blockData------The block data value, defaults to ``0``.
     Fomula:
       y=cos(x^2 + y^2)*1000.0/coefficience

8.drawMobius(self, x0, y0, z0, width, coefficience, blockType, blockData=0)
     param:
       x0-------------The x position of the start point.
       y0-------------The y position of the start point.
       z0-------------The z position of the start point.
       width----------The width of Mobius band.
       coefficience---The scale factor 
       blockType------The block id.
       blockData------The block data value, defaults to ``0``.
     Fomula:
       x=Cos[t]*(3+r Cos[t/2])*1000.0/coefficience
       y=Sin[t]*(3+r Cos[t/2])*1000.0/coefficience
       z=r*Sin[t/2]*1000.0/coefficience
         ( -width<r<width,0<t<2Pi )


9.drawSphere1(self, x0, y0, z0, length, coefficience, blockType, blockData=0)
     param:
       x0-------------The x position of the start point.
       y0-------------The y position of the start point.
       z0-------------The z position of the start point.
       length---------- The length of the x + -direction, z + -direction and y + -direction.
       coefficience---The scale factor 
       blockType------The block id.
       blockData------The block data value, defaults to ``0``.
     Fomula:
       r=(3 * (sin(alpha))^2 * cos(alpha) * sin(theta)*cos(theta))^(1/3), (0< alpha <Pi/2,0< theta <Pi/2)
       
       x=r * sin(alpha) * cos(theta) *length/coefficience
       z=r * sin(alpha) * sin(theta) *length/coefficience
       y=r * cos(alpha) *length/coefficience
