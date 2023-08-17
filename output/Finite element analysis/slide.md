---
marp: true
math: katex
theme: gaia
style: |
   @import url('https://unpkg.com/tailwindcss@2.2.19/dist/utilities.min.css');
   section {display: flex;flex-flow: column; font-size:35px; letter-spacing:1.4px;}

   header {overflow:visible} header > img.logo {position:absolute; right:15px;}

   header > img.logo {position:absolute; right:15px;}


---
<!-- backgroundColor: white -->
<!-- _class: lead -->

 # _Finite element analysis_

---
<style scoped>p,li {font-size:0.84em}</style>

 # _Basic Concepts_
- Finite element analysis is a numerical method for solving partial differential equations (PDEs)
- Divided into two main parts: weak formulation and discretization
- Weak formulation: find the solution that satisfies the PDE in a weak sense
- Discretization: approximate the solution using a finite number of basis functions


---
<style scoped>p,li {font-size:0.88em}</style>

 # **History**

- Finite element analysis was first introduced in the 1960s
- Early methods were based on piecewise-linear approximations
- Today, there are many different types of finite element methods and applications

---
<style scoped>p,li {font-size:0.76em}</style>

 # Technical Discussion
- The structure of finite element methods:

+ Weak formulation

+ Discretization
- Illustrative problems P1 and P2:

+ Poisson's equation in a rectangular domain

+ Navier-Stokes equations in a 2D rectangular domain


---
<style scoped>p,li {font-size:0.92em}</style>

 # Weak Formulation
- The weak form of P1: find the solution that satisfies the equation in a weak sense
- The weak form of P2: find the solution that satisfies the equation in a weak sense


---
<style scoped>p,li {font-size:0.92em}</style>

 # Proof Outline of Existence and Uniqueness of the Solution
- Existence: use the Lax-Milgram theorem to prove existence of a solution
- Uniqueness: use the energy method to prove uniqueness of the solution


---
<style scoped>p,li {font-size:0.84em}</style>

 # Discretization
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Finite_element_method_1D_illustration1.png/220px-Finite_element_method_1D_illustration1.png'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Divide the domain into smaller elements
- Approximate the solution using a finite number of basis functions
- Choose a basis that satisfies certain properties (e.g. small support, smoothness)
</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # **For Problem P1**
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Piecewise_linear_function2D.svg/220px-Piecewise_linear_function2D.svg.png'/>
</div>
</div>

- Discretize the domain into rectangular elements
- Use a piecewise-linear basis to approximate the solution

---
<style scoped>p,li {font-size:0.92em}</style>

 # For Problem P2
- Discretize the domain into triangular elements
- Use a piecewise-linear basis to approximate the solution


---
<style scoped>p,li {font-size:0.92em}</style>

 # Choosing a Basis
- Choose a basis that satisfies certain properties (e.g. small support, smoothness)
- Consider using a basis that is adapted to the problem (e.g. spectral basis for problems with periodic boundary conditions)


---
<style scoped>p,li {font-size:0.80em}</style>

 # Small Support of the Basis
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Finite_element_triangulation.svg/220px-Finite_element_triangulation.svg.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Finite_element_sparse_matrix.png/220px-Finite_element_sparse_matrix.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Finite_element_solution.svg/220px-Finite_element_solution.svg.png'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- The basis functions should have a small support to reduce the computational cost and improve accuracy
- Use a sparse grid or other techniques to reduce the number of basis functions needed
</div>

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Matrix Form of the Problem
- The finite element method can be written in matrix form: find the solution that satisfies the equation in a weak sense
- The matrix formulation allows for efficient computation and scalability


---
<style scoped>p,li {font-size:0.92em}</style>

 # General Form of the Finite Element Method

- The finite element method can be applied to a wide range of problems, including linear and nonlinear problems
- The method involves dividing the domain into smaller elements, approximating the solution using a finite number of basis functions, and solving the resulting system of equations

---
<style scoped>p,li {font-size:0.84em}</style>

 # **Various Types of Finite Element Methods**

- A EM (Arnoldi-Eisenstat-Mikhael) method for linear problems
- A-FEM (Algebraic-Finite Element Method) for nonlinear problems
- Generalized finite element method for problems with complex geometry and boundary conditions
- Mixed finite element method for problems with both continuous and discrete variables

---
<style scoped>p,li {font-size:0.84em}</style>

 # AEM, A-FEM, Generalized Finite Element Method, Mixed Finite Element Method
- AEM: uses a least-squares formulation to solve the system of equations
- A-FEM: uses an algebraic formulation to solve the system of equations
- Generalized FEM: uses a variational formulation to solve the system of equations
- Mixed FEM: combines continuous and discrete variables to improve accuracy and flexibility


---
<style scoped>p,li {font-size:0.92em}</style>

 # XFEM, SBFEM

- XFEM (eXtended Finite Element Method): extends the finite element method to handle problems with high-frequency oscillations and singularities
- SBFEM (Scaled Boundary Finite Element Method): uses a scaled boundary representation to improve accuracy and reduce computational cost for problems with complex boundaries

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Spectral Element Method_

- The spectral element method is a type of finite element method that uses a spectral basis to approximate the solution
- The method can be used for problems with periodic boundary conditions and high-frequency oscillations

---
<style scoped>p,li {font-size:0.92em}</style>

 # Meshfree Methods

- Meshfree methods are finite element methods that do not use a mesh to discretize the domain
- The methods are based on a collection of basis functions that are distributed throughout the domain

---
<style scoped>p,li {font-size:0.92em}</style>

 # Discontinuous Galerkin Methods

- Discontinuous Galerkin methods are finite element methods that allow for discontinuous solutions and non-smooth boundaries
- The methods can be used for problems with complex geometry and boundary conditions

---
<style scoped>p,li {font-size:0.92em}</style>

 # Finite Element Limit Analysis
- Finite element limit analysis is a technique used to study the behavior of a system as the mesh size tends to zero
- The method allows for a rigorous analysis of the accuracy and convergence of finite element methods


---
<style scoped>p,li {font-size:0.92em}</style>

 # Stretched Grid Method, Loubignac Iteration
- The stretched grid method is a technique used to improve the accuracy of finite element solutions by increasing the resolution of the mesh
- Loubignac iteration is an iterative technique used to solve the system of equations obtained from the finite element discretization


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Crystal Plasticity Finite Element Method (CPFEM)_

- CPFEM is a type of finite element method that is specifically designed for problems involving crystal plasticity and microstructure
- The method can be used to study the behavior of materials under complex loading conditions and non-linear deformation

---
<style scoped>p,li {font-size:0.92em}</style>

 # Virtual Element Method (VEM)
- VEM is a type of finite element method that uses a virtual element space to discretize the problem
- The method can be used for problems with high-dimensional spaces and complex geometry


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Link with the Gradient Discretization Method_
- The gradient discretization method is a technique used to approximate the gradient of the solution using a finite number of basis functions
- The method can be used in conjunction with finite element methods to improve accuracy and reduce computational cost


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Comparison to the Finite Difference Method_
- Finite element methods can be compared to finite difference methods, which are another type of numerical method for solving PDEs
- Both methods have their own strengths and weaknesses, and the choice of method depends on the specific problem and application


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Applications**

- Finite element methods have a wide range of applications in engineering, physics, and other fields
- Examples include the analysis of structural systems, heat transfer, fluid dynamics, and other problems involving PDEs.