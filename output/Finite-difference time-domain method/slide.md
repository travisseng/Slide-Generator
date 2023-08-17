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

 # Finite-difference time-domain method

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Introduction_
- Brief overview of FDTD method
- Importance and applications in various fields


---
<style scoped>p,li {font-size:0.92em}</style>

 # _History_

- Development history of FDTD method
- Key contributors and milestones

---
<style scoped>p,li {font-size:0.92em}</style>

 # Maxwell's Equations
- Overview of Maxwell's equations
- Formulation of wave equation using Maxwell's equations


---
<style scoped>p,li {font-size:0.84em}</style>

 # FDTD Models and Methods
- Overview of FDTD models and methods
- Finite-difference formulation of the wave equation
- Time-stepping schemes for solving the wave equation
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/FDTD_Yee_grid_2d-3d.svg/450px-FDTD_Yee_grid_2d-3d.svg.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # Using the FDTD Method

- Setting up a basic FDTD simulation
- Choosing appropriate grid size and spacing
- Handling boundary conditions

---
<style scoped>p,li {font-size:0.88em}</style>

 # _Strengths of FDTD Modeling_
- Accurate representation of complex geometries and materials
- Ability to handle non-uniform grids and adaptive mesh refinement
- Efficient computation of large-scale simulations


---
<style scoped>p,li {font-size:0.88em}</style>

 # Weaknesses of FDTD Modeling
- Sensitivity to grid size and spacing
- Difficulty in handling complex physics, such as multi-physics problems
- Limited applicability for simulating high-frequency phenomena


---
<style scoped>p,li {font-size:0.92em}</style>

 # Grid Truncation Techniques
- Overview of common grid truncation techniques (e.g., Gaussian tapering, finite-difference gradient correction)
- Discussion of their advantages and limitations


---
<style scoped>p,li {font-size:0.92em}</style>

 # Popularity and Implementations
- Comparison of popular FDTD software packages (e.g., COMSOL, ANSYS HFSS, OpenFOAM)
- Discussion of their features, strengths, and weaknesses


---
<style scoped>p,li {font-size:0.88em}</style>

 # Conclusion

- Summary of key points covered in the presentation
- Future directions and areas of active research in FDTD methodology

I hope this helps! Let me know if you have any questions or need further clarification.