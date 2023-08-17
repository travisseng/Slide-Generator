---
marp: true
math: katex
theme: uncover
paginate: True
style: |
   @import url('https://unpkg.com/tailwindcss@2.2.19/dist/utilities.min.css');
   section {display: flex;flex-flow: column; font-size:35px; letter-spacing:1.4px;}

   header {overflow:visible} header > img.logo {position:absolute; right:15px;}

   header > img.logo {position:absolute; right:15px;}


---
<!-- backgroundColor: white -->
<!-- _class: lead -->

 # _Exterior derivative_

---
<style scoped>p,li {font-size:0.92em}</style>

 # Definition
- The exterior derivative is a linear map that takes a form on a manifold and returns another form on the same manifold.
- It is defined as the differential of a function, but it has more properties than just being the differential of a function.


---
<style scoped>p,li {font-size:0.84em}</style>

 # In terms of Axioms
- The exterior derivative is defined in terms of the following axioms:

+ Linearity: $d(f\cdot g) = f\cdot dg + g\cdot df$

+ Leibniz rule: $d(f\cdot g) = f\cdot dg + g\cdot df$

+ Bilinearity: $d(af) = adf$ for any scalar $a$


---
<style scoped>p,li {font-size:0.88em}</style>

 # **In terms of Local Coordinates**

- The exterior derivative can be expressed in local coordinates as:

$$d\omega = \frac{\partial \omega}{\partial x^i} dx^i$$

where $\omega$ is a form and $x^i$ are local coordinates on the manifold.

---
<style scoped>p,li {font-size:0.92em}</style>

 # _In terms of Invariant Formula_
- The exterior derivative can also be expressed in terms of an invariant formula, which is independent of the choice of local coordinates:

$$d\omega = \sum_i \frac{\partial \omega}{\partial x^i} dx^i$$


---
<style scoped>p,li {font-size:0.88em}</style>

 # Examples

- Examples of forms that can be differentiated using the exterior derivative include:

+ The differential form $dx^1 \wedge dx^2$ on $\mathbb{R}^2$

+ The cotangent bundle form $dx^i \in T^\ast M$ on a manifold $M$

---
<style scoped>p,li {font-size:0.88em}</style>

 # Stokes' Theorem on Manifolds
- Stokes' theorem on manifolds states that the exterior derivative of a form is related to the integral of the form over a surface:

$$\int_S d\omega = \int_M \omega$$

where $S$ is a surface in the manifold $M$.


---
<style scoped>p,li {font-size:0.84em}</style>

 # **Further Properties**

- The exterior derivative has other properties that are useful in differential geometry, such as:

+ Closed and exact forms: $d(df) = f\cdot df$, $d(d\omega) = 0$

+ De Rham cohomology: $H^k(M, \mathbb{R}) \cong \frac{\ker d^k}{\im d^{k-1}}$

+ Naturality: $d(\phi^\ast \omega) = \phi^\ast d\omega$ for any smooth function $\phi$.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Closed and Exact Forms

- Closed forms are those that have no exact counterparts, i.e. $d\omega = 0$ implies $\omega$ is closed.
- Exact forms are those that can be written as the exterior derivative of another form, i.e. $\omega = d\eta$ for some form $\eta$.

---
<style scoped>p,li {font-size:0.92em}</style>

 # De Rham Cohomology
- De Rham cohomology is a way of measuring the obstructions to a smooth function being differentiable on an open set.
- It is defined as $H^k(M, \mathbb{R}) \cong \frac{\ker d^k}{\im d^{k-1}}$.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Naturality

- The exterior derivative has naturality, meaning that it pulls back to the same form under a smooth function.
- $d(\phi^\ast \omega) = \phi^\ast d\omega$ for any smooth function $\phi$.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Exterior Derivative in Vector Calculus
- The exterior derivative can also be used in vector calculus to define the gradient, divergence, and curl of a vector field.
- $\nabla f = \frac{\partial f}{\partial x^i} \frac{\partial }{\partial x^i}$ is the gradient of a function $f$.


---
<style scoped>p,li {font-size:0.88em}</style>

 # Gradient, Divergence, Curl
- The gradient of a function $f$ is defined as $\nabla f = \frac{\partial f}{\partial x^i} \frac{\partial }{\partial x^i}$.
- The divergence of a vector field $X$ is defined as $\div X = \sum_i \frac{\partial }{\partial x^i} (X^i)$.
- The curl of a vector field $X$ is defined as $\curl X = \sum_i \frac{\partial X^i}{\partial x^j} - \frac{\partial X^j}{\partial x^i}$.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Invariant Formulations of Operators in Vector Calculus
- The exterior derivative can also be used to define invariant formulations of operators in vector calculus, such as the Laplace-de Rham operator.
- $\Delta = d\cdot d$ is the Laplace-de Rham operator, which is self-adjoint and has a discrete spectrum.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Notes
- The exterior derivative has many applications in differential geometry and related fields.
- It is a fundamental tool for studying the properties of manifolds and the behavior of smooth functions on them.
