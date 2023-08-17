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

 # Coulomb's law

---
<style scoped>p,li {font-size:0.84em}</style>

 # _History_
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Coulomb.jpg/220px-Coulomb.jpg'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Bcoulomb.png/220px-Bcoulomb.png'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Coulomb's law was first proposed by French physicist Charles-Augustin de Coulomb in the late 18th century
- It was initially based on empirical observations, but later became a fundamental principle of physics
</div>

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Scalar form
- Coulomb's law can be expressed as a scalar equation: F = k\*q, where F is the electrostatic force between two charges q and k is Coulomb's constant
- This form is useful for simple calculations, but it does not take into account the direction of the forces


---
<style scoped>p,li {font-size:0.88em}</style>

 # Vector form
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Coulombslawgraph.svg/350px-Coulombslawgraph.svg.png'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Coulomb's law can also be expressed as a vector equation: F = k\*q/r^2, where r is the distance between the charges and F is the electrostatic force
- This form takes into account the direction of the forces and is more useful for complex calculations
</div>

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # _System of discrete charges_
- Coulomb's law can be applied to a system of multiple discrete charges, where the total force on each charge is the sum of the forces from all other charges
- This is useful for calculating the electrostatic forces in complex systems, such as those found in molecules and crystals


---
<style scoped>p,li {font-size:0.92em}</style>

 # Continuous charge distribution

- Coulomb's law can also be applied to a continuous charge distribution, such as a charged sphere or a charged wire
- In these cases, the electrostatic force is proportional to the density of charge and the distance between the charges

---
<style scoped>p,li {font-size:0.92em}</style>

 # Coulomb constant

- The Coulomb constant k is a fundamental constant of nature that appears in Coulomb's law
- It has a value of approximately 8.99 x 10^9 N m^2 C^-2

---
<style scoped>p,li {font-size:0.92em}</style>

 # Limitations

- Coulomb's law only applies to electrostatic forces and does not account for other types of forces, such as gravitational or magnetic forces
- It is also limited in its ability to describe the behavior of charged particles at very small distances or high speeds

---
<style scoped>p,li {font-size:0.88em}</style>

 # Electric field
- The electric field is a vector field that describes the strength and direction of the electrostatic force around a charge
- It is related to Coulomb's law by the equation E = k\*q/r^2
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Electric_field_one_charge_changing.gif/220px-Electric_field_one_charge_changing.gif'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Atomic forces**
- Coulomb's law is used to describe the electrostatic forces between atoms in molecules
- These forces are responsible for the structure and properties of materials


---
<style scoped>p,li {font-size:0.92em}</style>

 # Relation to Gauss's law
- Coulomb's law is related to Gauss's law, which describes the distribution of electric charge in a given region of space
- Gauss's law can be derived from Coulomb's law, and vice versa


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Deriving Gauss's law from Coulomb's law_

- To derive Gauss's law from Coulomb's law, we can start with the scalar equation F = k\*q and integrate it over all space to obtain a differential equation for the electric field
- This differential equation can be solved to obtain Gauss's law

---
<style scoped>p,li {font-size:0.92em}</style>

 # Deriving Coulomb's law from Gauss's law

- To derive Coulomb's law from Gauss's law, we can start with the differential equation for the electric field and use it to determine the electrostatic force between two charges
- This leads to the vector equation F = k\*q/r^2, which is Coulomb's law

---
<style scoped>p,li {font-size:0.92em}</style>

 # _In relativity_
- Coulomb's law is a classical concept that does not account for the effects of special relativity
- However, the principles of special relativity can be incorporated into a modified version of Coulomb's law known as the Lorentz-Coulomb law


---
<style scoped>p,li {font-size:0.92em}</style>

 # Coulomb potential
- The Coulomb potential is a mathematical function that describes the electrostatic force between two charges as a function of distance
- It is related to Coulomb's law by the equation V = k\*q/r


---
<style scoped>p,li {font-size:0.88em}</style>

 # Quantum field theory
- In quantum field theory, the behavior of charged particles is described using wave functions and operators that satisfy Coulomb's law
- This allows for a quantum mechanical description of the electrostatic forces between charges
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Feynman_diagram_-_Moller_scattering_1.svg/220px-Feynman_diagram_-_Moller_scattering_1.svg.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # **Simple experiment to verify Coulomb's law**
- One simple experiment to verify Coulomb's law is to measure the electrostatic force between two charged objects, such as a positively charged rod and a negatively charged sphere
- The force can be measured using a spring or a balance, and it will be proportional to the product of the charges and inversely proportional to the distance between them
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Verificacion_ley_coulomb.png/250px-Verificacion_ley_coulomb.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Related reading
- For further reading on Coulomb's law and its applications, some recommended texts include "The Feynman Lectures on Physics" by Richard Feynman, "Introduction to Electromagnetic Theory" by David J. Griffiths, and "Classical Electrodynamics" by David Morin

I hope this helps! Let me know if you have any questions or need further clarification.
