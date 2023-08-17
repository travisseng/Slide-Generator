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

 # **Periodic boundary conditions**

---
<style scoped>p,li {font-size:0.92em}</style>

 # Requirements and Artifacts
- Periodic boundary conditions are required for simulations of crystalline materials
- Artifacts can be introduced if not properly implemented


---
<style scoped>p,li {font-size:0.92em}</style>

 # Practical Implementation: Continuity and Minimum Image Convention

- Particle coordinates must be restricted to the simulation box
- The minimum image convention ensures continuity of properties across periodic images

---
<style scoped>p,li {font-size:0.92em}</style>

 # **(A) Restrict Particle Coordinates to the Simulation Box**
- Particles are restricted to move within the simulation box
- Periodic images are created by repeating the simulation box in all directions


---
<style scoped>p,li {font-size:0.92em}</style>

 # _(B) Do Not Restrict Particle Coordinates_

- Particles can move beyond the simulation box boundaries
- Requires careful treatment of periodic images

---
<style scoped>p,li {font-size:0.92em}</style>

 # Unit Cell Geometries

- Periodic boundary conditions require a unit cell definition
- The unit cell geometry determines the simulation box size and spacing

---
<style scoped>p,li {font-size:0.92em}</style>

 # General Dimension
- Periodic boundary conditions can be applied in any dimension
- Higher-dimensional simulations require more careful treatment of periodic images


---
<style scoped>p,li {font-size:0.92em}</style>

 # Conserved Properties

- Periodic boundary conditions conserve many important properties
- Examples include energy, momentum, and mass

---
<style scoped>p,li {font-size:0.88em}</style>

 # **Notes**

- Proper implementation of periodic boundary conditions is essential for accurate simulation results
- Careful consideration of artifacts and practical implementation is required

I hope this slide presentation helps you understand Periodic boundary conditions better. Let me know if you have any questions or need further clarification!