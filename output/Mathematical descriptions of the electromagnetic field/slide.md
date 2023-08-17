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

 # Mathematical descriptions of the electromagnetic field

---
<style scoped>p,li {font-size:0.96em}</style>

 # Introduction

- Overview: The electromagnetic field is a fundamental concept in physics that describes the interactions between charged particles and the electromagnetic force. There are several mathematical approaches to describing the electromagnetic field, each with its own strengths and weaknesses.

---
<style scoped>p,li {font-size:0.76em}</style>

 # Vector field approach
- Overview: In this approach, the electromagnetic field is described by a vector field, which assigns a direction and magnitude to the electric and magnetic fields at each point in space and time.

Maxwell's Equations in the Vector Field Approach
- Gauss's law for electric fields: ∇⋅E = ρ/ε0 (1)
- Gauss's law for magnetic fields: ∇×B = 0 (2)
- Faraday's law of induction: ∇×E = -∂B/∂t (3)
- Ampere's law with Maxwell's correction: ∇×B = μ0J + μ0ε0 ∂E/∂t (4)


---
<style scoped>p,li {font-size:0.76em}</style>

 # Potential field approach
- Overview: In this approach, the electromagnetic field is described by a set of potential functions that define the electric and magnetic fields.

Maxwell's Equations in the Potential Formulation
- Electric potential φ: ∇²φ = ρ/ε0 (1)
- Magnetic potential A: ∇×A = μ0J (2)
- Gauss's law for electric fields: ∇⋅E = 0 (3)
- Faraday's law of induction: ∇×E = -∂B/∂t (4)


---
<style scoped>p,li {font-size:0.84em}</style>

 # **Gauge freedom**

- Overview: The vector field and potential formulations are not unique and can be transformed into each other through a process called gauge transformation. This freedom allows us to choose the formulation that is most convenient for a given problem.

Gauge Transformation
- ∇ → ∇ + ∂/∂t (5)
- A → A - ∂φ/∂t (6)

---
<style scoped>p,li {font-size:0.80em}</style>

 # Coulomb gauge, Lorenz gauge condition
- Overview: The Coulomb gauge and Lorenz gauge condition are two commonly used gauge conditions that fix the freedom in the vector field formulation.

Coulomb Gauge
- ∇⋅E = 0 (7)

Lorenz Gauge Condition
- ∇×B - μ0J = 0 (8)


---
<style scoped>p,li {font-size:0.96em}</style>

 # Extension to quantum electrodynamics

- Overview: The mathematical descriptions of the electromagnetic field can be extended to include quantum effects, which lead to the development of quantum electrodynamics.

---
<style scoped>p,li {font-size:0.96em}</style>

 # Geometric algebra formulations
- Overview: Geometric algebra is a mathematical framework that can be used to describe the electromagnetic field in a more geometric and unified way.


---
<style scoped>p,li {font-size:0.96em}</style>

 # Differential forms approach
- Overview: The differential forms approach is a mathematical framework that uses differential forms to describe the electromagnetic field. This approach provides a more elegant and compact way of expressing Maxwell's equations.


---
<style scoped>p,li {font-size:0.96em}</style>

 # **Field 2-form, current 3-form, dual current 1-form**
- Overview: In the differential forms approach, the electromagnetic field is described by a 2-form (F), the electric current is described by a 3-form (J), and the magnetic current is described by a 1-form (B). These objects satisfy certain algebraic equations that are equivalent to Maxwell's equations.


---
<style scoped>p,li {font-size:0.96em}</style>

 # _Linear macroscopic influence of matter_
- Overview: The linear macroscopic influence of matter describes the effect of matter on the electromagnetic field in a way that is easy to compute and analyze. This approach is useful for understanding the behavior of charged particles in high-energy collisions.


---
<style scoped>p,li {font-size:0.96em}</style>

 # Alternate metric signature
- Overview: The alternate metric signature is a mathematical technique that allows us to describe the electromagnetic field in a way that is more manifestly covariant and easier to work with in certain situations.


---
<style scoped>p,li {font-size:0.96em}</style>

 # Curved spacetime
- Overview: In general relativity, spacetime is curved by the presence of matter and energy. This curvature affects the behavior of the electromagnetic field and must be taken into account when describing the interaction between light and matter in strong-field situations.


---
<style scoped>p,li {font-size:0.96em}</style>

 # Traditional formulation, formulation in terms of differential forms
- Overview: The traditional formulation of electromagnetism is based on the vector field approach, while the formulation in terms of differential forms is based on the potential field approach. Both formulations are equivalent and can be used to describe the electromagnetic field. The choice of formulation depends on the specific problem being solved and the desired level of mathematical complexity.


---
<style scoped>p,li {font-size:0.96em}</style>

 # **Manifestly covariant (tensor) approach**

- Overview: The manifestly covariant approach is a mathematical framework that describes the electromagnetic field in terms of tensors, which are more general and flexible than vectors. This approach provides a more elegant and unified way of describing the electromagnetic field and its interactions with matter.

---
<style scoped>p,li {font-size:0.96em}</style>

 # Differential geometric calculus approach
- Overview: The differential geometric calculus approach is a mathematical framework that uses differential geometry to describe the electromagnetic field. This approach provides a more elegant and unified way of describing the electromagnetic field and its interactions with matter.


---
<style scoped>p,li {font-size:0.96em}</style>

 # Notes

- Overview: These notes provide additional information and references for further reading on the mathematical descriptions of the electromagnetic field.

---
<style scoped>p,li {font-size:0.96em}</style>

 # Conclusion

- Overview: In conclusion, the mathematical descriptions of the electromagnetic field are a fundamental aspect of physics and engineering. There are several approaches to describing the electromagnetic field, each with its own strengths and weaknesses. The choice of approach depends on the specific problem being solved and the desired level of mathematical complexity.