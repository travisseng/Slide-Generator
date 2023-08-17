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
<!-- backgroundColor: white -->
<!-- _class: lead -->

 # Poynting vector

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Introduction**

- The Poynting vector is a measure of the energy density of an electromagnetic wave
- It is named after John Henry Poynting, who first introduced the concept in 1903

---
<style scoped>p,li {font-size:0.88em}</style>

 # Definition
- The Poynting vector is defined as the cross product of the electric and magnetic fields:

$$\mathbf{S} = \mathbf{E} \times \mathbf{B}$$

where $\mathbf{E}$ and $\mathbf{B}$ are the electric and magnetic fields, respectively.


---
<style scoped>p,li {font-size:0.84em}</style>

 # _Example - Power flow in a coaxial cable_
- The Poynting vector can be used to calculate the power flow in a coaxial cable
- The power flow is given by the dot product of the Poynting vector and the propagation direction:

$$\frac{dP}{dt} = \mathbf{S} \cdot \mathbf{u}$$

where $P$ is the power, $\mathbf{u}$ is the propagation direction, and $\mathbf{S}$ is the Poynting vector.


---
<style scoped>p,li {font-size:0.84em}</style>

 # Other forms
- The Poynting vector can also be expressed in terms of the electric and magnetic fields in other forms, such as:

$$\mathbf{S} = \frac{1}{2} \left( \mathbf{E} + \mathbf{B} \right)$$

or

$$\mathbf{S} = \frac{1}{2} \left( \mathbf{E} - \mathbf{B} \right)$$


---
<style scoped>p,li {font-size:0.92em}</style>

 # Interpretation
- The Poynting vector can be interpreted as the energy density of the electromagnetic wave
- It is a measure of the amount of energy that is carried by the wave per unit volume.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Plane waves
- The Poynting vector can be used to describe the properties of plane waves
- A plane wave is an electromagnetic wave that propagates in a single direction, with a constant frequency and amplitude.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Formulation in terms of microscopic fields
- The Poynting vector can also be used to describe the properties of the microscopic fields that make up an electromagnetic wave
- This can be done by expressing the electric and magnetic fields in terms of their microscopic components.


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Time-averaged Poynting vector_
- The time-averaged Poynting vector is a measure of the energy density of an electromagnetic wave over a period of time
- It can be calculated by taking the average of the Poynting vector over a single period of the wave.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Resistive dissipation
- The Poynting vector can be used to calculate the rate of resistive dissipation in an electromagnetic wave
- This can be done by taking the dot product of the Poynting vector and the resistance per unit length.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Radiation pressure

- The Poynting vector can also be used to calculate the radiation pressure exerted on a charged particle by an electromagnetic wave
- This can be done by taking the dot product of the Poynting vector and the charge per unit volume.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Uniqueness of the Poynting vector
- The Poynting vector is a unique quantity that can be used to describe the properties of electromagnetic waves
- It is not possible to measure the energy density of an electromagnetic wave using any other quantity.


---
<style scoped>p,li {font-size:0.84em}</style>

 # **Static fields**
- The Poynting vector can also be used to describe the properties of static electromagnetic fields
- A static field is one that does not change with time.

I hope this helps! Let me know if you have any questions or need further clarification on any of the topics.
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Poynting-Paradoxon.svg/250px-Poynting-Paradoxon.svg.png'/>
</div>
</div>
