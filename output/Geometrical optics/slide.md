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

 # _Geometrical optics_

---
<style scoped>p,li {font-size:0.88em}</style>

 # Explanation
- Geometrical optics is a branch of physics that studies the behavior of light as it interacts with objects in the world
- It deals with the geometry of light rays and their interactions with media of different refractive indices
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Plane_wave_wavefronts_3D.svg/220px-Plane_wave_wavefronts_3D.svg.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # **Reflection**
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Reflection is the change in direction of a light ray when it hits a surface and bounces back
- The angle of incidence equals the angle of reflection (Law of Reflection)
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Reflection_angles.svg/170px-Reflection_angles.svg.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.72em}</style>

 # _Refraction_
- Refraction is the bending of light as it passes from one medium to another with a different refractive index
- Snell's Law describes how the angle of incidence and the refractive indices of the two media determine the angle of refraction
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Snells_law.svg/300px-Snells_law.svg.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Lens3b.svg/360px-Lens3b.svg.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/2015-05-25_0820Incoming_parallel_rays_are_focused_by_a_convex_lens_into_an_inverted_real_image_one_focal_length_from_the_lens%2C_on_the_far_side_of_the.png/220px-2015-05-25_0820Incoming_parallel_rays_are_focused_by_a_convex_lens_into_an_inverted_real_image_one_focal_length_from_the_lens%2C_on_the_far_side_of_the.png'/>
</div>
</div>
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/2015-05-25_0836With_concave_lenses%2C_incoming_parallel_rays_diverge_after_going_through_the_lens%2C_in_such_a_way_that_they_seem_to_have_originated_at_an.png/220px-2015-05-25_0836With_concave_lenses%2C_incoming_parallel_rays_diverge_after_going_through_the_lens%2C_in_such_a_way_that_they_seem_to_have_originated_at_an.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Virtualimageframerate1.gif/220px-Virtualimageframerate1.gif'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Underlying Mathematics

- Geometrical optics is based on differential geometry, which studies the properties of curves and surfaces in space
- The mathematical tools used in geometrical optics include the concept of a parallel transport and the metric tensor

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Sommerfeld-Runge Method**

- The Sommerfeld-Runge method is a technique for solving problems in geometrical optics using partial differential equations
- It involves separating the variables and solving for the unknown functions using the method of separation of variables

---
<style scoped>p,li {font-size:0.92em}</style>

 # Luneburg Method
- The Luneburg method is another technique for solving problems in geometrical optics using partial differential equations
- It involves reducing the problem to a set of simpler problems using the method of characteristics


---
<style scoped>p,li {font-size:0.88em}</style>

 # General Equation Using Four-Vector Notation
- The general equation for the behavior of light rays can be written in four-vector notation as:

$$\frac{dP^\mu}{ds} = \Gamma^\mu_{\nu\lambda}P^\nu P^\lambda$$

where $P^\mu$ is the four-vector that describes the position and momentum of the light ray, and $\Gamma^\mu_{\nu\lambda}$ is the Christoffel symbol that describes the curvature of spacetime.


---
<style scoped>p,li {font-size:0.80em}</style>

 # English Translations of Some Early Books and Papers
- Some early books and papers on geometrical optics include:

+ "Opticks" by Isaac Newton (1704)

+ "Treatise on the Refraction of Light" by Willebrord Snellius (1695)

+ "Traité de la réfraction de la lumière" by Etienne Louis Malus (1812)

I hope this slide presentation is helpful! Let me know if you have any questions or need further clarification.
