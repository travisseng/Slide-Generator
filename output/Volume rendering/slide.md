---
marp: true
math: katex
theme: gaia
style: |
   @import url('https://unpkg.com/tailwindcss@2.2.19/dist/utilities.min.css');
   section {display: flex;flex-flow: column; font-size:35px; letter-spacing:1.4px;}

   header {overflow:visible} header > img.logo {position:absolute; right:15px;}

   header > img.logo {position:absolute; right:15px;}


---
<!-- backgroundImage: url('backgrounds/aaabstract (1).png') -->
<!-- _class: lead -->

 # Volume rendering

---
<style scoped>p,li {font-size:0.84em}</style>

 # **Scope**
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/CT_presentation_as_thin_slice%2C_projection_and_volume_rendering.jpg/220px-CT_presentation_as_thin_slice%2C_projection_and_volume_rendering.jpg'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Volume rendering is a technique used to visualize and explore 3D datasets
- Applications include scientific visualization, medical imaging, and video games
- Goal is to create an interactive and immersive experience for the user
</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # Direct Volume Rendering

- Direct volume rendering is a technique that renders the volume as is, without any pre-processing or simplification
- Advantages include accurate representation of the data and fast computation
- Challenges include high computational cost and potential for visual artifacts

---
<style scoped>p,li {font-size:0.84em}</style>

 # Volume Ray Casting
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Croc.5.3.10.a_gb1.jpg/300px-Croc.5.3.10.a_gb1.jpg'/>
</div>
</div>

- Volume ray casting is a technique that renders the volume by casting rays through the voxels and coloring them based on their properties
- Advantages include fast computation and simple implementation
- Challenges include potential for artifacts and limited interaction with the data

---
<style scoped>p,li {font-size:0.88em}</style>

 # Splatting

- Splatting is a technique that pre-computes and stores rendered images of the volume at different levels of detail
- Advantages include fast interaction and smooth animation
- Challenges include increased memory usage and potential for artifacts

---
<style scoped>p,li {font-size:0.84em}</style>

 # Shear Warp
- Shear warp is a technique that distorts the rendering of the volume to create a more intuitive viewing experience
- Advantages include improved visualization of complex data and reduced eye strain
- Challenges include potential for artifacts and limited control over the distortion
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/VolRenderShearWarp.gif/250px-VolRenderShearWarp.gif'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.84em}</style>

 # _Texture-Based Volume Rendering_
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/CTSkullImage.png/250px-CTSkullImage.png'/>
</div>
</div>

- Texture-based volume rendering is a technique that uses textures to represent the volume and its properties
- Advantages include fast computation and simple implementation
- Challenges include limited accuracy and potential for artifacts

---
<style scoped>p,li {font-size:0.88em}</style>

 # Hardware-Accelerated Volume Rendering
- Hardware-accelerated volume rendering is a technique that uses specialized hardware to accelerate the rendering of the volume
- Advantages include fast computation and improved performance
- Challenges include limited control over the acceleration and potential for artifacts


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Optimization Techniques**
- Optimization techniques are used to improve the performance and efficiency of volume rendering algorithms
- Examples include empty space skipping, early ray termination, octree and BSP space subdivision, and volume segmentation


---
<style scoped>p,li {font-size:0.88em}</style>

 # Empty Space Skipping

- Empty space skipping is a technique that skips rendering the empty spaces in the volume to improve performance
- Advantages include fast computation and reduced memory usage
- Challenges include potential for artifacts and limited control over the skipping

---
<style scoped>p,li {font-size:0.88em}</style>

 # Early Ray Termination
- Early ray termination is a technique that terminates the rendering of the volume early to improve performance
- Advantages include fast computation and reduced memory usage
- Challenges include potential for artifacts and limited control over the termination


---
<style scoped>p,li {font-size:0.88em}</style>

 # Octree and BSP Space Subdivision
- Octree and BSP space subdivision are techniques that partition the volume into smaller regions to improve performance
- Advantages include fast computation and reduced memory usage
- Challenges include potential for artifacts and limited control over the partitioning


---
<style scoped>p,li {font-size:0.80em}</style>

 # _Volume Segmentation_
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/CT_angiography_of_the_head_without_and_with_bone_removal.jpg/220px-CT_angiography_of_the_head_without_and_with_bone_removal.jpg'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/3D_CT_of_thorax.jpg/220px-3D_CT_of_thorax.jpg'/>
</div>
</div>

- Volume segmentation is a technique that divides the volume into smaller segments based on their properties to improve performance
- Advantages include fast computation and reduced memory usage
- Challenges include potential for artifacts and limited control over the segmentation

---
<style scoped>p,li {font-size:0.88em}</style>

 # Multiple and Adaptive Resolution Representation
- Multiple and adaptive resolution representation is a technique that uses multiple resolutions to represent the volume and its properties
- Advantages include fast computation and improved visualization of complex data
- Challenges include increased memory usage and potential for artifacts


---
<style scoped>p,li {font-size:0.88em}</style>

 # **Pre-Integrated Volume Rendering**
- Pre-integrated volume rendering is a technique that integrates the volume and its properties before rendering to improve performance
- Advantages include fast computation and improved visualization of complex data
- Challenges include potential for artifacts and limited control over the integration


---
<style scoped>p,li {font-size:0.88em}</style>

 # Image-Based Meshing

- Image-based meshing is a technique that creates a mesh from an image of the volume to improve performance
- Advantages include fast computation and improved visualization of complex data
- Challenges include potential for artifacts and limited control over the meshing

---
<style scoped>p,li {font-size:0.88em}</style>

 # Temporal Reuse of Voxels

- Temporal reuse of voxels is a technique that reuses the voxels from previous frames to improve performance in animations
- Advantages include fast computation and improved visualization of complex data
- Challenges include potential for artifacts and limited control over the reuse

---
<style scoped>p,li {font-size:0.88em}</style>

 # List of Related Software
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/V3d-display_01.png/250px-V3d-display_01.png'/>
</div>
</div>

- List of related software, including Paraview, Blender, and VTK.

I hope this slide presentation helps you understand the different techniques used in volume rendering!