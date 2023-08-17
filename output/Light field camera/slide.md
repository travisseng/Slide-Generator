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

 # **Light field camera**

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Introduction_

- Light field cameras are a type of imaging technology that captures not just the intensity of light, but also its direction and angle of incidence
- This allows for the creation of high-quality, 3D images and depth maps

---
<style scoped>p,li {font-size:0.88em}</style>

 # _History_
- The concept of light fields was first proposed by Harold Edgerton in the 1950s
- However, it wasn't until the 1990s that the technology began to be developed further
- In 2008, the first light field camera was released by Lytro


---
<style scoped>p,li {font-size:0.88em}</style>

 # **Early Research**

- Early research in light field cameras focused on developing algorithms for processing and rendering light fields
- This included work by computer vision researchers such as Michael J. Black and Jitendra Malik
- The development of efficient algorithms for light field processing has been a major focus of the field ever since

---
<style scoped>p,li {font-size:0.84em}</style>

 # Standard Plenoptic Camera
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Lytro_Illum_light_field_camera_demonstration.jpg/220px-Lytro_Illum_light_field_camera_demonstration.jpg'/>
</div>
</div>

- A standard plenoptic camera is one that captures a light field by recording the intensity of light at each point in space
- This is typically done using an array of small lenses or pinholes, which capture the light from different angles
- The resulting light field can be used to create 3D images and depth maps

---
<style scoped>p,li {font-size:0.88em}</style>

 # _Focused Plenoptic Camera_
- A focused plenoptic camera is a type of light field camera that uses a single lens or pinhole to capture the light field
- This allows for higher resolution and better depth accuracy than standard plenoptic cameras
- However, it also requires more complex processing to reconstruct the light field


---
<style scoped>p,li {font-size:0.88em}</style>

 # Coded Aperture Camera
- A coded aperture camera is a type of light field camera that uses a coded aperture to record the light field
- The coded aperture is a pattern of small openings or shutters that are used to modulate the light field
- This allows for high-speed capture of light fields and can be used in applications such as 3D scanning and augmented reality


---
<style scoped>p,li {font-size:0.84em}</style>

 # **Features**

- High-quality, 3D images and depth maps
- Ability to capture and manipulate light fields in real-time
- Compact and portable design
- Advanced algorithms for processing and rendering light fields

---
<style scoped>p,li {font-size:0.88em}</style>

 # Metalens Array
- A metalens array is a type of light field camera that uses an array of metalenses to capture the light field
- Metalenses are flat, lens-like structures that can be used to manipulate light
- The resulting light field can be used to create high-quality 3D images and depth maps


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Manufacturers_

- There are several companies that manufacture light field cameras, including Lytro, Microsoft, and Raytrix
- These companies offer a range of products, from consumer-grade light field cameras to high-end professional models

---
<style scoped>p,li {font-size:0.88em}</style>

 # Products

- Lytro offers the ILM 3.0, a high-end light field camera aimed at professional photographers and videographers
- Microsoft offers the Azure Kinect, a depth sensor that uses light field technology to create high-quality depth maps
- Raytrix offers the Vecto, a light field camera designed for industrial and scientific applications

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Prototypes_

- There are several prototype light field cameras that have been developed but not yet released to market
- These include the Light Field Camera by Google and the Leia Inc. Lume Pad

---
<style scoped>p,li {font-size:0.76em}</style>

 # Applications

- Light field cameras have a wide range of applications, including:

+ 3D imaging and depth mapping

+ Virtual reality and augmented reality

+ 3D scanning and reconstruction

+ Microscopy and scientific imaging

+ Machine vision and robotics

---
<style scoped>p,li {font-size:0.80em}</style>

 # Software

- There are several software packages available for processing and rendering light fields, including:

+ OpenLightField

+ LightField Studio

+ PyLFT

+ Lytro Desktop

---
<style scoped>p,li {font-size:0.88em}</style>

 # **Conclusion**

- Light field cameras offer a powerful tool for capturing and manipulating 3D images and depth maps
- The technology has a wide range of applications, from consumer-grade photography to industrial and scientific imaging
- As the field continues to evolve, we can expect to see new and innovative uses for light field cameras in the future.