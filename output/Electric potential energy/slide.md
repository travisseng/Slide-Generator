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

 # Electric potential energy

---
<style scoped>p,li {font-size:0.92em}</style>

 # Definition
- Electric potential energy is the energy stored in an electrostatic field
- Measured in units of volts (V)


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Units**
- Volts (V): unit of electric potential energy
- Coulombs (C): unit of charge


---
<style scoped>p,li {font-size:0.88em}</style>

 # _Electrostatic Potential Energy of One Point Charge_

- Electric potential energy of one point charge q is given by:

U = k \* q

where k is Coulomb's constant (8.99 x 10^9 N m^2 C^-2) and q is the magnitude of the point charge

---
<style scoped>p,li {font-size:0.84em}</style>

 # _One Point Charge q in the Presence of Another Point Charge Q_
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Electric potential energy of one point charge q in the presence of another point charge Q is given by:

U = k \* (q + Q)

where q and Q are the magnitudes of the two point charges, and k is Coulomb's constant
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Point_Charge_q_in_an_electric_field.svg/434px-Point_Charge_q_in_an_electric_field.svg.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.84em}</style>

 # **One Point Charge q in the Presence of N Point Charges Qi**
- Electric potential energy of one point charge q in the presence of n point charges Qi is given by:

U = k \* (q + ∑(Qi))

where Qi are the magnitudes of the n point charges, and k is Coulomb's constant
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Electric_potential_energy_3_charge.gif/220px-Electric_potential_energy_3_charge.gif'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # **Electrostatic Potential Energy Stored in a System of Point Charges**
- Electric potential energy stored in a system of point charges can be found by summing the potential energies of each individual charge:

U = ∑(k \* Q)

where Q are the magnitudes of the point charges, and k is Coulomb's constant


---
<style scoped>p,li {font-size:0.88em}</style>

 # Energy Stored in a System of One Point Charge
- Electric potential energy stored in a system of one point charge can be found using the equation:

U = k \* q

where q is the magnitude of the point charge, and k is Coulomb's constant


---
<style scoped>p,li {font-size:0.88em}</style>

 # _Energy Stored in a System of Two Point Charges_

- Electric potential energy stored in a system of two point charges can be found using the equation:

U = k \* (q1 + q2)

where q1 and q2 are the magnitudes of the two point charges, and k is Coulomb's constant

---
<style scoped>p,li {font-size:0.88em}</style>

 # _Energy Stored in a System of Three Point Charges_

- Electric potential energy stored in a system of three point charges can be found using the equation:

U = k \* (q1 + q2 + q3)

where q1, q2, and q3 are the magnitudes of the three point charges, and k is Coulomb's constant

---
<style scoped>p,li {font-size:0.88em}</style>

 # Energy Stored in an Electrostatic Field Distribution in Vacuum
- Electric potential energy stored in an electrostatic field distribution in vacuum can be found using the equation:

U = ∫(∇ \* E) d³x

where E is the electric field, and ∇ is the del operator


---
<style scoped>p,li {font-size:0.80em}</style>

 # Energy Stored in Electronic Elements
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Electronic_component_electrolytic_capacitors.jpg/143px-Electronic_component_electrolytic_capacitors.jpg'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Electric potential energy stored in electronic elements such as capacitors and batteries can be found using the equations:

U = q \* V (for a capacitor)

U = q \* I (for a battery)

where q is the charge, V is the voltage, and I is the current
</div>

</div>


---
<style scoped>p,li {font-size:0.76em}</style>

 # Notes
- Electric potential energy is a scalar quantity
- The units of electric potential energy are volts (V)
- Coulomb's constant (k) is a fundamental constant of nature that relates the electric charge to the electric potential energy
- The equation for the electric potential energy of a system of point charges can be derived using the method of images
- The electric potential energy of an electrostatic field distribution in vacuum can be found using the Lorentz-Heaviside formula

I hope this helps! Let me know if you have any questions or need further clarification.
