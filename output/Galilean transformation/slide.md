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

 # Galilean transformation

---
<style scoped>p,li {font-size:0.96em}</style>

 # Title Slide
- Subtitle: A Mathematical Framework for Describing Motions in Classical Mechanics


---
<style scoped>p,li {font-size:0.88em}</style>

 # Translation
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Standard_conf.png/300px-Standard_conf.png'/>
</div>
</div>

- Definition: A translation is a geometric transformation that moves an object from one position to another.
- Notation: T(x,y) = (x+a, y+b), where a and b are constants representing the displacement of the object.

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Galilean Transformations**
- Definition: A Galilean transformation is a composite of a translation and a rotation around a fixed axis.
- Notation: T(x,y)R(θ) = (x+a, y+b, z+c), where θ is the angle of rotation and a, b, and c are constants representing the displacement and orientation of the object.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Galilean Group
- Definition: The Galilean group is the set of all possible Galilean transformations, under composition.
- Notation: G = {T(x,y)R(θ) | a, b, c, and θ are constants}.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Origin in Group Contraction
- Definition: The origin of a group contraction is the identity element of the group, which represents the absence of any transformation.
- Notation: e = (0,0,0), where e is the identity element of G.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Central Extension of the Galilean Group

- Definition: The central extension of the Galilean group is a larger group that includes the original Galilean group and additional elements representing the centripetal force experienced by an object under circular motion.
- Notation: G' = {T(x,y)R(θ) | a, b, c, and θ are constants} ∪ {(0,0,r) | r > 0}, where (0,0,r) represents the central extension element.

---
<style scoped>p,li {font-size:0.84em}</style>

 # **Notes**
- The Galilean group is a fundamental concept in classical mechanics, providing a mathematical framework for describing motions and transformations.
- The origin of the group contraction is the identity element of the group, representing the absence of any transformation.
- The central extension of the Galilean group includes additional elements representing the centripetal force experienced by an object under circular motion.

I hope this slide presentation helps to provide a helpful overview of Galilean transformation! Let me know if you have any questions or if there is anything else I can help with.
