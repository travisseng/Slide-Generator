---
marp: true
math: katex
theme: uncover
style: |
   @import url('https://unpkg.com/tailwindcss@2.2.19/dist/utilities.min.css');
   section {display: flex;flex-flow: column; font-size:35px; letter-spacing:1.4px;}

   header {overflow:visible} header > img.logo {position:absolute; right:15px;}

   header > img.logo {position:absolute; right:15px;}


---
<!-- backgroundColor: white -->
<!-- _class: lead -->

 # _Maxwell's equations_

---
<style scoped>p,li {font-size:0.92em}</style>

 # Introduction
- Brief history of the development of Maxwell's equations
- Importance and relevance of Maxwell's equations in modern physics


---
<style scoped>p,li {font-size:0.92em}</style>

 # History of the Equations
- Overview of the key contributors to the development of Maxwell's equations (e.g. Coulomb, Gauss, Faraday, Ampère)
- Historical context and publication dates of the major milestones in the development of the equations


---
<style scoped>p,li {font-size:0.92em}</style>

 # Conceptual Descriptions

- Explanation of the basic concepts underlying Maxwell's equations (electric and magnetic fields, charges, currents, etc.)
- Visual aids to help illustrate these concepts

---
<style scoped>p,li {font-size:0.92em}</style>

 # Gauss's Law

- Statement of Gauss's law for electric fields
- Explanation of the Physical significance of Gauss's law

---
<style scoped>p,li {font-size:0.88em}</style>

 # **Gauss's Law for Magnetism**
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/VFPt_dipole_magnetic1.svg/220px-VFPt_dipole_magnetic1.svg.png'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Statement of Gauss's law for magnetic fields
- Explanation of the physical significance of Gauss's law for magnetism
</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # _Faraday's Law_
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Magnetosphere_rendition.jpg/320px-Magnetosphere_rendition.jpg'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Statement of Faraday's law of induction
- Explanation of the physical significance of Faraday's law
</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # Ampère's Law with Maxwell's Addition
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Magnetic_core.jpg/220px-Magnetic_core.jpg'/>
</div>
</div>

- Statement of Ampère's law with Maxwell's addition
- Explanation of the physical significance of Ampère's law and Maxwell's addition

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Formulation in Terms of Electric and Magnetic Fields**

- Overview of the different formulations of Maxwell's equations, including the microscopic or in vacuum version and the macroscopic version
- Explanation of the key notation used in these formulations

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Differential Equations**
- Overview of the differential equations that arise in the study of Maxwell's equations
- Explanation of the physical significance of these differential equations


---
<style scoped>p,li {font-size:0.92em}</style>

 # Integral Equations
- Overview of the integral equations that arise in the study of Maxwell's equations
- Explanation of the physical significance of these integral equations


---
<style scoped>p,li {font-size:0.92em}</style>

 # Formulation in SI Units Convention
- Overview of the SI units convention used to express Maxwell's equations
- Explanation of the physical significance of this convention


---
<style scoped>p,li {font-size:0.92em}</style>

 # Formulation in Gaussian Units Convention
- Overview of the Gaussian units convention used to express Maxwell's equations
- Explanation of the physical significance of this convention


---
<style scoped>p,li {font-size:0.92em}</style>

 # Relationship between Differential and Integral Formulations
- Explanation of the relationship between the differential and integral formulations of Maxwell's equations
- Visual aids to help illustrate this relationship


---
<style scoped>p,li {font-size:0.88em}</style>

 # Flux and Divergence
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Divergence_theorem_in_EM.svg/220px-Divergence_theorem_in_EM.svg.png'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Explanation of the concepts of flux and divergence in the context of Maxwell's equations
- Visual aids to help illustrate these concepts
</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # Circulation and Curl
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Curl_theorem_in_EM.svg/220px-Curl_theorem_in_EM.svg.png'/>
</div>
</div>

- Explanation of the concepts of circulation and curl in the context of Maxwell's equations
- Visual aids to help illustrate these concepts

