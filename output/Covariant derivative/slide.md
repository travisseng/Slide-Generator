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

 # Covariant derivative

---
<style scoped>p,li {font-size:0.96em}</style>

 # _Title_

- Covariant Derivative

---
<style scoped>p,li {font-size:0.92em}</style>

 # History
- The concept of the covariant derivative was introduced by Elie Cartan in the early 20th century.
- It has since become a fundamental tool in differential geometry and theoretical physics.


---
<style scoped>p,li {font-size:0.88em}</style>

 # Motivation
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/%D0%9A%D0%BE%D0%B2%D0%B0%D1%80%D0%B8%D0%B0%D0%BD%D1%82%D0%BD%D0%B0%D1%8F_%D0%BF%D1%80%D0%BE%D0%B8%D0%B7%D0%B2%D0%BE%D0%B4%D0%BD%D0%B0%D1%8F_c.jpg/144px-%D0%9A%D0%BE%D0%B2%D0%B0%D1%80%D0%B8%D0%B0%D0%BD%D1%82%D0%BD%D0%B0%D1%8F_%D0%BF%D1%80%D0%BE%D0%B8%D0%B7%D0%B2%D0%BE%D0%B4%D0%BD%D0%B0%D1%8F_c.jpg'/>
</div>
</div>

- The covariant derivative is a way to measure the rate of change of a vector or tensor field on a manifold, while preserving the geometric structure of the manifold.
- It is a key ingredient in the study of differentiable manifolds and their properties.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Remarks
- The covariant derivative is also known as the "connection" or "torsion" of a manifold.
- It is a way to measure the curvature of a manifold, and it plays an important role in the study of geodesics and other manifolds properties.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Informal definition using an embedding into Euclidean space
- The covariant derivative can be informally defined as the derivative of a vector or tensor field on a manifold, when we embed the manifold into Euclidean space.
- In this case, the derivative is taken with respect to the Euclidean coordinates, rather than the manifold's own coordinates.


---
<style scoped>p,li {font-size:0.88em}</style>

 # Formal definition
- The covariant derivative of a vector or tensor field $F$ on a manifold $M$ is defined as:

$$\frac{\partial F}{\partial x^i} = \frac{\partial }{\partial x^i} (F^a_{,i})$$

where $F^a$ is the component of $F$ in some local basis, and $x^i$ are the coordinates on $M$.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Functions
- The covariant derivative of a function $f$ on a manifold $M$ is defined as:

$$\frac{\partial f}{\partial x^i} = \frac{\partial }{\partial x^i} (f)$$


---
<style scoped>p,li {font-size:0.88em}</style>

 # Vector fields

- The covariant derivative of a vector field $V$ on a manifold $M$ is defined as:

$$\frac{\partial V}{\partial x^i} = \frac{\partial }{\partial x^i} (V^a)$$

where $V^a$ is the component of $V$ in some local basis.

---
<style scoped>p,li {font-size:0.88em}</style>

 # **Covector fields**

- The covariant derivative of a covector field $\alpha$ on a manifold $M$ is defined as:

$$\frac{\partial \alpha}{\partial x^i} = - \frac{\partial }{\partial x^i} (\alpha_a)$$

where $\alpha_a$ is the component of $\alpha$ in some local basis.

---
<style scoped>p,li {font-size:0.88em}</style>

 # Tensor fields
- The covariant derivative of a tensor field $T$ on a manifold $M$ is defined as:

$$\frac{\partial T}{\partial x^i} = \frac{\partial }{\partial x^i} (T_{ab})$$

where $T_{ab}$ is the component of $T$ in some local basis.


---
<style scoped>p,li {font-size:0.88em}</style>

 # _Coordinate description_
- The covariant derivative can be described in terms of the coordinates on $M$. Specifically, if we have a coordinate system $(x^i)$ on $M$, then:

$$\frac{\partial F}{\partial x^i} = \frac{\partial }{\partial x^i} (F^a)$$

where $F^a$ is the component of $F$ in some local basis.


---
<style scoped>p,li {font-size:0.96em}</style>

 # _Notation_
- The covariant derivative is often denoted by a symbol such as $\frac{\partial }{\partial x^i}$, or by a subscript such as $F_{,i}$.


---
<style scoped>p,li {font-size:0.80em}</style>

 # _Covariant derivative by field type_

- The covariant derivative can be defined differently for different types of fields on a manifold. For example:

$$\frac{\partial f}{\partial x^i} = \frac{\partial }{\partial x^i} (f)$$

$$\frac{\partial V}{\partial x^i} = \frac{\partial }{\partial x^i} (V^a)$$

$$\frac{\partial \alpha}{\partial x^i} = - \frac{\partial }{\partial x^i} (\alpha_a)$$

$$\frac{\partial T}{\partial x^i} = \frac{\partial }{\partial x^i} (T_{ab})$$

---
<style scoped>p,li {font-size:0.84em}</style>

 # Properties
- The covariant derivative has several important properties, including:

1. Linearity: $\frac{\partial (f+g)}{\partial x^i} = \frac{\partial f}{\partial x^i} + \frac{\partial g}{\partial x^i}$

2. Metric compatibility: $\frac{\partial f}{\partial x^i} = g^{ij} \frac{\partial f}{\partial g_{ij}}$

3. Torsion-freeness: $\frac{\partial F}{\partial x^i} - \frac{\partial F}{\partial x^j} + \frac{\partial F}{\partial x^k} = 0$


---
<style scoped>p,li {font-size:0.88em}</style>

 # Derivative along a curve
- The covariant derivative can also be defined for a curve on a manifold. Specifically, if we have a curve $c(t)$ on $M$, then:

$$\frac{DF}{dt} = \frac{\partial F}{\partial x^i} \dot{x}^i + \Gamma^a_{ij} F^j \dot{x}^i$$

where $\dot{x}^i$ is the velocity of $c(t)$, and $\Gamma^a_{ij}$ are the Christoffel symbols of $M$.


---
<style scoped>p,li {font-size:0.88em}</style>

 # Relation to Lie derivative
- The covariant derivative is closely related to the Lie derivative, which is a measure of how a vector field changes along a curve on a manifold. Specifically:

$$\frac{DV}{dt} = \frac{\partial V}{\partial x^i} \dot{x}^i + [V, \dot{x}^i]$$

where $[V, \dot{x}^i]$ is the Lie derivative of $V$ along $c(t)$.


---
<style scoped>p,li {font-size:0.88em}</style>

 # **Notes**
- The covariant derivative is a fundamental tool in differential geometry and theoretical physics.
- It is used to study the properties of manifolds and the behavior of fields on those manifolds.
- The covariant derivative has many applications, including in the study of geodesics, curvature, and tensors.
