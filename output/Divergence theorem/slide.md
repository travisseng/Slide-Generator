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
<!-- backgroundImage: url('backgrounds/aaabstract (2).png') -->
<!-- _class: lead -->

 # Divergence theorem

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Explanation using Liquid Flow_

- The Divergence Theorem states that the net flow of a fluid out of a closed surface is equal to the volume enclosed by the surface.
- Think of a liquid flowing into or out of a container with a small hole in it. The liquid flowing out of the hole is equal to the volume of the liquid inside the container.

---
<style scoped>p,li {font-size:0.84em}</style>

 # Mathematical Statement
- The Divergence Theorem states that for any closed surface S in a manifold, we have:

$$\int_{S} \nabla \cdot \mathbf{F} dA = \int_{V} \mathbf{F} dV$$

where $\mathbf{F}$ is a vector field on the manifold, $dA$ is the area element of the surface, and $dV$ is the volume element of the volume enclosed by the surface.
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Divergence_theorem.svg/250px-Divergence_theorem.svg.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.72em}</style>

 # _Informal Derivation_
- The Divergence Theorem can be informally derived by considering the definition of a gradient.
- The gradient of a function at a point is the direction in which the function increases most rapidly.
- If we have a vector field $\mathbf{F}$ and a surface $S$, we can think of the gradient of $\mathbf{F}$ as the "flow" of the vector field out of the surface.
- The Divergence Theorem states that the net flow of the vector field out of the surface is equal to the volume enclosed by the surface.
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Divergence_theorem_1_-_split_volume.png/440px-Divergence_theorem_1_-_split_volume.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Divergence_theorem_2_-_volume_partition.png/440px-Divergence_theorem_2_-_volume_partition.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Divergence_theorem_3_-_infinitesimals.png/220px-Divergence_theorem_3_-_infinitesimals.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.84em}</style>

 # **Proofs**
- There are several ways to prove the Divergence Theorem, including:

1. Using the definition of the gradient and the exterior derivative.

2. Using the fact that the divergence of a vector field is equal to the sum of the partial derivatives of the components of the vector field.

3. Using the Gauss-Bonnet theorem, which states that the total flux of a vector field out of a closed surface is equal to the total curvature of the surface.


---
<style scoped>p,li {font-size:0.92em}</style>

 # For Bounded Open Sets of Euclidean Space
- If $U$ is a bounded open set in $\mathbb{R}^n$, then we can use the Divergence Theorem to prove that the net flow of a vector field out of $U$ is equal to the volume of $U$.
- This has applications in physics, where it can be used to relate the flow of a fluid out of a container to the volume of the container.


---
<style scoped>p,li {font-size:0.92em}</style>

 # **For Compact Riemannian Manifolds with Boundary**
- If $M$ is a compact Riemannian manifold with boundary, then we can use the Divergence Theorem to prove that the net flow of a vector field out of $M$ is equal to the volume of $M$.
- This has applications in physics, where it can be used to relate the flow of a fluid out of a container to the volume of the container.


---
<style scoped>p,li {font-size:0.84em}</style>

 # Corollaries

- The Divergence Theorem has several corollaries that are useful in physics and engineering, including:

1. The Gauss-Bonnet theorem, which states that the total flux of a vector field out of a closed surface is equal to the total curvature of the surface.

2. The Stokes' theorem, which states that the line integral of a vector field along a curve is equal to the surface integral of the curl of the vector field over the surface enclosed by the curve.

3. The Maxwell's equation, which relates the electric and magnetic fields in a vacuum.

---
<style scoped>p,li {font-size:0.84em}</style>

 # **Example**
- Let $U$ be a bounded open set in $\mathbb{R}^3$ and let $\mathbf{F} = (F_1, F_2, F_3)$ be a vector field on $U$.
- Then, we can use the Divergence Theorem to prove that the net flow of $\mathbf{F}$ out of $U$ is equal to the volume of $U$.
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Vector_Field_on_a_Sphere.png/220px-Vector_Field_on_a_Sphere.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/SurfacesWithAndWithoutBoundary.svg/200px-SurfacesWithAndWithoutBoundary.svg.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.84em}</style>

 # Applications
