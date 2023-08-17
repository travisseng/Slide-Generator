---
marp: true
math: katex
theme: gaia
paginate: True
style: |
   @import url('https://unpkg.com/tailwindcss@2.2.19/dist/utilities.min.css');
   :root {--color-fg-default: #FFFFFF; --color-foreground: #FFFFFF;}

   section {display: flex;flex-flow: column; font-size:35px; letter-spacing:1.4px;}

   header {overflow:visible} header > img.logo {position:absolute; right:15px;}

   header > img.logo {position:absolute; right:15px;}


---
<!-- backgroundImage: url('backgrounds/aaabstract.png') -->
<!-- _class: lead -->

 # **Optics**

---
<style scoped>p,li {font-size:0.88em}</style>

 # **Introduction to Optics**

- Definition of optics
- Brief history of optics
- Importance of optics in modern technology

---
<style scoped>p,li {font-size:0.88em}</style>

 # History of Optics

- Early civilizations and their contributions to optics (e.g. Egyptians, Greeks)
- Key figures in the development of optics (e.g. Euclid, Newton)
- Major milestones in the history of optics (e.g. invention of the telescope, discovery of diffraction)

---
<style scoped>p,li {font-size:0.88em}</style>

 # Classical Optics
- Geometrical optics: refraction, reflection, and diffraction
- Wave-particle duality and the nature of light
- Mirrors, lenses, and their properties


---
<style scoped>p,li {font-size:0.84em}</style>

 # Geometrical Optics
- Reflection and refraction at plane and spherical surfaces
- Image formation and focal length
- Lens combinations and relay systems
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Reflection_and_refraction.svg/250px-Reflection_and_refraction.svg.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # Approximations in Optics
- Ray optics and its limitations
- Wave-front propagation and diffraction
- Mathematical models for optical systems


---
<style scoped>p,li {font-size:0.84em}</style>

 # Reflections
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Reflection_angles.svg/170px-Reflection_angles.svg.png'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Specular reflection and its applications
- Diffuse reflection and its properties
- Total internal reflection and its uses
</div>

</div>


---
<style scoped>p,li {font-size:0.84em}</style>

 # Refractions
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Refraction through plane and spherical surfaces
- Dispersion and prism effects
- Angle of incidence and refraction
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Snells_law.svg/300px-Snells_law.svg.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.76em}</style>

 # Lenses
- Types of lenses (e.g. convex, concave, plano-convex)
- Lens combinations and their applications
- Aberrations and their correction
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Lens3b.svg/360px-Lens3b.svg.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Lens1.svg/360px-Lens1.svg.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Thin_lens_images.svg/500px-Thin_lens_images.svg.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # Physical Optics

- Electromagnetic theory of light
- Interaction of light with matter
- Polarization and its effects

---
<style scoped>p,li {font-size:0.88em}</style>

 # Modelling and Design of Optical Systems

- Geometrical and physical optics methods
- Optimization techniques for optical systems
- Examples of complex optical systems and their design

---
<style scoped>p,li {font-size:0.84em}</style>

 # Superposition and Interference
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Principle of superposition
- Interference of light waves
- Applications of interference (e.g. holography, interferometry)
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Dieselrainbow.jpg/300px-Dieselrainbow.jpg'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.84em}</style>

 # Diffraction and Optical Resolution
- Diffraction and its applications
- Optical resolution and its limits
- Quantum optics and the Kapitsa-Dirac effect
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Double_slit_diffraction.svg/300px-Double_slit_diffraction.svg.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.80em}</style>

 # Dispersion and Scattering
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Light_dispersion_conceptual_waves.gif/220px-Light_dispersion_conceptual_waves.gif'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/b/bd/Wave_group.gif'/>
</div>
</div>

- Dispersion and its causes
- Scattering of light by particles and objects
- Applications of dispersion and scattering (e.g. spectroscopy, laser technology)

---
<style scoped>p,li {font-size:0.88em}</style>

 # Polarization

- Definition and properties of polarization
- Polarization states and their transformations
- Applications of polarization (e.g. LCD displays, polarizing filters)

---
<style scoped>p,li {font-size:0.88em}</style>

 # Changing Polarization
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Malus_law.svg/350px-Malus_law.svg.png'/>
</div>
</div>

- Mechanisms for changing polarization (e.g. birefringence, optically active media)
- Applications of changing polarization (e.g. polarization-sensitive devices, optical communication systems)

---
<style scoped>p,li {font-size:0.88em}</style>

 # Natural Light
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/CircularPolarizer.jpg/400px-CircularPolarizer.jpg'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Properties and applications of natural light
- Optical phenomena in nature (e.g. rainbows, halos)
</div>

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Modern Optics

- Advances in optics technology (e.g. laser technology, optical fibers)
- Applications of modern optics (e.g. telecommunications, biomedical imaging)

---
<style scoped>p,li {font-size:0.80em}</style>

 # Lasers
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Military_laser_experiment.jpg/220px-Military_laser_experiment.jpg'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/The_VLT%E2%80%99s_Artificial_Star.jpg/220px-The_VLT%E2%80%99s_Artificial_Star.jpg'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Principle and operation of lasers
- Types of lasers and their applications
- Laser safety and hazards
</div>

</div>


---
<style scoped>p,li {font-size:0.84em}</style>

 # Human Eye
- Structure and function of the human eye
- Visual perception and its limitations
- Applications of knowledge of the human eye (e.g. corrective lenses, visual prosthetics)
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Eye-diagram_no_circles_border.svg/300px-Eye-diagram_no_circles_border.svg.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # _Visual Effects_
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Ponzo_illusion.gif/220px-Ponzo_illusion.gif'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Optical phenomena and their applications in film and photography
- Techniques for creating visual effects (e.g. depth of field, motion blur)
</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # Optical Instruments
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Table_of_Opticks%2C_Cyclopaedia%2C_Volume_2.jpg/300px-Table_of_Opticks%2C_Cyclopaedia%2C_Volume_2.jpg'/>
</div>
</div>

- Types of optical instruments (e.g. telescopes, microscopes)
- Applications of optical instruments in science and technology

---
<style scoped>p,li {font-size:0.84em}</style>

 # _Photography_
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Principles of photography (e.g. exposure, aperture)
- Optical techniques for creating images (e.g. bokeh, diffraction)
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Jonquil_flowers_at_f32.jpg/300px-Jonquil_flowers_at_f32.jpg'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Jonquil_flowers_at_f5.jpg/300px-Jonquil_flowers_at_f5.jpg'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # Atmospheric Optics
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Firesunset2edit.jpg/300px-Firesunset2edit.jpg'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Optical phenomena in the atmosphere (e.g. mirages, sun dogs)
- Applications of atmospheric optics (e.g. weather forecasting, aerial photography)
</div>

</div>


---
<style scoped>p,li {font-size:0.84em}</style>

 # Conclusion
- Summary of key points and takeaways
- Future directions and challenges in optics research
- Closing remarks and final thoughts

I hope this helps! Let me know if you have any questions or need further assistance.
