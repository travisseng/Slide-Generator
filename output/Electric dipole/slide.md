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
<!-- backgroundColor: #828682 -->
<!-- _class: lead -->

 # Electric dipole

---
<style scoped>p,li {font-size:0.92em}</style>

 # Introduction

- Electric dipoles are a fundamental concept in physics and engineering
- They describe the distribution of electric charge and magnetic moment in a system

---
<style scoped>p,li {font-size:0.88em}</style>

 # Elementary Definition
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Electric_dipole_moment_definition.svg/220px-Electric_dipole_moment_definition.svg.png'/>
</div>
</div>

- An electric dipole is a pair of charges with equal magnitudes but opposite signs, separated by a distance
- The dipole moment is defined as the product of the charges and the distance between them

---
<style scoped>p,li {font-size:0.84em}</style>

 # **Energy and Torque**
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Electric_dipole_torque_uniform_field.svg/187px-Electric_dipole_torque_uniform_field.svg.png'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Electric dipoles can interact with external electric fields to gain or lose energy
- The energy of an electric dipole in an external field can be calculated using the potential energy formula
- The torque experienced by an electric dipole in an external field is proportional to the dipole moment and the strength of the external field
</div>

</div>


---
<style scoped>p,li {font-size:0.84em}</style>

 # Expression (General Case)

- The electric dipole moment can be expressed in terms of the charge distribution within the system
- For a system of N charges, the dipole moment is given by:

$$\mathbf{p} = \frac{1}{2}\sum_{i<j}q_i\mathbf{r}_{ij}$$

where $q_i$ is the charge of the $i$th charge, $\mathbf{r}_{ij}$ is the position vector of the $i$th charge relative to the $j$th charge, and the sum is over all pairs of charges

---
<style scoped>p,li {font-size:0.88em}</style>

 # Potential and Field of an Electric Dipole
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- The potential of an electric dipole can be calculated using the potential energy formula
- The field of an electric dipole can be calculated using the electric field equation
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/DipolePotential.tiff/lossy-page1-220px-DipolePotential.tiff.jpg'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Dipole Moment Density and Polarization Density_
- The dipole moment density is a measure of the distribution of dipole moments within a system
- The polarization density is a measure of the distribution of electric polarization within a system


---
<style scoped>p,li {font-size:0.96em}</style>

 # Medium with Charge and Dipole Densities

- A medium with charge and dipole densities can be described using the continuity equation for charges and the Maxwell's equation for the electric field

---
<style scoped>p,li {font-size:0.88em}</style>

 # **Surface Charge**
- The surface charge density is a measure of the distribution of electric charge on a surface
- The surface charge density can be calculated using the Gauss's law
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Dipole_polarization.JPG/220px-Dipole_polarization.JPG'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Dielectric Sphere in Uniform External Electric Field_
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Dielectric_sphere.svg/250px-Dielectric_sphere.svg.png'/>
</div>
</div>

- A dielectric sphere in a uniform external electric field will experience a dipole moment due to the interaction between the electric field and the polarization of the sphere

---
<style scoped>p,li {font-size:0.96em}</style>

 # General Media
- The electric dipole moment can be calculated for any type of medium, including dispersive and absorbing media


---
<style scoped>p,li {font-size:0.96em}</style>

 # Electric Dipole Moments of Fundamental Particles

- Electric dipole moments are a fundamental property of some fundamental particles, such as the electron and the quark

---
<style scoped>p,li {font-size:0.96em}</style>

 # Dipole Moments of Molecules
- Electric dipole moments can be observed in molecules due to the distribution of electric charge within the molecule


---
<style scoped>p,li {font-size:0.88em}</style>

 # Notes
- The electric dipole moment is a measure of the distribution of electric charge and magnetic moment within a system
- The electric dipole moment can be calculated using various methods, including the expression for the dipole moment in terms of the charge distribution and the potential energy formula
- Electric dipoles are important in many areas of physics and engineering, including electrostatics, electromagnetism, and materials science.
