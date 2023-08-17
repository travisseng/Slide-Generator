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

 # _Two-body problem in general relativity_

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Historical context**
- The Two-body problem has been studied for centuries as a fundamental problem in astronomy and physics
- Classical solutions were developed by Kepler, Newton, and Einstein


---
<style scoped>p,li {font-size:0.88em}</style>

 # Classical Kepler problem
- The Kepler problem is the classic solution for the motion of two bodies in a gravitational field
- Assumes that the masses of the two bodies are equal and the gravitational force is weak
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Elliptic_orbit.gif/220px-Elliptic_orbit.gif'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # _Apsidal precession_
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Precessing_Kepler_orbit_280frames_e0.6_smaller.gif/330px-Precessing_Kepler_orbit_280frames_e0.6_smaller.gif'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- The apsidal precession is a phenomenon observed in the orbits of binary star systems
- Caused by the tidal forces between the two stars, leading to a gradual shift in the orientation of their orbital planes
</div>

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Anomalous precession of Mercury

- The anomalous precession of Mercury is a discrepancy between the observed precession rate and the predicted rate based on Newton's law of gravity
- A puzzle that was resolved by Einstein's theory of general relativity

---
<style scoped>p,li {font-size:0.88em}</style>

 # Einstein's theory of general relativity
- General relativity is a theory of gravitation that describes how mass and energy warp the fabric of spacetime
- Predicts that the gravitational force is not just a simple attractive force, but a curved spacetime that affects the motion of objects
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/1919_eclipse_negative.jpg/220px-1919_eclipse_negative.jpg'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # General relativity, special relativity and geometry

- General relativity and special relativity are both based on the principles of geometry and the equivalence of all inertial reference frames
- Geometry plays a central role in understanding the structure of spacetime and the motion of objects within it

---
<style scoped>p,li {font-size:0.92em}</style>

 # Geodesic equation

- The geodesic equation describes the motion of a particle in a curved spacetime
- A solution to the geodesic equation determines the path that a particle follows as it moves through spacetime

---
<style scoped>p,li {font-size:0.92em}</style>

 # Schwarzschild solution
- The Schwarzschild solution is a solution to the Einstein field equations that describes the gravitational field of a spherically symmetric mass
- Provides a framework for understanding the motion of objects in the vicinity of a massive body


---
<style scoped>p,li {font-size:0.88em}</style>

 # Orbits about the central mass
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Orbits about the central mass are determined by the geodesic equation and the Schwarzschild solution
- The effective radial potential energy describes the gravitational force experienced by an object in orbit around a massive body
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Newton_versus_Schwarzschild_trajectories.gif/330px-Newton_versus_Schwarzschild_trajectories.gif'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.84em}</style>

 # Circular orbits and their stability
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Circular orbits are stable in the presence of a central mass, provided that the circular velocity is less than the escape velocity
- The stability of circular orbits is related to the concept of Lyapunov stability
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Schwarzschild_effective_potential.svg/330px-Schwarzschild_effective_potential.svg.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Schwarzschild_circular_radii.svg/330px-Schwarzschild_circular_radii.svg.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # **Precession of elliptical orbits**
- The precession of elliptical orbits is a consequence of the gravitational force acting on an object in orbit around a massive body
- The precession rate depends on the mass of the central body, the semi-major axis of the orbit, and the eccentricity of the orbit
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Relativistic_precession.svg/220px-Relativistic_precession.svg.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # _Beyond the Schwarzschild solution_
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/GR2bodyparameterspace.png/360px-GR2bodyparameterspace.png'/>
</div>
</div>

- Beyond the Schwarzschischild solution, there are a number of other solutions to the Einstein field equations that describe more complex gravitational fields
- These solutions can be used to study a variety of phenomena, such as black holes, neutron stars, and gravitational waves

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Post-Newtonian expansion**
- The post-Newtonian expansion is a way of approximating the effects of general relativity in situations where the gravitational field is weak
- Provides a framework for understanding the behavior of objects in the vicinity of a massive body, while ignoring the effects of black hole physics and other exotic phenomena


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Modern computational approaches**
- Modern computational approaches use numerical methods to solve the Einstein field equations and study the behavior of gravitational systems
- These methods have led to a number of important discoveries, such as the detection of gravitational waves and the study of black hole mergers


---
<style scoped>p,li {font-size:0.92em}</style>

 # Gravitational radiation
- Gravitational radiation is a prediction of general relativity that describes the emission of energy in the form of ripples in spacetime
- Detected indirectly through its effects on the motion of objects, such as the orbital decay of binary star systems


---
<style scoped>p,li {font-size:0.92em}</style>

 # Notes
- The Two-body problem has been studied extensively in the context of general relativity and other theories of gravitation
- There are a number of open questions and unresolved issues in the study of the Two-body problem, such as the nature of dark matter and the behavior of binary black hole systems


---
<style scoped>p,li {font-size:0.96em}</style>

 # Bibliography
- A list of references used in the presentation, including books, articles, and online resources.
