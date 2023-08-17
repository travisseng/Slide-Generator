---
marp: true
math: katex
theme: uncover
paginate: True
style: |
   @import url('https://unpkg.com/tailwindcss@2.2.19/dist/utilities.min.css');
   :root {--color-fg-default: #FFFFFF; --color-foreground: #FFFFFF;}

   section {display: flex;flex-flow: column; font-size:35px; letter-spacing:1.4px;}

   header {overflow:visible} header > img.logo {position:absolute; right:15px;}

   header > img.logo {position:absolute; right:15px;}


---
<!-- backgroundImage: url('backgrounds/aaabstract (8).png') -->
<!-- _class: lead -->

 # Nondimensionalization

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Rationale**
- Nondimensionalization is a powerful tool for simplifying complex systems and understanding their behavior
- By removing irrelevant scales and units, we can focus on the essential features of the system


---
<style scoped>p,li {font-size:0.88em}</style>

 # Nondimensionalization Steps

- Identify the relevant physical parameters and scales in the system
- Remove irrelevant scales and units by dividing by appropriate powers of the characteristic scale
- Express all quantities in terms of their nondimensionalized forms

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Conventions_

- Use consistent conventions for naming and defining nondimensionalized quantities
- Avoid ambiguous or misleading notation

---
<style scoped>p,li {font-size:0.92em}</style>

 # Substitutions

- Use substitutions to simplify the system, such as replacing a parameter with its inverse or a related quantity
- Be careful not to introduce new irrelevant scales or units

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Differential Operators_
- Use differential operators to describe the behavior of the system over time
- Carefully choose the appropriate order and form of the differential operator for the system being studied


---
<style scoped>p,li {font-size:0.92em}</style>

 # Forcing Function

- Identify any external forces or drivers that affect the system's behavior
- Incorporate these forcing functions into the nondimensionalized equations

---
<style scoped>p,li {font-size:0.92em}</style>

 # Linear Differential Equations with Constant Coefficients

- Many systems can be described by linear differential equations with constant coefficients
- These equations can be easily solved and their solutions expressed in terms of their characteristic units

---
<style scoped>p,li {font-size:0.92em}</style>

 # _First Order System_

- A first-order system is one that involves a single independent variable and its derivatives to the first power
- Examples include mechanical oscillations and electrical circuits

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Second Order System_

- A second-order system is one that involves two independent variables and their derivatives to the second power
- Examples include mechanical systems with friction and electrical filters

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Substitution Step_
- The substitution step involves expressing the nondimensionalized equations in terms of their characteristic units
- This allows us to determine the behavior of the system over time and under different conditions


---
<style scoped>p,li {font-size:0.92em}</style>

 # Determination of Characteristic Units

- The determination of characteristic units is a key part of the nondimensionalization process
- These units can be determined by examining the scales and units of the physical parameters in the system

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Higher Order Systems_
- Many systems involve higher-order derivatives and more complex equations
- Nondimensionalization techniques can still be applied to these systems, but require more careful consideration of the relevant scales and units


---
<style scoped>p,li {font-size:0.92em}</style>

 # Examples of Recovering Characteristic Units

- Once we have determined the characteristic units of a system, we can use them to recover the original physical scales and units
- This is done by multiplying the nondimensionalized equations by appropriate powers of the characteristic scale

---
<style scoped>p,li {font-size:0.88em}</style>

 # Mechanical Oscillations
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Mass-Spring-Damper.png/300px-Mass-Spring-Damper.png'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Mechanical oscillations are an important example of a first-order system
- Nondimensionalization can be used to simplify the equations of motion and understand the behavior of the system over time
</div>

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Electrical Oscillations_
- Electrical oscillations are another important example of a first-order system
- Nondimensionalization can be used to simplify the equations of motion and understand the behavior of the system over time


---
<style scoped>p,li {font-size:0.92em}</style>

 # First-Order Series RC Circuit

- A first-order series RC circuit is an example of a nondimensionalized electrical circuit
- The circuit can be analyzed using the techniques of nondimensionalization, and its behavior understood in terms of its characteristic units

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Second-Order Series RLC Circuit_

- A second-order series RLC circuit is an example of a more complex electrical circuit
- Nondimensionalization can still be applied to this system, but requires more careful consideration of the relevant scales and units

---
<style scoped>p,li {font-size:0.92em}</style>

 # Quantum Mechanics
- Quantum mechanics is the study of the behavior of matter and energy at the atomic and subatomic level
- Nondimensionalization techniques can be used to simplify the equations of quantum mechanics and understand its behavior


---
<style scoped>p,li {font-size:0.92em}</style>

 # Quantum Harmonic Oscillator

- The quantum harmonic oscillator is an important example of a quantum system that can be studied using nondimensionalization techniques
- This system involves the behavior of a particle in a potential well, and can be analyzed using the techniques of nondimensionalization

---
<style scoped>p,li {font-size:0.88em}</style>

 # **Statistical Analogs**
- Nondimensionalization techniques can also be used to study statistical systems, such as the behavior of particles in a gas
- These systems can be analyzed using the same techniques as physical systems, but with an emphasis on probability and statistics rather than determinism

I hope this presentation helps you understand the powerful tool of nondimensionalization and how it can be applied to a wide range of physical and quantum systems.
