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

 # Reissner–Nordström metric

---
<style scoped>p,li {font-size:0.92em}</style>

 # Introduction
- The Reissner-Nordström (RN) metric is a solution to the Einstein field equations that describes the gravitational field of a charged black hole.
- It was developed by Gunnar Nordström and Hans Reissner in the 1910s.


---
<style scoped>p,li {font-size:0.88em}</style>

 # **The Metric**

- The RN metric is given by:

ds^2 = -e^(-)dt^2 + e^(+)dr^2 + r^2 d\theta^2 + r^2 sin^2\theta d\phi^2

where (t,r,\θ,\φ) are the coordinates, and e^(±) = 1 – 2GM/r is the lapse function.

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Charged Black Holes**
- The RN metric describes a charged black hole with mass M and charge Q.
- The event horizon of the black hole is located at r = 2GM – Q.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Gravitational Time Dilation

- The gravitational time dilation effect causes time to pass more slowly near the event horizon of the black hole.
- The gravitational redshift effect causes light to be blue-shifted as it escapes from the black hole.

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Christoffel Symbols_
- The Christoffel symbols for the RN metric are:

Γ00 = -e^(-) / r^2, Γ01 = Γ02 = 0, Γ11 = e^(+) / r^2, Γ12 = Γ22 = -e^(+) / r^2 sin^2\theta


---
<style scoped>p,li {font-size:0.88em}</style>

 # Tetrad Form
- The RN metric can be written in tetrad form as:

ds^2 = -e(-) + h_0^2 dt^2 + h_1^2 dr^2 + h_2^2 d\theta^2 + h_3^2 sin^2\theta d\phi^2

where h_i are the tetrad components.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Equations of Motion
- The equations of motion for a test particle in the RN metric are:

dt = e^(-) / h_0, dr = h_1 / h_0, d\theta = h_2 / h_0, d\phi = h_3 / h_0


---
<style scoped>p,li {font-size:0.88em}</style>

 # **Alternative Formulation of Metric**
- The RN metric can also be written in the form:

ds^2 = -e^(-) dt^2 + e^(+) dr^2 + r^2 d\theta^2 + r^2 sin^2\theta d\phi^2

which is more suitable for certain applications.


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Quantum Gravitational Corrections to the Metric_
- The RN metric is a classical solution of the Einstein field equations, but it is known that quantum gravitational corrections must be included to obtain a complete description of the black hole.
- These corrections are not yet well understood and are an active area of research in theoretical physics.


---
<style scoped>p,li {font-size:0.88em}</style>

 # Notes
- The RN metric is a simple and important solution of the Einstein field equations, but it has several limitations.
- It does not include the effects of angular momentum or spin, for example.
- The RN metric is often used as a starting point for more detailed studies of black hole physics and gravitational waves.
