---
marp: true
math: katex
theme: uncover
paginate: True
style: |
   @import url('https://unpkg.com/tailwindcss@2.2.19/dist/utilities.min.css');
   section {display: flex;flex-flow: column; font-size:35px; letter-spacing:1.4px;}

   header {overflow:visible} header > img.logo {position:absolute; right:15px;}

   header > img.logo {position:absolute; right:15px;}


---
<!-- backgroundColor: #8e8585 -->
<!-- _class: lead -->

 # Gauss's law for magnetism

---
<style scoped>p,li {font-size:0.92em}</style>

 # Introduction
- Gauss's law for magnetism is a fundamental theorem in the study of magnetic fields
- It relates the magnetic field to the distribution of magnetic charge


---
<style scoped>p,li {font-size:0.88em}</style>

 # **Differential Form**

- The differential form of Gauss's law for magnetism states that:

∇ · B = μ₀ (∂B/∂t) + ∫∇ × B d^3r' / |r - r'|
- Here, B is the magnetic field, μ₀ is the magnetic permeability constant, and r' is a point in space

---
<style scoped>p,li {font-size:0.84em}</style>

 # _Integral Form_
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/SurfacesWithAndWithoutBoundary.svg/200px-SurfacesWithAndWithoutBoundary.svg.png'/>
</div>
</div>

- The integral form of Gauss's law for magnetism states that:

∇ × B = μ₀ (J + μ₀ ∂B/∂t)
- Here, J is the magnetic current density, and ∂B/∂t is the time derivative of the magnetic field

---
<style scoped>p,li {font-size:0.84em}</style>

 # _Vector Potential_
- The vector potential A is a mathematical construct that can be used to represent the magnetic field
- It satisfies the equation:

∇ × A = B
- Here, A is the vector potential, and B is the magnetic field


---
<style scoped>p,li {font-size:0.92em}</style>

 # Field Lines
- Field lines are a visualization tool for understanding the direction and magnitude of the magnetic field
- They are defined as the trajectories of particles that have a constant magnetic flux through them


---
<style scoped>p,li {font-size:0.84em}</style>

 # Incorporating Magnetic Monopoles

- Gauss's law for magnetism can be generalized to include magnetic monopoles, which are points with infinite magnetic charge
- The modified law is given by:

∇ · B = μ₀ (∂B/∂t) + ∫∇ × B d^3r' / |r - r'| - ∫δ(r - m) d³m
- Here, m is a magnetic monopole, and δ is the Dirac delta function

---
<style scoped>p,li {font-size:0.92em}</style>

 # History
- Gauss's law for magnetism was first formulated by Carl Friedrich Gauss in the early 19th century
- It has since been widely used in the study of magnetic fields and their applications


---
<style scoped>p,li {font-size:0.92em}</style>

 # Numerical Computation

- Gauss's law for magnetism can be computed numerically using methods such as the finite element method or the finite difference method
- These methods involve discretizing the domain of interest into smaller elements or cells, and solving the equations approximately

---
<style scoped>p,li {font-size:0.88em}</style>

 # Conclusion
- Gauss's law for magnetism is a fundamental tool for understanding magnetic fields and their properties
- It has a wide range of applications in physics, engineering, and other fields

I hope this helps! Let me know if you have any questions or need further clarification.
