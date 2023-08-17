---
marp: true
math: katex
theme: uncover
style: |
   @import url('https://unpkg.com/tailwindcss@2.2.19/dist/utilities.min.css');
   section {display: flex;flex-flow: column; font-size:35px; letter-spacing:1.4px;}

   header {overflow:visible} header > img.logo {position:absolute; right:15px;}

   header > img.logo {position:absolute; right:15px;}


---
<!-- backgroundImage: url('backgrounds/aaabstract (13).png') -->
<!-- _class: lead -->

 # Sinusoidal plane-wave solutions of the electromagnetic wave equation

---
<style scoped>p,li {font-size:0.88em}</style>

 # Explanation

- Electromagnetic waves are waves that propagate through the electromagnetic field and can transmit energy through space
- The electromagnetic wave equation describes how these waves behave
- Sinusoidal plane-wave solutions of this equation are important for understanding the properties of electromagnetic waves

---
<style scoped>p,li {font-size:0.84em}</style>

 # Plane Waves
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- A plane wave is a wave that propagates in a single direction, with no oscillations perpendicular to that direction
- In the context of electromagnetic waves, plane waves are waves that propagate in a single direction through space
- Sinusoidal plane-wave solutions of the electromagnetic wave equation describe how these waves behave
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Light-wave.svg/350px-Light-wave.svg.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # **Polarization State Vector**
- The polarization state vector is a mathematical object that describes the orientation of the electric and magnetic fields of an electromagnetic wave
- The polarization state vector can be represented as a complex quantity, with real and imaginary components corresponding to the electric and magnetic fields, respectively
- The polarization state vector is a useful tool for understanding the properties of electromagnetic waves


---
<style scoped>p,li {font-size:0.88em}</style>

 # Jones Vector
- The Jones vector is a mathematical object that describes the polarization state of an electromagnetic wave in a way that is independent of the reference frame in which it is observed
- The Jones vector is defined as the ratio of the electric and magnetic fields of the wave, and can be represented as a complex quantity
- The Jones vector is a useful tool for understanding the properties of electromagnetic waves


---
<style scoped>p,li {font-size:0.88em}</style>

 # Dual Jones Vector
- The dual Jones vector is a mathematical object that is related to the Jones vector, but is defined in a different way
- The dual Jones vector is defined as the ratio of the magnetic and electric fields of the wave, and can be represented as a complex quantity
- The dual Jones vector is a useful tool for understanding the properties of electromagnetic waves


---
<style scoped>p,li {font-size:0.84em}</style>

 # Normalization of the Jones Vector
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/2/2e/Linear_polarization_schematic.png'/>
</div>
</div>

- The Jones vector must be normalized to ensure that it has a finite magnitude and does not grow without bound as the wave propagates
- Normalization can be achieved by dividing the Jones vector by its magnitude, which is equal to the square root of the sum of the squares of the real and imaginary components of the vector
- The normalized Jones vector is a useful tool for understanding the properties of electromagnetic waves

---
<style scoped>p,li {font-size:0.80em}</style>

 # **Polarization States**
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Electromagnetic waves can have a variety of polarization states, including linear, elliptical, and circular polarization
- Linear polarization is a special case in which the electric field oscillates in a single direction, while the magnetic field is zero
- Elliptical and circular polarization are more general cases in which the electric field oscillates in a plane that is not fixed, and the magnetic field is non-zero
- The polarization state of an electromagnetic wave can be described using the Jones vector
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/6/6a/Elliptical_polarization_schematic.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # Linear Polarization
- Linear polarization is a special case in which the electric field oscillates in a single direction, while the magnetic field is zero
- Linearly polarized waves have a constant orientation of the electric field, and are described by a single complex number
- The Jones vector for a linearly polarized wave is simply a complex number representing the magnitude and phase of the electric field


---
<style scoped>p,li {font-size:0.88em}</style>

 # Elliptical Polarization
- Elliptical polarization is a more general case in which the electric field oscillates in a plane that is not fixed, and the magnetic field is non-zero
- The polarization state of an elliptically polarized wave can be described using the Jones vector, which is a complex quantity with real and imaginary components corresponding to the electric and magnetic fields, respectively
- The magnitude of the Jones vector for an elliptically polarized wave is equal to the square root of the sum of the squares of the real and imaginary components of the vector


---
<style scoped>p,li {font-size:0.88em}</style>

 # Circular Polarization
- Circular polarization is a special case in which the electric field oscillates in a circular motion, while the magnetic field is zero
- The polarization state of a circularly polarized wave can be described using the Jones vector, which is a complex quantity with real and imaginary components corresponding to the electric and magnetic fields, respectively
- The magnitude of the Jones vector for a circularly polarized wave is equal to the square root of the sum of the squares of the real and imaginary components of the vector


---
<style scoped>p,li {font-size:0.88em}</style>

 # **Conclusion**
- Sinusoidal plane-wave solutions of the electromagnetic wave equation are important for understanding the properties of electromagnetic waves
- The polarization state vector, Jones vector, and dual Jones vector are useful tools for describing the properties of electromagnetic waves
- Understanding the properties of electromagnetic waves is essential for a wide range of applications in physics, engineering, and other fields.
