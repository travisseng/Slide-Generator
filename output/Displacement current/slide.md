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
<!-- backgroundColor: #87808a -->
<!-- _class: lead -->

 # **Displacement current**

---
<style scoped>p,li {font-size:0.92em}</style>

 # Explanation

- Displacement current is a phenomenon where an electric current flows through a dielectric material (such as a capacitor) even when there is no direct connection to the material.
- This current is caused by the changing electric field in the material, which creates a "displacement" of charge within the material.

---
<style scoped>p,li {font-size:0.84em}</style>

 # **Isotropic Dielectric Case**

- In an isotropic dielectric material, the permittivity (ε) is the same in all directions.
- The displacement current density (D) can be expressed as:

D = ε0(E + p)

where E is the electric field strength, p is the polarization density, and ε0 is the vacuum permittivity.

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Necessity**
- The existence of displacement current is necessary to explain the behavior of capacitors and other dielectric devices.
- Without displacement current, the electric field within a capacitor would be constant, and there would be no charge storage or discharge.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Generalizing Ampère's Circuital Law
- Ampère's circuital law states that the line integral of the magnetic field around a closed loop is proportional to the current flowing through the loop.
- Displacement current generalizes this law to include dielectric materials, where the electric field is not necessarily conservative (i.e., it can change even when there is no net current flowing).


---
<style scoped>p,li {font-size:0.76em}</style>

 # Current in Capacitors
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Current_continuity_in_capacitor.svg/200px-Current_continuity_in_capacitor.svg.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Displacement_current_in_capacitor.svg/200px-Displacement_current_in_capacitor.svg.png'/>
</div>
</div>

- In a capacitor, the displacement current flows through the dielectric material and creates an electric field that stores energy.
- The current density in the dielectric material can be expressed as:

J = D/2ε0

where J is the current density, D is the displacement current density, and ε0 is the vacuum permittivity.

---
<style scoped>p,li {font-size:0.88em}</style>

 # Mathematical Formulation
- The mathematical formulation of displacement current can be expressed as:

∇ x E = ∂D/∂t

where ∇ x E is the cross product of the electric field and the gradient of the displacement current density, and ∂D/∂t is the material derivative of the displacement current density with respect to time.


---
<style scoped>p,li {font-size:0.84em}</style>

 # **Wave Propagation**
- Displacement current can be described as a wave that propagates through the dielectric material at a speed determined by the material properties.
- The wave equation for displacement current can be expressed as:

∇²D = (1/c^2) ∂²D/∂t²

where c is the speed of light and ∇² is the Laplacian operator.


---
<style scoped>p,li {font-size:0.92em}</style>

 # _History and Interpretation_
- The concept of displacement current was first proposed by Maxwell in the 19th century as part of his theory of electromagnetic waves.
- It has since been widely adopted and is an important concept in the study of dielectric materials and capacitors.


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Maxwell's Papers_
- Maxwell's papers on displacement current and electromagnetic theory have had a profound impact on the development of modern physics and engineering.
- His work laid the foundation for many later developments, including the invention of radio and the understanding of the nature of light.


---
<style scoped>p,li {font-size:0.88em}</style>

 # Conclusion

- Displacement current is an important concept in the study of dielectric materials and capacitors.
- It has a wide range of applications, from electronic devices to optical communication systems.
- The mathematical formulation of displacement current provides a powerful tool for understanding the behavior of these materials and systems.