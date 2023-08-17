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

 # Numerical partial differential equations

---
<style scoped>p,li {font-size:0.92em}</style>

 # Overview of Numerical Methods for Partial Differential Equations
- Numerical methods are used to approximate solutions of PDEs when the exact solution cannot be found or is too complex to handle.
- There are several numerical methods available, each with its own strengths and weaknesses.


---
<style scoped>p,li {font-size:0.88em}</style>

 # Finite Difference Method

- Finite difference method discretizes the domain into a grid of discrete points in both space and time.
- The PDE is approximated by finite differences at each point in the grid, yielding a set of algebraic equations.
- Example: Taylor series expansion of the solution around a given point.

---
<style scoped>p,li {font-size:0.88em}</style>

 # Method of Lines
- Method of lines discretizes the domain into a grid of discrete points in space and a continuous range of values in time.
- The PDE is approximated by finite differences in space and finite elements in time.
- Example: Linearization of the solution around a given point in time.


---
<style scoped>p,li {font-size:0.88em}</style>

 # Finite Element Method

- Finite element method discretizes the domain into smaller elements, allowing for a more flexible mesh.
- The PDE is approximated by piecewise-defined functions within each element.
- Example: Hexahedral elements for solving the Poisson equation.

---
<style scoped>p,li {font-size:0.88em}</style>

 # Gradient Discretization Method

- Gradient discretization method approximates the gradient of the solution by finite differences in space and time.
- The PDE is solved iteratively, with each iteration refining the approximation of the solution.
- Example: Advection equation with a discrete-time scheme.

---
<style scoped>p,li {font-size:0.88em}</style>

 # Finite Volume Method
- Finite volume method discretizes the domain into small control volumes, allowing for conservation properties.
- The PDE is approximated by updating the cell averages of the solution at each time step.
- Example: Advection equation with a finite volume scheme.


---
<style scoped>p,li {font-size:0.88em}</style>

 # Spectral Method
- Spectral method represents the solution as a series of orthogonal basis functions, such as sine and cosine functions.
- The PDE is approximated by projecting the solution onto the basis functions and solving the resulting system of linear equations.
- Example: Fourier series for solving the Poisson equation on a sphere.


---
<style scoped>p,li {font-size:0.88em}</style>

 # Meshfree Methods
- Meshfree methods do not require a predefined grid, allowing for more complex geometries and boundary conditions.
- The PDE is approximated by representing the solution as a set of basis functions that are adapted to the problem.
- Example: Radial basis function method for solving the Poisson equation in 3D.


---
<style scoped>p,li {font-size:0.88em}</style>

 # Domain Decomposition Methods
- Domain decomposition methods break down the large problem into smaller subdomains, allowing for more efficient computation and parallelization.
- The PDE is solved iteratively within each subdomain, with communication between subdomains to ensure accuracy.
- Example: Parallel solution of the Poisson equation using domain decomposition.


---
<style scoped>p,li {font-size:0.88em}</style>

 # Multigrid Methods

- Multigrid methods use a combination of coarse and fine grids to solve the PDE efficiently.
- The solution is represented at multiple scales, with iteration between the grids to refine the approximation.
- Example: Solving the Poisson equation using a multigrid method.

---
<style scoped>p,li {font-size:0.88em}</style>

 # Comparison of Numerical Methods

- Each numerical method has its own strengths and weaknesses, depending on the problem and desired accuracy.
- The choice of method depends on factors such as computational resources, problem complexity, and desired level of accuracy.

I hope this slide presentation provides a helpful overview of numerical partial differential equations!