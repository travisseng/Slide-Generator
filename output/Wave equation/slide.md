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

 # Wave equation

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Introduction**

- The wave equation is a fundamental equation in the study of wave propagation
- It describes the evolution of a wave field in space and time

---
<style scoped>p,li {font-size:0.84em}</style>

 # _Wave Equation in One Space Dimension_
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Alembert.jpg/220px-Alembert.jpg'/>
</div>
</div>

- The wave equation in one space dimension can be written as:

$$ \frac{\partial^2 \psi}{\partial x^2} - \frac{1}{c^2} \frac{\partial^2 \psi}{\partial t^2} = 0 $$

where $\psi$ is the wave field, $x$ is the spatial coordinate, $t$ is time, and $c$ is the speed of the wave.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Derivation of the Wave Equation
- The wave equation can be derived from Hooke's law for springs
- Hooke's law states that the force on a spring is proportional to its displacement


---
<style scoped>p,li {font-size:0.92em}</style>

 # From Hooke's Law
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/1d_wave_equation_animation.gif/220px-1d_wave_equation_animation.gif'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- The wave equation can be obtained by taking the derivative of Hooke's law with respect to time
</div>

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Stress Pulse in a Bar_

- A stress pulse is a disturbance that propagates along a bar
- The wave equation can be used to describe the propagation of stress pulses in a bar

---
<style scoped>p,li {font-size:0.92em}</style>

 # General Solution

- The general solution of the wave equation is a superposition of plane waves
- Plane waves are solutions of the wave equation that have a constant phase velocity

---
<style scoped>p,li {font-size:0.92em}</style>

 # Algebraic Approach

- The algebraic approach involves solving the wave equation using algebraic techniques
- This can be useful for solving problems with complex boundary conditions

---
<style scoped>p,li {font-size:0.92em}</style>

 # Plane-Wave Eigenmodes

- Plane-wave eigenmodes are special solutions of the wave equation that have a constant frequency and wavelength
- They are useful for studying the properties of wave propagation in simple systems.

---
<style scoped>p,li {font-size:0.84em}</style>

 # Vectorial Wave Equation in Three Space Dimensions

- The vectorial wave equation describes the propagation of waves in three space dimensions
- It can be written as:

$$ \frac{\partial^2 \mathbf{u}}{\partial x^2} - \frac{1}{c^2} \frac{\partial^2 \mathbf{u}}{\partial t^2} = 0 $$

where $\mathbf{u}$ is the wave field, $x$ is the spatial coordinate, $t$ is time, and $c$ is the speed of the wave.

---
<style scoped>p,li {font-size:0.80em}</style>

 # _Scalar Wave Equation in Three Space Dimensions_
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Leonhard_Euler_2.jpg/220px-Leonhard_Euler_2.jpg'/>
</div>
</div>

- The scalar wave equation describes the propagation of waves in three space dimensions
- It can be written as:

$$ \frac{\partial^2 \psi}{\partial x^2} - \frac{1}{c^2} \frac{\partial^2 \psi}{\partial t^2} = 0 $$

where $\psi$ is the wave field, $x$ is the spatial coordinate, $t$ is time, and $c$ is the speed of the wave.

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Spherical Waves_
- Spherical waves are solutions of the wave equation that have a spherical symmetry
- They are useful for studying the properties of wave propagation in three-dimensional systems.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Example

- An example of the wave equation in action is the study of seismic waves in the Earth's interior
- Seismic waves are generated by earthquakes and can be used to study the structure of the Earth's interior.

---
<style scoped>p,li {font-size:0.88em}</style>

 # **Monochromatic Spherical Wave**
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Spherical_Wave.gif/220px-Spherical_Wave.gif'/>
</div>
</div>

- A monochromatic spherical wave is a solution of the wave equation that has a constant frequency and wavelength
- It can be used to study the properties of wave propagation in simple systems.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Solution of a General Initial-Value Problem
- The solution of a general initial-value problem for the wave equation is a superposition of plane waves
- The superposition can be obtained by solving the wave equation with the appropriate boundary conditions.


---
<style scoped>p,li {font-size:0.88em}</style>

 # **Scalar Wave Equation in Two Space Dimensions**
- The scalar wave equation in two space dimensions can be written as:

$$ \frac{\partial^2 \psi}{\partial x^2} - \frac{1}{c^2} \frac{\partial^2 \psi}{\partial t^2} = 0 $$

where $\psi$ is the wave field, $x$ is the spatial coordinate, $t$ is time, and $c$ is the speed of the wave.


---
<style scoped>p,li {font-size:0.88em}</style>

 # Scalar Wave Equation in General Dimension

