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
<!-- backgroundColor: #84808d -->
<!-- _class: lead -->

 # Computational electromagnetics

---
<style scoped>p,li {font-size:0.92em}</style>

 # Background
- Computational electromagnetics (CEM) is the use of numerical methods to solve Maxwell's equations and related problems in electromagnetism
- CEM is a powerful tool for simulating and analyzing a wide range of electromagnetic phenomena, from antennas and waveguides to plasmonics and metamaterials


---
<style scoped>p,li {font-size:0.64em}</style>

 # **Overview of Methods**
- Overview of popular CEM methods, including:

+ Finite difference time domain (FDTD)

+ Finite element method (FEM)

+ Method of moments (MoM)

+ Boundary element method (BEM)

+ Fast multipole method (FMM)

+ Plane wave time-domain (PW)

+ Partial element equivalent circuit (PEEC)

+ Cagniard-deHoop moment method (CDH)


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Maxwell's Equations in Hyperbolic PDE Form**
- Maxwell's equations can be written as a set of nonlinear partial differential equations (PDEs)
- The hyperbolic nature of the equations allows for the use of advanced numerical methods to solve them efficiently


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Integral Equation Solvers**
- Integral equation solvers are used to solve the homogenous and heterogeneous problems in CEM
- Examples include the finite element method, the boundary element method, and the moment method


---
<style scoped>p,li {font-size:0.92em}</style>

 # _The Discrete Dipole Approximation_

- The discrete dipole approximation (DDA) is a numerical method used to simulate the scattering of electromagnetic waves by discrete objects such as particles and inclusions
- DDA is based on the idea that the electric and magnetic fields can be approximated as a superposition of discrete dipoles

---
<style scoped>p,li {font-size:0.92em}</style>

 # Method of Moments
- The method of moments (MoM) is a numerical method used to solve Maxwell's equations for electromagnetic scattering and radiation problems
- MoM is based on the idea that the electric and magnetic fields can be represented as a superposition of orthogonal basis functions, such as spherical harmonics or Legendre polynomials


---
<style scoped>p,li {font-size:0.92em}</style>

 # Boundary Element Method

- The boundary element method (BEM) is a numerical method used to solve boundary value problems in CEM
- BEM is based on the idea that the electric and magnetic fields can be represented as a superposition of basis functions defined on the boundaries of the problem domain

---
<style scoped>p,li {font-size:0.92em}</style>

 # Fast Multipole Method
- The fast multipole method (FMM) is a numerical method used to accelerate the computation of electromagnetic simulations involving large numbers of particles or inclusions
- FMM is based on the idea that the electric and magnetic fields can be approximated as a superposition of multipole moments


---
<style scoped>p,li {font-size:0.92em}</style>

 # Plane Wave Time-Domain Method

- The plane wave time-domain (PW) method is a numerical method used to simulate the propagation of electromagnetic waves in lossless media
- PW is based on the idea that the electric and magnetic fields can be represented as a superposition of plane wave components

---
<style scoped>p,li {font-size:0.92em}</style>

 # Partial Element Equivalent Circuit Method

- The partial element equivalent circuit (PEEC) method is a numerical method used to simulate the behavior of electromagnetic devices such as antennas and waveguides
- PEEC is based on the idea that the electric and magnetic fields can be represented as a superposition of element-circuit models

---
<style scoped>p,li {font-size:0.92em}</style>

 # Cagniard-deHoop Moment Method

- The Cagniard-deHoop moment method (CDH) is a numerical method used to simulate the behavior of electromagnetic devices such as antennas and waveguides
- CDH is based on the idea that the electric and magnetic fields can be represented as a superposition of moment components

---
<style scoped>p,li {font-size:0.92em}</style>

 # Differential Equation Solvers

- Differential equation solvers are used to solve the time-dependent and frequency-domain problems in CEM
- Examples include the finite-difference time-domain (FDTD) method, the discontinuous Galerkin time-domain (DG-TD) method, and the pseudospectral time-domain (PSTD) method

---
<style scoped>p,li {font-size:0.92em}</style>

 # Finite-Difference Time-Domain Method
- The finite-difference time-domain (FDTD) method is a numerical method used to simulate the propagation of electromagnetic waves in lossy media
- FDTD is based on the idea that the electric and magnetic fields can be represented as a superposition of finite-difference equations


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Discontinuous Galerkin Time-Domain Method**
- The discontinuous Galerkin time-domain (DG-TD) method is a numerical method used to simulate the propagation of electromagnetic waves in lossy media
- DG-TD is based on the idea that the electric and magnetic fields can be represented as a superposition of discontinuous Galerkin equations


---
<style scoped>p,li {font-size:0.92em}</style>

 # Multiresolution Time-Domain Method
- The multiresolution time-domain (MRTD) method is a numerical method used to simulate the propagation of electromagnetic waves in lossy media
- MRTD is based on the idea that the electric and magnetic fields can be represented as a superposition of wavelet basis functions


---
<style scoped>p,li {font-size:0.92em}</style>

 # Finite Element Method
- The finite element method (FEM) is a numerical method used to solve partial differential equations (PDEs) in a variational framework
- FEM is widely used in CEM for problems involving the simulation of electromagnetic fields in complex geometries


---
<style scoped>p,li {font-size:0.92em}</style>

 # Finite Integration Technique
- The finite integration technique (FIT) is a numerical method used to solve integral equations in CEM
- FIT is based on the idea that the electric and magnetic fields can be represented as a superposition of basis functions defined over a finite integration domain


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Pseudospectral Time-Domain Method_
- The pseudospectral time-domain (PSTD) method is a numerical method used to simulate the propagation of electromagnetic waves in lossy media
- PSTD is based on the idea that the electric and magnetic fields can be represented as a superposition of pseudospectral basis functions


---
<style scoped>p,li {font-size:0.92em}</style>

 # Validation and Comparison

- Validation and comparison of simulation results with analytical formulations and experimental data is crucial for the accuracy and reliability of CEM simulations
- Examples include the comparison of FDTD and PSTD results with analytical formulas for the scattering of electromagnetic waves by spheres and cylinders

---
<style scoped>p,li {font-size:0.92em}</style>

 # Cross-Comparison between Codes
- Cross-comparison between different CEM codes is useful for verifying the accuracy and consistency of simulation results
- Examples include the comparison of FDTD and MoM results for the simulation of a simple antenna design


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Comparison with Measurement**

- Comparison of simulation results with experimental measurement is crucial for the accuracy and reliability of CEM simulations
- Examples include the comparison of FDTD and PSTD results with experimental data for the characterization of a novel electromagnetic device

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Light Scattering Codes_

- Light scattering codes are used to simulate the interaction of light with particles and inclusions in a medium
- Examples include the finite-difference time-domain (FDTD) method, the discrete dipole approximation (DDA), and the moment method (MoM)

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Conclusion**

- Computational electromagnetics is a powerful tool for simulating and analyzing a wide range of electromagnetic phenomena
- The choice of numerical method depends on the specific problem being solved, the desired level of accuracy, and the computational resources available.