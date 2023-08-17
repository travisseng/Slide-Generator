---
marp: true
math: katex
theme: default
paginate: True
style: |
   @import url('https://unpkg.com/tailwindcss@2.2.19/dist/utilities.min.css');
   section {display: flex;flex-flow: column; font-size:35px; letter-spacing:1.4px;}

   header {overflow:visible} header > img.logo {position:absolute; right:15px;}

   header > img.logo {position:absolute; right:15px;}


---
<!-- backgroundImage: url('backgrounds/wwwatercolor (8).png') -->
<!-- _class: lead -->

 # Boundary (topology)

---
<style scoped>p,li {font-size:0.64em}</style>

 # Title Slide
- Common definitions
- Properties
- Examples
- Characterizations and general examples
- Concrete examples
- Boundary of an open ball vs. its surrounding sphere
- Boundary of a boundary
- Notes
- Citations


---
<style scoped>p,li {font-size:0.88em}</style>

 # Common Definitions

- A boundary is a set of points that separate one region from another
- In topology, boundaries are defined based on the connectedness of spaces
- Boundaries can be thought of as the "edges" of a space

---
<style scoped>p,li {font-size:0.88em}</style>

 # _Properties_
- A boundary is a closed set (i.e., it contains all its limit points)
- The boundary of a space is always a subset of that space
- The boundary of a space is unique up to isomorphism


---
<style scoped>p,li {font-size:0.88em}</style>

 # Examples

- The boundary of a disk is a circle
- The boundary of a sphere is a sphere (i.e., the sphere's boundary is itself)
- The boundary of a torus is a donut-shaped set

---
<style scoped>p,li {font-size:0.88em}</style>

 # Characterizations and General Examples

- A space can be characterized by its boundary, e.g., a space with a non-empty boundary is not compact
- The boundary of a space can be used to determine the connectedness of that space
- Boundaries are important in topology because they describe the "edges" of a space and can be used to classify spaces

---
<style scoped>p,li {font-size:0.84em}</style>

 # _Concrete Examples_
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- The boundary of an open ball is a circle
- The boundary of a closed ball is a sphere (i.e., the ball's boundary is itself)
- The boundary of a cube is a rectangle
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Mandelbrot_Components.svg/220px-Mandelbrot_Components.svg.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Boundary of an Open Ball vs. its Surrounding Sphere**

- The boundary of an open ball is a circle, while the boundary of its surrounding sphere is the entire sphere
- This illustrates the difference between a boundary and a "full" boundary

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Boundary of a Boundary**

- The boundary of a boundary is a set of points that separate one region from another (i.e., it is another boundary)
- This concept can be used to recursively define boundaries within boundaries

---
<style scoped>p,li {font-size:0.88em}</style>

 # Notes

- Boundaries are an important concept in topology and are used to describe the "edges" of a space
- The boundary of a space can be used to determine the connectedness of that space
- Boundaries are unique up to isomorphism, meaning that two spaces with the same boundary are not necessarily isomorphic

---
<style scoped>p,li {font-size:0.84em}</style>

 # **Citations**
- "Topology" by James R. Munkres (2nd edition)
- "Introduction to Topology" by John McCleary (2nd edition)
- "A First Course in Topology: Continuity and Dimension" by John L. Kelley

I hope this slide presentation is helpful! Let me know if you have any questions or need further clarification on any of the topics.
