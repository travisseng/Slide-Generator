---
marp: true
math: katex
theme: default
paginate: True
style: |
   @import url('https://unpkg.com/tailwindcss@2.2.19/dist/utilities.min.css');
   section {display: flex;flex-flow: column; font-size:35px; letter-spacing:1.4px;}

   header {overflow:visible} header > img.logo {position:absolute; right:15px;}

   header > img.logo {position:absolute; right:15px;}


---
<!-- backgroundImage: url('backgrounds/aaabstract (4).png') -->
<!-- _class: lead -->

 # Unit normal

---
<style scoped>p,li {font-size:0.92em}</style>

 # Introduction
- Brief overview of the topic of unit normals in 3D space
- Importance of understanding unit normals in computer graphics, computer vision, and other fields


---
<style scoped>p,li {font-size:0.88em}</style>

 # Normal to Surfaces in 3D Space
- Definition of a surface normal: a vector that is perpendicular to a surface at a given point
- Explanation of how surface normals are used to represent the orientation of a surface in 3D space
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Normal_vectors_on_a_curved_surface.svg/310px-Normal_vectors_on_a_curved_surface.svg.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.84em}</style>

 # _Calculating a Surface Normal_

- Methods for calculating surface normals, including:

+ Dot product of the surface position and a tangent vector at a point on the surface

+ Cross product of two tangent vectors at a point on the surface

+ Other methods, such as using texture coordinates or gradient descent

---
<style scoped>p,li {font-size:0.80em}</style>

 # Choice of Normal
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Surface_normals.svg/300px-Surface_normals.svg.png'/>
</div>
</div>

- Discussion of the different choices for the direction of the surface normal, including:

+ Outward-facing normal (default choice)

+ Inward-facing normal (used in some applications where the surface is being swept inward)

+ Other choices, such as using the gradient of a function to determine the surface normal

---
<style scoped>p,li {font-size:0.84em}</style>

 # **Transforming Normals**

- Explanation of how surface normals are transformed when the coordinate system changes, including:

+ Rotations and translations of the surface

+ Changes in the scale or orientation of the surface

+ Other transformations, such as shearing or stretching

---
<style scoped>p,li {font-size:0.92em}</style>

 # Hypersurfaces in n-Dimensional Space

- Definition of a hypersurface: a surface in an n-dimensional space
- Explanation of how surface normals are used to represent the orientation of hypersurfaces in n-dimensional space

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Varieties Defined by Implicit Equations in n-Dimensional Space_
- Definition of a variety: a set of points in an n-dimensional space that satisfy an equation
- Explanation of how surface normals can be used to represent the orientation of varieties defined by implicit equations in n-dimensional space


---
<style scoped>p,li {font-size:0.84em}</style>

 # Example
- Use of unit normals in a specific example, such as:

+ Calculating the normal to a surface in 3D space

+ Representing the orientation of a hypersurface in n-dimensional space

+ Other examples, such as using surface normals to compute the curvature of a surface


---
<style scoped>p,li {font-size:0.80em}</style>

 # _Uses of Unit Normals_

- Discussion of the various applications of unit normals, including:

+ Computer graphics and computer animation

+ Computer vision and image processing

+ Robotics and machine learning

+ Other fields where unit normals are used, such as physics or engineering

---
<style scoped>p,li {font-size:0.92em}</style>

 # Normal in Geometric Optics
- Explanation of how surface normals are used in geometric optics to describe the orientation of light rays and other objects in 3D space
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Reflection_angles.svg/170px-Reflection_angles.svg.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Conclusion_
- Summary of the main points covered in the presentation
- Final thoughts on the importance of unit normals in computer graphics, computer vision, and other fields.
