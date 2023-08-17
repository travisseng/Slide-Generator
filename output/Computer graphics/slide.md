---
marp: true
math: katex
theme: gaia
paginate: True
style: |
   @import url('https://unpkg.com/tailwindcss@2.2.19/dist/utilities.min.css');
   section {display: flex;flex-flow: column; font-size:35px; letter-spacing:1.4px;}

   header {overflow:visible} header > img.logo {position:absolute; right:15px;}

   header > img.logo {position:absolute; right:15px;}


---
<!-- backgroundColor: #838494 -->
<!-- _class: lead -->

 # Computer graphics

---
<style scoped>p,li {font-size:0.88em}</style>

 # Overview
- Computer graphics are images and animations created using computers
- Involve a combination of software, hardware, and techniques
- Used in various fields such as movies, video games, architecture, and scientific visualization


---
<style scoped>p,li {font-size:0.88em}</style>

 # _History_
- Early beginnings in the 1950s with experimental computer graphics
- Development of graphics software and hardware in the 1960s and 1970s
- Widespread use of computer graphics in the 1980s and 1990s with the rise of video games and computer-aided design


---
<style scoped>p,li {font-size:0.88em}</style>

 # 1950s
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/SAGE_control_room.png/220px-SAGE_control_room.png'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Early experiments in computer graphics, such as the "NURBS" (Non-uniform rational B-spline) algorithm developed by Paul de Castelnau
- First computer-generated animations, such as the "Dragon" animation created by William Fetter and Robert C. Fletcher
</div>

</div>


---
<style scoped>p,li {font-size:0.80em}</style>

 # **1960s**
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Spacewar%21-PDP-1-20070512.jpg/220px-Spacewar%21-PDP-1-20070512.jpg'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Pong.png/170px-Pong.png'/>
</div>
</div>

- Development of graphics software, such as Sketchpad (1963) and GRASS (1967)
- Increased use of computer graphics in education, research, and industry
- Emergence of vector graphics and the first pixel art algorithms

---
<style scoped>p,li {font-size:0.88em}</style>

 # 1970s
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Utah_teapot.png/250px-Utah_teapot.png'/>
</div>
</div>

- Continued advancements in graphics software and hardware, such as the introduction of 3D graphics and the first computer-aided design (CAD) systems
- Increased use of computer graphics in movies and television, such as the 1972 film "A Computer Animated Hand"

---
<style scoped>p,li {font-size:0.84em}</style>

 # 1980s
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Widespread use of computer graphics in video games and home computers
- Development of pixel art and sprite graphics
- Emergence of 3D modeling and animation techniques, such as the "ray tracing" algorithm
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Donkey_Kong_arcade_at_the_QuakeCon_2005.png/170px-Donkey_Kong_arcade_at_the_QuakeCon_2005.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # **1990s**
- Continued advancements in 3D graphics and rendering techniques, such as the introduction of "global illumination" and "physically-based rendering"
- Increased use of computer graphics in fields such as architecture, product design, and scientific visualization
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Quarxs-Affiche.jpg/175px-Quarxs-Affiche.jpg'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # 2000s
- Continued advancements in 3D graphics and rendering techniques, such as the introduction of "real-time ray tracing" and "subsurface scattering"
- Increased use of computer graphics in fields such as virtual reality, augmented reality, and computer-aided design
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Killing_Floor_Biohazard1.jpg/260px-Killing_Floor_Biohazard1.jpg'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # 2010s
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Physically_Based_Rendering_Sample_2.png/220px-Physically_Based_Rendering_Sample_2.png'/>
</div>
</div>

- Emergence of generative machine-learning models for computer graphics, such as "Generative Adversarial Networks" (GANs) and "Variational Autoencoders" (VAEs)
- Increased use of computer graphics in fields such as film and television, video games, and virtual reality

---
<style scoped>p,li {font-size:0.92em}</style>

 # Image Types
- Two-dimensional (2D) images, such as pixel art and sprite graphics
- Three-dimensional (3D) models and animations, such as computer animation and 3D modeling


---
<style scoped>p,li {font-size:0.92em}</style>

 # Two-Dimensional Graphics
- Pixel art, which uses a grid of pixels to create an image
- Sprite graphics, which use a combination of pixels and vector graphics to create an image


---
<style scoped>p,li {font-size:0.92em}</style>

 # Three-Dimensional Graphics
- Computer animation, which uses a series of 3D models and animations to create a moving image
- 3D modeling, which creates three-dimensional models using techniques such as "polygon modeling" and "point cloud modeling"


---
<style scoped>p,li {font-size:0.88em}</style>

 # _Vector Graphics_
- Use vectors (lines and curves) to create images, rather than pixels
- Can be used for both two-dimensional and three-dimensional graphics
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Bitmap_VS_SVG.svg/200px-Bitmap_VS_SVG.svg.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # **Generative Machine-Learning Models**
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/An_astronaut_riding_a_horse_%28Hiroshige%29_2022-08-30.png/200px-An_astronaut_riding_a_horse_%28Hiroshige%29_2022-08-30.png'/>
</div>
</div>

- Use machine-learning algorithms to generate computer graphics, such as "Generative Adversarial Networks" (GANs) and "Variational Autoencoders" (VAEs)
- Can be used for both two-dimensional and three-dimensional graphics

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Pixels**
- The smallest unit of a computer image, made up of a single color and intensity value
- Used to create both two-dimensional and three-dimensional graphics


---
<style scoped>p,li {font-size:0.92em}</style>

 # Primitives

- Basic shapes and objects used to build more complex images and models, such as points, lines, and triangles
- Can be used for both two-dimensional and three-dimensional graphics

---
<style scoped>p,li {font-size:0.88em}</style>

 # Rendering
- The process of generating an image from a computer model, using techniques such as ray tracing and scanline rendering
- Can be used for both two-dimensional and three-dimensional graphics
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Shading1.jpg/220px-Shading1.jpg'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Volume Rendering
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/CTWristImage.png/220px-CTWristImage.png'/>
</div>
</div>

- A technique used to visualize and render 3D models by assigning a density value to each voxel (3D pixel) in the model

---
<style scoped>p,li {font-size:0.96em}</style>

 # 3D Modeling
- The process of creating three-dimensional models using techniques such as polygon modeling, point cloud modeling, and surface reconstruction


---
<style scoped>p,li {font-size:0.96em}</style>

 # Pioneers in Computer Graphics

- People who made significant contributions to the field of computer graphics, such as Ivan Sutherland, Douglas T. Ross, and James B. Blinn

---
<style scoped>p,li {font-size:0.92em}</style>

 # Other Pioneers
- People who made significant contributions to the field of computer graphics, such as John H. Conway, David E. Evans, and Louis M. Brill
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Utah_teapot_simple_2.png/220px-Utah_teapot_simple_2.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.96em}</style>

 # Organizations

- Organizations that have played a significant role in the development and advancement of computer graphics, such as the Association for Computing Machinery (ACM) and the IEEE Computer Society

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Study of Computer Graphics**
- The study of computer graphics involves a combination of mathematics, computer science, and art
- Includes topics such as geometry, lighting, shading, and rendering


---
<style scoped>p,li {font-size:0.96em}</style>

 # Applications
- Computer graphics are used in a wide range of fields, including film and television, video games, architecture, product design, and scientific visualization


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Notes**
- Computer graphics have had a significant impact on society, influencing fields such as entertainment, education, and architecture
- The field of computer graphics continues to evolve and advance with new technologies and techniques being developed all the time.
