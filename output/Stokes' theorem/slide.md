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

 # _Stokes' theorem_

---
<style scoped>p,li {font-size:0.96em}</style>

 # _Theorem_
- Stokes' theorem states that for a closed curve C in the plane, the line integral of the curl of a vector field around C is equal to the surface integral of the divergence of the vector field over any surface enclosed by C.


---
<style scoped>p,li {font-size:0.96em}</style>

 # Proof
- The proof of Stokes' theorem involves a sequence of steps that we will go through in detail.


---
<style scoped>p,li {font-size:0.96em}</style>

 # **Elementary Proof**

- The elementary proof of Stokes' theorem involves parametrizing the integral and defining the pullback of a vector field.

---
<style scoped>p,li {font-size:0.96em}</style>

 # **First Step (Parametrization of Integral)**
- The first step is to parametrize the integral of the curl of a vector field around a closed curve C. We can do this by choosing a parameterized curve C(t), where t is a real number from 0 to 1, and integrating the curl of the vector field over this curve.


---
<style scoped>p,li {font-size:0.96em}</style>

 # Second Step (Defining the Pullback)

- The second step is to define the pullback of a vector field along a parameterized curve C(t). This involves taking the derivative of the vector field with respect to t and evaluating it at each point on the curve.

---
<style scoped>p,li {font-size:0.96em}</style>

 # Third Step (Second Equation)
- The third step is to use the definition of the pullback to write down an equation that relates the line integral of the curl of a vector field around C to the surface integral of the divergence of the vector field over any surface enclosed by C.


---
<style scoped>p,li {font-size:0.96em}</style>

 # Fourth Step (Reduction to Green's Theorem)
- The fourth step is to reduce Stokes' theorem to Green's theorem, which states that the line integral of a vector field around a closed curve is equal to the surface integral of the curl of the vector field over any surface enclosed by the curve. This allows us to simplify the equation from the third step.


---
<style scoped>p,li {font-size:0.96em}</style>

 # **Proof via Differential Forms**

- Another way to prove Stokes' theorem is by using differential forms. The idea is to define a differential form on the surface enclosed by C and then use the exterior derivative to relate the line integral of the curl of the vector field around C to the surface integral of the divergence of the vector field over the surface.

---
<style scoped>p,li {font-size:0.96em}</style>

 # Applications

- Stokes' theorem has many applications in physics, engineering, and mathematics. For example, it can be used to calculate the flux of a vector field across a surface, or the circulation of a vector field around a closed curve. It is also closely related to other important results such as Green's theorem and the Helmholtz theorems.

---
<style scoped>p,li {font-size:0.96em}</style>

 # Irrotational Fields

- One important application of Stokes' theorem is in the study of irrotational fields, which are vector fields that have no rotational component. These fields can be characterized by the fact that their curl is zero everywhere. Stokes' theorem allows us to relate the line integral of an irrotational field around a closed curve to the surface integral of the field over any surface enclosed by the curve.

---
<style scoped>p,li {font-size:0.96em}</style>

 # _The Helmholtz's Theorems_

- The Helmholtz theorems are a set of results that relate the line integral of a vector field around a closed curve to the surface integral of the field over any surface enclosed by the curve. They are closely related to Stokes' theorem and can be used to simplify many calculations involving vector fields.

---
<style scoped>p,li {font-size:0.96em}</style>

 # Proof of the Helmholtz's Theorems
- The proof of the Helmholtz theorems involves using Stokes' theorem to relate the line integral of a vector field around a closed curve to the surface integral of the field over any surface enclosed by the curve. This allows us to simplify many calculations involving vector fields.


---
<style scoped>p,li {font-size:0.96em}</style>

 # Conservative Forces

- Another important application of Stokes' theorem is in the study of conservative forces, which are forces that conserve energy. These forces can be characterized by the fact that their line integral around any closed curve is zero. Stokes' theorem allows us to relate the line integral of a conservative force around a closed curve to the surface integral of the force over any surface enclosed by the curve.

---
<style scoped>p,li {font-size:0.96em}</style>

 # _Maxwell's Equations_
- Stokes' theorem also has many applications in electromagnetism, particularly in Maxwell's equations. These equations describe how electric and magnetic fields interact with charges and currents, and they can be used to calculate a wide range of physical phenomena, such as the electric field around a point charge or the magnetic field around a current-carrying wire.


---
<style scoped>p,li {font-size:0.96em}</style>

 # **Notes**

- Some additional notes on Stokes' theorem include the fact that it is a fundamental result in mathematics and physics, and that it has many important consequences and applications. It is also closely related to other important results, such as Green's theorem and the Helmholtz theorems.