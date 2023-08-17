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
<!-- backgroundImage: url('backgrounds/aaabstract (3).png') -->
<!-- _class: lead -->

 # Newton's laws of motion

---
<style scoped>p,li {font-size:0.88em}</style>

 # Prerequisites

- Overview of classical mechanics
- Mathematical preliminaries (calculus, vector algebra)
- Important concepts: inertia, force, momentum, energy

---
<style scoped>p,li {font-size:0.64em}</style>

 # Laws
- First Law: Inertia

+ Objects at rest remain at rest, objects in motion remain in motion

+ Inertial reference frames
- Second Law: Force and Acceleration

+ F = ma (force is equal to mass times acceleration)

+ Relationship between force and momentum
- Third Law: Momentum Conservation

+ Total momentum of a closed system remains constant

+ Momentum is conserved in all directions


---
<style scoped>p,li {font-size:0.88em}</style>

 # **First Law Candidates**

- Heraclitus' concept of "stasis" ( stability)
- Aristotle's concept of "horme" (innate tendency)
- Descartes' concept of "vis inertiae" (inertial force)

---
<style scoped>p,li {font-size:0.88em}</style>

 # Work and Energy

- Work as a transfer of energy
- Types of work: kinetic, potential, total
- Energy conservation: dE/dt = 0 (energy is conserved)

---
<style scoped>p,li {font-size:0.84em}</style>

 # Examples

- Simple harmonic motion
- Gravitational motion
- Projectile motion
- Rotational motion

---
<style scoped>p,li {font-size:0.88em}</style>

 # **Uniformly Accelerated Motion**
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Bouncing_ball_strobe_edit.jpg/290px-Bouncing_ball_strobe_edit.jpg'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Constant acceleration in one direction
- Equations of motion: x(t) = x0 + v0t + (1/2)at^2, etc.
</div>

</div>


---
<style scoped>p,li {font-size:0.84em}</style>

 # **Uniform Circular Motion**
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Constant speed, constant direction
- Centripetal force: F = (mω^2)/r
- Equations of motion: r(t) = r0 + (mω/r0)t, etc.
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/a/ae/Binary_system_orbit_q%3D3_e%3D0.gif'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Harmonic Motion

- Simple harmonic motion as a special case of oscillatory motion
- Sinusoidal position, velocity, and acceleration

---
<style scoped>p,li {font-size:0.88em}</style>

 # **Objects with Variable Mass**
- Rigid-body motion and rotation
- Conservation of momentum in systems with variable mass
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Space_Shuttle_Atlantis_launches_from_KSC_on_STS-132_side_view.jpg/220px-Space_Shuttle_Atlantis_launches_from_KSC_on_STS-132_side_view.jpg'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Rotational Analogues of Newton's Laws

- Angular momentum and its conservation
- Torque and angular velocity

---
<style scoped>p,li {font-size:0.88em}</style>

 # _Multi-Body Gravitational System_
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Three-body_Problem_Animation.gif/220px-Three-body_Problem_Animation.gif'/>
</div>
</div>

- Interaction between multiple objects with mass
- Gravitational potential energy and force

---
<style scoped>p,li {font-size:0.92em}</style>

 # Chaos and Unpredictability
- Complex systems exhibiting chaotic behavior
- Sensitivity to initial conditions


---
<style scoped>p,li {font-size:0.88em}</style>

 # Nonlinear Dynamics
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Demonstrating_Chaos_with_a_Double_Pendulum.gif/220px-Demonstrating_Chaos_with_a_Double_Pendulum.gif'/>
</div>
</div>

- Systems with nonlinear forces or interactions
- Phenomena such as bifurcation, chaos, and self-organization

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Singularities**
- Points where the solution of a differential equation becomes infinite or undefined
- Examples from classical mechanics and other fields


---
<style scoped>p,li {font-size:0.92em}</style>

 # Relation to Other Formulations of Classical Physics

- Lagrangian and Hamiltonian formulations
- Relationship between energy, momentum, and angular momentum

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Lagrangian and Hamiltonian**

- Lagrangian mechanics as an alternative formulation of classical mechanics
- Hamiltonian mechanics and the concept of generalized coordinates

---
<style scoped>p,li {font-size:0.92em}</style>

 # Hamilton-Jacobi Theory

- Wave-like nature of mechanical systems
- Hamilton-Jacobi equation and its applications

---
<style scoped>p,li {font-size:0.88em}</style>

 # Relation to Other Physical Theories
- Electromagnetism and the Lorentz force
- Thermodynamics and statistical physics
- Quantum mechanics and wave-particle duality


---
<style scoped>p,li {font-size:0.92em}</style>

 # History
- Development of classical mechanics from ancient times to modern era
- Contributions of major scientists such as Archimedes, Galileo, and Newton


---
<style scoped>p,li {font-size:0.88em}</style>

 # Notes
- Summary of key concepts and equations
- Important applications and real-world examples
- Open questions and future directions in classical mechanics research.
