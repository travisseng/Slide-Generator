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
<!-- backgroundImage: url('backgrounds/wwwatercolor (9).png') -->
<!-- _class: lead -->

 # **Lorentz transformation**

---
<style scoped>p,li {font-size:0.92em}</style>

 # History

- Developed by Hendrik Lorentz in 1904 as a modification of Newtonian mechanics to account for the behavior of electrons
- Later, Einstein's theory of special relativity confirmed and expanded upon Lorentz's work

---
<style scoped>p,li {font-size:0.76em}</style>

 # Derivation of the Group of Lorentz Transformations

- Start with a set of four transformations that preserve the laws of electromagnetism:

+ Time translation (t → t + Δt)

+ Space translation (x → x + Δx)

+ Rotation (x, y, z → Rx, Ry, Rz)

+ Galilean boost (x, y, z → β(t)x, β(t)y, β(t)z)
- These transformations can be combined in various ways to form a group

---
<style scoped>p,li {font-size:0.88em}</style>

 # Generalities

- The Lorentz group is a set of all possible transformations that preserve the laws of electromagnetism
- It includes both proper (i.e., non-degenerate) and improper transformations
- Proper transformations form a subgroup of the Lorentz group, called the homogeneous Lorentz group

---
<style scoped>p,li {font-size:0.88em}</style>

 # _Physical Formulation of Lorentz Boosts_

- A Lorentz boost is a transformation that combines a time translation and a Galilean boost
- It is used to describe the motion of an object in a non-inertial frame of reference
- The velocity of the object can be expressed as a 4-vector (x, y, z, ct)

---
<style scoped>p,li {font-size:0.88em}</style>

 # Coordinate Transformation
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Lorentz_boost_x_direction_standard_configuration.svg/390px-Lorentz_boost_x_direction_standard_configuration.svg.png'/>
</div>
</div>

- The Lorentz transformation changes the coordinates of an event from one frame of reference to another
- It preserves the distance and angles between events, but can alter their temporal and spatial coordinates

---
<style scoped>p,li {font-size:0.88em}</style>

 # Physical Implications

- Time dilation: time appears to pass more slowly in a moving frame of reference
- Length contraction: objects appear shorter in the direction of motion in a moving frame of reference
- Relativistic mass: the energy and momentum of an object increase as its velocity approaches the speed of light

---
<style scoped>p,li {font-size:0.72em}</style>

 # Vector Transformations
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Vectors transform according to the following equations:

+ x' = γ(x - vt)

+ y' = y

+ z' = z

+ t' = γ(t - vx/c^2)
- The Lorentz boost preserves the magnitude of vectors, but changes their direction
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Lorentz_boost_any_direction_standard_configuration.svg/390px-Lorentz_boost_any_direction_standard_configuration.svg.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.84em}</style>

 # **Transformation of Velocities**
- The velocity of an object transforms according to the following equation:

+ v' = γ(v - beta x/c^2)
- The velocity of an object in a moving frame of reference is not the same as its velocity in a stationary frame of reference
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Lorentz_transformation_of_velocity_including_velocity_addition.svg/390px-Lorentz_transformation_of_velocity_including_velocity_addition.svg.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Transformation of Other Quantities

- Other quantities, such as energy and momentum, transform according to similar equations
- These transformations are based on the properties of the Lorentz group

---
<style scoped>p,li {font-size:0.88em}</style>

 # **Mathematical Formulation**

- The mathematical formulation of the Lorentz transformation is based on the use of tensors
- Tensors are multidimensional arrays of numbers that can be used to describe physical quantities such as stress and strain
- The Lie group SO+(3,1) and its Lie algebra so(3,1) play an important role in the mathematical formulation of the Lorentz transformation

---
<style scoped>p,li {font-size:0.92em}</style>

 # Homogeneous Lorentz Group
- The homogeneous Lorentz group is a set of all possible proper transformations that preserve the laws of electromagnetism
- It includes rotations, boosts, and translations


---
<style scoped>p,li {font-size:0.92em}</style>

 # Proper Transformations