- The Divergence Theorem has several applications in physics and engineering, including:

1. Fluid dynamics, where it can be used to relate the flow of a fluid out of a container to the volume of the container.

2. Electromagnetism, where it can be used to relate the electric and magnetic fields in a vacuum.

3. Continuum mechanics, where it can be used to relate the stress and strain of a material.


---
<style scoped>p,li {font-size:0.76em}</style>

 # Differential and Integral Forms of Physical Laws
- Many physical laws can be expressed in both differential and integral forms.
- For example, Newton's second law of motion can be expressed as:

$$\frac{d\mathbf{p}}{dt} = \mathbf{F}$$

or as:

$$\int_{t_1}^{t_2} \mathbf{F}(t) dt = \Delta \mathbf{p}$$

where $\mathbf{p}$ is the momentum of an object, $F$ is the force acting on the object, and $\Delta \mathbf{p}$ is the change in momentum over time.


---
<style scoped>p,li {font-size:0.84em}</style>

 # Continuity Equations
- In addition to the Divergence Theorem, there are several other important theorems in differential geometry, including:

1. The Continuity Equation, which states that the divergence of a vector field is equal to the sum of the partial derivatives of the components of the vector field.

2. The Gauss-Bonnet theorem, which states that the total flux of a vector field out of a closed surface is equal to the total curvature of the surface.

3. The Stokes' theorem, which states that the line integral of a vector field along a curve is equal to the surface integral of the curl of the vector field over the surface enclosed by the curve.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Inverse-Square Laws

- Many physical laws can be expressed in inverse-square form, where the magnitude of a quantity decreases with the distance from a source.
- For example, the law of gravity states that the gravitational force between two objects decreases with the square of the distance between them.

---
<style scoped>p,li {font-size:0.92em}</style>

 # History

- The Divergence Theorem has a long history, dating back to the work of Gauss and Bonnet in the early 19th century.
- The theorem was later developed by Stokes and other mathematicians, who used it to prove several important results in physics and engineering.

---
<style scoped>p,li {font-size:0.84em}</style>

 # Worked Examples

- Let's consider a few examples of how the Divergence Theorem can be applied in practice:

1. Find the net flow of a vector field out of a bounded open set in $\mathbb{R}^3$.

2. Prove that the total flux of a vector field out of a closed surface is equal to the total curvature of the surface.

3. Apply the Divergence Theorem to a physical problem, such as fluid dynamics or electromagnetism.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Example 1
- Let $U$ be a bounded open set in $\mathbb{R}^3$ and let $\mathbf{F} = (F_1, F_2, F_3)$ be a vector field on $U$.
- Then, we can use the Divergence Theorem to prove that the net flow of $\mathbf{F}$ out of $U$ is equal to the volume of $U$.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Example 2

- Let $M$ be a compact Riemannian manifold with boundary and let $\mathbf{F} = (F_1, F_2, F_3)$ be a vector field on $M$.
- Then, we can use the Divergence Theorem to prove that the net flow of $\mathbf{F}$ out of $M$ is equal to the volume of $M$.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Generalizations
- The Divergence Theorem can be generalized to higher-dimensional spaces and to more complex vector fields.
- For example, we can define a divergence operator on a manifold that assigns a scalar value to each point on the manifold.


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Multiple Dimensions_

- In higher-dimensional spaces, the Divergence Theorem can be generalized to include multiple dimensions.
- For example, we can define a divergence operator on a manifold in $\mathbb{R}^n$ that assigns a scalar value to each point on the manifold.

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Tensor Fields_
- In addition to vector fields, we can also define divergence operators for tensor fields.
- For example, we can define a divergence operator for a rank-2 tensor field that assigns a scalar value to each point on the manifold.


---
<style scoped>p,li {font-size:0.88em}</style>

 # Conclusion
- The Divergence Theorem is a fundamental theorem in differential geometry and physics that relates the net flow of a vector field out of a surface to the volume enclosed by the surface.
- It has many applications in physics and engineering, including fluid dynamics, electromagnetism, and continuum mechanics.
- By understanding the Divergence Theorem, we can gain insights into the behavior of physical systems and solve important problems in physics and engineering.
