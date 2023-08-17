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
<!-- backgroundImage: url('backgrounds/aaabstract (11).png') -->
<!-- _class: lead -->

 # Multi-exposure HDR capture

---
<style scoped>p,li {font-size:0.88em}</style>

 # _Benefits_

- High dynamic range (HDR) images have a wider range of tonal values than standard images
- More detail in both bright and dark areas of the image
- Better representation of real-world scenes with high contrast ratios

---
<style scoped>p,li {font-size:0.80em}</style>

 # Limitations
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Hdr_capture_golf_swing_ghost_effect.jpg/400px-Hdr_capture_golf_swing_ghost_effect.jpg'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/HDR_ghosting_from_motion_-_playground_-_HDR_on.jpg/220px-HDR_ghosting_from_motion_-_playground_-_HDR_on.jpg'/>
</div>
</div>

- Requires multiple exposures, which can be time-consuming and increase the cost of capture
- Can be computationally intensive to merge the images into an HDR image
- May require post-capture processing to achieve optimal results

---
<style scoped>p,li {font-size:0.88em}</style>

 # Process

- Capture multiple exposures of the same scene with different settings (e.g., ISO, shutter speed, aperture)
- Use software to merge the exposures into an HDR image
- Tone mapping can be applied to enhance the contrast and color of the image

---
<style scoped>p,li {font-size:0.88em}</style>

 # Capturing multiple images (exposure bracketing)
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Einfluss_der_Zeit_auf_die_Belichtung.jpg/220px-Einfluss_der_Zeit_auf_die_Belichtung.jpg'/>
</div>
</div>

- Exposure bracketing involves capturing multiple images with different settings, each with a slightly different exposure value
- This allows for more flexibility in post-capture processing and merging of the images

---
<style scoped>p,li {font-size:0.88em}</style>

 # _Merging the images into an HDR image_
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Dynamic_Range_Increase.jpg/220px-Dynamic_Range_Increase.jpg'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Software can be used to merge the multiple exposures into a single HDR image
- The merged image can be created using different methods, such as weighted averaging or tone mapping
</div>

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Storing
- HDR images can be stored in various formats, including RAW, JPEG, and TIFF
- Some cameras and software support native HDR format storage


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Tone mapping_

- Tone mapping is the process of enhancing the contrast and color of an HDR image
- Can be done using various algorithms and techniques, such as gradient descent, optimization, or machine learning

---
<style scoped>p,li {font-size:0.88em}</style>

 # Types of HDR

- Single-exposure HDR: uses a single exposure, but can still produce an HDR image with more tonal values than a standard image
- Multi-exposure HDR: uses multiple exposures to capture a wider range of tonal values
- Bracketed HDR: captures multiple exposures and merges them into a single HDR image

---
<style scoped>p,li {font-size:0.88em}</style>

 # Examples

- Landscapes, such as sunsets or mountains, can benefit from HDR capture
- Portraits, such as in bright outdoor light or low-light indoor settings, can also benefit from HDR capture
- Surveillance cameras can use HDR to improve the quality of footage and reduce noise

---
<style scoped>p,li {font-size:0.84em}</style>

 # Devices

- Digital cameras, such as DSLRs and mirrorless cameras
- Smartphones with HDR capabilities
- Action cameras, such as GoPros and drones
- Surveillance cameras, such as security cameras and IP cameras

---
<style scoped>p,li {font-size:0.88em}</style>

 # **Post-capture software**
- Adobe Photoshop and Lightroom
- Capture One
- HDR software, such as HDR Express, HDR Darkroom, and HDR Universe


---
<style scoped>p,li {font-size:0.88em}</style>

 # **Photography**
- Landscape photography can benefit from HDR capture to capture a wider range of tonal values
- Portrait photography can also benefit from HDR capture to improve the quality of the image
- Product photography can use HDR to enhance the detail and contrast of the product


---
<style scoped>p,li {font-size:0.88em}</style>

 # _Videography_
- HDR video capture is becoming more common in movie production, television shows, and streaming services
- Can be used to create more realistic and immersive video content
- Requires the use of specialized equipment and software for capture and processing


---
<style scoped>p,li {font-size:0.88em}</style>

 # _Surveillance cameras_
- HDR surveillance cameras can improve the quality of footage and reduce noise
- Can be used in various settings, such as airports, train stations, and city streets
- May be more expensive than standard surveillance cameras


---
<style scoped>p,li {font-size:0.80em}</style>

 # _History_

- Mid 19th century: Photography was invented, but images were limited to a small dynamic range
- Mid 20th century: Film technology improved, allowing for more detail in both bright and dark areas
- Late 20th century: Digital photography emerged, with the ability to capture and process HDR images
- 21st century: HDR technology has become more widespread and accessible, with the development of software and hardware for capture and processing

I hope this presentation provides a comprehensive overview of Multi-exposure HDR capture! Let me know if you have any questions or need further clarification.