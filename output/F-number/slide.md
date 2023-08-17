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
<!-- backgroundColor: #88888d -->
<!-- _class: lead -->

 # **F-number**

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Notation**
- F-number (F-stop) notation: f/#, where # is the stop value
- Examples: f/2, f/4, f/8, etc.


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Stops_

- Stop values: 1, 2, 4, 8, 16, etc.
- Each stop represents a doubling or halving of the amount of light entering the camera

---
<style scoped>p,li {font-size:0.84em}</style>

 # f-stop Conventions
- Traditional f-stop conventions:

+ Small numbers for large apertures (e.g. f/2)

+ Large numbers for small apertures (e.g. f/16)
- Why this convention? To make the math easier!


---
<style scoped>p,li {font-size:0.92em}</style>

 # Exposure
- F-number affects exposure time: higher f-numbers require longer exposure times
- Exposure = f-number x shutter speed x ISO setting


---
<style scoped>p,li {font-size:0.92em}</style>

 # Fractional Stops

- Instead of whole stops, photographers often use fractional stops (e.g. f/2.8 instead of f/4)
- Why? To allow for more precise adjustments in exposure and depth of field.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Standard Full-Stop F-Number Scale

- f/1, f/1.4, f/2, f/2.8, f/4, f/5.6, f/8, f/11, etc.
- Note that the scale is not linear, but rather exponential.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Typical One-Half-Stop F-Number Scale

- f/0.5, f/1, f/1.5, f/2, f/2.5, f/3.5, f/4, f/4.5, etc.
- Note that the half-stop scale is more commonly used in practice than the full-stop scale.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Typical One-Third-Stop F-Number Scale
- f/0.33, f/0.5, f/0.67, f/1, f/1.33, f/1.67, f/2, etc.
- Note that the third-stop scale is even more finely grained than the half-stop scale.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Typical One-Quarter-Stop F-Number Scale

- f/0.25, f/0.33, f/0.4, f/0.5, f/0.67, f/0.8, f/1, etc.
- Note that the quarter-stop scale is even more precise than the third-stop scale.

---
<style scoped>p,li {font-size:0.92em}</style>

 # _H-Stop and T-Stop_

- H-stop: a measure of the actual light transmission through the lens, taking into account the lens's loss of light due to aberrations and other factors.
- T-stop: a measure of the total light transmission, including the effect of the lens's loss of light as well as the camera's sensitivity.

---
<style scoped>p,li {font-size:0.96em}</style>

 # Sunny 16 Rule
- A general guideline for achieving proper exposure in daylight: f/5.6 at 1/100th sec. or f/4 at 1/200th sec.


---
<style scoped>p,li {font-size:0.84em}</style>

 # Effects on Image Sharpness
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Depth of field: the range of distance in an image that appears to be in focus.
- F-number affects depth of field, with lower f-numbers resulting in shallower depth of field and higher f-numbers resulting in deeper depth of field.
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Jonquil_flowers_merged.jpg/400px-Jonquil_flowers_merged.jpg'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Blumen_im_Sommer.jpg/400px-Blumen_im_Sommer.jpg'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.96em}</style>

 # **Human Eye**
- The human eye has a relatively narrow depth of field, so we tend to notice the subject in focus and blur the background.


---
<style scoped>p,li {font-size:0.88em}</style>

 # Focal Ratio in Telescopes
- In telescopes, the focal ratio is the ratio of the focal length to the diameter of the objective lens.
- A higher focal ratio results in a longer exposure time and more sensitive images.
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Focal_ratio.svg/250px-Focal_ratio.svg.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Camera Equation (G#)

- The camera equation relates the f-number, shutter speed, and ISO setting to achieve proper exposure.
- G# = (f-number x shutter speed x ISO setting) / (2^exposure_steps)

---
<style scoped>p,li {font-size:0.96em}</style>

 # Working F-Number
- The working f-number is the actual f-number used by the photographer, taking into account any lens aberrations or other factors that affect the amount of light transmitted through the lens.


---
<style scoped>p,li {font-size:0.80em}</style>

 # History
- Origins of relative aperture:

+ The concept of relative aperture can be traced back to the early days of photography, when photographers used different sized lenses to achieve different effects.

+ The term "f-stop" was coined in the early 20th century to describe the relationship between lens size and exposure time.
- Typographical standardization:

+ Over time, the notation for f-stops has become standardized, with f/ being the most commonly used symbol.


---
<style scoped>p,li {font-size:0.88em}</style>

 # Aperture Numbering Systems
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Different camera manufacturers use different numbering systems for apertures, but they all follow the same basic principles of relative aperture.
- Some common numbering systems include Canon's "EV" system and Nikon's " stops" system.
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/No1-A_Autographic_Kodak_Jr.jpg/220px-No1-A_Autographic_Kodak_Jr.jpg'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Conclusion
- F-number is an essential aspect of photography that affects both exposure and depth of field.
- Understanding the concept of relative aperture and how it is used in practice can help photographers achieve better results and more precise control over their images.
