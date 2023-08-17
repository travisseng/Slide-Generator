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

 # Vector (geometric)

---
<style scoped>p,li {font-size:0.88em}</style>

 # **History**

- Vector mathematics has its roots in ancient Greece, particularly in the works of Euclid and Archimedes
- Modern development of vector calculus can be traced back to the 17th and 18th centuries, with contributions from mathematicians such as Newton, Leibniz, and Euler
- In the 20th century, vector mathematics became an essential tool for physics, engineering, and computer science

---
<style scoped>p,li {font-size:0.84em}</style>

 # Overview

- Vectors are mathematical objects used to represent quantities with both magnitude and direction
- Vectors can be added, subtracted, and scaled by numbers (scalars)
- Vectors can be represented graphically as arrows in a two-dimensional or three-dimensional space
- Vectors are used to describe physical phenomena such as displacement, velocity, acceleration, force, energy, and work

---
<style scoped>p,li {font-size:0.84em}</style>

 # Further Information
- Vectors are defined in terms of their magnitude (length) and direction, which can be represented by an arrow pointing in a specific direction
- Vectors can be added by adding their magnitudes and maintaining their directions, or by using the parallelogram law
- Vectors can be subtracted by subtracting their magnitudes and reversing their directions, or by using the parallelogram law
- Scalar multiplication of vectors is defined as the product of a scalar (a number) and a vector, resulting in a new vector with a scaled magnitude and the same direction


---
<style scoped>p,li {font-size:0.88em}</style>

 # Examples in One Dimension
- Displacement vector: describes the distance an object moves in one dimension
- Velocity vector: describes the rate of change of displacement in one dimension
- Acceleration vector: describes the rate of change of velocity in one dimension


---
<style scoped>p,li {font-size:0.88em}</style>

 # **In Physics and Engineering**

- Vectors are used to describe motion, forces, energy, and work in physics and engineering
- Displacement, velocity, acceleration, force, energy, and work can all be represented as vectors
- Vectors are essential for understanding and solving problems in mechanics, electromagnetism, and other areas of physics and engineering

---
<style scoped>p,li {font-size:0.88em}</style>

 # _In Cartesian Space_

- Vectors in Cartesian space can be represented by arrows pointing in the x, y, or z directions
- Vectors can be added and subtracted using the parallelogram law
- Scalar multiplication of vectors is defined as the product of a scalar and a vector, resulting in a new vector with a scaled magnitude and the same direction

---
<style scoped>p,li {font-size:0.92em}</style>

 # Euclidean and Affine Vectors
- Euclidean vectors are vectors in Euclidean space that can be represented by their coordinates (x, y, z)
- Affine vectors are vectors in affine space that can be represented by their coordinates (x, y, z) and a scalar multiple of the vector (e.g., 2x, 3y, 4z)


---
<style scoped>p,li {font-size:0.92em}</style>

 # Generalizations
- Vectors can be generalized to higher dimensions and to more abstract spaces, such as vector spaces and tensor spaces
- Vectors can also be generalized to other mathematical structures, such as pseudovectors and bivectors


---
<style scoped>p,li {font-size:0.84em}</style>

 # Representations
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Vectors can be represented graphically as arrows in a two-dimensional or three-dimensional space
- Vectors can also be represented symbolically using notation such as boldface letters (e.g., \mathbf{a}, \mathbf{b}, \mathbf{c})
- Vectors can be represented numerically using values for their components (e.g., x, y, z)
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Position_vector.svg/220px-Position_vector.svg.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Decomposition or Resolution
- Vectors can be decomposed into their component parts using techniques such as the dot product and the cross product
- Vectors can also be resolved into their component parts using techniques such as the resolvent matrix


---
<style scoped>p,li {font-size:0.84em}</style>

 # _Basic Properties_
- Equality: two vectors are equal if they have the same magnitude and direction
- Opposite: the opposite of a vector is a vector with the same magnitude but with the opposite direction
- Parallel: two vectors are parallel if they have the same direction but different magnitudes
- Antiparallel: the antiparallel of a vector is a vector with the same magnitude but with the opposite direction


---
<style scoped>p,li {font-size:0.92em}</style>

 # Addition and Subtraction
- Vectors can be added by adding their magnitudes and maintaining their directions, or by using the parallelogram law
- Vectors can be subtracted by subtracting their magnitudes and reversing their directions, or by using the parallelogram law


---
<style scoped>p,li {font-size:0.88em}</style>

 # Scalar Multiplication
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Scalar_multiplication_by_r%3D3.svg/250px-Scalar_multiplication_by_r%3D3.svg.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Scalar_multiplication_of_vectors2.svg/250px-Scalar_multiplication_of_vectors2.svg.png'/>
</div>
</div>

- Scalar multiplication of vectors is defined as the product of a scalar (a number) and a vector, resulting in a new vector with a scaled magnitude and the same direction

