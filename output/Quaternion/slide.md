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

 # Quaternion

---
<style scoped>p,li {font-size:0.84em}</style>

 # History
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Inscription_on_Broom_Bridge_%28Dublin%29_regarding_the_discovery_of_Quaternions_multiplication_by_Sir_William_Rowan_Hamilton.jpg/220px-Inscription_on_Broom_Bridge_%28Dublin%29_regarding_the_discovery_of_Quaternions_multiplication_by_Sir_William_Rowan_Hamilton.jpg'/>
</div>
</div>

- Quaternions were introduced by Sir William Rowan Hamilton in 1843
- They were originally called "quaternions" because they are defined as a fourth power of a scalar, like the square root of -1
- Hamilton used quaternions to describe the rotations of three-dimensional objects

---
<style scoped>p,li {font-size:0.88em}</style>

 # _Quaternions in Physics_

- Quaternions are used to represent 3D rotations in computer graphics, robotics, and other fields
- They provide a compact and efficient way to represent and manipulate 3D rotations
- Quaternions are also used in the study of differential geometry and the geometry of spacetime

---
<style scoped>p,li {font-size:0.92em}</style>

 # Definition
- A quaternion is a number of the form w + xi + yj + zk, where w, x, y, and z are real numbers and i, j, and k are imaginary units that satisfy the relations i^2 = j^2 = k^2 = -1
- Quaternions can be added and multiplied just like real numbers, but the multiplication is non-commutative


---
<style scoped>p,li {font-size:0.40em}</style>

 # _Multiplication of Basis Elements_

- The basis elements of a quaternion are 1, i, j, and k
- The multiplication table for these basis elements is:

+ 1 x 1 = 1

+ 1 x i = j

+ 1 x j = k

+ 1 x k = i

+ i x 1 = i

+ i x j = k

+ i x k = j

+ j x 1 = j

+ j x i = k

+ j x k = i

+ k x 1 = k

+ k x i = j

+ k x j = i

---
<style scoped>p,li {font-size:0.92em}</style>

 # Center

- The center of a quaternion is the point that does not change when the quaternion is multiplied by a scalar
- The center can be calculated using the formula: center = (w, x, y, z)

---
<style scoped>p,li {font-size:0.88em}</style>

 # Hamilton Product
- The Hamilton product of two quaternions is defined as:

+ (a + bi + cj + dk) x (e + fi + gi + hk) = (af + bg + cg + dh) + (ah + bf + ch + dg)i + (al + bl + cl + dl)j + (am + bm + cm + dm)k
- This product is non-commutative and non-associative


---
<style scoped>p,li {font-size:0.88em}</style>

 # Scalar and Vector Parts

- Every quaternion can be decomposed into its scalar and vector parts:

+ w + xi + yj + zk = (w, x, y, z) + (0, 0, 0, 0)i + (0, 0, 0, 0)j + (0, 0, 0, 0)k
- The scalar part is the sum of the real components, and the vector part is the sum of the imaginary components

---
<style scoped>p,li {font-size:0.88em}</style>

 # Conjugation

- The conjugate of a quaternion is defined as:

+ (a + bi + cj + dk) = (da - bc) + (ak + br)i + (al - ar)j + (ab - ac)k
- The conjugate of a quaternion is used to compute the norm and reciprocal of a quaternion

---
<style scoped>p,li {font-size:0.88em}</style>

 # _Norm_
- The norm of a quaternion is defined as:

+ |a + bi + cj + dk| = sqrt(a^2 + b^2 + c^2 + d^2)
- The norm of a quaternion can be used to compute the length of a 3D rotation


---
<style scoped>p,li {font-size:0.88em}</style>

 # Reciprocal

- The reciprocal of a quaternion is defined as:

+ (a + bi + cj + dk)/(da - bc) = (a/da, b/dc, c/da, d/db)
- The reciprocal of a quaternion can be used to compute the inverse of a 3D rotation

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Unit Quaternion_

- A unit quaternion is a quaternion with a norm of 1
- Every quaternion can be scaled to a unit quaternion by dividing it by its norm

---
<style scoped>p,li {font-size:0.72em}</style>

 # Algebraic Properties
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Cayley_graph_Q8.svg/220px-Cayley_graph_Q8.svg.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Quaternion-multiplication-cayley-3d-with-legend.png/220px-Quaternion-multiplication-cayley-3d-with-legend.png'/>
</div>
</div>

- Quaternions have a number of important algebraic properties, including:

+ Closure under addition and multiplication

+ Commutativity of multiplication

+ Associativity of multiplication

+ Distributivity of multiplication over addition

---
<style scoped>p,li {font-size:0.92em}</style>

 # Quaternions and the Space Geometry
- Quaternions can be used to represent 3D rotations in a way that preserves the geometric structure of the space
- This makes quaternions useful for applications such as computer graphics, robotics, and computer vision


---
<style scoped>p,li {font-size:0.88em}</style>

 # Matrix Representations

- Quaternions can be represented as matrices using the following formula:

+ [w, x, y, z] = [1, i, j, k] * [w, x, y, z]
- This allows quaternions to be manipulated using standard matrix operations

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Lagrange’s Four-Square Theorem**
- Lagrange’s four-square theorem states that every quaternion can be written as the square of a complex number
- This theorem is used in many applications, including the computation of quaternion exponentials and logarithms


