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
<!-- backgroundImage: url('backgrounds/aaabstract (5).png') -->
<!-- _class: lead -->

 # Electrical resistance and conductance

---
<style scoped>p,li {font-size:0.84em}</style>

 # Introduction
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Electrical resistance is the opposition to the flow of electric current in a conductor
- Measured in ohms (Ω)
- Conductors have low resistance, while resistors have high resistance
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/ResistanceHydraulicAnalogy.svg/350px-ResistanceHydraulicAnalogy.svg.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # **Conductors and Resistors**
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Conductors: materials that allow electric current to flow easily, such as copper and silver
- Resistors: materials that oppose the flow of electric current, such as rubber and plastic
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Metal_film_resistor.jpg/250px-Metal_film_resistor.jpg'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # Ohm's Law
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- The relationship between voltage (V), current (I), and resistance (R) is given by Ohm's law: V = I x R
- This law applies to all conductors and resistors
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/FourIVcurves.svg/500px-FourIVcurves.svg.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # Relation to Resistivity and Conductivity
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Resistivity is the resistance of a material per unit length and unit cross-sectional area
- Conductivity is the ability of a material to conduct electricity, with higher conductivity meaning lower resistance
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Resistivity_geometry.png/220px-Resistivity_geometry.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # Measurement
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Sanwa_SM-1005s.jpg/220px-Sanwa_SM-1005s.jpg'/>
</div>
</div>

- Resistance can be measured using a multimeter or a voltage source and ammeter
- The measurement can be taken at room temperature or at different temperatures, depending on the material being tested

---
<style scoped>p,li {font-size:0.92em}</style>

 # Typical Values
- The typical resistance range for conductors is 10^-5 to 10^3 ohms
- The typical resistance range for resistors is 10^3 to 10^12 ohms


---
<style scoped>p,li {font-size:0.92em}</style>

 # Static and Differential Resistance
- Static resistance is the opposition to the flow of electric current in a conductor when there is no change in voltage
- Differential resistance is the opposition to the flow of electric current in a conductor when there is a change in voltage


---
<style scoped>p,li {font-size:0.92em}</style>

 # AC Circuits

- In alternating current (AC) circuits, the resistance can vary depending on the frequency of the AC signal
- The reactance of a conductor is the opposition to the flow of an AC current

---
<style scoped>p,li {font-size:0.88em}</style>

 # Impedance and Admittance
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/VI_phase.svg/300px-VI_phase.svg.png'/>
</div>
</div>

- Impedance is the total opposition to the flow of an AC current in a circuit, including both resistance and reactance
- Admittance is the ease with which an AC current flows through a circuit, equal to the reciprocal of impedance

---
<style scoped>p,li {font-size:0.92em}</style>

 # Frequency Dependence

- The resistance and impedance of a conductor can vary depending on the frequency of the AC signal
- At high frequencies, the resistance can become significant due to the skin effect and other factors

---
<style scoped>p,li {font-size:0.88em}</style>

 # Energy Dissipation and Joule Heating
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Cartridge-heater-hot.jpg/220px-Cartridge-heater-hot.jpg'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- When an electric current flows through a conductor, it can cause energy dissipation in the form of heat, known as Joule heating
- The amount of Joule heating depends on the resistance of the conductor and the magnitude of the current
</div>

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Dependence on Other Conditions_

- The resistance of a conductor can be affected by other factors such as temperature, strain, and light illumination
- These factors can cause changes in the resistivity and conductivity of the material

---
<style scoped>p,li {font-size:0.92em}</style>

 # Temperature Dependence
- The resistance of many materials decreases with increasing temperature, due to the increased thermal motion of the atoms
- However, some materials such as rubber and plastic have a resistance that increases with temperature


---
<style scoped>p,li {font-size:0.92em}</style>

 # Strain Dependence
- The resistance of a conductor can be affected by strain, which is the deformation of the material due to external forces
- Some materials such as metals have a resistance that increases with strain, while others such as rubber and plastic have a resistance that decreases with strain


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Light Illumination Dependence**
- The resistance of some materials can be affected by light illumination, due to the photovoltaic effect or other mechanisms
- This can cause changes in the resistivity and conductivity of the material


---
<style scoped>p,li {font-size:0.24em}</style>

 # **Superconductivity**
- Superconductors are materials that have zero resistance when cooled below a certain temperature, known as the critical temperature
- This allows for the efficient transmission of electricity with no energy loss due to resistance

Footnotes:

1. Resistance is measured in ohms (Ω) and is defined as the opposition to the flow of electric current.

2. Conductors have low resistance, while resistors have high resistance.

3. Ohm's law states that the voltage (V) is equal to the current (I) times the resistance (R).

4. The resistivity of a material is the resistance per unit length and unit cross-sectional area.

5. Conductivity is the ability of a material to conduct electricity, with higher conductivity meaning lower resistance.

6. Static resistance is the opposition to the flow of electric current in a conductor when there is no change in voltage.

7. Differential resistance is the opposition to the flow of electric current in a conductor when there is a change in voltage.

8. AC circuits have alternating current and voltage, and the resistance can vary depending on the frequency of the AC signal.

9. Impedance is the total opposition to the flow of an AC current in a circuit, including both resistance and reactance.

10. Admittance is the ease with which an AC current flows through a circuit, equal to the reciprocal of impedance.

11. Joule heating is the energy dissipation due to the flow of electric current through a conductor, resulting in heat.

12. The resistance of a conductor can be affected by other factors such as temperature, strain, and light illumination.

13. Some materials have a resistance that decreases with increasing temperature, while others have a resistance that increases with temperature.

14. Strain can cause changes in the resistivity and conductivity of a material.

15. Light illumination can affect the resistivity and conductivity of some materials.

16. Superconductors have zero resistance when cooled below a certain temperature, allowing for efficient transmission of electricity with no energy loss due to resistance.
