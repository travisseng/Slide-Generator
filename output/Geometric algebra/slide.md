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
<!-- backgroundImage: url('backgrounds/aaabstract (1).png') -->
<!-- _class: lead -->

 # **Geometric algebra**

---
<style scoped>p,li {font-size:0.88em}</style>

 # Definition and Notation
- Geometric Algebra (GA) is a mathematical framework that combines vectors, scalars, and multivectors in a single algebraic structure.
- GA is also known as Clifford Algebra or Geometric Calculus.
- In GA, vectors and multivectors are represented by geometric objects such as points, lines, planes, and volumes.


---
<style scoped>p,li {font-size:0.84em}</style>

 # The Geometric Product
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/GA_parallel_and_perpendicular_vectors.svg/200px-GA_parallel_and_perpendicular_vectors.svg.png'/>
</div>
</div>

- The geometric product of two vectors is defined as the volume of the parallelepiped formed by the two vectors.
- The geometric product of a vector and a multivector is defined as the sum of the products of the component vectors and multivectors.
- The geometric product has the following properties: commutative, associative, and distributive over addition.

---
<style scoped>p,li {font-size:0.88em}</style>

 # _Blades, Grades, and Canonical Basis_

- A blade is a one-dimensional subspace of GA, spanned by a single vector.
- A grade is a two-dimensional subspace of GA, spanned by two vectors.
- The canonical basis is a set of basis vectors that span the entire space of GA.

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Grade Projection_

- Grade projection is the process of projecting a multivector onto a lower-grade subspace.
- Grade projection can be used to extract the component vectors of a multivector.

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Representation of Subspaces**
- Any subspace of GA can be represented as the span of a set of basis vectors.
- The choice of basis vectors is not unique and can be changed without affecting the properties of the subspace.


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Unit Pseudoscalars_
- A unit pseudoscalar is a scalar that satisfies the equation |ψ| = 1, where |ψ| is the magnitude of ψ.
- Unit pseudoscalars are used to represent the orientation of objects in GA.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Extensions of the Inner and Exterior Products
- The inner product can be extended to higher-grade subspaces by using the grade projection operator.
- The exterior product can be extended to higher-grade subspaces by using the wedge product.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Dual Basis
- A dual basis is a set of basis vectors that are dual to each other, meaning that the inner product of any two basis vectors is zero.
- The dual basis is used to represent the dual space of GA.


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Linear Functions**

- A linear function is a function that preserves the operations of vector addition and scalar multiplication.
- Linear functions can be represented as multivectors in GA.

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Modeling Geometries_

- GA can be used to model a wide range of geometric objects and systems, including points, lines, planes, volumes, and more.
- GA provides a unified framework for representing and manipulating these objects and systems.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Vector Space Model
- The vector space model is a way of representing GA as a vector space over the reals or other fields.
- This model is useful for many applications, such as computer graphics and machine learning.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Spacetime Model
- The spacetime model is a way of representing GA as a geometric object that includes both space and time.
- This model is useful for applications in physics and engineering.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Homogeneous Model
- The homogeneous model is a way of representing GA as a set of homogeneous coordinates.
- This model is useful for applications in computer vision and image processing.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Conformal Model
- The conformal model is a way of representing GA as a set of conformal coordinates.
- This model is useful for applications in differential geometry and mathematical physics.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Models for Projective Transformation

- Projective transformation is a way of transforming geometric objects using a set of basis vectors that span the entire space of GA.
- There are several models for projective transformation, including the vector space model, the spacetime model, and the homogeneous model.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Geometric Interpretation

- The geometric interpretation of GA is based on the idea that geometric objects can be represented as multivectors in a high-dimensional space.
- This allows for the manipulation of geometric objects using geometric algebra operations, such as the geometric product and the exterior product.

---
<style scoped>p,li {font-size:0.88em}</style>

 # **Projection and Rejection**
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/GA_plane_subspace_and_projection.svg/300px-GA_plane_subspace_and_projection.svg.png'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Projection is the process of extracting a lower-grade subspace from a higher-grade subspace.
- Rejection is the process of discarding a lower-grade subspace from a higher-grade subspace.
</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # Reflection
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/GA_reflection_along_vector.svg/200px-GA_reflection_along_vector.svg.png'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Reflection is the process of reflecting a geometric object about a hyperplane.
- Reflection can be performed using the grade projection operator and the wedge product.
</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # Rotations
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/GA_planar_rotations.svg/200px-GA_planar_rotations.svg.png'/>
</div>
</div>

- Rotation is the process of rotating a geometric object about an axis.
- Rotation can be performed using the grade projection operator and the wedge product.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Versor

- A versor is a multivector that represents a direction in GA.
- Versors are used to represent the orientation of objects in GA.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Subgroups of Γ
- The group of grade-preserving transformations, denoted by Γ, has several subgroups, including the special orthogonal group, the unitary group, and the symplectic group.
- These subgroups have important applications in computer vision, image processing, and other fields.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Examples and Applications
- GA has many examples and applications, including computer graphics, machine learning, robotics, and more.
- GA provides a powerful framework for representing and manipulating geometric objects and systems.


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Hypervolume of a Parallelotope Spanned by Vectors**

- The hypervolume of a parallelotope spanned by vectors is the volume of the parallelepiped formed by the vectors.
- This quantity can be used to represent the size and shape of geometric objects in GA.

---
<style scoped>p,li {font-size:0.88em}</style>

 # Intersection of a Line and a Plane
- The intersection of a line and a plane is a point or a line, depending on the orientation of the line and the plane.
- This quantity can be used to represent the intersection of geometric objects in GA.
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/LinePlaneIntersect.png/220px-LinePlaneIntersect.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # Rotating Systems
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Exterior_calc_cross_product.svg/220px-Exterior_calc_cross_product.svg.png'/>
</div>
</div>

- A rotating system is a set of objects that rotate about a fixed axis.
- The rotation of these objects can be represented using the grade projection operator and the wedge product.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Geometric Calculus

- Geometric calculus is a way of performing calculations on geometric objects using GA.
- This includes operations such as addition, multiplication, and differentiation.

---
<style scoped>p,li {font-size:0.92em}</style>

 # History
- The history of GA can be traced back to the work of William Kingdon Clifford in the late 19th century.
- Since then, GA has been developed and applied in a wide range of fields, including computer graphics, machine learning, and physics.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Notes, Citations, References, and Further Reading

- There are many resources available for learning more about GA, including books, research articles, and online tutorials.
- Some recommended references include the works of William Kingdon Clifford, the book "Geometric Algebra with Applications in Computer Science" by David H. Delany, and the website of the Geometric Algebra Group at the University of California, Los Angeles.