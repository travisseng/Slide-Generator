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
<!-- backgroundImage: url('backgrounds/hhholographic (1).png') -->
<!-- _class: lead -->

 # **Volume integral**

---
<style scoped>p,li {font-size:0.88em}</style>

 # Introduction to Volume Integrals

- Definition of a volume integral
- Also known as the volume element or volume differential
- Used to find the volume of a 3D region

---
<style scoped>p,li {font-size:0.92em}</style>

 # In Coordinates

- The idea behind volume integrals is to integrate the area of the 3D region with respect to all three coordinates (x, y, and z)
- This can be done using a change of variables, where we switch from Cartesian coordinates to spherical or cylindrical coordinates

---
<style scoped>p,li {font-size:0.88em}</style>

 # Example 1 - Spherical Coordinates

- Suppose we have a volume that is symmetrical about the x-axis and y-axis, and we want to find its volume in spherical coordinates
- We can switch to spherical coordinates by setting x = r cos(θ), y = r sin(θ), and z = h (where r and θ are the radial and angular distances from the origin, respectively)
- The volume element in spherical coordinates is dV = r^2 sin(θ) dr dθ dh

---
<style scoped>p,li {font-size:0.88em}</style>

 # Example 2 - Cylindrical Coordinates

- Suppose we have a volume that is symmetrical about the x-axis and z-axis, and we want to find its volume in cylindrical coordinates
- We can switch to cylindrical coordinates by setting x = r cos(θ), y = r sin(θ), and z = h (where r and θ are the radial and angular distances from the origin, respectively)
- The volume element in cylindrical coordinates is dV = r^2 sin(θ) dr dθ dh

---
<style scoped>p,li {font-size:0.88em}</style>

 # Applications of Volume Integrals
- Volume integrals have many applications in physics, engineering, and other fields
- Examples include finding the volume of a sphere, a cylinder, or a cone
- They can also be used to solve problems involving fluid flow, heat transfer, and electric field analysis


---
<style scoped>p,li {font-size:0.84em}</style>

 # _Conclusion_
- Volume integrals are an important concept in calculus that allow us to find the volume of 3D regions
- They can be performed using different coordinate systems, such as spherical or cylindrical coordinates
- With practice and experience, you will become more comfortable with performing volume integrals and applying them to real-world problems.

I hope this helps! Let me know if you have any questions or need further clarification.