---
<style scoped>p,li {font-size:0.92em}</style>

 # Length
- The length of a vector is its magnitude, or the size of the vector
- The length of a vector can be calculated using the magnitude formula (e.g., |a| = sqrt(x^2 + y^2 + z^2))


---
<style scoped>p,li {font-size:0.88em}</style>

 # _Unit Vector_
- A unit vector is a vector with a magnitude of one, often used as a reference direction for other vectors
- Unit vectors can be represented graphically as arrows pointing in specific directions, or symbolically using notation such as \hat{x}, \hat{y}, or \hat{z}
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Vector_normalization.svg/220px-Vector_normalization.svg.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Zero Vector

- A zero vector is a vector with a magnitude of zero, often used as a reference direction for other vectors
- Zero vectors can be represented graphically as arrows pointing in any direction, or symbolically using notation such as \mathbf{0}

---
<style scoped>p,li {font-size:0.92em}</style>

 # Dot Product

- The dot product of two vectors is the product of their magnitudes and the cosine of the angle between them
- The dot product can be used to calculate the magnitude of the resultant vector, or to determine if two vectors are perpendicular or parallel

---
<style scoped>p,li {font-size:0.88em}</style>

 # Cross Product
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- The cross product of two vectors is the product of their magnitudes and the sine of the angle between them
- The cross product can be used to calculate the magnitude of the resultant vector, or to determine if two vectors are perpendicular or parallel
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Cross_product_vector.svg/220px-Cross_product_vector.svg.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Scalar Triple Product

- The scalar triple product of three vectors is the product of their magnitudes and the cosine of the angle between each pair of vectors
- The scalar triple product can be used to calculate the magnitude of the resultant vector, or to determine if three vectors are perpendicular or parallel

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Conversion between Multiple Cartesian Bases**
- Vectors can be converted between different cartesian bases using techniques such as rotation and translation
- The resulting vectors will have the same magnitude but a different direction


---
<style scoped>p,li {font-size:0.92em}</style>

 # Other Dimensions

- Vectors can be defined in higher dimensions, such as four-dimensional space or n-dimensional space
- Vectors in higher dimensions can be used to describe phenomena such as motion in four-dimensional space or the behavior of particles in n-dimensional space

---
<style scoped>p,li {font-size:0.92em}</style>

 # Physics

- Vectors are essential for understanding and solving problems in physics, particularly in mechanics, electromagnetism, and other areas of physics
- Vectors can be used to describe motion, forces, energy, and work in physics

---
<style scoped>p,li {font-size:0.88em}</style>

 # Length and Units
- The length of a vector is its magnitude, or the size of the vector
- The length of a vector can be calculated using the magnitude formula (e.g., |a| = sqrt(x^2 + y^2 + z^2))
- Vectors can have units such as meters, kilograms, and seconds, which are used to describe physical phenomena in physics


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Vector-Valued Functions_
- A vector-valued function is a function that produces a vector as its output, often used to describe motion or forces in physics
- Vector-valued functions can be represented graphically as arrows in a two-dimensional or three-dimensional space, or symbolically using notation such as f(x,y,z)


---
<style scoped>p,li {font-size:0.88em}</style>

 # Position, Velocity, and Acceleration
- Position is the location of an object in space, often described by a vector
- Velocity is the rate of change of position, often described by a vector
- Acceleration is the rate of change of velocity, often described by a vector


---
<style scoped>p,li {font-size:0.88em}</style>

 # Force, Energy, and Work
- Force is a vector that describes the push or pull on an object, often used to describe the interaction between objects in physics
- Energy is a scalar that describes the ability of a system to do work, often used to describe the motion of objects in physics
- Work is the product of force and displacement, often used to describe the energy transfer between objects in physics


---
<style scoped>p,li {font-size:0.88em}</style>

 # Notes
- Vectors can be used to describe physical phenomena such as motion, forces, energy, and work in physics and engineering
- Vectors are essential for understanding and solving problems in mechanics, electromagnetism, and other areas of physics and engineering
- Vectors can be represented graphically, symbolically, or numerically using values for their components


---
<style scoped>p,li {font-size:0.92em}</style>

 # Mathematical Treatments
- Vectors can be treated mathematically using techniques such as the dot product, cross product, and scalar multiplication
- Vectors can be manipulated and transformed using these mathematical techniques to solve problems in physics and engineering


---
<style scoped>p,li {font-size:0.92em}</style>

 # Physical Treatments

- Vectors are used to describe physical phenomena such as motion, forces, energy, and work in physics and engineering
- Understanding the physical significance of vectors is essential for solving problems in mechanics, electromagnetism, and other areas of physics and engineering

---
<style scoped>p,li {font-size:0.80em}</style>

 # References

- Euclid's "Elements"
- Newton's "Principia Mathematica"
- Leibniz's "Monadology"
- Euler's "Calculus"
- Other relevant texts and resources for further study