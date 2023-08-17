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
<!-- backgroundImage: url('backgrounds/wwwatercolor (5).png') -->
<!-- _class: lead -->

 # **Vector field**

---
<style scoped>p,li {font-size:0.92em}</style>

 # Definition

- A vector field is a mathematical object that assigns a vector to each point in a manifold
- The vectors are typically denoted by the symbol "F" and are defined at each point in the manifold

---
<style scoped>p,li {font-size:0.92em}</style>

 # Vector fields on subsets of Euclidean space
- Vector fields can be defined on any subset of Euclidean space, including open sets, closed sets, and domains with non-trivial boundary
- The domain of a vector field is the set of all points where the vector field is defined


---
<style scoped>p,li {font-size:0.88em}</style>

 # _Coordinate transformation law_
- The coordinate transformation law states that if two charts are used to cover the same domain, then the vector fields transform according to the following formula:

F' = J(x',y') \* F \* J(x',y')^-1

where F is the vector field in one chart, F' is the transformed vector field in the other chart, and J is the Jacobian matrix of the transformation.


---
<style scoped>p,li {font-size:0.88em}</style>

 # _Vector fields on manifolds_
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Vector fields can be defined on any manifold, including smooth manifolds and topological manifolds
- The definition of a vector field on a manifold is similar to the definition on Euclidean space, but the vectors are defined at each point in the manifold rather than at each point in Euclidean space.
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Vector_sphere.svg/200px-Vector_sphere.svg.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.84em}</style>

 # _Examples_
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Gradient field in Euclidean spaces: The gradient of a function is a vector field that points in the direction of steepest ascent.
- Central field in Euclidean spaces: The central field of a function is a vector field that points towards the center of the function.
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Cessna_182_model-wingtip-vortex.jpg/250px-Cessna_182_model-wingtip-vortex.jpg'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Bezier_curves_composition_ray-traced_in_3D.png/220px-Bezier_curves_composition_ray-traced_in_3D.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Operations on vector fields_

- Addition: Two vector fields can be added pointwise by adding their components at each point in the domain.
- Scalar multiplication: A vector field can be multiplied by a scalar, which changes the magnitude of the vectors but not their direction.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Line integral

- The line integral of a vector field is the sum of the dot products of the vectors and the segments of the path.
- The line integral can be used to compute the total flux of a vector field across a closed curve.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Divergence
- The divergence of a vector field is the net flow of the field out of a surface.
- The divergence can be used to determine if a vector field is converging or diverging at a point.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Curl in three dimensions
- The curl of a vector field is a measure of how much the field is twisting and turning at each point.
- The curl can be visualized as the rotation of the field around a point.


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Index of a vector field**
- The index of a vector field is a measure of how many independent components the field has at each point.
- The index can be used to determine if a vector field is conservative or not.


---
<style scoped>p,li {font-size:0.88em}</style>

 # Physical intuition
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Vector fields can be used to model physical phenomena such as fluid flow, electromagnetic fields, and gravitational fields.
- The properties of a vector field, such as its divergence and curl, can be used to infer physical properties of the system being modeled.
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Magnet0873.png/220px-Magnet0873.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Flow curves

- A flow curve is a curve in the domain of a vector field that represents the direction of the flow at each point.
- The flow curve can be used to visualize the direction of the flow and to compute the integral of the flow over a closed curve.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Complete vector fields

- A complete vector field is a vector field that is defined on all of Euclidean space or on a manifold.
- The completeness of a vector field can be used to determine if it is possible to integrate the field over all of Euclidean space or a manifold.

---
<style scoped>p,li {font-size:0.92em}</style>

 # f-relatedness
- Two vector fields are related if one can be obtained from the other by a coordinate transformation.
- The f-relatedness of two vector fields can be used to determine if they are physically equivalent or not.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Generalizations

- Vector fields can be generalized to higher-dimensional spaces and to more exotic manifolds such as Riemannian manifolds and symplectic manifolds.
- The properties of vector fields in these settings can be used to model physical phenomena in a more general setting.

---
<style scoped>p,li {font-size:0.96em}</style>

 # Bibliography

- List of references for further reading on vector fields, including textbooks, research articles, and online resources.