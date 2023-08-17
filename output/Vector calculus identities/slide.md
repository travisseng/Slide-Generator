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

 # Vector calculus identities

---
<style scoped>p,li {font-size:0.92em}</style>

 # Introduction

- Vector calculus is a branch of mathematics that deals with the study of vectors and their properties in space
- It is used to describe the behavior of physical systems, such as fluids and gases, and is essential for studying topics such as optimization, mechanics, and electromagnetism

---
<style scoped>p,li {font-size:0.88em}</style>

 # Operator Notation

- Vector operators are represented by boldface symbols, such as $\mathbf{ Grad}$ and $\mathbf{ Divergence}$
- These operators act on vectors and produce other vectors as output
- The notation is often used to simplify complex calculations and make them more intuitive

---
<style scoped>p,li {font-size:0.92em}</style>

 # Gradient
- The gradient of a function $f(\mathbf{x})$ is the vector of partial derivatives of $f$ with respect to each component of $\mathbf{x}$
- The gradient is used to find the maximum or minimum values of a function, and is essential for studying optimization problems


---
<style scoped>p,li {font-size:0.92em}</style>

 # Divergence
- The divergence of a vector field $\mathbf{F}$ is the sum of the partial derivatives of each component of $\mathbf{F}$ with respect to each component of $\mathbf{x}$
- The divergence is used to describe the source or sink of a vector field, and is essential for studying conservation laws in physics


---
<style scoped>p,li {font-size:0.92em}</style>

 # Curl
- The curl of a vector field $\mathbf{F}$ is the vector that is perpendicular to both the direction of $\mathbf{F}$ and the direction of increasing $x$ coordinate
- The curl is used to describe the rotation of a vector field, and is essential for studying electromagnetism and fluid dynamics


---
<style scoped>p,li {font-size:0.88em}</style>

 # Laplacian
- The laplacian of a function $f(\mathbf{x})$ is the sum of the second partial derivatives of $f$ with respect to each component of $\mathbf{x}$
- The laplacian is denoted by $\nabla^2 f$ or $\frac{\partial^2 f}{\partial x^2}\frac{\partial^2 f}{\partial y^2}\frac{\partial^2 f}{\partial z^2}$
- The laplacian is used to describe the behavior of a function in three-dimensional space, and is essential for studying problems in physics and engineering


---
<style scoped>p,li {font-size:0.88em}</style>

 # _Special Notations_
- The del operator, denoted by $\nabla$, is used to represent the gradient, divergence, and curl of a vector field
- The dot product, denoted by $\cdot$, is used to calculate the scalar product of two vectors
- The cross product, denoted by $\times$, is used to calculate the vector product of two vectors


---
<style scoped>p,li {font-size:0.88em}</style>

 # First Derivative Identities

