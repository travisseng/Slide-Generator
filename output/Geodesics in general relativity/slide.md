---
marp: true
math: katex
theme: default
style: |
   @import url('https://unpkg.com/tailwindcss@2.2.19/dist/utilities.min.css');
   section {display: flex;flex-flow: column; font-size:35px; letter-spacing:1.4px;}

   header {overflow:visible} header > img.logo {position:absolute; right:15px;}

   header > img.logo {position:absolute; right:15px;}


---
<!-- backgroundColor: white -->
<!-- _class: lead -->

 # **Geodesics in general relativity**

---
<style scoped>p,li {font-size:0.92em}</style>

 # Introduction

- Geodesics are the shortest paths on a curved surface, and play a crucial role in general relativity
- In this presentation, we will explore the mathematical expression of geodesics in general relativity, their equivalent expression using coordinate time as parameter, and the different ways to derive the geodesic equation

---
<style scoped>p,li {font-size:0.88em}</style>

 # Mathematical Expression

- The geodesic equation for a massless particle can be written as:

$$\frac{d^2x^\mu}{d\lambda^2} + \Gamma^\mu_{\nu\rho}\frac{dx^\nu}{d\lambda}\frac{dx^\rho}{d\lambda} = 0$$

where $\lambda$ is an affine parameter, $x^\mu$ is the position of the particle, and $\Gamma^\mu_{\nu\rho}$ are the Christoffel symbols

---
<style scoped>p,li {font-size:0.88em}</style>

 # _Equivalent Expression using Coordinate Time as Parameter_
- Instead of using the affine parameter $\lambda$, we can use coordinate time $t$ as the parameter

$$\frac{d^2x^\mu}{dt^2} + \Gamma^\mu_{\nu\rho}\frac{dx^\nu}{dt}\frac{dx^\rho}{dt} = 0$$

This equivalent expression is often more convenient to work with, especially when dealing with particle motion in flat space-time


---
<style scoped>p,li {font-size:0.84em}</style>

 # Derivation directly from the Equivalence Principle

- The equivalence principle states that all observers in uniform motion relative to one another should experience the same physical laws

By applying this principle to the concept of a shortest path, we can derive the geodesic equation

$$\frac{d^2x^\mu}{dt^2} = \frac{1}{2}\nabla_\nu\left(g^{\mu\nu} + \Gamma^{\mu\nu}\right)$$

where $g^{\mu\nu}$ is the metric tensor, $\Gamma^{\mu\nu}$ are the Christoffel symbols, and $\nabla_\nu$ is the covariant derivative

---
<style scoped>p,li {font-size:0.80em}</style>

 # _Deriving the Geodesic Equation via an Action_
- Another way to derive the geodesic equation is by considering the action of a particle moving on a curved space-time

The action for a massless particle can be written as:

$$S = \int\sqrt{g(\dot{x}^2 - m^2)}d\lambda$$

where $g$ is the determinant of the metric tensor, $m$ is the rest mass of the particle, and $\dot{x}$ is the velocity of the particle

By varying this action with respect to the position of the particle, we can derive the geodesic equation


---
<style scoped>p,li {font-size:0.92em}</style>

 # Equation of Motion may follow from the Field Equations for Empty Space
- In some cases, the geodesic equation may be derived by solving the field equations for empty space

For example, in the case of a charged particle, the geodesic equation can be derived from Maxwell's equations and the Einstein field equations


---
<style scoped>p,li {font-size:0.84em}</style>

 # Extension to the Case of a Charged Particle

- To extend the previous equation to the case of a charged particle, we need to include the electromagnetic field

The geodesic equation for a charged particle can be written as:

$$\frac{d^2x^\mu}{dt^2} + \Gamma^\mu_{\nu\rho}\frac{dx^\nu}{dt}\frac{dx^\rho}{dt} = \frac{1}{2}\left(F_{\nu\rho} - Q\Gamma_{\nu\rho}\right)^2$$

where $F_{\nu\rho}$ is the electromagnetic field strength, $Q$ is the charge of the particle, and $\Gamma_{\nu\rho}$ are the Christoffel symbols

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Geodesics as Curves of Stationary Interval_

- In a flat space-time, the geodesics are simply straight lines

However, in a curved space-time, the geodesics can be thought of as curves of stationary interval, which are the shortest paths between two points on the space-time

---
<style scoped>p,li {font-size:0.88em}</style>

 # Derivation using Autoparallel Transport

- Another way to derive the geodesic equation is by using the concept of autoparallel transport

Autoparallel transport is a way of parallel transporting a vector along a curve, such that the magnitude of the vector remains constant

By using this concept, we can derive the geodesic equation for a massless particle

---
<style scoped>p,li {font-size:0.80em}</style>

 # **Bibliography**
- Some of the key references for this presentation include:

+ "Gravitation" by Charles W. Misner, Kip S. Thorne, and John A. Wheeler

+ "Differential Geometry and Relativity" by Michael Spivak

+ "Introduction to General Relativity" by Sean Carroll

Note: The above slides provide a basic outline of the key concepts related to geodesics in general relativity. For a more detailed and rigorous treatment, please consult the references listed in the bibliography.