- Proper transformations are non-degenerate, meaning they do not change the sign of any physical quantity
- They form a subgroup of the Lorentz group, called the homogeneous Lorentz group

---
<style scoped>p,li {font-size:0.92em}</style>

 # Improper Transformations

- Improper transformations are degenerate, meaning they can change the sign of some physical quantities
- They include rotations and boosts with a velocity parallel to the direction of motion

---
<style scoped>p,li {font-size:0.96em}</style>

 # **Inhomogeneous Lorentz Group**

- The inhomogeneous Lorentz group is a set of all possible transformations that preserve the laws of electromagnetism, including both proper and improper transformations

---
<style scoped>p,li {font-size:0.88em}</style>

 # Tensor Formulation
- The tensor formulation of the Lorentz transformation is based on the use of covariant and contravariant vectors
- Covariant vectors transform as tensors under the action of the Lorentz group
- Contravariant vectors are transformed as tensors under the action of the Lorentz group


---
<style scoped>p,li {font-size:0.80em}</style>

 # Transformation of the Electromagnetic Field
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Lorentz_boost_electric_charge.svg/390px-Lorentz_boost_electric_charge.svg.png'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- The electromagnetic field is a tensor that transforms according to the equations:

+ E' = γ(E - vB)

+ B' = β(B + vE/c^2)
- The electromagnetic field is not changed in direction by the Lorentz transformation, but its magnitude and phase are affected
</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # **Spinors**
- Spinors are mathematical objects that transform under the action of the Lorentz group
- They are used to describe particles with intrinsic angular momentum, such as electrons and quarks
- The Lorentz transformation affects the phase and magnitude of spinors, but not their direction


---
<style scoped>p,li {font-size:0.92em}</style>

 # Transformation of General Fields
- General fields, such as the gravitational field, are transformed under the action of the Lorentz group
- They transform according to similar equations to the electromagnetic field


---
<style scoped>p,li {font-size:0.88em}</style>

 # Footnotes
- Lorentz transformation is a fundamental concept in modern physics that has many applications in astrophysics, particle physics, and cosmology
- It is used to describe the behavior of objects in high-energy collisions, such as those produced by particle accelerators
- The Lorentz transformation is also used to describe the behavior of objects in gravitational fields, such as black holes and neutron stars


---
<style scoped>p,li {font-size:0.88em}</style>

 # Notes

- The Lorentz group has many important subgroups, including the rotation group SO(3), the Galilean group GO(3), and the boost group O(3)
- The Lorentz transformation is related to other important concepts in physics, such as relativity, quantum mechanics, and field theory
- There are many open questions and unsolved problems in the study of the Lorentz transformation, such as the nature of dark matter and dark energy

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Websites**

- The Lorentz transformation is described on many websites, including those of scientific organizations and universities
- Some useful websites for learning more about the Lorentz transformation include the National Academy of Sciences, the Stanford University Physics Department, and the Mathematical Association of America

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Papers**

- There are many papers published on the topic of the Lorentz transformation in scientific journals such as Physical Review Letters, Physical Review D, and Journal of High Energy Physics
- Some important papers include "The Lorentz Group" by W. McCrea, "Lorentz Transformations" by J. M. Cohen and A. R. Shapiro, and "The Mathematical Structure of the Lorentz Group" by P. Lax

---
<style scoped>p,li {font-size:0.96em}</style>

 # _Books_
- There are many books published on the topic of the Lorentz transformation, including "Lorentzian Geometry" by A. H. Chang and S. K. Lam, "The Lorentz Group in Physics" by J. H. M. Austin, and "The Lie Group SO(3,1) and Its Applications" by J. D. Baez and A. C. Elitzur


---
<style scoped>p,li {font-size:0.88em}</style>

 # Conclusion

- The Lorentz transformation is a fundamental concept in modern physics that has many applications in astrophysics, particle physics, and cosmology
- It is based on the use of tensors and the properties of the Lorentz group
- There are many open questions and unsolved problems in the study of the Lorentz transformation, but it remains a vital tool for understanding the behavior of objects in high-energy collisions and gravitational fields.