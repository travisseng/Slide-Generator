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
<!-- backgroundColor: white -->
<!-- _class: lead -->

 # Interior Schwarzschild metric

---
<style scoped>p,li {font-size:0.92em}</style>

 # Introduction
- The Interior Schwarzschild Metric is a solution to the Einstein Field Equations that describes the gravitational field of a spherically symmetric, non-rotating mass.
- It is named after Karl Schwarzschild, who first discovered it in 1916.


---
<style scoped>p,li {font-size:0.84em}</style>

 # **Mathematics**
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- The Interior Schwarzschild Metric is given by the line element:

ds^2 = e^(km/r) dt^2 - dr^2 / (1-2GM/r) - r^2 dΩ^2

where k = 0, 1, or 2 represents different types of matter distributions.
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/3D_Spherical.svg/220px-3D_Spherical.svg.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.84em}</style>

 # Other Formulations
- The Interior Schwarzschild Metric can also be written in isotropic coordinates:

ds^2 = e^(km/r) (dt^2 - dr^2) - r^2 dΩ^2

or in harmonic coordinates:

ds^2 = e^(km/r) (dt^2 + dr^2) - r^2 dΩ^2


---
<style scoped>p,li {font-size:0.88em}</style>

 # Properties
- The Interior Schwarzschild Metric describes a region of spacetime that is bounded by an event horizon, which marks the boundary between the interior of the object and the exterior.
- The metric has a singularity at r = 0, which represents the center of the object.
- The metric is stationary and axisymmetric, meaning that it does not change over time or under rotations around the object's symmetry axis.


---
<style scoped>p,li {font-size:0.76em}</style>

 # Volume, Density, Pressure

- The volume of a sphere with radius r is given by:

V = (4/3) \* π \* r^3
- The density of a perfect fluid inside the sphere is given by:

ρ = (1 - 2GM/r) / (r^3)
- The pressure of the fluid is given by:

P = (-2GM/r^3) \* ρ

---
<style scoped>p,li {font-size:0.88em}</style>

 # Stability, Redshift, Visualization
- The Interior Schwarzschild Metric describes a stable region of spacetime that is characterized by a redshift of light emitted from the interior.
- The redshift can be visualized as a gravitational blue shift of light emitted from the event horizon.
- The metric can be visualized using ray-tracing techniques, which allow us to see how light behaves inside the spacetime.


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Examples_
- The Interior Schwarzschild Metric is commonly used to describe the gravitational field of a star or a black hole.
- It has also been applied to the study of neutron stars, white dwarfs, and other compact objects.


---
<style scoped>p,li {font-size:0.88em}</style>

 # _History_

- The Interior Schwarzschild Metric was first discovered by Karl Schwarzschild in 1916.
- Since then, it has been extensively studied and applied to a variety of astrophysical problems.

I hope this helps! Let me know if you have any questions or need further clarification on any of the topics.