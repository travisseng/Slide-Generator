---
marp: true
math: katex
theme: gaia
paginate: True
style: |
   @import url('https://unpkg.com/tailwindcss@2.2.19/dist/utilities.min.css');
   :root {--color-fg-default: #FFFFFF; --color-foreground: #FFFFFF;}

   section {display: flex;flex-flow: column; font-size:35px; letter-spacing:1.4px;}

   header {overflow:visible} header > img.logo {position:absolute; right:15px;}

   header > img.logo {position:absolute; right:15px;}


---
<!-- backgroundImage: url('backgrounds/aaabstract.png') -->
<!-- _class: lead -->

 # **Analytical mechanics**

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Motivation for Analytical Mechanics**

- Analytical mechanics is a powerful tool for studying the motion of objects in the presence of forces and constraints.
- It provides a framework for understanding the behavior of complex systems and making predictions about their future motion.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Intrinsic Motion
- Intrinsic motion refers to the motion of an object relative to its own body frame.
- This type of motion is important in understanding the dynamics of rigid bodies and other non-deformable objects.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Generalized Coordinates and Constraints
- Generalized coordinates are a set of coordinates that describe the position and orientation of an object in a way that is independent of the choice of reference frame.
- Constraints are conditions that restrict the motion of an object, such as joint limits in robotics or the fixed endpoints of a massless string.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Difference between Curvillinear and Generalized Coordinates

- Curvillinear coordinates describe the position and orientation of an object using a set of parametric equations.
- Generalized coordinates, on the other hand, describe the motion of an object using a set of independent variables that are not necessarily parametrically related.

---
<style scoped>p,li {font-size:0.96em}</style>

 # **D'Alembert's Principle**
- D'Alembert's principle is a fundamental concept in analytical mechanics that states that the time rate of change of the generalized momentum is equal to the net force acting on an object.


---
<style scoped>p,li {font-size:0.96em}</style>

 # Holonomic Constraints

- Holonomic constraints are constraints that can be described using a set of holonomic equations, which are equations that involve the derivatives of the generalized coordinates with respect to time.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Lagrangian Mechanics
- Lagrangian mechanics is a branch of analytical mechanics that uses the Lagrangian function to describe the motion of objects.
- The Lagrangian function is defined as the difference between the kinetic energy and potential energy of an object.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Hamiltonian Mechanics

- Hamiltonian mechanics is another branch of analytical mechanics that uses the Hamiltonian function to describe the motion of objects.
- The Hamiltonian function is defined as the sum of the kinetic energy and potential energy of an object.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Properties of the Lagrangian and Hamiltonian Functions
- Both the Lagrangian and Hamiltonian functions have certain properties that make them useful for studying the motion of objects.
- These properties include conservation of energy, momentum, and angular momentum.


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Principle of Least Action**
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- The principle of least action is a fundamental concept in analytical mechanics that states that the motion of an object is such as to minimize its action, which is a measure of the total energy expended by the object.
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Least_action_principle.svg/250px-Least_action_principle.svg.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Hamiltonian-Jacobi Mechanics
- Hamiltonian-Jacobi mechanics is a branch of analytical mechanics that uses the Hamiltonian and Jacobi functions to describe the motion of objects.
- The Hamiltonian function describes the kinetic energy of an object, while the Jacobi function describes its potential energy.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Routhian Mechanics

- Routhian mechanics is a branch of analytical mechanics that uses the Routhian function to describe the motion of objects.
- The Routhian function is defined as the difference between the kinetic energy and potential energy of an object, plus the sum of the constraints acting on the object.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Appellian Mechanics
- Appellian mechanics is a branch of analytical mechanics that uses the Appellian function to describe the motion of objects.
- The Appellian function is defined as the difference between the kinetic energy and potential energy of an object, plus the sum of the constraints acting on the object, minus the total energy of the object.


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Extensions to Classical Field Theory**

- Analytical mechanics can be extended to classical field theory by using the concept of fields to describe the motion of objects.
- This allows for the study of more complex systems, such as electromagnetic fields and fluid dynamics.

---
<style scoped>p,li {font-size:0.88em}</style>

 # **Symmetry, Conservation, and Noether's Theorem**

- Symmetry is an important concept in analytical mechanics that refers to the lack of change in the properties of an object under certain transformations.
- Conservation laws are fundamental principles that describe the conservation of certain quantities, such as energy and momentum.
- Noether's theorem states that for every continuous symmetry in a physical system, there is a corresponding conservation law.

---
<style scoped>p,li {font-size:0.92em}</style>

 # References and Notes

- Here are some references and notes on analytical mechanics for further reading.

I hope this slide presentation helps you understand the basics of analytical mechanics!