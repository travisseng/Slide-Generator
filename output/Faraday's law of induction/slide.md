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

 # Faraday's law of induction

---
<style scoped>p,li {font-size:0.80em}</style>

 # History
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Faraday_emf_experiment.svg/290px-Faraday_emf_experiment.svg.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Faraday_disk_generator.jpg/220px-Faraday_disk_generator.jpg'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Faraday's law of induction was discovered by Michael Faraday in 1831
- It states that a changing magnetic field induces an electromotive force (EMF) in a closed loop of wire
- This discovery revolutionized the understanding of electromagnetism and led to the development of many modern technologies, including generators, motors, and transformers
</div>

</div>


---
<style scoped>p,li {font-size:0.84em}</style>

 # Faraday's Law
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Electromagnetic_induction_-_solenoid_to_loop_-_animation.gif/220px-Electromagnetic_induction_-_solenoid_to_loop_-_animation.gif'/>
</div>
</div>

- The mathematical statement of Faraday's law is:

emf = -N(dΦ/dt)

where emf is the electromotive force (in volts), N is the number of turns of the loop (in units of 1/m), and dΦ/dt is the rate of change of the magnetic flux (in webers per second)

---
<style scoped>p,li {font-size:0.84em}</style>

 # _Mathematical Statement_
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Surface_integral_illustration.svg/220px-Surface_integral_illustration.svg.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/4/45/Salu%27s_left-hand_rule_%28magnetic_induction%29.png'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- The mathematical statement of Faraday's law can be written in terms of the magnetic field strength (B) and the area enclosed by the loop (A):

emf = -N(dB/dt) × A
</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # Maxwell-Faraday Equation
- The Maxwell-Faraday equation is a more general statement of Faraday's law that includes the effects of both magnetic and electric fields:

∇ × E = -∂B/∂t

where E is the electric field (in volts per meter) and B is the magnetic field (in teslas)


---
<style scoped>p,li {font-size:0.96em}</style>

 # Proof

- The proof of Faraday's law involves using the definition of the electromotive force and the equation for the magnetic flux to show that the EMF induced in a loop is proportional to the rate of change of the magnetic flux.

---
<style scoped>p,li {font-size:0.96em}</style>

 # Exceptions
- There are some exceptions to Faraday's law, such as the case where the changing magnetic field is due to a magnetic monopole, which do not induce an EMF according to the law.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Faraday's Law and Relativity

- Faraday's law can be seen as a special case of Einstein's theory of general relativity, which describes how gravity is the curvature of spacetime caused by the presence of mass and energy.
- In this context, the magnetic field can be thought of as a "gravitational" field that curves spacetime in a way that induces an EMF.

---
<style scoped>p,li {font-size:0.88em}</style>

 # Two Phenomena

- Faraday's law can explain two different phenomena:

1. The production of electrical energy through the use of magnetic fields, such as in generators and motors.

2. The manipulation of magnetic fields through the use of electrical currents, such as in transformers and solenoids.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Explanation Based on Four-Dimensional Formalism
- Faraday's law can be understood in terms of a four-dimensional formalism that includes both space and time, which is the basis of Einstein's theory of general relativity.
- In this framework, the magnetic field is seen as a curvature of spacetime that induces an EMF.


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Einstein's View**

- Einstein himself did not explicitly discuss Faraday's law, but he did recognize the importance of electromagnetism in his theory of general relativity.
- In fact, Einstein's theory can be seen as a further development and extension of Faraday's ideas about electromagnetism and the nature of spacetime.