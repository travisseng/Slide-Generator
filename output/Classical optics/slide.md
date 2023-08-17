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
<!-- backgroundImage: url('backgrounds/hhholographic.png') -->
<!-- _class: lead -->

 # Classical optics

---
<style scoped>p,li {font-size:0.96em}</style>

 # Introduction
- Subtitle: Geometrical and Physical Optics


---
<style scoped>p,li {font-size:0.72em}</style>

 # History
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Subtitle: From ancient times to modern days
- Content: Overview of the history of optics, from ancient civilizations to modern developments.
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Nimrud_lens_British_Museum.jpg/220px-Nimrud_lens_British_Museum.jpg'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Ibn_Sahl_manuscript.jpg/170px-Ibn_Sahl_manuscript.jpg'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Kepler_-_Ad_Vitellionem_paralipomena_quibus_astronomiae_pars_optica_traditur%2C_1604_-_158093_F.jpg/220px-Kepler_-_Ad_Vitellionem_paralipomena_quibus_astronomiae_pars_optica_traditur%2C_1604_-_158093_F.jpg'/>
</div>
</div>
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Opticks.jpg/170px-Opticks.jpg'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Table_of_Opticks%2C_Cyclopaedia%2C_Volume_2.jpg/170px-Table_of_Opticks%2C_Cyclopaedia%2C_Volume_2.jpg'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Classical Optics
- Subtitle: Rays and Mirrors
- Content: Explanation of the principles of geometrical optics, including reflections and refractions.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Approximations

- Subtitle: Simple approximations for complex phenomena
- Content: Introduction to ray tracing and its applications in classical optics.

---
<style scoped>p,li {font-size:0.88em}</style>

 # Reflections
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Reflection_angles.svg/170px-Reflection_angles.svg.png'/>
</div>
</div>

- Subtitle: Mirrors, refraction, and the laws of reflection
- Content: Explanation of the laws of reflection, including Snell's law and the mirror equation.

---
<style scoped>p,li {font-size:0.88em}</style>

 # **Refractions**
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Snells_law.svg/300px-Snells_law.svg.png'/>
</div>
</div>

- Subtitle: Bending light with surfaces
- Content: Explanation of the principles of refraction, including total internal reflection and critical angle.

---
<style scoped>p,li {font-size:0.80em}</style>

 # Lenses
- Subtitle: Thin lenses and lens combinations
- Content: Overview of lenses in classical optics, including thin lenses, converging lenses, and diverging lenses.
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
<style scoped>p,li {font-size:0.92em}</style>

 # **Physical Optics**
- Subtitle: The study of light and its properties
- Content: Explanation of physical optics as a branch of classical optics that deals with the study of light and its properties, including polarization and dispersion.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Modelling and Design of Optical Systems
- Subtitle: Using physical optics to design systems
- Content: Overview of the process of modelling and designing optical systems using physical optics, including the use of geometric optics and physical principles.


---
<style scoped>p,li {font-size:0.88em}</style>

 # Superposition and Interference
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Subtitle: The properties of light waves
- Content: Explanation of the principles of superposition and interference in classical optics, including the concept of constructive and destructive interference.
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Dieselrainbow.jpg/300px-Dieselrainbow.jpg'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # Diffraction and Optical Resolution
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Double_slit_diffraction.svg/300px-Double_slit_diffraction.svg.png'/>
</div>
</div>

- Subtitle: The limits of classical optics
- Content: Explanation of the principles of diffraction and its impact on optical resolution, including the Rayleigh criterion and the diffraction limit.

---
<style scoped>p,li {font-size:0.84em}</style>

 # _Dispersion and Scattering_
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Subtitle: The effects of light interaction with matter
- Content: Explanation of the principles of dispersion and scattering in classical optics, including the concept of refractive index and the effects of light scattering on optical systems.
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Light_dispersion_conceptual_waves.gif/220px-Light_dispersion_conceptual_waves.gif'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/b/bd/Wave_group.gif'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Polarization_
- Subtitle: The orientation of light waves
- Content: Explanation of the principles of polarization in classical optics, including the concept of polarization states and the effects of polarization on optical systems.


---
<style scoped>p,li {font-size:0.88em}</style>

 # **Changing Polarization**
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Subtitle: The manipulation of light waves
- Content: Overview of the methods for changing the polarization state of light, including the use of polarizing filters and waveplates.
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Malus_law.svg/350px-Malus_law.svg.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # Natural Light
- Subtitle: The study of light in nature
- Content: Explanation of the principles of natural light, including the properties of daylight and the effects of atmospheric refraction on light propagation.
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/CircularPolarizer.jpg/400px-CircularPolarizer.jpg'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Modern Optics
- Subtitle: The evolution of optics beyond classical limits
- Content: Overview of modern optics, including the development of lasers, fiber optics, and other advanced optical technologies.


---
<style scoped>p,li {font-size:0.84em}</style>

 # Lasers
- Subtitle: The ultimate source of coherent light
- Content: Explanation of the principles of lasers, including the concept of stimulated emission and the properties of laser light.
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Military_laser_experiment.jpg/220px-Military_laser_experiment.jpg'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/The_VLT%E2%80%99s_Artificial_Star.jpg/220px-The_VLT%E2%80%99s_Artificial_Star.jpg'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Kapitsa–Dirac Effect**
- Subtitle: The phenomenon of quantum coherence in classical optics
- Content: Explanation of the Kapitsa–Dirac effect, including its properties and applications in modern optics.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Applications

- Subtitle: From telescopes to microscopes
- Content: Overview of the diverse range of applications of classical optics, including astronomy, biology, and materials science.

---
<style scoped>p,li {font-size:0.88em}</style>

 # Human Eye
- Subtitle: The most complex optical system in nature
- Content: Explanation of the structure and function of the human eye, including the cornea, lens, retina, and visual processing.
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Eye-diagram_no_circles_border.svg/300px-Eye-diagram_no_circles_border.svg.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # Visual Effects
- Subtitle: The art of manipulating light and perception
- Content: Overview of the principles of visual effects in classical optics, including the use of mirrors, lenses, and other optical elements to create illusions and manipulate perception.
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Ponzo_illusion.gif/220px-Ponzo_illusion.gif'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # Optical Instruments
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Table_of_Opticks%2C_Cyclopaedia%2C_Volume_2.jpg/300px-Table_of_Opticks%2C_Cyclopaedia%2C_Volume_2.jpg'/>
</div>
</div>

- Subtitle: The tools of classical optics
- Content: Overview of the diverse range of optical instruments used in classical optics, including telescopes, microscopes, and other optical devices.

---
<style scoped>p,li {font-size:0.84em}</style>

 # Photography
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Jonquil_flowers_at_f32.jpg/300px-Jonquil_flowers_at_f32.jpg'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Jonquil_flowers_at_f5.jpg/300px-Jonquil_flowers_at_f5.jpg'/>
</div>
</div>

- Subtitle: The capture of light and time
- Content: Explanation of the principles of photography, including the use of lenses, aperture, and shutter speed to capture images.

---
<style scoped>p,li {font-size:0.88em}</style>

 # Atmospheric Optics
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Firesunset2edit.jpg/300px-Firesunset2edit.jpg'/>
</div>
</div>

- Subtitle: The study of light in the atmosphere
- Content: Explanation of the principles of atmospheric optics, including the effects of atmospheric refraction and scattering on light propagation.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Conclusion
- Subtitle: Summary and future directions
- Content: Summary of the key points covered in the presentation, along with some thoughts on the future directions of classical optics research.
