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

 # Magnetic vector potential

---
<style scoped>p,li {font-size:0.96em}</style>

 # Magnetic Vector Potential

Magnetic vector potential is a mathematical construct used to describe the magnetic field of a charged particle in motion. It is a vector field that represents the strength and direction of the magnetic force acting on a test charge at any point in space.


---
<style scoped>p,li {font-size:0.84em}</style>

 # Gauge Choices

When working with the magnetic vector potential, it is important to choose a gauge. There are several gauges available, each with its own set of advantages and disadvantages. Some common gauges include:
- Lorentz gauge: This gauge chooses the magnetic field as the primary quantity of interest, and the electric field is derived from it.
- Coulomb gauge: This gauge chooses the electric field as the primary quantity of interest, and the magnetic field is derived from it.
- Feynman gauge: This gauge chooses the electric field and magnetic field to be mutually perpendicular at every point in space.


---
<style scoped>p,li {font-size:0.80em}</style>

 # Maxwell's Equations in Terms of Vector Potential

Maxwell's equations can be written in terms of the magnetic vector potential, which is why it is such an important concept in electromagnetism. Here are the four Maxwell's equations in terms of the magnetic vector potential:
- Gauss's law for magnetism: ∇⋅B = 0 (no magnetic charges)
- Faraday's law of induction: ∇×E = -∂B/∂t
- Ampere's law with Maxwell's correction: ∇×B = μ₀J + μ₀ε₀∂E/∂t
- Gauss's law for electricity: ∇⋅E = ρ/ε₀ (conservation of charge)


---
<style scoped>p,li {font-size:0.80em}</style>

 # Calculation of Potentials from Source Distributions


To calculate the magnetic vector potential, we need to know the source distributions (such as charges and currents) in the space. Here are the steps to calculate the potentials:

1. Choose a gauge.

2. Write down Maxwell's equations in terms of the potentials.

3. Use the source distributions to solve for the potentials.

4. Verify that the potentials satisfy the boundary conditions.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Depiction of the A-Field
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Magnetic_Vector_Potential_Circular_Toroid.svg/450px-Magnetic_Vector_Potential_Circular_Toroid.svg.png'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">


The magnetic vector potential is often depicted as a vector field, with the magnitude and direction of the vectors representing the strength and direction of the magnetic force at each point in space. Here is an example of such a depiction:
</div>

</div>


---
<style scoped>p,li {font-size:0.96em}</style>

 # Electromagnetic Four-Potential

The electromagnetic four-potential is a mathematical construct that combines the electric and magnetic vector potentials into a single object. It is a four-dimensional vector field that represents the entire electromagnetic field, including both the electric and magnetic components. Here is an example of such a depiction:


---
<style scoped>p,li {font-size:0.84em}</style>

 # Notes
- The magnetic vector potential is a fundamental concept in electromagnetism and is used to describe the magnetic field of charged particles in motion.
- Gauge choices can affect the results of calculations, so it is important to choose a gauge carefully.
- Maxwell's equations can be written in terms of the magnetic vector potential, which makes it an important tool for solving problems in electromagnetism.
- The depiction of the A-field as a vector field can be useful for visualizing the strength and direction of the magnetic force at each point in space.
