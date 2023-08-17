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

 # Classical mechanics

---
<style scoped>p,li {font-size:0.84em}</style>

 # Description of the Theory
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Tir_parab%C3%B2lic.svg/220px-Tir_parab%C3%B2lic.svg.png'/>
</div>
</div>

- Classical mechanics is a branch of physics that studies the motion of objects using the principles of Newtonian mechanics
- Developed by Sir Isaac Newton in the late 17th and early 18th centuries
- Based on three laws of motion and the concept of force

---
<style scoped>p,li {font-size:0.88em}</style>

 # Position and its Derivatives

- Position is a measure of an object's location in space
- Derivatives are used to describe the changing position of an object over time
- Derivatives include velocity, acceleration, and jerk (the rate of change of acceleration)

---
<style scoped>p,li {font-size:0.88em}</style>

 # Velocity and Speed

- Velocity is the rate of change of position with respect to time
- Speed is the magnitude of velocity
- Velocity and speed are related by the equation v = d/t, where v is velocity, d is distance, and t is time

---
<style scoped>p,li {font-size:0.92em}</style>

 # Acceleration

- Acceleration is the rate of change of velocity with respect to time
- Acceleration is related to force by Newton's second law (F = ma), where F is force, m is mass, and a is acceleration

---
<style scoped>p,li {font-size:0.92em}</style>

 # Frames of Reference

- Frames of reference are used to describe the motion of objects relative to each other
- There are several different frames of reference, including fixed, rotating, and moving frames

---
<style scoped>p,li {font-size:0.88em}</style>

 # **Forces and Newton's Second Law**
- Forces are pushes or pulls that act on objects
- Newton's second law states that force equals mass times acceleration (F = ma)
- This law applies to all objects, regardless of their mass or size


---
<style scoped>p,li {font-size:0.88em}</style>

 # Work and Energy
- Work is the product of force and displacement (W = F \* d)
- Energy is the ability to do work (energy = force x distance)
- There are several different forms of energy, including kinetic energy (the energy of motion), potential energy (stored energy), and thermal energy (the energy of heat)


---
<style scoped>p,li {font-size:0.88em}</style>

 # **Beyond Newton's Laws**
- Newton's laws are a good approximation of the behavior of large, slow-moving objects
- However, they do not accurately describe the behavior of very small or very fast-moving objects
- For these cases, more advanced theories such as quantum mechanics and special relativity are needed


---
<style scoped>p,li {font-size:0.88em}</style>

 # _Limits of Validity_
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Newton's laws are only valid for objects that are large compared to the size of atoms and for speeds much slower than the speed of light
- At smaller scales and higher speeds, other theories such as quantum mechanics and special relativity become more important
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Physicsdomains.svg/380px-Physicsdomains.svg.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # The Newtonian Approximation to Special Relativity
- Special relativity is a theory that describes the behavior of objects at very high speeds (approaching the speed of light)
- Newton's laws can be used as an approximation to special relativity for objects moving at slow speeds


---
<style scoped>p,li {font-size:0.92em}</style>

 # The Classical Approximation to Quantum Mechanics
- Quantum mechanics is a theory that describes the behavior of very small objects (such as atoms and subatomic particles)
- Classical mechanics can be used as an approximation to quantum mechanics for large, slow-moving objects


---
<style scoped>p,li {font-size:0.76em}</style>

 # _History_
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- The development of classical mechanics can be traced back to ancient Greek philosophers such as Aristotle and Archimedes
- However, it was not until the work of Sir Isaac Newton in the late 17th and early 18th centuries that the modern theory of classical mechanics began to take shape
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Theory_of_impetus.svg/180px-Theory_of_impetus.svg.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Portrait_of_Sir_Isaac_Newton%2C_1689.jpg/240px-Portrait_of_Sir_Isaac_Newton%2C_1689.jpg'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Joseph_Louis_Lagrange2.jpg/180px-Joseph_Louis_Lagrange2.jpg'/>
</div>
</div>
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/WilliamRowanHamilton.jpeg/180px-WilliamRowanHamilton.jpeg'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.96em}</style>

 # Branches

- Classical mechanics has several branches, including statics (the study of objects at rest), dynamics (the study of objects in motion), and kinematics (the study of the motion of objects without considering the forces that cause the motion)

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Notes**

- Classical mechanics is a powerful tool for understanding the behavior of objects in the everyday world, but it has its limitations (such as not applying to very small or very fast-moving objects)
- It is important to understand the limitations of classical mechanics and when to use more advanced theories such as quantum mechanics and special relativity.