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
<!-- backgroundImage: url('backgrounds/wwwatercolor (1).png') -->
<!-- _class: lead -->

 # **Metric tensor**

---
<style scoped>p,li {font-size:0.92em}</style>

 # Introduction

- The metric tensor is a fundamental concept in differential geometry and plays a central role in the study of curved spaces
- It encodes information about the distances and angles between points in a manifold, and is used to define various geometric quantities such as length, area, and volume

---
<style scoped>p,li {font-size:0.92em}</style>

 # Arc Length
- The arc length of a curve on a manifold is the length of the shortest path between two points on the curve
- The arc length can be computed using the metric tensor, and is an important quantity in the study of geodesics and curvature


---
<style scoped>p,li {font-size:0.92em}</style>

 # Coordinate Transformations

- Coordinate transformations are changes of basis in a manifold that preserve the metric tensor
- Under coordinate transformations, the arclength of a curve remains unchanged, which means that the metric tensor is invariant under these transformations

---
<style scoped>p,li {font-size:0.92em}</style>

 # Invariance of Arclength under Coordinate Transformations
- The invariance of arclength under coordinate transformations is a fundamental property of the metric tensor
- This invariance allows us to define geometric quantities such as length and angle in a way that is independent of the choice of coordinates


---
<style scoped>p,li {font-size:0.92em}</style>

 # Length and Angle

- The length of a curve on a manifold can be computed using the metric tensor, and is given by the integral of the magnitude of the tangent vector to the curve
- The angle between two curves on a manifold can also be computed using the metric tensor, and is given by the angle between the tangent vectors to the curves

---
<style scoped>p,li {font-size:0.96em}</style>

 # Area
- The area of a surface in a manifold can be computed using the metric tensor, and is given by the integral of the dot product of the normal vector to the surface and the outward-pointing tangent vector to the surface


---
<style scoped>p,li {font-size:0.92em}</style>

 # Definition
- The metric tensor is defined as a symmetric rank-2 tensor field on a manifold that encodes information about the distances and angles between points in the manifold
- The metric tensor is denoted by g, and its components are typically written as g_ij, where i and j range over the set of indices for the manifold


---
<style scoped>p,li {font-size:0.92em}</style>

 # Components of the Metric

- The components of the metric tensor can be organized into a matrix that represents the geometry of the manifold
- The matrix elements of the metric tensor are related to the distances and angles between points in the manifold, and can be used to define various geometric quantities such as length, area, and volume

---
<style scoped>p,li {font-size:0.92em}</style>

 # Metric in Coordinates
- The metric tensor can also be expressed in a coordinate basis, which allows us to compute geometric quantities such as length and angle in terms of the coordinates
- The components of the metric tensor in a coordinate basis are given by g_ij = g_ij^a \partial_a \otimes \partial_i, where a ranges over the set of indices for the manifold and \partial_a are the partial derivatives with respect to the coordinates


---
<style scoped>p,li {font-size:0.92em}</style>

 # Signature of a Metric
- The signature of a metric tensor is the number of negative, zero, and positive eigenvalues of the matrix representation of the metric tensor
- The signature of a metric tensor can be used to classify the geometry of the manifold, and is related to the number of dimensions and the type of curvature present in the manifold


---
<style scoped>p,li {font-size:0.92em}</style>

 # Inverse Metric
- The inverse of the metric tensor is denoted by g^i_j, and is defined as the transpose of the matrix representation of the metric tensor
- The inverse of the metric tensor can be used to compute the distance between points in the manifold, and is related to the geometry of the manifold


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Raising and Lowering Indices_

- The raising and lowering of indices in the metric tensor is a fundamental operation in differential geometry that allows us to convert between different coordinate systems and define geometric quantities such as length and angle
- The rules for raising and lowering indices are given by the formula g_ik^j = g_i^k \delta_k^j, where \delta_k^j is the Kronecker delta symbol

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Induced Metric_
- The induced metric on a submanifold of a manifold is the restriction of the metric tensor to the submanifold
- The induced metric can be used to define geometric quantities such as length and angle on the submanifold, and is related to the geometry of the parent manifold


---
<style scoped>p,li {font-size:0.92em}</style>

 # Intrinsic Definitions of a Metric
- There are several intrinsic definitions of a metric that are independent of the choice of coordinates
- These definitions include the length of a curve, the angle between two curves, and the volume of a region in the manifold


---
<style scoped>p,li {font-size:0.92em}</style>

 # Metric as a Section of a Bundle
- The metric tensor can be viewed as a section of a vector bundle over the manifold, which allows us to study the geometry of the manifold in terms of the properties of the bundle
- The bundle is typically denoted by TM, where M is the manifold, and the sections of the bundle are denoted by s: M -> TM


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Metric in a Vector Bundle_

- The metric tensor can also be viewed as a section of a vector bundle over the manifold, which allows us to study the geometry of the manifold in terms of the properties of the bundle
- The bundle is typically denoted by TM, where M is the manifold, and the sections of the bundle are denoted by s: M -> TM

---
<style scoped>p,li {font-size:0.92em}</style>

 # Tangent–Cotangent Isomorphism

- The tangent–cotangent isomorphism is a fundamental operation in differential geometry that allows us to relate the tangent and cotangent spaces at a point in the manifold
- The tangent–cotangent isomorphism is given by the formula T_pM -> T_p \Circle T_p', where T_pM is the tangent space at a point p in the manifold, and T_p' is the cotangent space at p

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Arclength and the Line Element_

- The arclength of a curve on a manifold can be computed using the metric tensor, and is given by the integral of the magnitude of the tangent vector to the curve
- The line element of a manifold is a measure of the distance between two points in the manifold, and is given by the formula ds^2 = g_ij dx^i dx^j, where x^i are the coordinates on the manifold

---
<style scoped>p,li {font-size:0.88em}</style>

 # Energy, Variational Principles, and Geodesics

- The energy of a curve on a manifold can be computed using the metric tensor, and is given by the formula E = \int ds \sqrt{g_ij dx^i dx^j}
- Variational principles in differential geometry are used to study the properties of manifolds, and are related to the energy of curves on the manifold
- Geodesics on a manifold are curves that extremize the length of a curve, and can be studied using variational principles and the metric tensor

---
<style scoped>p,li {font-size:0.92em}</style>

 # Canonical Measure and Volume Form
- The canonical measure on a manifold is a measure that is induced by the metric tensor, and is used to define geometric quantities such as volume and area
- The volume form of a manifold is a differential form that represents the volume of a region in the manifold, and is given by the formula vol_M = \sqrt{|g|} dx^1 \wedge ... \wedge dx^n, where g is the determinant of the metric tensor and n is the number of dimensions of the manifold


---
<style scoped>p,li {font-size:0.88em}</style>

 # Examples
- Euclidean metric on Euclidean space
- Round metric on a sphere
- Lorentzian metrics from relativity


---
<style scoped>p,li {font-size:0.88em}</style>

 # Notes

- The metric tensor is a fundamental concept in differential geometry that encodes information about the distances and angles between points in a manifold
- The metric tensor can be used to define various geometric quantities such as length, area, and volume, and is related to the geometry of the manifold
- There are several intrinsic definitions of a metric that are independent of the choice of coordinates, and include the length of a curve, the angle between two curves, and the volume of a region in the manifold.