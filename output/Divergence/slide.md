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

 # Divergence

---
<style scoped>p,li {font-size:0.96em}</style>

 # Introduction

- Subtitle: A fundamental concept in differential geometry and tensor analysis

---
<style scoped>p,li {font-size:0.92em}</style>

 # Physical Interpretation of Divergence
- Definition: The divergence of a vector field is a measure of how the magnitude of the field is changing at a point.
- Physical interpretation: Think of a vector field as a fluid flowing through a region. The divergence of the field at a point tells us whether the fluid is accumulating or dispersing at that location.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Definition
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Mathematical definition: Let $F$ be a vector field on a manifold $M$. The divergence of $F$ at a point $p$ is defined as $\nabla\cdot F(p) = \sum_{i=1}^n \frac{\partial F_i}{\partial x_i}(p)$, where $n$ is the dimension of $M$, $F_i$ are the components of $F$, and $x_i$ are the local coordinates on $M$.
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Definition_of_divergence.svg/220px-Definition_of_divergence.svg.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # **Definition in Coordinates**
- In Cartesian coordinates, the divergence of a vector field $F = (F_1, F_2, F_3)$ is given by $\nabla\cdot F = \frac{\partial F_1}{\partial x} + \frac{\partial F_2}{\partial y} + \frac{\partial F_3}{\partial z}$.
- In cylindrical coordinates, the divergence of a vector field $F = (F_1, F_2, F_3)$ is given by $\nabla\cdot F = \frac{\partial F_1}{\partial r} + \frac{1}{r}\frac{\partial F_2}{\partial \theta} + \frac{\partial F_3}{\partial z}$.
- In spherical coordinates, the divergence of a vector field $F = (F_1, F_2, F_3)$ is given by $\nabla\cdot F = \frac{\partial F_1}{\partial r} + \frac{1}{r^2}\frac{\partial F_2}{\partial \theta} + \frac{1}{r^2\sin\theta}\frac{\partial F_3}{\partial \phi}$.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Tensor Field
- A tensor field is a multi-dimensional generalization of a vector field. The divergence of a tensor field can be defined in a similar way to the vector field case.
- Let $T$ be a tensor field on a manifold $M$. The divergence of $T$ at a point $p$ is defined as $\nabla\cdot T(p) = \sum_{i=1}^n \frac{\partial T_{ij}}{\partial x_i}(p)$, where $n$ is the dimension of $M$, $T_{ij}$ are the components of $T$, and $x_i$ are the local coordinates on $M$.


---
<style scoped>p,li {font-size:0.92em}</style>

 # General Coordinates

- The divergence of a vector field or tensor field can be defined in any coordinate system, not just Cartesian, cylindrical, or spherical.
- In general coordinates, the divergence is given by $\nabla\cdot F = \sum_{i=1}^n \frac{\partial F_i}{\partial x_i}$, where $x_i$ are the local coordinates on $M$.

---
<style scoped>p,li {font-size:0.88em}</style>

 # **Properties**

- The divergence of a vector field or tensor field has several important properties.
- One property is that the divergence of a closed form (a form that is exact) is zero. This is known as the "divergence theorem".
- Another property is that the divergence of a gradient field is zero. This means that the magnitude of a gradient field is not changing at any point.

---
<style scoped>p,li {font-size:0.88em}</style>

 # Decomposition Theorem
- The divergence of a vector field can be decomposed into its component parts.
- Let $F = (F_1, F_2, \ldots, F_n)$ be a vector field on a manifold $M$. Then we have $\nabla\cdot F = \sum_{i=1}^n \frac{\partial F_i}{\partial x_i}$.
- This decomposition is useful for analyzing the properties of vector fields and tensor fields.


---
<style scoped>p,li {font-size:0.92em}</style>

 # In Arbitrary Finite Dimensions
- The concept of divergence can be generalized to arbitrary finite dimensions.
- Let $F$ be a tensor field on a manifold $M$. Then we have $\nabla\cdot F = \sum_{i=1}^n \frac{\partial F_{ij}}{\partial x_i}$, where $n$ is the dimension of $M$ and $F_{ij}$ are the components of $F$.


---
<style scoped>p,li {font-size:0.88em}</style>

 # _Relation to the Exterior Derivative_
- The divergence of a vector field or tensor field is related to the exterior derivative.
- Let $M$ be a manifold and let $F$ be a vector field or tensor field on $M$. Then we have $\nabla\cdot F = d\cdot F$, where $d$ is the exterior derivative.
- This relation is useful for understanding the properties of vector fields and tensor fields.


---
<style scoped>p,li {font-size:0.88em}</style>

 # In Curvilinear Coordinates
- The divergence of a vector field or tensor field can be defined in curvilinear coordinates.
- Let $F$ be a vector field or tensor field on a manifold $M$. Then we have $\nabla\cdot F = \sum_{i=1}^n \frac{\partial F_i}{\partial x_i}$, where $x_i$ are the local coordinates on $M$.
- This definition is useful for analyzing the properties of vector fields and tensor fields in curved spaces.


---
<style scoped>p,li {font-size:0.92em}</style>

 # The Divergence of Tensors

- The divergence of a tensor field can be defined in a similar way to the vector field case.
- Let $T$ be a tensor field on a manifold $M$. Then we have $\nabla\cdot T = \sum_{i=1}^n \frac{\partial T_{ij}}{\partial x_i}$, where $n$ is the dimension of $M$, $T_{ij}$ are the components of $T$, and $x_i$ are the local coordinates on $M$.

---
<style scoped>p,li {font-size:0.88em}</style>

 # Notes

- The divergence of a vector field or tensor field can be used to study the properties of these objects.
- In particular, the divergence can be used to find the "source" or "sink" of a vector field or tensor field.
- The divergence can also be used to study the behavior of vector fields and tensor fields under diffeomorphisms.

---
<style scoped>p,li {font-size:0.84em}</style>

 # Citations
- Some references for further reading on the topic of divergence include:

+ J. R. Munkres, "Topology," Prentice Hall, 2000.

+ A. D. Alexander and J. E. F. Baez, "Introduction to Tensor Calculus," University of California, Berkeley, 2017.

+ S. S. Chern, "Differential Geometry," Science Press, 1984.
