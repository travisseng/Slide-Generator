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

 # Capacitor

---
<style scoped>p,li {font-size:0.80em}</style>

 # History
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Leidse_flessen_Museum_Boerhave_december_2003_2.jpg/170px-Leidse_flessen_Museum_Boerhave_december_2003_2.jpg'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Radio_Times_-_1923-12-28_-_page_39_-_Dubilier.png/193px-Radio_Times_-_1923-12-28_-_page_39_-_Dubilier.png'/>
</div>
</div>

- Capacitors have been known since the 17th century
- Early uses included electrostatic generators and Leyden jars
- Modern capacitors were developed in the early 20th century

---
<style scoped>p,li {font-size:0.80em}</style>

 # **Theory of Operation**
- Capacitors store energy in an electric field
- Capacitance is proportional to plate area and inversely proportional to distance between plates
- Energy stored in a capacitor is given by:

E = (1/2)CV^2

where E is the energy, C is the capacitance, V is the voltage


---
<style scoped>p,li {font-size:0.80em}</style>

 # Overview
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Capacitor_schematic_with_dielectric.svg/220px-Capacitor_schematic_with_dielectric.svg.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Plattenkondensator_hg.jpg/220px-Plattenkondensator_hg.jpg'/>
</div>
</div>

- Capacitors are passive components that store energy
- They have many applications in electronics and electrical systems
- Types of capacitors include ceramic, film, and electrolytic

---
<style scoped>p,li {font-size:0.84em}</style>

 # **Hydraulic Analogy**
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Capacitor-animation.gif/220px-Capacitor-animation.gif'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Capacitance can be thought of as a "pressure" in an electric circuit
- Just as water flows through a pipe, current flows through a capacitor
- The "pressure" inside the capacitor is proportional to the voltage applied
</div>

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Circuit Equivalence at Short-Time Limit and Long-Time Limit

- In DC circuits, a capacitor can be replaced by an open circuit at short times
- At long times, a capacitor can be replaced by a wire of negligible resistance

---
<style scoped>p,li {font-size:0.76em}</style>

 # Parallel-Plate Capacitor
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Parallel_plate_capacitor.svg/220px-Parallel_plate_capacitor.svg.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Big_SMD_capacitor_2.jpg/220px-Big_SMD_capacitor_2.jpg'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- A parallel-plate capacitor is a simple type of capacitor with two metal plates separated by a dielectric material
- The capacitance of a parallel-plate capacitor is given by:

C = (ε0A/d)

where C is the capacitance, ε0 is the permittivity of free space, A is the area of the plates, d is the distance between the plates
</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # Interleaved Capacitor
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- An interleaved capacitor is a type of capacitor that has multiple layers of metal foil separated by dielectric material
- This type of capacitor can store more energy than a single parallel-plate capacitor
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Interleaved_Capacitor.jpg/220px-Interleaved_Capacitor.jpg'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # Energy Stored in a Capacitor
- The energy stored in a capacitor is given by:

E = (1/2)CV^2

where E is the energy, C is the capacitance, V is the voltage


---
<style scoped>p,li {font-size:0.88em}</style>

 # Current-Voltage Relation

- The current through a capacitor is given by:

I = CdV/dt

where I is the current, C is the capacitance, dV/dt is the rate of change of voltage

---
<style scoped>p,li {font-size:0.88em}</style>

 # DC Circuits
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Capacitors in DC circuits can be used for energy storage and filtering
- The voltage across a capacitor in a DC circuit will decay over time
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/RC_switch.svg/220px-RC_switch.svg.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # _AC Circuits_

- Capacitors in AC circuits can be used for power factor correction, harmonic filtering, and noise suppression
- The current through a capacitor in an AC circuit will oscillate at the same frequency as the input voltage

---
<style scoped>p,li {font-size:0.84em}</style>

 # _Laplace Circuit Analysis (s-Domain)_

- The Laplace transform can be used to analyze circuits with capacitors
- The transfer function of a capacitor is given by:

H(s) = (1/sC)

where H(s) is the transfer function, C is the capacitance

---
<style scoped>p,li {font-size:0.76em}</style>

 # Circuit Analysis
- Capacitors can be analyzed using circuit equations and simulations
- The analysis of capacitors in circuits is important for designing and optimizing electronic systems
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Capacitors_in_parallel.svg/220px-Capacitors_in_parallel.svg.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Kondensator_C1_plus_C2.svg/220px-Kondensator_C1_plus_C2.svg.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Capacitors_in_series.svg/220px-Capacitors_in_series.svg.png'/>
</div>
</div>
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Kondensator_C1_C2_Reihe.svg/220px-Kondensator_C1_C2_Reihe.svg.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Non-Ideal Behavior

- Real capacitors exhibit non-ideal behavior due to factors such as resistance, leakage, and dielectric absorption
- These effects can be modeled using equations such as the Cole-Cole equation

---
<style scoped>p,li {font-size:0.92em}</style>

 # Breakdown Voltage

- Capacitors can experience breakdown at high voltages, leading to failure of the component
- The breakdown voltage of a capacitor is determined by the strength of the dielectric material and the geometry of the capacitor

---
<style scoped>p,li {font-size:0.88em}</style>

 # **Equivalent Circuit**
