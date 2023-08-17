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

 # Fresnel equations

---
<style scoped>p,li {font-size:0.92em}</style>

 # Overview
- Fresnel equations describe the behavior of light at interfaces between media with different refractive indices
- Important in optics and photonics, including imaging, spectroscopy, and optical communications


---
<style scoped>p,li {font-size:0.88em}</style>

 # S and P Polarizations
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Plane_of_incidence.svg/425px-Plane_of_incidence.svg.png'/>
</div>
</div>

- Light can be polarized in two main ways: S (circular) and P (linear)
- S polarization has a constant electric field orientation, while P polarization has a linear electric field orientation that varies with time

---
<style scoped>p,li {font-size:0.80em}</style>

 # Power (Intensity) Reflection and Transmission Coefficients
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Fresnel1.svg/300px-Fresnel1.svg.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Fresnel_power_air-to-glass.svg/220px-Fresnel_power_air-to-glass.svg.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Fresnel_power_glass-to-air.svg/220px-Fresnel_power_glass-to-air.svg.png'/>
</div>
</div>

- Power reflection and transmission coefficients describe the amount of light that is reflected or transmitted at an interface
- The coefficients are related to the refractive indices of the two media and the angle of incidence

---
<style scoped>p,li {font-size:0.92em}</style>

 # Special Cases

- Brewster's angle: the angle at which the reflection and transmission coefficients are equal
- Total internal reflection: light is completely reflected at an interface when it hits a medium with a higher refractive index at an angle greater than the critical angle

---
<style scoped>p,li {font-size:0.96em}</style>

 # Normal Incidence
- At normal incidence (i.e., the light is perpendicular to the interface), the reflection and transmission coefficients reduce to simple fractions of the refractive indices of the two media


---
<style scoped>p,li {font-size:0.92em}</style>

 # Brewster's Angle

- Brewster's angle is the angle at which the reflected and transmitted waves are equal in intensity
- The angle can be calculated using the Fresnel equations and is related to the refractive indices of the two media

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Total Internal Reflection_

- Total internal reflection occurs when light hits a medium with a higher refractive index at an angle greater than the critical angle
- The reflected wave is completely internal to the second medium

---
<style scoped>p,li {font-size:0.88em}</style>

 # Complex Amplitude Reflection and Transmission Coefficients
- The Fresnel equations can be written in terms of complex amplitude reflection and transmission coefficients, which provide a more complete description of the light's behavior at the interface
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Fresnel_amplitudes_air-to-glass.svg/220px-Fresnel_amplitudes_air-to-glass.svg.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Fresnel_amplitudes_glass-to-air.svg/220px-Fresnel_amplitudes_glass-to-air.svg.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Alternative Forms
- The Fresnel equations can also be expressed in alternative forms, such as the Lorentz-Lippmann equation and the Abraham-Lorentz equation
- These alternative forms are useful for certain applications and can provide a more straightforward analysis of the light's behavior


---
<style scoped>p,li {font-size:0.92em}</style>

 # Multiple Surfaces

- The Fresnel equations can be applied to situations involving multiple surfaces, such as in multi-layer optical coatings or waveguides
- The equations can be modified to account for the presence of multiple interfaces and the associated reflections and transmissions

---
<style scoped>p,li {font-size:0.92em}</style>

 # _History_
- The Fresnel equations were developed by Augustin-Jean Fresnel in the early 19th century as part of his work on wave optics
- The equations have since been widely used in a variety of fields, including optics, photonics, and electromagnetism


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Derivation**

- The Fresnel equations can be derived using the principles of electromagnetic theory and the laws of physics that govern light's behavior
- The derivation involves a combination of mathematical techniques and physical reasoning

---
<style scoped>p,li {font-size:0.92em}</style>

 # Material Parameters
- The Fresnel equations involve several material parameters, including the refractive indices of the two media and the angle of incidence
- These parameters are important for understanding the light's behavior at the interface and can be measured or calculated using various techniques


---
<style scoped>p,li {font-size:0.92em}</style>

 # Electromagnetic Plane Waves

- The Fresnel equations are based on the idea of electromagnetic plane waves, which describe the propagation of light through a medium
- The waves have both electric and magnetic components and are described by a complex amplitude that varies with space and time

---
<style scoped>p,li {font-size:0.88em}</style>

 # The Wave Vectors
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Wave_vectors_n1_to_n2.svg/305px-Wave_vectors_n1_to_n2.svg.png'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- The wave vectors of the Fresnel equations describe the direction and magnitude of the light's propagation
- The vectors can be visualized as arrows pointing in the direction of the light's propagation
</div>

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # **The S Components**

- The S components of the Fresnel equations describe the polarization state of the light at the interface
- The components are related to the electric field orientation and can be used to analyze the light's behavior in different polarization states

---
<style scoped>p,li {font-size:0.92em}</style>

 # The P Components
- The P components of the Fresnel equations describe the polarization state of the light at the interface
- The components are related to the magnetic field orientation and can be used to analyze the light's behavior in different polarization states


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Power Ratios (Reflectivity and Transmissivity)_
- The power ratios of the Fresnel equations describe the relative amounts of light that are reflected and transmitted at an interface
- The ratios can be expressed as reflectivity (the ratio of reflected power to incident power) and transmissivity (the ratio of transmitted power to incident power)


---
<style scoped>p,li {font-size:0.92em}</style>

 # Equal Refractive Indices

- When the refractive indices of the two media are equal, the Fresnel equations reduce to simple fractions that describe the reflection and transmission coefficients
- This is known as the Brewster's angle condition and can be used to determine the angle at which the reflected and transmitted waves are equal in intensity

---
<style scoped>p,li {font-size:0.92em}</style>

 # Non-Magnetic Media
- The Fresnel equations assume that the media involved are non-magnetic, meaning that they do not have a magnetic permeability that varies with frequency
- This assumption is reasonable for most optics applications, but can be relaxed in certain situations where magnetic effects become important


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Equal Permittivities_

- When the permittivities of the two media are equal, the Fresnel equations reduce to simple fractions that describe the reflection and transmission coefficients
- This is known as the Brewster's angle condition and can be used to determine the angle at which the reflected and transmitted waves are equal in intensity

---
<style scoped>p,li {font-size:0.92em}</style>

 # Notes

- The Fresnel equations can be applied to a wide range of optics problems, including thin lens design, beam propagation, and optical imaging
- The equations are based on the principles of electromagnetic theory and have been widely used in a variety of fields

---
<style scoped>p,li {font-size:0.92em}</style>

 # Sources
- Several sources are available for learning more about the Fresnel equations and their applications
- These include textbooks, research articles, and online resources such as the Optical Society of America and the IEEE Photonics Society
