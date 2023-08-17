---
marp: true
math: katex
theme: default
paginate: True
style: |
   @import url('https://unpkg.com/tailwindcss@2.2.19/dist/utilities.min.css');
   :root {--color-fg-default: #FFFFFF; --color-foreground: #FFFFFF;}

   section {display: flex;flex-flow: column; font-size:35px; letter-spacing:1.4px;}

   header {overflow:visible} header > img.logo {position:absolute; right:15px;}

   header > img.logo {position:absolute; right:15px;}


---
<!-- backgroundImage: url('backgrounds/aaabstract (15).png') -->
<!-- _class: lead -->

 # Tensor calculus

---
<style scoped>p,li {font-size:0.92em}</style>

 # Introduction to Tensor Calculus
- Tensor calculus is a mathematical framework for describing and analyzing physical systems in terms of tensors, which are multi-dimensional arrays of numbers.
- It is used in many areas of physics, including general relativity, differential geometry, and quantum field theory.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Syntax

- Tensors are often represented as matrices, but they have a different syntax than matrix operations.
- Tensor operations are denoted by Greek letters (e.g. ∇, ∑, etc.) and are read from the inside out.

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Key Concepts**

- Tensors are objects that transform according to the rules of the Lorentz group, which is a group of transformations that preserve the geometry of spacetime.
- The Lorentz group has two fundamental types of transformations: translations and rotations.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Vector Decomposition

- Vectors can be decomposed into their constituent parts using the Hodge star operator, which maps a vector to its dual vector.
- The Hodge star operator is denoted by the symbol * and is used to raise and lower indices on vectors.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Covariant Vector Decomposition
- The covariant derivative of a vector is defined as the derivative of the vector in the direction of the vector itself.
- The covariant derivative is denoted by the symbol D and is used to measure the rate of change of a vector in a given direction.


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Contravariant Vector Decomposition_

- The contravariant derivative of a vector is defined as the derivative of the vector in the direction of the space itself.
- The contravariant derivative is denoted by the symbol D and is used to measure the rate of change of a vector in a given direction.

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Metric Tensor**
- The metric tensor is a symmetric tensor that encodes the geometry of spacetime.
- It defines the length and angle between vectors in spacetime and is denoted by the symbol g.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Jacobian
- The Jacobian is a matrix that describes the linear transformation between two sets of coordinates.
- It is used to describe the change in the orientation of vectors under a change of coordinates.


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Gradient Vector_
- The gradient vector is a vector that points in the direction of the steepest increase of a function.
- It is used to describe the rate of change of a function in a given direction.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Conclusion
- Tensor calculus is a powerful tool for describing and analyzing physical systems.
- Understanding the concepts of tensor calculus is essential for any physicist or mathematician working in the areas of general relativity, differential geometry, or quantum field theory.
