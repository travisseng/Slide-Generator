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

 # **Ohm's law**

---
<style scoped>p,li {font-size:0.80em}</style>

 # History
- Ohm's Law was first discovered by Georg Simon Ohm in the 1820s
- It states that the current flowing through a conductor is directly proportional to the voltage applied across it, and inversely proportional to the resistance of the conductor
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Ohm3.gif/200px-Ohm3.gif'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/en/thumb/5/51/Internal_resistance_model.svg/220px-Internal_resistance_model.svg.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Ohmsches_Gesetz_in_Georg_Simon_Ohms_Laborbuch.jpg/220px-Ohmsches_Gesetz_in_Georg_Simon_Ohms_Laborbuch.jpg'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Scope
- Ohm's Law applies to all conductors, including metals, semiconductors, and insulators
- It is a fundamental principle that underlies the behavior of electric circuits


---
<style scoped>p,li {font-size:0.88em}</style>

 # Microscopic Origins
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Electrona_in_crystallo_fluentia.svg/200px-Electrona_in_crystallo_fluentia.svg.png'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- The current flowing through a conductor is due to the movement of charged particles (electrons) within the conductor
- The voltage across a conductor is caused by the force exerted on these charged particles by an external electric field
</div>

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Hydraulic Analogy

- Ohm's Law can be visualized as a hydraulic analogy, where the current flowing through a conductor is like the flow of water through a pipe
- The resistance of the conductor is like the frictional force opposing the flow of water in the pipe

---
<style scoped>p,li {font-size:0.84em}</style>

 # Circuit Analysis
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Ohm's Law can be used to analyze and design electric circuits
- By understanding the relationship between voltage, current, and resistance, engineers can design circuits that are efficient and safe
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Ohm_law_mnemonic_principle.svg/170px-Ohm_law_mnemonic_principle.svg.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Ohms_law_wheel_WVOA.svg/220px-Ohms_law_wheel_WVOA.svg.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Resistive Circuits

- Resistive circuits are those that contain only resistors and a power source
- Ohm's Law can be used to predict the current and voltage across each resistor in a circuit

---
<style scoped>p,li {font-size:0.92em}</style>

 # Reactive Circuits with Time-Varying Signals
- Reactive circuits are those that contain capacitors and/or inductors, which store energy in an electric field or magnetic field
- Ohm's Law can be modified to account for the time-varying nature of signals in reactive circuits


---
<style scoped>p,li {font-size:0.92em}</style>

 # Linear Approximations
- Ohm's Law can be linearized for small signal conditions, allowing engineers to make simplifying assumptions about the behavior of electric circuits
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/FourIVcurves.svg/400px-FourIVcurves.svg.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Temperature Effects

- The resistance of a conductor changes with temperature, which can affect the current flowing through it
- Ohm's Law must be modified to account for temperature effects in certain applications

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Relation to Heat Conduction_

- Heat conduction is the transfer of heat between objects in physical contact with each other
- Ohm's Law can be used to predict the heat generated by an electric current flowing through a conductor, and vice versa

---
<style scoped>p,li {font-size:0.88em}</style>

 # Other Versions
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/en/thumb/5/54/Ohms_law_vectors.svg/290px-Ohms_law_vectors.svg.png'/>
</div>
</div>

- There are variations of Ohm's Law that apply to different types of circuits and materials
- For example, the "Ohm's Law for capacitors" states that the current flowing through a capacitor is directly proportional to the voltage across it, and inversely proportional to the capacitance of the capacitor

---
<style scoped>p,li {font-size:0.92em}</style>

 # Magnetic Effects

- Ohm's Law does not account for magnetic effects, such as the interaction between currents and magnetic fields
- However, these effects can be included in more advanced versions of Ohm's Law, such as the "Ohm's Law for magnetically conducting materials"

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Conductive Fluids_
- Ohm's Law can be applied to conductive fluids, such as electrolytes and plasmas
- These fluids can be used in a variety of applications, including electromagnetic sensors and fusion reactors


---
<style scoped>p,li {font-size:0.88em}</style>

 # External Links and Further Reading
- For more information on Ohm's Law and its applications, you can consult the following external links and resources:

+ [Insert list of links to relevant articles, papers, or websites]

I hope this slide presentation helps you understand Ohm's Law and its importance in the field of electrical engineering. Let me know if you have any questions or need further clarification on any of the topics covered!
