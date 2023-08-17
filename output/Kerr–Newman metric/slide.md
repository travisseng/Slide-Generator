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

 # Kerr–Newman metric

---
<style scoped>p,li {font-size:0.92em}</style>

 # History

- The Kerr-Newman metric was first introduced by Roy Kerr and Ezra Newman in the 1960s as a solution to the Einstein field equations with charged and rotating matter.
- The Kerr-Newman metric is important in astrophysics because it describes the spacetime geometry of black holes and other extreme objects.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Overview of the Solution
- The Kerr-Newman metric is a solution to the Einstein field equations that describes the spacetime geometry of rotating, charged matter.
- The solution is given in terms of the mass, charge, and angular momentum of the object.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Limiting Cases

- The Kerr-Newman metric reduces to the Kerr metric in the limit where the charge and angular momentum are zero.
- In the limit where the mass and angular momentum are zero, but the charge is nonzero, the solution is known as the Reissner-Nordström metric.

---
<style scoped>p,li {font-size:0.88em}</style>

 # The Metric
- The Kerr-Newman metric is described by the line element:

ds^2 = -dt^2 + (2Mr)^2 / (r^2 + a^2 \cos^2\theta) d\phi^2 - (r^2 + a^2)^2 / (r^2 + a^2 \cos^2\theta) dr^2
- Where M is the mass, a is the angular momentum, and r and $\theta$ are the usual spherical coordinates.


---
<style scoped>p,li {font-size:0.84em}</style>

 # Boyer-Lindquist Coordinates

- The Boyer-Lindquest coordinates are a set of coordinates that simplify the line element of the Kerr-Newman metric.
- In these coordinates, the metric takes the form:

ds^2 = -dt^2 + (2Mr)^2 / (r^2 + a^2 \cos^2\theta) d\phi^2 - (r^2 + a^2)^2 / (r^2 + a^2 \cos^2\theta) dr^2
- These coordinates are useful for studying the properties of the Kerr-Newman metric.

---
<style scoped>p,li {font-size:0.88em}</style>

 # Electromagnetic Field Tensor in Boyer-Lindquist Form

- The electromagnetic field tensor can be written in Boyer-Lindquist form as:

F = (2Q/r^2, 0, 0, -2Q/r^2)
- Where Q is the charge of the object and r is the distance from the center of the object.

---
<style scoped>p,li {font-size:0.84em}</style>

 # Kerr-Schild Coordinates

- The Kerr-Schild coordinates are another set of coordinates that simplify the line element of the Kerr-Newman metric.
- In these coordinates, the metric takes the form:

ds^2 = -dt^2 + (2Mr)^2 / (r^2 + a^2 \cos^2\theta) d\phi^2 - dr^2 + d\theta^2
- These coordinates are useful for studying the properties of the Kerr-Newman metric in the equatorial plane.

---
<style scoped>p,li {font-size:0.88em}</style>

 # Electromagnetic Fields in Kerr-Schild Form
- The electromagnetic field tensor can be written in Kerr-Schild form as:

F = (0, -2Qr, 0, 2Qr)
- These coordinates are useful for studying the properties of the Kerr-Newman metric in the equatorial plane.


---
<style scoped>p,li {font-size:0.84em}</style>

 # Irreducible Mass

- The irreducible mass is a measure of the total energy of the object, including both the rest mass and the rotational energy.
- The irreducible mass can be expressed as:

M = (m) + (a^2/2G)
- Where m is the rest mass, a is the angular momentum, G is the gravitational constant, and (a^2/2G) is the rotational energy.

---
<style scoped>p,li {font-size:0.84em}</style>

 # Important Surfaces
- The important surfaces in the Kerr-Newman geometry include the event horizon, the ergosphere, and the equatorial plane.
- The event horizon is the boundary beyond which nothing can escape from the black hole.
- The ergosphere is a region outside of the event horizon where the rotation of the black hole creates a "gravitational drag" effect that can extract energy from objects that enter it.
- The equatorial plane is a plane that passes through the center of the black hole and is perpendicular to its axis of rotation.


---
<style scoped>p,li {font-size:0.80em}</style>

 # Equations of Motion
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Spinning_and_chargend_black_hole_with_accretion_disk.jpg/220px-Spinning_and_chargend_black_hole_with_accretion_disk.jpg'/>
</div>
</div>

- The equations of motion for a particle in the Kerr-Newman geometry can be derived from the geodesic equation.
- In Boyer-Lindquist coordinates, the geodesic equation takes the form:

(d^2x^a/d\lambda^2) + (2GMr)^2 / (r^2 + a^2 \cos^2\theta) \delta^a_b = 0
- Where x^a is the position of the particle, \lambda is an affine parameter, G is the gravitational constant, and M is the mass of the black hole.

---
<style scoped>p,li {font-size:0.80em}</style>

 # Bibliography

- Some important references for the Kerr-Newman metric include:

+ Kerr, R. P. (1963). "Cosmological solutions of the Einstein field equations". Physical Review Letters, 11(10), 237-240.

+ Newman, E. (1965). "The exact solution of the Einstein-Maxwell equations for a rotating mass with arbitrary charge and rotation". The Astrophysical Journal, 140, 553-562.

+ Wald, R. M. (1984). General relativity. University of Chicago Press.

I hope this helps! Let me know if you have any questions or need further clarification.