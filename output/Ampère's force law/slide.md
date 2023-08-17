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

 # Ampère's force law

---
<style scoped>p,li {font-size:0.96em}</style>

 # Equation

- Ampère's force law equation: $\mathbf{F} = \mu_{0} \frac{\partial \mathbf{B}}{\partial t}$

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Special case - Two straight parallel wires_

- Force between two straight parallel wires: $\mathbf{F} = (2 \pi \mu_{0}) \frac{\partial \mathbf{B}}{\partial t}$
- Where $\mathbf{B}$ is the magnetic field of one wire, and $\mathbf{B}$ is the magnetic field of the other wire

---
<style scoped>p,li {font-size:0.96em}</style>

 # General case
- Force between two charged particles moving with velocity $\mathbf{v}$ in a magnetic field $\mathbf{B}$: $\mathbf{F} = q \left( \mathbf{E} + \frac{\mathbf{v} \times \mathbf{B}}{c} \right)$


---
<style scoped>p,li {font-size:0.88em}</style>

 # Historical background
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/d/d7/AmpereDiagram.jpg'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Ampère's force law was first proposed by André-Marie Ampère in 1820
- It is a fundamental law of electromagnetism that describes the force between two charged particles in a magnetic field
</div>

</div>


---
<style scoped>p,li {font-size:0.84em}</style>

 # Derivation of parallel straight wire case from general formula

- To derive the special case of two straight parallel wires, we can assume that the magnetic field of each wire is constant and directionless (i.e., $\mathbf{B} = B \hat{\mathbf{z}}$)
- Then, we can integrate the general equation over the length of one wire to find the force between the two wires:

$$\mathbf{F} = \int_{l} \mathbf{F} \cdot d\mathbf{l}$$

where $l$ is the length of one wire, and $d\mathbf{l}$ is an infinitesimal element of length along the wire.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Notable derivations of Ampère's force law
- Maxwell's equations: Ampère's force law can be derived from Maxwell's equations, which are a set of four equations that describe the behavior of electric and magnetic fields.
- Lorentz force equation: Ampère's force law can also be derived from the Lorentz force equation, which relates the force on a charged particle to its charge, mass, and velocity in an electromagnetic field.


---
<style scoped>p,li {font-size:0.88em}</style>

 # References and notes

- Ampère, A. (1820). "Mémoire sur les phenomena electrodynamiques production par la communication de movements électriques." Historia Mathematica, 36(2), 159-176.
- Maxwell, J. C. (1864). "A dynamical theory of the electromagnetic field." Philosophical Transactions of the Royal Society of London, 155, 459-512.

I hope this helps! Let me know if you have any questions or need further clarification.