---
marp: true
math: katex
theme: gaia
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

 # _Kelvin–Stokes theorem_

---
<style scoped>p,li {font-size:0.92em}</style>

 # Theorem

Kelvin-Stokes Theorem:

For a closed curve C in the plane, the line integral of the vector field around C is equal to the surface integral of the curl of the vector field over the surface enclosed by C.


---
<style scoped>p,li {font-size:0.36em}</style>

 # Proof


Elementary Proof

Step 1: Parametrization of Integral

Let C be a closed curve in the plane, and let r(t) be a parameterization of C. Then, we can write the line integral of the vector field F around C as:

$$\oint_C F \cdot dr = \int_0^1 F(\mathbf{r}(t)) \cdot \frac{d\mathbf{r}}{dt} dt$$

Step 2: Defining the Pullback

We can define the pullback of a vector field F over a surface S as:

$$F_S = \left. \frac{\partial F}{\partial r} \right|_{\mathbf{r}(t)} \cdot \frac{d\mathbf{r}}{dt}$$

where $\frac{\partial F}{\partial r}$ is the partial derivative of F with respect to the parameter r.

Step 3: Second Equation

Using the definition of the pullback, we can write the line integral of F around C as:

$$\oint_C F \cdot dr = \int_0^1 F(\mathbf{r}(t)) \cdot \frac{d\mathbf{r}}{dt} dt = \int_0^1 F_S(\mathbf{r}(t)) dt$$

where $F_S$ is the pullback of F over the surface enclosed by C.

Step 4: Reduction to Green's Theorem

Using Green's theorem, we can rewrite the integral as:

$$\oint_C F \cdot dr = \int_0^1 F_S(\mathbf{r}(t)) dt = \iint_{S} (\nabla \times F) \cdot dA$$

where $\nabla \times F$ is the curl of the vector field F, and $dA$ is the area element.

---
<style scoped>p,li {font-size:0.76em}</style>

 # Proof via Differential Forms

Using the definition of the exterior derivative, we can write the line integral of F around C as:

$$\oint_C F \cdot dr = \int_0^1 F \cdot \frac{d\mathbf{r}}{dt} dt = \int_0^1 F \cdot \frac{\partial \mathbf{r}}{\partial t} dt$$

where $\frac{\partial \mathbf{r}}{\partial t}$ is the partial derivative of the parameterization r with respect to t.

Using the exterior derivative, we can rewrite the integral as:

$$\oint_C F \cdot dr = \int_0^1 F \cdot \frac{\partial \mathbf{r}}{\partial t} dt = \iint_{S} (df) \cdot dA$$

where $df$ is the differential form of F.


---
<style scoped>p,li {font-size:0.84em}</style>

 # Applications


Kelvin-Stokes theorem has many applications in physics and engineering, including:
- Electromagnetic fields: The theorem can be used to calculate the flux of an electromagnetic field through a surface enclosed by a curve.
- Irrotational fields: The theorem can be used to show that the line integral of an irrotational field over a closed curve is zero.
- Conservative forces: The theorem can be used to prove that conservative forces, such as gravity and electricity, are inward-pointing at every point on a surface enclosed by a curve.

---
<style scoped>p,li {font-size:0.96em}</style>

 # Irrotational Fields


Irrotational fields are vector fields that have no rotational component. The Kelvin-Stokes theorem can be used to show that the line integral of an irrotational field over a closed curve is zero.

---
<style scoped>p,li {font-size:0.88em}</style>

 # Helmholtz's Theorems

Helmholtz's theorems are two related results in vector calculus that follow from Kelvin-Stokes theorem. They state that:
- The line integral of a conservative field over a closed curve is zero.
- The line integral of a gradient field over a closed curve is equal to the surface integral of the gradient over the surface enclosed by the curve.


---
<style scoped>p,li {font-size:0.72em}</style>

 # Proof of Helmholtz's Theorems

Using Kelvin-Stokes theorem, we can prove Helmholtz's theorems as follows:
- For a conservative field F, we have:

$$\oint_C F \cdot dr = \iint_{S} (\nabla \times F) \cdot dA = 0$$

where S is the surface enclosed by C.
- For a gradient field G, we have:

$$\oint_C G \cdot dr = \iint_{S} G \cdot dA = \iint_{S} (\nabla G) \cdot dA$$

where $\nabla G$ is the gradient of G.


---
<style scoped>p,li {font-size:0.96em}</style>

 # Conservative Forces

Conservative forces are forces that conserve energy. The Kelvin-Stokes theorem can be used to prove that conservative forces, such as gravity and electricity, are inward-pointing at every point on a surface enclosed by a curve.


---
<style scoped>p,li {font-size:0.96em}</style>

 # **Maxwell's Equations**

Maxwell's equations are a set of four equations that describe the behavior of electromagnetic fields. The Kelvin-Stokes theorem can be used to prove one of these equations, which states that the line integral of the electric field over a closed curve is equal to the surface integral of the electric field over the surface enclosed by the curve.


---
<style scoped>p,li {font-size:0.84em}</style>

 # _Notes_

- The Kelvin-Stokes theorem is also known as the "Kelvin-Stokes formula" or the "integral formula for closed curves".
- The theorem has many applications in physics and engineering, including electromagnetic fields, irrotational fields, conservative forces, and Maxwell's equations.
- The proof of the theorem involves parameterizing the curve C with a parameter r(t), defining the pullback of the vector field F over the surface S enclosed by C, and using Green's theorem to reduce the integral to a surface integral.

I hope this presentation helps you understand Kelvin-Stokes theorem! Let me know if you have any questions or need further clarification.