- The scalar wave equation in general dimension can be written as:

$$ \frac{\partial^2 \psi}{\partial x^n}^2 - \frac{1}{c^2} \frac{\partial^2 \psi}{\partial t^m}^2 = 0 $$

where $\psi$ is the wave field, $x$ is the spatial coordinate, $t$ is time, $n$ and $m$ are integers greater than or equal to one, and $c$ is the speed of the wave.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Kirchhoff's Formulas
- Kirchhoff's formulas are used to calculate the boundary values of the wave field at a surface
- They are useful for studying the reflection and transmission of waves at boundaries between two media.


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Odd Dimensions**

- In odd dimensions, the wave equation has no solutions that are periodic in space and time
- This means that there can be no standing waves in odd dimensions.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Even Dimensions

- In even dimensions, the wave equation has solutions that are periodic in space and time
- This means that there can be standing waves in even dimensions.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Problems with Boundaries

- When studying wave propagation in systems with boundaries, it is important to consider the reflection and transmission of waves at the boundary
- This can be done using Kirchhoff's formulas.

---
<style scoped>p,li {font-size:0.92em}</style>

 # One Space Dimension

- In one space dimension, the wave equation has a simple solution that involves a step function
- This solution can be used to study the propagation of waves in simple systems.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Reflection and Transmission at the Boundary of Two Media
- When a wave reaches the boundary between two media with different properties, it can be reflected or transmitted
- The reflection and transmission coefficients can be calculated using Kirchhoff's formulas.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Sturm–Liouville Formulation

- The wave equation can be formulated as a Sturm–Liouville problem
- This can be useful for studying the properties of wave propagation in systems with boundaries.

---
<style scoped>p,li {font-size:0.68em}</style>

 # Investigation by Numerical Methods
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/String_wave_0.svg/512px-String_wave_0.svg.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/String_wave_1.svg/600px-String_wave_1.svg.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/String_wave_2.svg/600px-String_wave_2.svg.png'/>
</div>
</div>
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/String_wave_3.svg/600px-String_wave_3.svg.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/String_wave_4.svg/600px-String_wave_4.svg.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/String_wave_5.svg/600px-String_wave_5.svg.png'/>
</div>
</div>

- The wave equation can be solved numerically using methods such as the finite difference method or the finite element method
- These methods can be useful for studying the properties of wave propagation in complex systems.

---
<style scoped>p,li {font-size:0.88em}</style>

 # Several Space Dimensions
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- In several space dimensions, the wave equation has more complicated solutions that involve multiple plane waves
- These solutions can be used to study the properties of wave propagation in complex systems.
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Drum_vibration_mode12.gif/220px-Drum_vibration_mode12.gif'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.84em}</style>

 # Inhomogeneous Wave Equation in One Dimension
- The inhomogeneous wave equation in one dimension describes the propagation of waves in a medium with variable properties
- It can be written as:

$$ \frac{\partial^2 \psi}{\partial x^2} - \frac{1}{c(x)^2} \frac{\partial^2 \psi}{\partial t^2} = 0 $$

where $\psi$ is the wave field, $x$ is the spatial coordinate, $t$ is time, and $c(x)$ is the speed of the wave at the point $x$.


---
<style scoped>p,li {font-size:0.88em}</style>

 # Wave Equation for Inhomogeneous Media in Three Dimensions
- The wave equation for inhomogeneous media in three dimensions can be written as:

$$ \frac{\partial^2 \mathbf{u}}{\partial x^2} - \frac{1}{c(x,y,z)^2} \frac{\partial^2 \mathbf{u}}{\partial t^2} = 0 $$

where $\mathbf{u}$ is the wave field, $x$ is the spatial coordinate, $y$ and $z$ are the other spatial coordinates, $t$ is time, and $c(x,y,z)$ is the speed of the wave at the point $(x,y,z)$.


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Other Coordinate Systems**

- The wave equation can be solved in other coordinate systems, such as cylindrical or spherical coordinates
- These coordinate systems can be useful for studying the properties of wave propagation in systems with symmetry.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Further Generalizations
- The wave equation can be further generalized to include nonlinear effects and other physical phenomena
- These generalizations can be useful for studying complex systems that cannot be described by linear equations.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Elastic Waves

- Elastic waves are waves that propagate through a medium by disturbing the elastic properties of the medium
- They can be studied using the wave equation and other mathematical techniques.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Dispersion Relation

- The dispersion relation is a mathematical relationship between the frequency and wavelength of a wave
- It can be used to study the properties of wave propagation in different media.

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Notes**

- Wave propagation is an important area of research in physics and engineering
- The wave equation is a fundamental tool for studying wave propagation in different systems.