---
<style scoped>p,li {font-size:0.92em}</style>

 # Charge Conservation

- Explanation of charge conservation in the context of Maxwell's equations
- Visual aids to help illustrate this concept

---
<style scoped>p,li {font-size:0.92em}</style>

 # Vacuum Equations

- Overview of the vacuum equations that arise in the study of Maxwell's equations
- Explanation of the physical significance of these equations

---
<style scoped>p,li {font-size:0.92em}</style>

 # Electromagnetic Waves and Speed of Light

- Overview of electromagnetic waves and their relationship to Maxwell's equations
- Explanation of the speed of light and its role in Maxwell's equations

---
<style scoped>p,li {font-size:0.92em}</style>

 # Macroscopic Formulation

- Overview of the macroscopic formulation of Maxwell's equations
- Explanation of the physical significance of this formulation

---
<style scoped>p,li {font-size:0.88em}</style>

 # _Bound Charge and Current_
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Polarization_and_magnetization.svg/300px-Polarization_and_magnetization.svg.png'/>
</div>
</div>

- Overview of bound charge and current in the context of Maxwell's equations
- Explanation of the physical significance of these concepts

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Auxiliary Fields, Polarization, and Magnetization_
- Overview of auxiliary fields, polarization, and magnetization in the context of Maxwell's equations
- Explanation of the physical significance of these concepts


---
<style scoped>p,li {font-size:0.92em}</style>

 # Constitutive Relations

- Overview of constitutive relations in the context of Maxwell's equations
- Explanation of the physical significance of these relations

---
<style scoped>p,li {font-size:0.92em}</style>

 # Alternative Formulations
- Overview of alternative formulations of Maxwell's equations, including the Lorentz-Maxwell equation and the Teleparallel formulation
- Explanation of the physical significance of these alternative formulations


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Relativistic Formulations_

- Overview of relativistic formulations of Maxwell's equations, including the Einstein-Maxwell equation and the Dirac-Maxwell equation
- Explanation of the physical significance of these relativistic formulations

---
<style scoped>p,li {font-size:0.92em}</style>

 # Solutions

- Overview of the different types of solutions that arise in the study of Maxwell's equations, including electrostatic, electromagnetic wave, and plasma solutions
- Explanation of the physical significance of these solutions

---
<style scoped>p,li {font-size:0.96em}</style>

 # **Overdetermination of Maxwell's Equations**
- Explanation of the overdetermination of Maxwell's equations and its implications for the study of electromagnetism


---
<style scoped>p,li {font-size:0.92em}</style>

 # Maxwell's Equations as the Classical Limit of QED
- Overview of the relationship between Maxwell's equations and quantum electrodynamics (QED)
- Explanation of how Maxwell's equations can be understood as the classical limit of QED


---
<style scoped>p,li {font-size:0.92em}</style>

 # Variations
- Overview of the different variations of Maxwell's equations that have been proposed over the years, including the Lorentz-Maxwell equation and the Teleparallel formulation
- Explanation of the physical significance of these variations


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Magnetic Monopoles**
- Overview of magnetic monopoles and their relationship to Maxwell's equations
- Explanation of the physical significance of magnetic monopoles in the context of electromagnetism


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Explanatory Notes**
- Additional explanations and notes on the key concepts and formulations presented in the previous slides
- Visual aids to help illustrate these concepts and formulations


---
<style scoped>p,li {font-size:0.96em}</style>

 # **Historical Publications**

- Overview of some of the key historical publications that have contributed to the development of Maxwell's equations, including works by Coulomb, Gauss, Faraday, and Ampère

---
<style scoped>p,li {font-size:0.92em}</style>

 # Modern Treatments
- Overview of modern treatments of Maxwell's equations, including their application in fields such as electrical engineering, optics, and particle physics
- Explanation of the key challenges and open questions in the study of Maxwell's equations


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Other**
- Overview of other topics and areas that are related to Maxwell's equations, including plasma physics, electromagnetic wave propagation, and the application of Maxwell's equations to materials science and engineering
- Explanation of the key challenges and open questions in these areas
