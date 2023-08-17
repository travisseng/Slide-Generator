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

 # _Laplace–Beltrami operator_

---
<style scoped>p,li {font-size:0.88em}</style>

 # Details
- The Laplace-Beltrami operator is a differential operator defined on a Riemannian manifold
- It is named after Pierre-Simon Laplace and Gabriello Beltrami
- Also known as the Laplace-de Rham operator or the Riemannian Hodge star operator


---
<style scoped>p,li {font-size:0.88em}</style>

 # Formal Self-Adjointness
- The Laplace-Beltrami operator is a formal self-adjoint operator, meaning that it satisfies the equation

$$\int_{M} \nabla^{LB}_{x} f(x) \cdot \nabla^{LB}_{x} g(x) dV(x) = \int_{M} f(x) \cdot \nabla^{LB}_{x} g(x) dV(x)$$

where $M$ is a Riemannian manifold, $f$ and $g$ are smooth functions on $M$, and $\nabla^{LB}$ is the Laplace-Beltrami operator.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Eigenvalues of the Laplace-Beltrami Operator (Lichnerowicz-Obata Theorem)
- The Laplace-Beltrami operator has a discrete spectrum, consisting of non-negative eigenvalues
- The Lichnerowicz-Obata theorem states that the eigenvalues of the Laplace-Beltrami operator are given by $L \cdot \Vol(M)$, where $L$ is the scalar curvature of $M$ and $\Vol(M)$ is the volume of $M$.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Tensor Laplacian
- The Laplace-Beltrami operator can be viewed as a tensor, with indices that are induced by the Riemannian metric on $M$
- This allows us to define the tensor Laplacian, which is a generalization of the Laplace-Beltrami operator to higher-rank tensors.


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Laplace-de Rham Operator_
- The Laplace-de Rham operator is a variant of the Laplace-Beltrami operator that is defined on differential forms instead of functions
- It is used in the study of smoothness and analyticity of functions on manifolds.


---
<style scoped>p,li {font-size:0.88em}</style>

 # Examples

- Euclidean space: the Laplace-Beltrami operator is proportional to the identity operator, so all eigenvalues are equal to $0$.
- Spherical Laplacian: the Laplace-Beltrami operator on the sphere is a second-order differential operator that is self-adjoint and has a discrete spectrum.
- Hyperbolic space: the Laplace-Beltrami operator on hyperbolic space is a second-order differential operator that is self-adjoint and has a discrete spectrum, but with a different set of eigenvalues than the spherical Laplacian.

---
<style scoped>p,li {font-size:0.88em}</style>

 # Notes

- The Laplace-Beltrami operator is a fundamental tool in the study of Riemannian geometry and analysis on manifolds.
- It has applications in a wide range of fields, including physics, engineering, and computer science.
- The eigenvalues of the Laplace-Beltrami operator can be used to understand the geometry and topology of the manifold.