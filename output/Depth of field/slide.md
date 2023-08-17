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
<!-- backgroundImage: url('backgrounds/wwwatercolor (4).png') -->
<!-- _class: lead -->

 # _Depth of field_

---
<style scoped>p,li {font-size:0.92em}</style>

 # Introduction to Depth of Field
- Definition: The range of distance in an image that appears to be in focus.
- Importance: DOF is a critical aspect of photography, as it can greatly impact the overall look and feel of an image.


---
<style scoped>p,li {font-size:0.68em}</style>

 # Factors Affecting Depth of Field
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Depth_of_field_illustration.svg/220px-Depth_of_field_illustration.svg.png'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Aperture (f-number)

+ Lower f-numbers result in shallower DOF, while higher f-numbers result in deeper DOF.

+ Aperture has the greatest impact on DOF of all the factors.
- Focal length

+ Wider lenses result in shallower DOF, while longer lenses result in deeper DOF.
- Distance from the camera to the subject

+ Closer subjects will have a shallower DOF, while farther subjects will have a deeper DOF.
</div>

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Effect of Lens Aperture on Depth of Field

- As aperture decreases (f-number increases), the depth of field increases, resulting in more of the image being in focus.
- Conversely, as aperture increases (f-number decreases), the depth of field decreases, resulting in less of the image being in focus.

---
<style scoped>p,li {font-size:0.88em}</style>

 # _Effect of Circle of Confusion on Depth of Field_
- The circle of confusion is the size of the pixel in the image sensor.
- As the aperture decreases (f-number increases), the circle of confusion becomes smaller, resulting in a deeper DOF.
- Conversely, as the aperture increases (f-number decreases), the circle of confusion becomes larger, resulting in a shallower DOF.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Camera Movements and Depth of Field

- Camera movements such as tilting or swinging can affect the DOF in an image.
- These movements can cause blur and distortion in the image, which can impact the overall look and feel of the photo.

---
<style scoped>p,li {font-size:0.84em}</style>

 # Object-Field Calculation Methods
- There are several methods for calculating the depth of field, including:

+ Hyperfocal distance method

+ Circle of confusion method

+ Depth of field tables


---
<style scoped>p,li {font-size:0.84em}</style>

 # Overcoming DOF Limitations

- There are several techniques for overcoming the limitations of DOF, including:

+ Focus stacking

+ Tilt-shift lenses

+ Selective focusing

---
<style scoped>p,li {font-size:0.92em}</style>

 # Diffraction and Depth of Field
- Diffraction occurs when light passes through a small opening, such as an aperture.
- As the aperture becomes smaller (f-number increases), diffraction can become more pronounced, resulting in a shallower DOF.


---
<style scoped>p,li {font-size:0.76em}</style>

 # _DOF Scales_
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/DOF_scale_detail.png/220px-DOF_scale_detail.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/TessinaDOF.jpg/220px-TessinaDOF.jpg'/>
</div>
</div>

- There are several DOF scales available, including:

+ Depth of field chart

+ DOF calculator app

+ Online DOF tools

---
<style scoped>p,li {font-size:0.76em}</style>

 # Hyperfocal Distance
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Contessa_hyperfocal.JPG/220px-Contessa_hyperfocal.JPG'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Minox_LX_hyperfocal.JPG/220px-Minox_LX_hyperfocal.JPG'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Nikon_28mm_lens_at_hyperfocus.jpg/220px-Nikon_28mm_lens_at_hyperfocus.jpg'/>
</div>
</div>
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Minolta_100-300_at_hyperfocal_distance.jpg/220px-Minolta_100-300_at_hyperfocal_distance.jpg'/>
</div>
</div>

- The hyperfocal distance is the distance at which the lens is focused such that the depth of field is maximized.
- Knowing the hyperfocal distance can help photographers achieve a deeper DOF in their images.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Near:Far Distribution
- The near:far distribution refers to the balance between the subject and the background in an image.
- A shallow DOF can create a strong contrast between the subject and the background, while a deep DOF can result in a more evenly focused image.


---
<style scoped>p,li {font-size:0.84em}</style>

 # DOF Formulae

- There are several formulae available for calculating the depth of field, including:

+ Hyperfocal distance formula

+ Circle of confusion formula

+ DoF scales formula

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Focus and f-number from DOF Limits**

- The focus and f-number settings can be adjusted to achieve a specific depth of field.
- Understanding the relationship between these settings is critical for achieving the desired DOF in an image.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Foreground and Background Blur

- A shallow DOF can result in a strong blur effect in the background, while a deep DOF can create a more evenly focused image with minimal blur.
- The amount of blur in the foreground and background can greatly impact the overall look and feel of an image.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Notes
- DOF is a critical aspect of photography that can greatly impact the overall look and feel of an image.
- Understanding the factors that affect DOF, as well as techniques for overcoming limitations, is essential for achieving the desired depth of field in an image.


---
<style scoped>p,li {font-size:0.96em}</style>

 # Citations

- List any sources used in the presentation, such as books or online articles.

---
<style scoped>p,li {font-size:0.96em}</style>

 # Sources

- Provide a list of sources for further information on depth of field, including books, online articles, and videos.