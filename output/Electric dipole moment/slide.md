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

 # **Electric dipole moment**

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Introduction**

- Electric dipole moment is a measure of the distribution of electric charge within a system
- It is a fundamental concept in physics and engineering, and has applications in many fields, including electromagnetism, optics, and materials science

---
<style scoped>p,li {font-size:0.88em}</style>

 # Elementary Definition
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Electric_dipole_moment_definition.svg/220px-Electric_dipole_moment_definition.svg.png'/>
</div>
</div>

- An electric dipole is a pair of charges with opposite signs that are located at two different points in space
- The electric dipole moment is the product of the charge and the distance between the two points

---
<style scoped>p,li {font-size:0.88em}</style>

 # Energy and Torque
- The energy of an electric dipole in an external electric field can be calculated using the equation: U = (1/2) Q^2 E^2, where U is the energy, Q is the charge, and E is the electric field strength
- The torque experienced by an electric dipole in an external electric field can be calculated using the equation: τ = (1/2) Q E^2, where τ is the torque, Q is the charge, and E is the electric field strength
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Electric_dipole_torque_uniform_field.svg/187px-Electric_dipole_torque_uniform_field.svg.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.96em}</style>

 # Expression (General Case)
- The electric dipole moment can be expressed in terms of the distribution of electric charge within a system using the equation: p = ∫ (ρ(r) x r) d^3r, where p is the electric dipole moment, ρ(r) is the electric charge density, and x is the cross product operator


---
<style scoped>p,li {font-size:0.88em}</style>

 # Potential and Field of an Electric Dipole
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/DipolePotential.tiff/lossy-page1-220px-DipolePotential.tiff.jpg'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- The potential distribution around an electric dipole can be calculated using the equation: Φ(r) = (1/4πε0) \* (p x r / r^3), where Φ(r) is the potential, p is the electric dipole moment, ε0 is the vacuum permittivity constant, and r is the distance from the dipole
- The electric field distribution around an electric dipole can be calculated using the equation: E(r) = (1/4πε0) \* (p / r^3), where E(r) is the electric field, p is the electric dipole moment, and ε0 is the vacuum permittivity constant
</div>

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Dipole Moment Density and Polarization Density**

- The dipole moment density is a measure of the distribution of electric dipole moments within a system
- The polarization density is a measure of the distribution of electric polarization within a system

---
<style scoped>p,li {font-size:0.96em}</style>

 # **Medium with Charge and Dipole Densities**

- In a medium with charges and dipole densities, the total electric field can be calculated using the equation: E = ∑ (ρ(r) + p(r)), where E is the total electric field, ρ(r) is the electric charge density, p(r) is the electric dipole moment density, and the sum is over all points in the medium

---
<style scoped>p,li {font-size:0.88em}</style>

 # Surface Charge
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Dipole_polarization.JPG/220px-Dipole_polarization.JPG'/>
</div>
</div>

- The surface charge of a medium is the charge distribution on the surface of the medium
- The surface charge can be calculated using the equation: Σ = ∫ (ρ(r) x n) d^2r, where Σ is the surface charge, ρ(r) is the electric charge density, n is the normal vector to the surface, and the integral is over all points on the surface

---
<style scoped>p,li {font-size:0.88em}</style>

 # _Dielectric Sphere in Uniform External Electric Field_
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- The dielectric sphere is a simplified model of a medium with a uniform electric field external to the sphere
- The electric field within the sphere can be calculated using the equation: E(r) = (1/4πε0) \* (E_ext - Σ / r), where E(r) is the electric field, E_ext is the external electric field, Σ is the total surface charge of the sphere, and r is the distance from the center of the sphere
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Dielectric_sphere.svg/250px-Dielectric_sphere.svg.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.96em}</style>

 # General Media
- In a general medium with charges and dipole moments, the electric field can be calculated using the equation: E = ∑ (ρ(r) + p(r)) / (4πε0), where E is the total electric field, ρ(r) is the electric charge density, p(r) is the electric dipole moment density, and ε0 is the vacuum permittivity constant


---
<style scoped>p,li {font-size:0.96em}</style>

 # **Electric Dipole Moments of Fundamental Particles**
- The electric dipole moments of fundamental particles are important in particle physics and have applications in many areas of research


---
<style scoped>p,li {font-size:0.96em}</style>

 # Dipole Moments of Molecules

- The electric dipole moments of molecules are important in understanding the properties of molecules and their interactions with other molecules and with external fields

---
<style scoped>p,li {font-size:0.84em}</style>

 # Notes

- The electric dipole moment is a measure of the distribution of electric charge within a system
- The electric field and potential distributions around an electric dipole can be calculated using the equations given in slides 5 and 6
- The dipole moment density and polarization density are important in understanding the properties of media with charges and dipole moments

I hope this helps! Let me know if you have any questions or need further clarification.