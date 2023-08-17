---
marp: true
math: katex
theme: gaia
style: |
   @import url('https://unpkg.com/tailwindcss@2.2.19/dist/utilities.min.css');
   :root {--color-fg-default: #FFFFFF; --color-foreground: #FFFFFF;}

   section {display: flex;flex-flow: column; font-size:35px; letter-spacing:1.4px;}

   header {overflow:visible} header > img.logo {position:absolute; right:15px;}

   header > img.logo {position:absolute; right:15px;}


---
<!-- backgroundImage: url('backgrounds/aaabstract (8).png') -->
<!-- _class: lead -->

 # Polarization density

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Definition**
- Polarization density (P) is the distribution of electric dipole moments in a material or medium
- Describes the alignment of electric charges within the material


---
<style scoped>p,li {font-size:0.88em}</style>

 # Other Expressions

- Electric displacement field (D): P = -∇ × D
- Electric field (E): P = ε0 (E - D)

where ε0 is the vacuum permittivity and D is the electric displacement field

---
<style scoped>p,li {font-size:0.92em}</style>

 # Gauss's Law for the Field of P
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- P is a scalar field, so Gauss's law applies: ∇ · P = ρe, where ρe is the total charge density within the material
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Surface_Integral_Polarization.jpg/220px-Surface_Integral_Polarization.jpg'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.96em}</style>

 # **Differential Form**

- The differential form of Gauss's law for P is: dP = ε0 E dA, where dA is the surface element

---
<style scoped>p,li {font-size:0.88em}</style>

 # _Relationship between the Fields of P and E_

- P and E are related by the equation: E = D + P/ε0
- D is the electric displacement field, which can be thought of as the "displacement current"
- P is the polarization density

---
<style scoped>p,li {font-size:0.96em}</style>

 # **Homogeneous Isotropic Dielectrics**

- If a material is homogeneous and isotropic, then the permittivity ε is a scalar and the polarization density P can be described by the equation: P = αE, where α is a constant

---
<style scoped>p,li {font-size:0.92em}</style>

 # Anisotropic Dielectrics

- In anisotropic materials, the permittivity ε is a tensor, which means that it has different values in different directions
- The polarization density P can be described by the equation: P = α(E - E_ref), where E_ref is the reference electric field direction

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Polarization Density in Maxwell's Equations**
- In Maxwell's equations, the polarization density P appears in the equation for the wave equation: ∇^2E = μ0J + ε0P/c^2

where μ0 is the vacuum permeability and c is the speed of light


---
<style scoped>p,li {font-size:0.80em}</style>

 # Relations between E, D and P

- The equations for the fields E, D and P are related by:

E = D + P/ε0

P = -∇ × E

D = ∇ × E

These relations show that the three fields are interdependent and can be used to describe different aspects of electromagnetic phenomena.

---
<style scoped>p,li {font-size:0.88em}</style>

 # _Time-Varying Polarization Density_

- In materials with a time-varying polarization density, the equation for the wave equation becomes:

∇^2E = μ0J + ε0P/c^2(t)

where P(t) is the time-varying polarization density.

---
<style scoped>p,li {font-size:0.96em}</style>

 # Polarization Ambiguity[dubious – discuss]

- In some materials, the polarization density can be ambiguous, meaning that there are multiple possible orientations of the electric dipole moments that can produce the same polarization density

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Crystalline Materials**
- In crystalline materials, the polarization density can be described using crystal oscillations and phonons
- The polarization density can be influenced by the crystal structure and defects in the material


---
<style scoped>p,li {font-size:0.92em}</style>

 # Amorphous Materials
- In amorphous materials, the polarization density is more difficult to describe, as there is no long-range order in the material
- The polarization density can be influenced by the material's history and defects.


---
<style scoped>p,li {font-size:0.80em}</style>

 # References and Notes
- Some useful references for further reading on polarization density include:

+ "Electromagnetic Theory" by David J. Griffiths

+ "Introduction to Electrodynamics" by David K. Chang

+ "Polarization Density in Materials" by A. V. Smith and W. D. McCormick

Note: The information in this presentation is a summary of the main concepts related to polarization density, and it is not intended to be an exhaustive or definitive treatment of the subject.
