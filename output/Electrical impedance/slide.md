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
<!-- backgroundImage: url('backgrounds/aaabstract (10).png') -->
<!-- _class: lead -->

 # _Electrical impedance_

---
<style scoped>p,li {font-size:0.88em}</style>

 # History

- Impedance has been studied for over a century
- Early work by Heaviside, Hertz, and Maxwell laid the foundation for modern impedance theories
- The concept of impedance is essential in understanding how electric circuits behave

---
<style scoped>p,li {font-size:0.88em}</style>

 # Introduction

- Impedance is a measure of the opposition to current flow in an electric circuit
- It is defined as the ratio of voltage to current (Z = V/I)
- Impedance is a complex quantity, with both magnitude and phase angle components

---
<style scoped>p,li {font-size:0.84em}</style>

 # Complex Impedance
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Complex impedance is represented as Z = X + jY, where X is the resistance and Y is the reactance
- The real part of the impedance (X) represents the resistance of the circuit, while the imaginary part (Y) represents the reactance
- Reactance is the opposition to current flow due to the presence of inductive or capacitive elements in the circuit
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Complex_Impedance.svg/200px-Complex_Impedance.svg.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # Complex Voltage and Current
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Impedance_symbol_comparison.svg/165px-Impedance_symbol_comparison.svg.png'/>
</div>
</div>

- The voltage and current in a complex impedance circuit are also complex quantities, with the same magnitude and phase angle as the impedance
- The complex voltage (V) and current (I) can be represented as V = V_r + jV_x, I = I_r + jI_x, where V_r and I_r are the real parts and V_x and I_x are the imaginary parts

---
<style scoped>p,li {font-size:0.92em}</style>

 # Validity of Complex Representation
- The complex representation of impedance is valid for circuits that have both resistance and reactance elements
- The complex representation allows us to analyze and design AC circuits more easily, as it avoids the need for multiple unknowns in the circuit equations


---
<style scoped>p,li {font-size:0.88em}</style>

 # Ohm's Law
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/General_AC_circuit.svg/165px-General_AC_circuit.svg.png'/>
</div>
</div>

- Ohm's law states that the current (I) flowing through a conductor is directly proportional to the voltage (V) applied across it, and inversely proportional to the resistance (R) of the conductor
- The equation for Ohm's law is I = V/R

---
<style scoped>p,li {font-size:0.92em}</style>

 # Phasors

- Phasors are mathematical objects used to represent complex quantities, such as impedances and voltages/currents, in a circuit
- Phasors are drawn as vectors in a complex plane, with the real part of the vector representing the real component and the imaginary part representing the imaginary component

---
<style scoped>p,li {font-size:0.92em}</style>

 # Device Examples

- Resistors, inductors, and capacitors are examples of devices that can be represented using impedance analysis
- Each device has a specific impedance curve, which describes how the impedance of the device changes with frequency

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Deriving the Device-Specific Impedances_
- The impedance of each device can be derived using formulas that relate the device's properties to its impedance
- For example, the impedance of a resistor (R) is given by Z = R, while the impedance of an inductor (L) is given by Z = 2πfL, where f is the frequency of the current flowing through the inductor


---
<style scoped>p,li {font-size:0.92em}</style>

 # Resistor
- The impedance of a resistor (R) is given by Z = R
- The reactance of a resistor (X) is given by X = 1/R


---
<style scoped>p,li {font-size:0.92em}</style>

 # Inductor
- The impedance of an inductor (L) is given by Z = 2πfL, where f is the frequency of the current flowing through the inductor
- The reactance of an inductor (X) is given by X = 2πfL


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Capacitor_
- The impedance of a capacitor (C) is given by Z = 1/C, where C is the capacitance of the capacitor
- The reactance of a capacitor (X) is given by X = 1/C


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Combining Impedances**
- When two or more devices are connected in series or parallel, their impedances can be combined using the principles of circuit analysis
- The total impedance of a series circuit is the sum of the impedances of each device, while the total impedance of a parallel circuit is the ratio of the total current to the total voltage


---
<style scoped>p,li {font-size:0.92em}</style>

 # Series Combination
- When two or more devices are connected in series, their impedances can be added together to obtain the total impedance of the circuit
- The total impedance (Z_total) is given by Z_total = Z1 + Z2 + ... + Zn, where Z1, Z2, ..., Zn are the impedances of each device in the series circuit


---
<style scoped>p,li {font-size:0.92em}</style>

 # Parallel Combination

- When two or more devices are connected in parallel, their impedances can be combined by dividing the total current (I_total) by the total voltage (V_total) to obtain the total impedance of the circuit
- The total impedance (Z_total) is given by Z_total = I_total/V_total, where I_total and V_total are the total current and total voltage of the parallel circuit

---
<style scoped>p,li {font-size:0.92em}</style>

 # Measurement

- Impedance can be measured using instruments such as impedance meters and network analyzers
- The measurement process typically involves applying a known voltage or current to the device under test and measuring the resulting voltage or current

---
<style scoped>p,li {font-size:0.92em}</style>

 # Example

- An example of a complex impedance circuit is a series RLC circuit, which consists of a resistor (R), an inductor (L), and a capacitor (C) connected in series
- The total impedance of the circuit can be calculated using the formulas for each device's impedance, and the resulting impedance curve can be used to analyze the behavior of the circuit

---
<style scoped>p,li {font-size:0.92em}</style>

 # Variable Impedance

- Some devices, such as variable capacitors and inductors, have impedances that can be varied over a range of values
- These devices are useful in applications where the impedance of the circuit needs to be adjusted or controlled

---
<style scoped>p,li {font-size:0.88em}</style>

 # _Notes_
- Impedance is a measure of the opposition to current flow in an electric circuit
- Complex impedance is a more accurate representation of impedance that takes into account the presence of reactance components in the circuit
- Ohm's law and the formulas for deriving device-specific impedances are fundamental principles of electrical engineering that are used extensively in the design and analysis of AC circuits.
