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
<!-- backgroundColor: white -->
<!-- _class: lead -->

 # Quantum electrodynamics

---
<style scoped>p,li {font-size:0.76em}</style>

 # History
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Developed in the 1920s and 1930s by physicists such as Paul Dirac, Vladimir Fock, and Wolfgang Pauli
- Quantized version of classical electromagnetism
- First quantum field theory to be developed
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Paul_Dirac%2C_1933%2C_head_and_shoulders_portrait%2C_bw.jpg/170px-Paul_Dirac%2C_1933%2C_head_and_shoulders_portrait%2C_bw.jpg'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Hans_Bethe.jpg/170px-Hans_Bethe.jpg'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Feynman_and_Oppenheimer_at_Los_Alamos.jpg/220px-Feynman_and_Oppenheimer_at_Los_Alamos.jpg'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # _Feynman's View of QED_

- Richard Feynman called QED "the jewel of physics"
- A beautiful and simple theory that underlies all electromagnetic phenomena
- Powerful tool for calculating observables in high-energy physics

---
<style scoped>p,li {font-size:0.84em}</style>

 # **Introduction**
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Quantum electrodynamics is a quantum field theory of the electromagnetic interaction
- Describes the interactions between charged particles and photons
- Fermions (electrons, quarks) and bosons (photons) are the fundamental particles
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Feynman_Diagram_Components.svg/300px-Feynman_Diagram_Components.svg.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.80em}</style>

 # Basic Constructions
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Compton_Scattering.svg/200px-Compton_Scattering.svg.png'/>
</div>
</div>

- Photon: the gauge boson of the electromagnetic interaction
- Electron: a negatively charged fermion
- Positron: an positively charged fermion
- Electromagnetic wave: a wave-like disturbance in the electromagnetic field

---
<style scoped>p,li {font-size:0.76em}</style>

 # Probability Amplitudes
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/7/77/Feynmans_QED_probability_amplitudes.gif'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/AdditionComplexes.svg/200px-AdditionComplexes.svg.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/MultiplicationComplexes.svg/200px-MultiplicationComplexes.svg.png'/>
</div>
</div>

- Probability amplitude: a mathematical object that encodes the probability of a given process
- Born rule: the probability of a process is proportional to the square of the amplitude
- Scattering cross-section: the probability of scattering as a function of energy and angle

---
<style scoped>p,li {font-size:0.88em}</style>

 # Propagators
- Propagator: a mathematical object that describes the propagation of particles in space and time
- Dirac equation: a relativistic wave equation for fermions
- Feynman integral: a mathematical expression for the propagator


---
<style scoped>p,li {font-size:0.84em}</style>

 # Mass Renormalization
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Electron_self_energy_loop.svg/200px-Electron_self_energy_loop.svg.png'/>
</div>
</div>

- Mass renormalization: the process of removing the infinite self-energy of a particle
- Renormalization group: a mathematical framework for understanding the running of couplings and masses
- Dimensional regularization: a technique for regulating infrared divergences

---
<style scoped>p,li {font-size:0.88em}</style>

 # _Conclusions_
- QED is a powerful tool for calculating observables in high-energy physics
- Renormalization group: a mathematical framework for understanding the running of couplings and masses
- Nonperturbative phenomena: phenomena that cannot be described using perturbation theory, such as confinement and the quark-gluon plasma


---
<style scoped>p,li {font-size:0.88em}</style>

 # Mathematical Formulation
- QED action: a mathematical expression for the electromagnetic interaction
- Equations of motion: mathematical equations that describe the behavior of particles in the presence of the electromagnetic field
- Feynman diagrams: a graphical representation of the perturbation theory


---
<style scoped>p,li {font-size:0.88em}</style>

 # _QED Action_
- QED action: a mathematical expression for the electromagnetic interaction
- Lagrangian density: a mathematical expression for the energy and momentum of a system
- Electromagnetic field strength tensor: a mathematical object that describes the electromagnetic field


---
<style scoped>p,li {font-size:0.88em}</style>

 # Equations of Motion

- Equation of motion for ψ: a mathematical equation that describes the behavior of an electron in the presence of the electromagnetic field
- Equation of motion for Aμ: a mathematical equation that describes the behavior of the electromagnetic field
- Interaction picture: a mathematical framework for understanding the interaction between particles and the electromagnetic field

---
<style scoped>p,li {font-size:0.88em}</style>

 # Feynman Diagrams
- Feynman diagrams: a graphical representation of the perturbation theory
- Vertexes: points in space-time where particles interact with the electromagnetic field
- Propagators: mathematical objects that describe the propagation of particles in space and time


---
<style scoped>p,li {font-size:0.88em}</style>

 # Nonperturbative Phenomena

- Nonperturbative phenomena: phenomena that cannot be described using perturbation theory, such as confinement and the quark-gluon plasma
- Confinement: the phenomenon of particles being "confined" within a certain distance range
- Quark-gluon plasma: a state of matter that is thought to have existed in the early universe

---
<style scoped>p,li {font-size:0.88em}</style>

 # Renormalizability

- Renormalizability: the property of a theory that it can be calculated using perturbation theory
- Perturbative: a mathematical framework for understanding the interaction between particles and the electromagnetic field
- Non-perturbative: a mathematical framework for understanding phenomena that cannot be described using perturbation theory

---
<style scoped>p,li {font-size:0.88em}</style>

 # Nonconvergence of Series

- Nonconvergence of series: the property of a mathematical series not converging to a finite value
- Divergent series: a mathematical series that does not converge to a finite value
- Renormalization group: a mathematical framework for understanding the running of couplings and masses

---
<style scoped>p,li {font-size:0.88em}</style>

 # Electrodynamics in Curved Spacetime

- Electrodynamics in curved spacetime: the study of the electromagnetic interaction in the presence of gravity
- General relativity: a theory of gravity that describes the curvature of spacetime
- Quantum field theory in curved spacetime: a mathematical framework for understanding the interaction between particles and the electromagnetic field in the presence of gravity

---
<style scoped>p,li {font-size:0.88em}</style>

 # Books

- "Quantum Electrodynamics" by J. Schwartz
- "The Quantum Theory of Fields" by S. Weinberg
- "Electrodynamics in Curved Spacetime" by T. H. Boyer and B. L. DeWitt

---
<style scoped>p,li {font-size:0.84em}</style>

 # Journals
- Physical Review Letters
- Physical Review D
- Journal of High Energy Physics

I hope this slide presentation helps you understand the basics of Quantum Electrodynamics!