- An equivalent circuit can be used to model the behavior of a capacitor in a circuit
- This type of circuit takes into account the non-ideal behavior of the capacitor and can be used for design and analysis
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Capacitor_equivalent_circuits.svg/220px-Capacitor_equivalent_circuits.svg.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Q Factor**

- The Q factor of a capacitor is a measure of its quality factor, or how well it stores energy
- A higher Q factor means that the capacitor will store more energy and have less loss due to resistance and other factors

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Ripple Current_
- Ripple current is the variation in current through a capacitor caused by changes in voltage
- This type of current can be reduced using techniques such as filtering or smoothing


---
<style scoped>p,li {font-size:0.92em}</style>

 # Capacitance Instability
- Capacitors can exhibit instability in their capacitance due to factors such as temperature and aging
- This can lead to changes in the behavior of the circuit and may require compensation using other components


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Current and Voltage Reversal_
- In some cases, the current and voltage across a capacitor can reverse, leading to unexpected behavior in the circuit
- This type of behavior is more common in AC circuits than DC circuits


---
<style scoped>p,li {font-size:0.92em}</style>

 # Dielectric Absorption
- Dielectric absorption is the phenomenon where a dielectric material absorbs energy from an electric field and releases it as heat
- This can lead to changes in the behavior of the capacitor and may require compensation using other components


---
<style scoped>p,li {font-size:0.92em}</style>

 # Leakage

- Leakage is the phenomenon where the dielectric material of a capacitor leaks charge over time
- This can lead to a decrease in the capacitance of the capacitor and may require compensation using other components

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Electrolytic Failure from Disuse**
- Electrolytic capacitors can fail due to disuse, leading to loss of energy storage and other functions
- This type of failure is more common in capacitors that are not used for long periods of time


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Lifespan_

- The lifespan of a capacitor can be affected by factors such as usage, temperature, and aging
- Some types of capacitors have a longer lifespan than others, such as electrolytic capacitors

---
<style scoped>p,li {font-size:0.92em}</style>

 # Capacitor Types
- There are many different types of capacitors available, including ceramic, film, and electrolytic
- Each type has its own strengths and weaknesses, and is suited to different applications


---
<style scoped>p,li {font-size:0.84em}</style>

 # Dielectric Materials
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Condensators.JPG/220px-Condensators.JPG'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Electronic-Component-Elec-Capacitors.jpg/220px-Electronic-Component-Elec-Capacitors.jpg'/>
</div>
</div>

- Dielectric materials are the heart of a capacitor, and there are many different types available
- The choice of dielectric material depends on the application and requirements of the circuit

---
<style scoped>p,li {font-size:0.92em}</style>

 # Voltage-Dependent Capacitors

- Some capacitors change capacitance in response to changes in voltage
- This type of capacitor is useful for applications such as voltage regulation and power factor correction

---
<style scoped>p,li {font-size:0.92em}</style>

 # Frequency-Dependent Capacitors

- Some capacitors change capacitance in response to changes in frequency
- This type of capacitor is useful for applications such as audio filtering and oscillation

---
<style scoped>p,li {font-size:0.84em}</style>

 # Styles
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Photo-SMDcapacitors.jpg/220px-Photo-SMDcapacitors.jpg'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Axial_electrolytic_capacitors.jpg/220px-Axial_electrolytic_capacitors.jpg'/>
</div>
</div>

- Capacitors come in a variety of styles, including through-hole, surface-mount, and chip capacitors
- The choice of style depends on the application and requirements of the circuit

---
<style scoped>p,li {font-size:0.92em}</style>

 # Capacitor Markings
- Capacitors often have markings that indicate their characteristics and specifications
- These markings can include information such as the capacitance, voltage rating, and tolerance


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Three-/Four-Character Marking Code for Larger Capacitors_
- Larger capacitors may use a three- or four-character marking code to indicate their specifications
- This code is often used in conjunction with other markings such as the capacitance and voltage rating


---
<style scoped>p,li {font-size:0.92em}</style>

 # Two-Character Marking Code for Small Capacitors
- Small capacitors may use a two-character marking code to indicate their specifications
- This code is often used in conjunction with other markings such as the capacitance and voltage rating


---
<style scoped>p,li {font-size:0.92em}</style>

 # **RKM Code**
- The RKM code is a system for indicating the specifications of a capacitor using a combination of letters and numbers
- This code is commonly used for electrolytic capacitors


---
<style scoped>p,li {font-size:0.92em}</style>

 # Historical Background
- Capacitors have been known since the 17th century, and were first used in electrostatic generators and Leyden jars
- The modern capacitor was developed in the early 20th century using new materials such as ceramic and film


---
<style scoped>p,li {font-size:0.88em}</style>

 # Applications
- Capacitors have a wide range of applications in electronics and electrical systems, including energy storage, power conditioning, and filtering
- They are also used in pulsed power and weapons, motor starters, signal processing, and other areas
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Mylar-film_oil-filled_low-inductance_capacitor_6.5_MFD_%40_5000_VDC.jpg/170px-Mylar-film_oil-filled_low-inductance_capacitor_6.5_MFD_%40_5000_VDC.jpg'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Notes_
- Capacitors are an important component in many electronic systems, and their characteristics and specifications must be carefully considered for optimal performance
- This presentation has covered the main topics related to capacitors, including theory of operation, types, and applications.
