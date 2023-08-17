---
marp: true
math: katex
theme: uncover
style: |
   @import url('https://unpkg.com/tailwindcss@2.2.19/dist/utilities.min.css');
   section {display: flex;flex-flow: column; font-size:35px; letter-spacing:1.4px;}

   header {overflow:visible} header > img.logo {position:absolute; right:15px;}

   header > img.logo {position:absolute; right:15px;}


---
<!-- backgroundColor: white -->
<!-- _class: lead -->

 # **Electrical network**

---
<style scoped>p,li {font-size:0.88em}</style>

 # **Introduction**
- Electrical networks are used to model and analyze electrical circuits
- Can be used for design, simulation, and measurement
- Important in fields such as electronics, electrical engineering, and power systems


---
<style scoped>p,li {font-size:0.88em}</style>

 # Classification

- Electrical networks can be classified into two main types:

+ Linear networks: represent linear electrical circuits

+ Nonlinear networks: represent nonlinear electrical circuits

---
<style scoped>p,li {font-size:0.88em}</style>

 # **By Passivity**

- A passive network is one that does not have any active devices (such as amplifiers or sources)
- Passive networks can be represented using resistors, capacitors, and inductors
- Examples of passive networks include RC filters and LC circuits

---
<style scoped>p,li {font-size:0.88em}</style>

 # By Linearity
- A linear network is one in which the voltage and current are directly proportional
- Linear networks can be represented using linear equations
- Examples of linear networks include series and parallel resonant circuits


---
<style scoped>p,li {font-size:0.88em}</style>

 # _By Lumpiness_
- A lumped network is one in which all the components are connected at a single point (called a "lump")
- Lumped networks can be represented using Thevenin's and Norton's theorems
- Examples of lumped networks include RC filters and voltage dividers


---
<style scoped>p,li {font-size:0.88em}</style>

 # Classification of Sources
- Electrical sources can be classified into two main types:

+ Independent sources: do not depend on any other source

+ Dependent sources: depend on one or more other sources


---
<style scoped>p,li {font-size:0.88em}</style>

 # Applying Electrical Laws

- Ohm's law: voltage = current x resistance
- Kirchoff's laws: sum of voltages around a loop = 0, sum of currents into a node = 0
- These laws can be used to analyze and design electrical networks

---
<style scoped>p,li {font-size:0.84em}</style>

 # Design Methods

- There are several methods for designing electrical networks, including:

+ Analog circuit design: uses analog components such as resistors, capacitors, and inductors

+ Digital circuit design: uses digital components such as logic gates and flip-flops

+ Hybrid circuit design: combines analog and digital components

---
<style scoped>p,li {font-size:0.84em}</style>

 # Network Simulation Software
- There are several software packages available for simulating electrical networks, including:

+ SPICE (Simulation Program with Integrated Circuit Emphasis)

+ PSCAD (Power System Computer-Aided Design)

+ MATLAB/SIMULINK


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Linearization Around Operating Point_
- A linearized model of a nonlinear network is one that approximates the behavior of the network near a certain operating point
- Can be useful for designing control systems and stability analysis


---
<style scoped>p,li {font-size:0.92em}</style>

 # Piecewise-Linear Approximation

- A piecewise-linear approximation of a nonlinear network is one that breaks the network into smaller linear sub-networks
- Can be useful for simple and fast analysis and design

---
<style scoped>p,li {font-size:0.84em}</style>

 # Representation
- Electrical networks can be represented in several ways, including:

+ Equations: uses mathematical equations to describe the behavior of the network

+ Graphs: uses graphs to visually represent the components and their connections

+ Block diagrams: uses blocks to represent the components and their connections


---
<style scoped>p,li {font-size:0.84em}</style>

 # _Design and Analysis Methodologies_
- There are several methodologies for designing and analyzing electrical networks, including:

+ Top-down design: starts with high-level specifications and breaks them down into smaller components

+ Bottom-up design: starts with low-level components and builds them up into a network

+ Model-based design: uses mathematical models to represent the behavior of the network


---
<style scoped>p,li {font-size:0.88em}</style>

 # Measurement
- Electrical networks can be measured using several techniques, including:

+ Voltage and current measurement: uses oscilloscopes or multimeters to measure voltage and current

+ Network analysis: uses specialized equipment such as network analyzers to measure the behavior of the network


---
<style scoped>p,li {font-size:0.84em}</style>

 # Analogies

- Electrical networks can be compared to other systems, including:

+ Water flow: compares the flow of electrical current to the flow of water

+ Traffic flow: compares the flow of electrical current to the flow of traffic

+ Electric circuits: compares the behavior of electrical networks to the behavior of electric circuits

---
<style scoped>p,li {font-size:0.84em}</style>

 # _Specific Topologies_

- There are several specific topologies of electrical networks, including:

+ Power systems: includes power generation, transmission, and distribution

+ Control systems: includes control of temperature, speed, and other parameters

+ Data communication systems: includes data transmission over wired or wireless networks

---
<style scoped>p,li {font-size:0.88em}</style>

 # Conclusion

- Electrical networks are a fundamental part of modern technology
- Can be used for design, simulation, and measurement in a variety of fields
- Understanding electrical networks is essential for any aspiring engineer.