- The chain rule, denoted by $\frac{d}{dx}f(\mathbf{x}) = \frac{d}{dx}f(g(\mathbf{x}))\cdot \frac{dg}{dx}$, is used to calculate the derivative of a composition of functions
- The product rule for multiplication by a scalar, denoted by $(af)'(x) = a'f'(x) + af'(x)$, is used to calculate the derivative of a function times a constant
- The quotient rule for division by a scalar, denoted by $\frac{d}{dx}\left(\frac{f}{a}\right) = \frac{1}{a^2}\left(\frac{df}{dx} - f'a\right)$, is used to calculate the derivative of a function divided by a constant

---
<style scoped>p,li {font-size:0.92em}</style>

 # Distributive Properties
- The distributive property of multiplication over addition, denoted by $(ab)f = afb + afo$, is used to simplify complex calculations involving multiple functions
- The distributive property of division over subtraction, denoted by $\frac{a}{b} - \frac{c}{d} = \frac{a - c}{b - d}$, is used to simplify complex calculations involving fractions


---
<style scoped>p,li {font-size:0.96em}</style>

 # Product Rule for Multiplication by a Scalar

- The product rule for multiplication by a scalar, denoted by $(af)'(x) = a'f'(x) + af'(x)$, is used to calculate the derivative of a function times a constant

---
<style scoped>p,li {font-size:0.96em}</style>

 # Quotient Rule for Division by a Scalar
- The quotient rule for division by a scalar, denoted by $\frac{d}{dx}\left(\frac{f}{a}\right) = \frac{1}{a^2}\left(\frac{df}{dx} - f'a\right)$, is used to calculate the derivative of a function divided by a constant


---
<style scoped>p,li {font-size:0.96em}</style>

 # **Chain Rule**
- The chain rule, denoted by $\frac{d}{dx}f(g(\mathbf{x})) = \frac{d}{dx}f(h(x)) \cdot \frac{dh}{dx}$, is used to calculate the derivative of a composition of functions


---
<style scoped>p,li {font-size:0.96em}</style>

 # Dot Product Rule

- The dot product rule, denoted by $\mathbf{a} \cdot \mathbf{b} = a_1b_1 + a_2b_2 + a_3b_3$, is used to calculate the scalar product of two vectors

---
<style scoped>p,li {font-size:0.96em}</style>

 # _Cross Product Rule_

- The cross product rule, denoted by $\mathbf{a} \times \mathbf{b} = a_1b_2 - a_2b_1 + a_3b_3$, is used to calculate the vector product of two vectors

---
<style scoped>p,li {font-size:0.92em}</style>

 # Second Derivative Identities
- The second derivative of a function $f(\mathbf{x})$ is denoted by $\frac{\partial^2 f}{\partial x^2}$
- The second derivative can be calculated using the chain rule and the first derivative identities


---
<style scoped>p,li {font-size:0.96em}</style>

 # _Divergence of Curl is Zero_
- The divergence of the curl of a vector field $\mathbf{F}$ is zero, denoted by $\nabla \cdot (\nabla \times \mathbf{F}) = 0$


---
<style scoped>p,li {font-size:0.96em}</style>

 # Divergence of Gradient is Laplacian
- The divergence of the gradient of a function $f(\mathbf{x})$ is the laplacian of $f$, denoted by $\nabla \cdot (\nabla f) = \nabla^2 f$


---
<style scoped>p,li {font-size:0.96em}</style>

 # **Divergence of Divergence is Not Defined**

- The divergence of the divergence of a vector field $\mathbf{F}$ is not defined, denoted by $\nabla \cdot (\nabla \cdot \mathbf{F}) = \frac{\partial }{\partial t}$ is not a well-defined quantity

---
<style scoped>p,li {font-size:0.96em}</style>

 # Curl of Gradient is Zero

- The curl of the gradient of a function $f(\mathbf{x})$ is zero, denoted by $\nabla \times (\nabla f) = 0$

---
<style scoped>p,li {font-size:0.96em}</style>

 # Curl of Curl
- The curl of the curl of a vector field $\mathbf{F}$ is not defined, denoted by $\nabla \times (\nabla \times \mathbf{F}) = \frac{\partial }{\partial y}$ is not a well-defined quantity


---
<style scoped>p,li {font-size:0.96em}</style>

 # A Mnemonic
- The mnemonic "GDC" can be used to remember the order of operations for vector calculus: gradient, divergence, curl


---
<style scoped>p,li {font-size:0.92em}</style>

 # Summary of Important Identities
- Vector calculus identities include the chain rule, product rule for multiplication by a scalar, quotient rule for division by a scalar, dot product rule, cross product rule, and second derivative identities
- These identities are essential for studying problems in physics and engineering


---
<style scoped>p,li {font-size:0.92em}</style>

 # Differentiation

- Differentiation is the process of finding the derivative of a function
- Vector calculus provides powerful tools for differentiating functions of vectors and scalars

---
<style scoped>p,li {font-size:0.96em}</style>

 # Vector Dot Del Operator

- The vector dot del operator is used to calculate the dot product of two vectors in a way that is consistent with the chain rule and the product rule for multiplication by a scalar

---
<style scoped>p,li {font-size:0.92em}</style>

 # Second Derivatives
- Second derivatives are used to study the behavior of functions over time or space
- Vector calculus provides powerful tools for calculating second derivatives and studying their properties


---
<style scoped>p,li {font-size:0.96em}</style>

 # _Third Derivatives_

- Third derivatives are used to study the behavior of functions over time or space, and are essential for studying problems in physics and engineering

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Integration**

- Integration is the process of finding the definite integral of a function
- Vector calculus provides powerful tools for integrating functions of vectors and scalars, and is essential for studying problems in physics and engineering.