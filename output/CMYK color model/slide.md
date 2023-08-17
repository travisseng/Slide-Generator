---
marp: true
math: katex
theme: default
paginate: True
style: |
   @import url('https://unpkg.com/tailwindcss@2.2.19/dist/utilities.min.css');
   section {display: flex;flex-flow: column; font-size:35px; letter-spacing:1.4px;}

   header {overflow:visible} header > img.logo {position:absolute; right:15px;}

   header > img.logo {position:absolute; right:15px;}


---
<!-- backgroundColor: white -->
<!-- _class: lead -->

 # CMYK color model

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Introduction**

- The CMYK color model is used in printing and design to produce high-quality color images
- CMYK stands for Cyan, Magenta, Yellow, and Black

---
<style scoped>p,li {font-size:0.88em}</style>

 # Halftoning
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Halftoningcolor.svg/220px-Halftoningcolor.svg.png'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Halftoning is the process of converting a continuous-tone image into a binary image using dots
- This allows for the printing of high-quality images with a range of colors
</div>

</div>


---
<style scoped>p,li {font-size:0.84em}</style>

 # Comparison to CMY
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Barns_grand_tetons.jpg/400px-Barns_grand_tetons.jpg'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/CMYK_offset_on_paper2.jpg/220px-CMYK_offset_on_paper2.jpg'/>
</div>
</div>

- CMYK is similar to the CMY color model, but with the addition of black (K)
- The K layer helps to improve the overall print quality and darken shadows

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Other Printer Color Models_

- Other printer color models include RGB (Red, Green, Blue) and Pantone
- RGB is used in digital displays and produces a wider range of colors, while Pantone is a standardized color matching system

---
<style scoped>p,li {font-size:0.88em}</style>

 # **Comparison with RGB Displays**
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- RGB displays produce a wider range of colors than CMYK prints
- However, CMYK prints have better color accuracy and can reproduce deeper blacks
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/CIE1931xy_gamut_comparison.svg/220px-CIE1931xy_gamut_comparison.svg.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # **Spectrum of Printed Paper**
- The spectrum of printed paper shows the range of colors that can be produced using CMYK inks
- The spectrum includes a wide range of blues, greens, yellows, and reds
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/CMYK_Spectrum_printed_paper.pdf/page1-800px-CMYK_Spectrum_printed_paper.pdf.jpg'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # Conversion
- Converting RGB images to CMYK can result in color shift and loss of detail
- It's important to use the correct color profile and conversion software to ensure accurate results
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/NIEdot367.jpg/220px-NIEdot367.jpg'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # _Conclusion_
- CMYK is a widely used color model in printing and design that produces high-quality, accurate colors
- Understanding the CMYK color model can help designers and printers produce better prints with more vivid colors.

I hope this presentation helps you understand the CMYK color model! Let me know if you have any other questions or if there's anything else I can do to help.
