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

 # Overdetermined system

---
<style scoped>p,li {font-size:0.92em}</style>

 # Overdetermined Linear Systems of Equations

- Definition: A system of linear equations with more equations than unknowns.
- Also known as "over-determined" or "under-determined" systems.

---
<style scoped>p,li {font-size:0.60em}</style>

 # An Example in Two Dimensions
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Consider the system of two linear equations:

+ 2x + 3y = 10

+ x - 2y = -3
- This system is overdetermined because we have two equations and only two unknowns (x and y).
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/3_equations_-1.JPG/220px-3_equations_-1.JPG'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/3_equations_-2.JPG/220px-3_equations_-2.JPG'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/3_equations_-3.JPG/220px-3_equations_-3.JPG'/>
</div>
</div>
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/3_equations_-4.JPG/220px-3_equations_-4.JPG'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/3_equations_-5.JPG/220px-3_equations_-5.JPG'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/3_equations_-6.JPG/220px-3_equations_-6.JPG'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # Matrix Form

- Overdetermined systems can be represented in matrix form as:

+ Ax = b

+ where A is a matrix of coefficients, x is the vector of unknowns, and b is a vector of constants.

---
<style scoped>p,li {font-size:0.96em}</style>

 # Homogeneous Case

- If the system is homogeneous (i.e., all the coefficients of the equations are zero), then the solution is trivial: x = y = 0.

---
<style scoped>p,li {font-size:0.96em}</style>

 # Non-Homogeneous Case
- If the system is non-homogeneous, then we can solve for the solution using elimination or substitution methods.


---
<style scoped>p,li {font-size:0.84em}</style>

 # Exact Solutions
- In some cases, it is possible to find an exact solution to the system of equations.
- For example, using Cramer's rule, we can find the solution to the system:

+ 2x + 3y = 10

+ x - 2y = -3


---
<style scoped>p,li {font-size:0.84em}</style>

 # Approximate Solutions

- In other cases, it may be necessary to use approximation methods to find a solution.
- For example, we can use the Newton-Raphson method to find an approximate solution to the system:

+ x^2 + y^2 = 10

+ x - y = -3

---
<style scoped>p,li {font-size:0.96em}</style>

 # Overdetermined Nonlinear Systems of Equations
- Overdetermined systems can also be nonlinear, and can be solved using numerical methods such as the Newton-Raphson method.


---
<style scoped>p,li {font-size:0.88em}</style>

 # In General Use
- Overdetermined systems are common in many fields, including physics, engineering, and computer science.
- Solving overdetermined systems can help us understand the behavior of complex systems and make predictions about their behavior.

I hope this slide presentation is helpful! Let me know if you have any questions or need further clarification.
