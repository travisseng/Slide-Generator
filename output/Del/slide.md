---
marp: true
math: katex
theme: uncover
style: |
   @import url('https://unpkg.com/tailwindcss@2.2.19/dist/utilities.min.css');
   section {display: flex;flex-flow: column; font-size:35px; letter-spacing:1.4px;}

   header {overflow:visible} header > img.logo {position:absolute; right:15px;}

   header > img.logo {position:absolute; right:15px;}


---
<!-- backgroundImage: url('backgrounds/aaabstract (6).png') -->
<!-- _class: lead -->

 # Del

---
<style scoped>p,li {font-size:0.88em}</style>

 # Definition
- Del (∂) is a symbol used to represent the derivative of a function
- It is often used to denote partial derivatives, which are derived from a function of multiple variables
- The notation ∂f/∂x indicates the derivative of the function f with respect to the variable x


---
<style scoped>p,li {font-size:0.88em}</style>

 # Notational uses

- Del can be used as a shortcut for the notation ∂/∂x, ∂^2/∂x^2, etc.
- It is commonly used in multi-variable calculus and in applications such as optimization and physics
- The notation ∇f represents the gradient of a function f, which is a vector of partial derivatives

---
<style scoped>p,li {font-size:0.88em}</style>

 # Gradient
- The gradient of a function f at a point x = (x1, x2, ..., xn) is a vector of partial derivatives:

∇f(x) = (∂f/∂x1, ∂f/∂x2, ..., ∂f/∂xn)
- The gradient tells us the rate of change of the function in each direction


---
<style scoped>p,li {font-size:0.88em}</style>

 # Divergence

- The divergence of a vector field F at a point x = (x1, x2, ..., xn) is defined as:

∇⋅F(x) = ∂Fx/∂x1 + ∂Fy/∂x2 + ... + ∂Fz/∂xn
- The divergence measures the overall rate of increase of the vector field at a point

---
<style scoped>p,li {font-size:0.88em}</style>

 # Curl
- The curl of a vector field F at a point x = (x1, x2, ..., xn) is defined as:

∇×F(x) = (∂Fz/∂y1 - ∂Fy/∂z1, ∂Fx/∂y2 - ∂Fy/∂x2, ..., ∂Fx/∂z2 - ∂Fz/∂x2)
- The curl measures the rotation of the vector field at a point


---
<style scoped>p,li {font-size:0.88em}</style>

 # Directional derivative
- The directional derivative of a function f at a point x = (x1, x2, ..., xn) in the direction v = (v1, v2, ..., vn) is defined as:

df(x, v) = ∂f/∂x + v·∇f(x)
- The directional derivative tells us the rate of change of the function in a specific direction


---
<style scoped>p,li {font-size:0.88em}</style>

 # **Laplacian**
- The laplacian of a function f at a point x = (x1, x2, ..., xn) is defined as:

∇²f(x) = ∂²f/∂x² + ∂²f/∂y² + ... + ∂²f/∂z²
- The laplacian measures the rate of change of the function in all directions


---
<style scoped>p,li {font-size:0.88em}</style>

 # **Hessian matrix**

- The hessian matrix of a function f at a point x = (x1, x2, ..., xn) is a matrix of second partial derivatives:

Hf(x) = (∂²f/∂x² | ∂²f/∂y² | ... | ∂²f/∂z²)
- The hessian matrix tells us the rate of change of the function in all directions at a point

---
<style scoped>p,li {font-size:0.88em}</style>

 # _Tensor derivative_
- The tensor derivative of a function f at a point x = (x1, x2, ..., xn) is a tensor that represents the rate of change of the function in all directions:

df(x) = (∂f/∂x | ∂f/∂y | ... | ∂f/∂z)
- The tensor derivative is a more general concept than the partial derivatives and can be used to represent the rate of change of functions of multiple variables.


---
<style scoped>p,li {font-size:0.88em}</style>

 # **Product rules**
- The product rule for differentiation states that:

df(x) = (∂f/∂x | ∂f/∂y | ... | ∂f/∂z) = f'(x) + f''(x)
- This rule allows us to compute the derivative of a product of functions by breaking it down into the derivatives of each function and summing them together.


---
<style scoped>p,li {font-size:0.84em}</style>

 # Second derivatives
- The second derivative of a function f at a point x = (x1, x2, ..., xn) is defined as:

df''(x) = ∂²f/∂x² + ∂²f/∂y² + ... + ∂²f/∂z²
- The second derivative measures the rate of change of the function in all directions at a point
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/DCG_chart.svg/220px-DCG_chart.svg.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Precautions_

- When working with partial derivatives, it is important to be careful with the notation and to ensure that the variables are correctly indexed
- It is also important to remember that the partial derivatives of a function can be different at different points, so it is important to specify the point at which the derivative is being taken.