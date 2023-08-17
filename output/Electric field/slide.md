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

 # **Electric field**

---
<style scoped>p,li {font-size:0.88em}</style>

 # Description
- Electric field is a fundamental concept in physics that describes the influence of electric charges on other charged particles
- It is a vector field that describes the direction and magnitude of the force experienced by a test charge near other charges
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/VFPt_image_charge_plane_horizontal.svg/250px-VFPt_image_charge_plane_horizontal.svg.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # Mathematical Formulation
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Cat_demonstrating_static_cling_with_styrofoam_peanuts.jpg/310px-Cat_demonstrating_static_cling_with_styrofoam_peanuts.jpg'/>
</div>
</div>

- Electric field can be mathematically formulated using the equation: E = ∇⋅P, where E is the electric field strength, P is the electric flux density, and ∇ is the del operator
- This equation states that the electric field at any point in space is proportional to the electric flux density at that point

---
<style scoped>p,li {font-size:0.92em}</style>

 # Electrostatics

- Electric field is a central concept in electrostatics, which deals with the study of stationary electric charges
- Electrostatics is based on the idea that electric charges can be treated as point charges, and the electric field can be calculated using simple algebraic equations

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Superposition Principle_

- The superposition principle is a fundamental principle in electrostatics that states that the electric field due to multiple point charges can be found by adding the electric fields due to each individual charge
- This principle allows for a more straightforward calculation of the electric field in complex situations

---
<style scoped>p,li {font-size:0.92em}</style>

 # Continuous Charge Distributions
- Electric fields can also be calculated for continuous charge distributions, such as those encountered in solids and liquids
- In these cases, the electric field is determined by integrating the electric flux density over the entire distribution


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Electric Potential**
- Electric potential is a related concept to electric field that describes the energy required to move a test charge from one point to another in an electric field
- The electric potential can be calculated using the equation: V = ∫E·dL, where V is the electric potential, E is the electric field strength, and dL is the path element


---
<style scoped>p,li {font-size:0.92em}</style>

 # Continuous vs. Discrete Charge Representation
- Electric fields can be represented using both continuous and discrete charge distributions
- The choice of representation depends on the specific problem being solved and the desired level of accuracy


---
<style scoped>p,li {font-size:0.88em}</style>

 # Electrostatic Fields
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/VFPt_charges_plus_minus_thumb.svg/220px-VFPt_charges_plus_minus_thumb.svg.png'/>
</div>
</div>

- Electrostatic fields are electric fields that arise from stationary charges
- These fields can be calculated using simple algebraic equations and are often represented graphically using field lines or equipotential surfaces

---
<style scoped>p,li {font-size:0.92em}</style>

 # Parallels between Electrostatic and Gravitational Fields

- Electrostatic and gravitational fields share some similarities, such as the fact that both are vector fields that can be described using mathematical equations
- However, there are also significant differences between the two types of fields

---
<style scoped>p,li {font-size:0.88em}</style>

 # Uniform Fields
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/VFPt_capacitor-square-plate.svg/220px-VFPt_capacitor-square-plate.svg.png'/>
</div>
</div>

- Uniform electric fields are those in which the electric field strength and direction are constant over all space
- These fields can be represented using simple algebraic equations and are often used in engineering applications

---
<style scoped>p,li {font-size:0.88em}</style>

 # Electrodynamic Fields
- Electrodynamic fields are electric fields that arise from moving charges or changing magnetic fields
- These fields are more complex than electrostatic fields and require the use of calculus and Maxwell's equations to calculate
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Electrostatic_induction.svg/370px-Electrostatic_induction.svg.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Energy in the Electric Field

- Energy can be stored in an electric field, especially in the form of electric capacitors and inductors
- The energy density of an electric field can be calculated using the equation: ρ = ε0E^2, where ρ is the energy density, E is the electric field strength, and ε0 is the vacuum permittivity constant

---
<style scoped>p,li {font-size:0.92em}</style>

 # The Electric Displacement Field

- The electric displacement field is a related concept to the electric field that describes the density of electric charge in space
- The electric displacement field can be calculated using the equation: D = ∇×E, where D is the electric displacement field and E is the electric field strength

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Definitive Equation of Vector Fields_

- The definitive equation of vector fields is a mathematical equation that describes the behavior of a vector field under changes in the coordinate system
- This equation is a fundamental tool for understanding the properties of vector fields and their applications

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Constitutive Relation_
- The constitutive relation is a mathematical equation that describes the relationship between the electric field and the electric flux density
- This equation is a fundamental tool for understanding the behavior of electric fields and their applications


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Relativistic Effects on Electric Field_
- Relativistic effects can have a significant impact on the behavior of electric fields, especially at high speeds and in strong gravitational fields
- These effects can be calculated using specialized mathematical techniques and are an important area of research in modern physics


---
<style scoped>p,li {font-size:0.96em}</style>

 # Point Charge in Uniform Motion
- The electric field due to a point charge in uniform motion can be calculated using the equation: E = (Q/r^2) \* (v/c), where E is the electric field strength, Q is the charge of the particle, r is the distance between the particle and the observer, v is the velocity of the particle, and c is the speed of light


---
<style scoped>p,li {font-size:0.88em}</style>

 # Propagation of Disturbances in Electric Fields
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Bremsstrahlung.gif/220px-Bremsstrahlung.gif'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Electromagnetic waves can propagate through electric fields, especially in the form of light and radio waves
- The propagation of these disturbances can be described using Maxwell's equations and is an important area of research in modern physics
</div>

</div>


---
<style scoped>p,li {font-size:0.96em}</style>

 # Arbitrarily Moving Point Charge

- The electric field due to an arbitrarily moving point charge can be calculated using the equation: E = (Q/r^2) \* (v/c), where E is the electric field strength, Q is the charge of the particle, r is the distance between the particle and the observer, v is the velocity of the particle, and c is the speed of light

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Some Common Electric Field Values_
- Electric fields can have a wide range of values, depending on the specific application and the properties of the charges involved
- Some common electric field values include those encountered in electrical power distribution systems, electromagnetic induction, and electrical discharge lamps.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Conclusion

- Electric fields are a fundamental concept in physics that describe the influence of electric charges on other charged particles
- They are an important tool for understanding a wide range of physical phenomena and have many practical applications in engineering and technology.