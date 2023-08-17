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

 # Ricci calculus

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Introduction to Ricci Calculus**
- Notation for indices: Latin letters from a to n (except for i and j) will be used to represent indices, which are labels that take values in a given range.
- Basis-related distinctions: We will use the phrase "basis" to refer to a set of vectors that span the space in which we are working.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Space and Time Coordinates

- Coordinate and index notation: We will use coordinate notation to describe points in space and time, where each coordinate is labeled by an index.
- Reference to basis: The basis vectors will be used to raise and lower indices.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Upper and Lower Indices

- Covariant tensor components: Tensor components that transform with the same transformation as the basis vectors are called covariant.
- Contravariant tensor components: Tensor components that transform with the inverse transformation of the basis vectors are called contravariant.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Mixed-Variance Tensor Components
- Tensor type and degree: Tensors can be classified by their type (covariant, contravariant, or mixed-variance) and degree (the number of indices).
- Summation convention: We will use the summation convention, where repeated indices are summed over.


---
<style scoped>p,li {font-size:0.96em}</style>

 # **Multi-Index Notation**
- Sequential summation: When working with multi-index notation, we can use sequential summation to simplify expressions.


---
<style scoped>p,li {font-size:0.96em}</style>

 # _Raising and Lowering Indices_
- Correlations between index positions and invariance: The position of an index is important, as it determines the transformation properties of a tensor.


---
<style scoped>p,li {font-size:0.96em}</style>

 # General Outlines for Index Notation and Operations

- Free and dummy indices: We will use free indices to denote uncontracted indices, and dummy indices to denote contracted indices.

---
<style scoped>p,li {font-size:0.96em}</style>

 # A Tensor Equation Represents Many Ordinary (Real-Valued) Equations
- Indices are replaceable labels: Indices can be treated as labels that can be replaced with any other label in a tensor equation.


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Symmetric and Antisymmetric Parts**

- Symmetric part of tensor: The symmetric part of a tensor is the sum of all possible pairs of identical indices.
- Antisymmetric or alternating part of tensor: The antisymmetric part of a tensor is the sum of all possible pairs of non-identical indices.

---
<style scoped>p,li {font-size:0.96em}</style>

 # Sum of Symmetric and Antisymmetric Parts

- Differentiation: Tensors can be differentiated using partial derivatives, covariant derivatives, and exterior derivatives.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Connection Types

- Exterior derivative: The exterior derivative is a linear operator that acts on forms and measures the failure of a form to be closed.
- Lie derivative: The Lie derivative is a way of measuring the change in a tensor under a diffeomorphism.

---
<style scoped>p,li {font-size:0.88em}</style>

 # Notable Tensors

- Kronecker delta: The Kronecker delta is a tensor that has a value of 1 when its indices are equal, and 0 otherwise.
- Torsion tensor: The torsion tensor is a measure of the amount of twisting between two tangent spaces at a point.
- Riemann curvature tensor: The Riemann curvature tensor is a measure of the amount of curving in a direction at a point.

---
<style scoped>p,li {font-size:0.96em}</style>

 # Metric Tensor
- Notation for indices: We will use the notation g_ij to represent the components of the metric tensor.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Notes and Sources
- References for further reading and study.

This presentation covers the basic concepts and notations of Ricci calculus, including the use of indices to describe tensors, the distinction between covariant and contravariant components, and the manipulation of tensors using various operations such as summation, differentiation, and exterior derivative. It also introduces notable tensors such as the Kronecker delta, torsion tensor, and Riemann curvature tensor, and discusses the concept of invariance and symmetry in tensor equations.
