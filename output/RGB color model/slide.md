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

 # **RGB color model**

---
<style scoped>p,li {font-size:0.92em}</style>

 # Introduction

- RGB (Red, Green, Blue) color model is a widely used method for creating and displaying colors on electronic devices
- Additive colors are used in RGB, meaning that the combination of red, green, and blue light creates white

---
<style scoped>p,li {font-size:0.84em}</style>

 # Physical Principles for the Choice of Red, Green, and Blue
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- The choice of red, green, and blue is based on the way human eyes perceive color
- Red light has a longer wavelength than green or blue light, so it is more easily detected by the eye
- Green light is more easily detected than blue light, so it is used as a secondary color
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/CIExy1931_sRGB_gamut_D65.png/220px-CIExy1931_sRGB_gamut_D65.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # History of RGB Color Model Theory and Usage
- The RGB color model was first developed in the early 20th century for use in television and film production
- It became widely adopted in the computer industry in the 1980s and 1990s as a standard for displaying colors on screens


---
<style scoped>p,li {font-size:0.92em}</style>

 # Photography

- RGB is used in digital photography to capture and display images
- Most cameras use an RGB color space to represent the colors of an image

---
<style scoped>p,li {font-size:0.92em}</style>

 # Television

- RGB is used in television production to create and display colors
- TVs use RGB to display images and video content

---
<style scoped>p,li {font-size:0.92em}</style>

 # Personal Computers

- RGB is widely used in personal computers for displaying colors on screens
- Most computer graphics and multimedia applications use RGB as their default color space

---
<style scoped>p,li {font-size:0.92em}</style>

 # _RGB Devices_

- RGB devices include TVs, computer monitors, smartphones, and other electronic displays
- These devices use RGB to create and display colors

---
<style scoped>p,li {font-size:0.76em}</style>

 # RGB and Displays
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- RGB is used in displays to create and display colors
- The RGB color model is well-suited for displays because it can produce a wide range of colors
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/CRT_color_enhanced.png/250px-CRT_color_enhanced.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/RGB_color_wheel_10.svg/250px-RGB_color_wheel_10.svg.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/RGB_pixels_on_a_CRT_monitor.jpg/250px-RGB_pixels_on_a_CRT_monitor.jpg'/>
</div>
</div>
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/RGB_pixels.jpg/250px-RGB_pixels.jpg'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Video Electronics**

- RGB is used in video electronics, such as TVs and computer monitors, to display video content
- These devices use RGB to create and display colors in video signals

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Video Framebuffer**

- The video framebuffer is a memory buffer that stores the video signal before it is displayed on the screen
- RGB is used in the video framebuffer to store and process the video signal

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Nonlinearity**
- The RGB color model is nonlinear, meaning that the colors are not equally spaced on the color spectrum
- This nonlinearity can cause issues with color accuracy and reproduction


---
<style scoped>p,li {font-size:0.88em}</style>

 # RGB and Cameras
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Bayer_pattern_on_sensor.svg/220px-Bayer_pattern_on_sensor.svg.png'/>
</div>
</div>

- RGB is used in cameras to capture and store images
- Most camera sensors use an RGB color space to represent the colors of an image

---
<style scoped>p,li {font-size:0.92em}</style>

 # RGB and Scanners
- RGB is used in scanners to capture and store images
- Most scanners use an RGB color space to represent the colors of an image


---
<style scoped>p,li {font-size:0.84em}</style>

 # **Numeric Representations**
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- RGB colors can be represented using numerical values, such as 0-255 for each primary color
- These numerical values are used in computer graphics and multimedia applications
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/RGB_sliders.svg/220px-RGB_sliders.svg.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Palette_of_125_main_colors_with_RGB_components_divisible_by_64.gif/220px-Palette_of_125_main_colors_with_RGB_components_divisible_by_64.gif'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Color Depth

- The color depth of an RGB image refers to the number of bits used to represent the colors
- Higher color depths can produce more accurate and detailed colors, but they also require more memory and processing power

---
<style scoped>p,li {font-size:0.88em}</style>

 # Geometric Representation
- RGB colors can be represented geometrically using a color cube or a color wheel
- These geometric representations can help artists and designers visualize and manipulate colors
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/RGB_color_solid_cube.png/220px-RGB_color_solid_cube.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Colors in Web-Page Design
- RGB is widely used in web-page design to create and display colors on websites
- Web designers can use RGB to create and customize the colors of their websites


---
<style scoped>p,li {font-size:0.92em}</style>

 # Color Management

- Color management is the process of managing and maintaining color accuracy across different devices and media
- RGB color management is important for ensuring consistent and accurate colors in graphic design, photography, and other fields

---
<style scoped>p,li {font-size:0.92em}</style>

 # RGB Model and Luminance–Chrominance Formats Relationship
- The RGB model can be used in conjunction with luminance-chrominance formats to create and display colors on electronic devices
- This combination allows for a wide range of colors and improved color accuracy


---
<style scoped>p,li {font-size:0.88em}</style>

 # Conclusion
- RGB is a widely used color model in the computer industry and other fields
- It has many applications, including photography, television, personal computers, and web-page design
- Understanding the physical principles, history, and usage of RGB can help artists, designers, and technologists create and display colors accurately and effectively.
