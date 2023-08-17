---
marp: true
math: katex
theme: uncover
style: |
   @import url('https://unpkg.com/tailwindcss@2.2.19/dist/utilities.min.css');
   section {display: flex;flex-flow: column; font-size:35px; letter-spacing:1.4px;}

   header {overflow:visible} header > img.logo {position:absolute; right:15px;}

   header > img.logo {position:absolute; right:15px;}


---
<!-- backgroundColor: white -->
<!-- _class: lead -->

 # Finite element method

---
<style scoped>p,li {font-size:0.92em}</style>

 # Basic Concepts
- Introduction to Finite Element Method (FEM)
- Overview of basic concepts and principles


---
<style scoped>p,li {font-size:0.92em}</style>

 # **History**

- Brief history of FEM
- Key milestones and contributions

---
<style scoped>p,li {font-size:0.88em}</style>

 # Technical Discussion

- Governing equations and their discretization
- Finite element spaces and approximations
- Variational formulation and its connection to weak forms

---
<style scoped>p,li {font-size:0.88em}</style>

 # _The Structure of Finite Element Methods_

- Overview of the structure of FEM
- Elements, nodes, and connectivity
- Quadratic and linear elements

---
<style scoped>p,li {font-size:0.88em}</style>

 # Illustrative Problems P1 and P2

- Definition of problems P1 and P2
- Geometry and boundary conditions
- Examples of physical phenomena modeled using FEM

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Weak Formulation_
- Weak form of P1 and P2
- Dual forms and their connection to the primal problem


---
<style scoped>p,li {font-size:0.92em}</style>

 # The Weak Form of P1 and P2

- Derivation of the weak forms for P1 and P2
- Use of test functions and dual variables

---
<style scoped>p,li {font-size:0.92em}</style>

 # A Proof Outline of Existence and Uniqueness of the Solution
- Overview of the proof outline
- Existence and uniqueness theorems for FEM


---
<style scoped>p,li {font-size:0.88em}</style>

 # Discretization
- Introduction to discretization techniques
- Finite element discretization of P1 and P2
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Finite_element_method_1D_illustration1.png/220px-Finite_element_method_1D_illustration1.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.84em}</style>

 # For Problem P1
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Piecewise_linear_function2D.svg/220px-Piecewise_linear_function2D.svg.png'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Finite element discretization of P1
- Choosing a basis and small support of the basis
- Matrix form of the problem
</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # _For Problem P2_
- Finite element discretization of P2
- Choosing a basis and small support of the basis
- Matrix form of the problem


---
<style scoped>p,li {font-size:0.92em}</style>

 # Choosing a Basis

- Overview of choice of basis in FEM
- Types of bases (e.g., piecewise linear, quadratic)

---
<style scoped>p,li {font-size:0.80em}</style>

 # Small Support of the Basis
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Importance of small support of the basis
- Techniques for reducing support (e.g., interpolation, smoothness)
</div>

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

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Matrix Form of the Problem
- Overview of matrix form of the problem
- Use of matrices to represent the system


---
<style scoped>p,li {font-size:0.92em}</style>

 # General Form of the Finite Element Method
- Overview of the general form of FEM
- Various types of finite element methods (e.g., AEM, A-FEM, GFEM)


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Various Types of Finite Element Methods_

- Introduction to different types of FEM
- AEM, A-FEM, GFEM, Mixed FEM, VEM, XFEM, SBFEM, S-FEM

---
<style scoped>p,li {font-size:0.92em}</style>

 # Discretization Techniques

- Overview of discretization techniques in FEM
- Finite difference, finite element, and spectral methods

---
<style scoped>p,li {font-size:0.92em}</style>

 # Finite Element Limit Analysis

- Introduction to limit analysis in FEM
- Stretched grid method, Loubignac iteration

---
<style scoped>p,li {font-size:0.92em}</style>

 # Crystal Plasticity Finite Element Method (CPFEM)

- Overview of CPFEM
- Key features and applications

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Virtual Element Method (VEM)**
- Overview of VEM
- Connection to gradient discretization method


---
<style scoped>p,li {font-size:0.92em}</style>

 # Link with the Gradient Discretization Method

- Overview of gradient discretization method
- Comparison to FEM and other methods

---
<style scoped>p,li {font-size:0.92em}</style>

 # Comparison to Finite Difference Method
- Overview of finite difference method
- Comparison to FEM in terms of accuracy and efficiency


---
<style scoped>p,li {font-size:0.80em}</style>

 # Application
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Overview of applications of FEM
- Examples from various fields (e.g., mechanical, civil, electrical engineering)
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Vanadis_a1_test.gif/245px-Vanadis_a1_test.gif'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Vanadis_a2_test.gif/245px-Vanadis_a2_test.gif'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Human_knee_joint_FE_model.png/245px-Human_knee_joint_FE_model.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # **Conclusion**

- Summary of key concepts and techniques in FEM
- Future directions and challenges in FEM research

I hope this helps! Let me know if you have any questions or need further clarification.