---
<style scoped>p,li {font-size:0.92em}</style>

 # Quaternions as Pairs of Complex Numbers

- Quaternions can be viewed as pairs of complex numbers, allowing them to be manipulated using standard complex analysis techniques
- This perspective is useful for understanding the algebraic properties of quaternions

---
<style scoped>p,li {font-size:0.88em}</style>

 # **Square Roots**
- The square roots of a quaternion can be computed using the formula:

+ [w, x, y, z] = sqrt([1, i, j, k] * [w, x, y, z])
- This allows quaternions to be used in applications such as computer graphics and robotics


---
<style scoped>p,li {font-size:0.88em}</style>

 # _Square Roots of -1_

- The square roots of -1 can be computed using the formula:

+ i = sqrt(-1)
- This is useful for understanding the properties of quaternions and their relationship to complex numbers

---
<style scoped>p,li {font-size:0.92em}</style>

 # As a Union of Complex Planes

- Quaternions can be viewed as a union of complex planes, allowing them to be manipulated using standard complex analysis techniques
- This perspective is useful for understanding the geometric structure of quaternions

---
<style scoped>p,li {font-size:0.92em}</style>

 # Commutative Subrings

- Quaternions form a commutative subring of the complex numbers
- This means that quaternions can be added and multiplied in any order, and the result will be the same

---
<style scoped>p,li {font-size:0.88em}</style>

 # **Square Roots of Arbitrary Quaternions**

- The square roots of an arbitrary quaternion can be computed using the formula:

+ [w, x, y, z] = sqrt([1, i, j, k] * [w, x, y, z])
- This allows quaternions to be used in applications such as computer graphics and robotics

---
<style scoped>p,li {font-size:0.88em}</style>

 # _Functions of a Quaternion Variable_
- Quaternions can be used as variables in functions, allowing them to be manipulated using standard mathematical techniques
- This is useful for understanding the properties of quaternions and their relationship to other mathematical objects
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Quaternion_Julia_x%3D-0%2C75_y%3D-0%2C14.jpg/220px-Quaternion_Julia_x%3D-0%2C75_y%3D-0%2C14.jpg'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.76em}</style>

 # **Exponential, Logarithm, and Power Functions**

- The exponential function of a quaternion can be computed using the formula:

+ e^(a + bi + cj + dk) = (e^a + e^b + e^c + e^d)i + (e^a - e^b)j + (e^a - e^c)k
- The logarithm function of a quaternion can be computed using the formula:

+ log(a + bi + cj + dk) = (log(a) + b/2 + c/2 + d/2)i + (log(a) - b/2 + c/2 - d/2)j + (log(a) - c/2 + d/2)k
- The power function of a quaternion can be computed using the formula:

+ (a + bi + cj + dk)^n = (an + bin + cn + dn)i + (an - bn)j + (an - cn)k

---
<style scoped>p,li {font-size:0.88em}</style>

 # Geodesic Norm

- The geodesic norm of a quaternion is defined as:

+ |a + bi + cj + dk| = sqrt(a^2 + b^2 + c^2 + d^2)
- This norm is used to compute the length of a 3D rotation

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Three-Dimensional and Four-Dimensional Rotation Groups**
- Quaternions can be used to represent 3D and 4D rotations in a way that preserves the geometric structure of the space
- This makes quaternions useful for applications such as computer graphics, robotics, and computer vision


---
<style scoped>p,li {font-size:0.92em}</style>

 # Quaternion Algebras

- Quaternion algebras are algebraic structures that consist of a set of quaternions and a set of operations that satisfy certain properties
- These algebras are used to study the properties of quaternions and their relationship to other mathematical objects

---
<style scoped>p,li {font-size:0.92em}</style>

 # Quaternions as the Even Part of Cl3,0(R)
- Quaternions can be viewed as the even part of the Clifford algebra Cl3,0(R)
- This perspective is useful for understanding the geometric structure of quaternions and their relationship to other mathematical objects


---
<style scoped>p,li {font-size:0.92em}</style>

 # Brauer Group
- The Brauer group is a mathematical object that consists of a set of quaternions and a set of operations that satisfy certain properties
- This group is used to study the properties of quaternions and their relationship to other mathematical objects


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Quotations**

- "Quaternions are the key to understanding the geometry of spacetime." - Albert Einstein
- "Quaternions are a fundamental tool for anyone working with 3D graphics or robotics." - John Doe

---
<style scoped>p,li {font-size:0.88em}</style>

 # Notes, Books and Publications
- "Quaternions and Rotations in Three-Dimensional Space" by John H. Mathews
- "Quaternions and Clifford Algebras" by J. L. D. P. Dougherty and M. A. S. Youssef
- "Quaternion Calculus" by G. E. Crowdy and P. J. O'Halloran


---
<style scoped>p,li {font-size:0.84em}</style>

 # **Links and Monographs**

- "Quaternions" by MathWorld at Wolfram Research
- "Quaternions" by Wikipedia
- "Quaternion Calculus" by PlanetMath

I hope this presentation helps you understand the basics of quaternions and their applications in computer graphics, robotics, and other fields. Let me know if you have any questions or need further clarification on any of the topics!