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
<!-- backgroundImage: url('backgrounds/wwwatercolor (5).png') -->
<!-- _class: lead -->

 # Graphics file format

---
<style scoped>p,li {font-size:0.92em}</style>

 # Introduction to Graphics File Formats

- Graphics file formats are used to store and transmit images and other graphical content
- There are many different types of graphics file formats, each with their own strengths and weaknesses

---
<style scoped>p,li {font-size:0.92em}</style>

 # Image File Sizes

- Image file sizes can vary greatly depending on the format and quality of the image
- Large image files can be unwieldy and difficult to transmit, while small image files may lose detail and quality

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Image File Compression**

- Image file compression is a technique used to reduce the size of image files without losing detail or quality
- Many graphics file formats include built-in compression algorithms to help reduce file sizes

---
<style scoped>p,li {font-size:0.72em}</style>

 # Major Graphic File Formats
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Some major graphic file formats include:

+ JPEG (Joint Photographic Experts Group)

+ GIF (Graphics Interchange Format)

+ PNG (Portable Network Graphics)

+ JPEG 2000 (a successor to JPEG with improved compression and features)

+ WebP (a web-optimized format developed by Google)
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Image_formats_by_scope.svg/660px-Image_formats_by_scope.svg.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # Raster Formats (2D)

- Raster formats are used to store two-dimensional images
- Examples include:

+ JPEG, GIF, PNG, and JPEG 2000

---
<style scoped>p,li {font-size:0.88em}</style>

 # Delivery Formats

- Delivery formats are used to transmit and display graphics files on the web or other digital platforms
- Examples include:

+ JPEG, GIF, PNG, WebP, and JPEG 2000

---
<style scoped>p,li {font-size:0.92em}</style>

 # JPEG
- JPEG (Joint Photographic Experts Group) is a widely used raster format for photographic images
- Features include lossy compression, color correction, and progressive rendering


---
<style scoped>p,li {font-size:0.92em}</style>

 # GIF

- GIF (Graphics Interchange Format) is a raster format used for animations and simple graphics
- Features include lossless compression, transparency, and limited color depth

---
<style scoped>p,li {font-size:0.92em}</style>

 # _PNG_

- PNG (Portable Network Graphics) is a raster format used for high-quality images and graphics
- Features include lossless compression, transparent backgrounds, and support for alpha channels

---
<style scoped>p,li {font-size:0.92em}</style>

 # JPEG 2000

- JPEG 2000 is a successor to JPEG with improved compression and features
- Features include lossy compression, color correction, and support for high-dynamic-range images

---
<style scoped>p,li {font-size:0.92em}</style>

 # WebP

- WebP is a web-optimized format developed by Google for images and graphics on the web
- Features include lossy and lossless compression, transparency, and support for alpha channels

---
<style scoped>p,li {font-size:0.92em}</style>

 # HDR Raster Formats
- High dynamic range (HDR) raster formats are used to store images with a higher range of colors and contrast than traditional formats
- Examples include JPEG XL and HEIF


---
<style scoped>p,li {font-size:0.92em}</style>

 # HEIF and AVIF

- HEIF (High Efficiency Image Format) is a raster format developed by the MPEG group for high-quality images and graphics
- AVIF (Alliance of Virtuous Image Formats) is a related format developed by the Alliance of Open Media

---
<style scoped>p,li {font-size:0.92em}</style>

 # JPEG XL
- JPEG XL is a raster format developed by the Joint Photographic Experts Group for high-quality images and graphics
- Features include lossy compression, color correction, and support for high-dynamic-range images


---
<style scoped>p,li {font-size:0.92em}</style>

 # Authoring / Interchange Formats
- Authoring formats are used to create and edit graphics files, while interchange formats are used to transmit and display them between different systems
- Examples include TIFF (Tagged Image File Format), BMP (Bitmap), PPM (Pixmap), PGM (Pixmap), and PBM (Pixmap)


---
<style scoped>p,li {font-size:0.92em}</style>

 # Container Formats of Raster Graphics Editors
- Many raster graphics editors use their own proprietary file formats for storing and transmitting images
- Examples include Adobe Photoshop's PSD format, GIMP's XCF format, and CorelDRAW's CDR format


---
<style scoped>p,li {font-size:0.80em}</style>

 # Other Raster Formats

- Other raster formats include:

+ Targa ( Truevision TARGA)

+ PCX (Paintbrush Computer eXchange)

+ PICT (Picture)

+ DIB (Device Independent Bitmap)

---
<style scoped>p,li {font-size:0.80em}</style>

 # Vector Formats

- Vector formats are used to store two-dimensional graphics as mathematical equations rather than pixel values
- Examples include:

+ CGM (Computer Graphics Metafile)

+ Gerber format (RS-274X)

+ SVG (Scalable Vector Graphics)

---
<style scoped>p,li {font-size:0.80em}</style>

 # Other 2D Vector Formats
- Other 2D vector formats include:

+ EPS (Encapsulated PostScript)

+ PDF (Portable Document Format)

+ AI (Adobe Illustrator Artwork)

+ WMF (Windows Metafile)


---
<style scoped>p,li {font-size:0.80em}</style>

 # 3D Vector Formats
- 3D vector formats are used to store three-dimensional graphics as mathematical equations rather than pixel values
- Examples include:

+ OBJ (Object File Format)

+ STL (STereoLithography)

+ 3DS (3D Studio)


---
<style scoped>p,li {font-size:0.80em}</style>

 # **Compound Formats**

- Compound formats are used to store multiple graphics files or other data in a single file
- Examples include:

+ PSD (Photoshop Document)

+ PPT (PowerPoint Presentation)

+ DOCX (Office Open XML Document)

---
<style scoped>p,li {font-size:0.80em}</style>

 # _Stereo Formats_

- Stereo formats are used to store stereoscopic images or videos for viewing with stereoscopic glasses or other devices
- Examples include:

+ JPEG 3D

+ MPO (Multi-view Palettized OBJ)

+ MBF (Metafile Binary Format)

---
<style scoped>p,li {font-size:0.88em}</style>

 # **Conclusion**
- Graphics file formats are essential for storing and transmitting images and other graphical content
- There are many different types of graphics file formats, each with their own strengths and weaknesses
- By understanding the different formats and their uses, you can choose the best format for your needs.
