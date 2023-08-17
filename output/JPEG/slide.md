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
<!-- backgroundColor: #828c97 -->
<!-- _class: lead -->

 # JPEG

---
<style scoped>p,li {font-size:0.88em}</style>

 # **Introduction**

- JPEG (Joint Photographic Experts Group) is a widely used image compression format
- Developed in the late 1980s and early 1990s by the International Organization for Standardization (ISO)
- Designed to reduce the size of digital images for efficient storage and transmission

---
<style scoped>p,li {font-size:0.88em}</style>

 # **History**
- First version of JPEG released in 1992 as ISO/IEC 10918-1
- Successive versions have been published regularly since then, with the latest being JPEG XL in 2020
- JPEG has become a standard format for digital images and is supported by most image editing software and web browsers


---
<style scoped>p,li {font-size:0.88em}</style>

 # _Background_

- JPEG is a lossy compression format, meaning that some of the original image data is discarded during compression
- Lossy compression allows for much smaller file sizes but may result in noticeable artifacts or loss of detail in the image
- JPEG is designed to be visually lossless, meaning that the compressed image should appear as good as the original to the human eye

---
<style scoped>p,li {font-size:0.88em}</style>

 # _JPEG Standard_

- JPEG defines a set of algorithms and techniques for compressing and decompressing images
- The standard includes specifications for color spaces, sampling, and other aspects of image processing
- JPEG is defined by a series of ISO/IEC standards, with the most recent being ISO/IEC 10918-4:2020

---
<style scoped>p,li {font-size:0.88em}</style>

 # Patent Controversy
- The original JPEG algorithm was developed by a team of researchers at the University of California, Los Angeles (UCLA)
- The team held patents on the technology, which led to licensing disputes and legal action in the early 2000s
- The patent controversy has largely been resolved, with many of the original patents having expired or been re-assigned


---
<style scoped>p,li {font-size:0.88em}</style>

 # **Typical Use**

- JPEG is commonly used for digital photographs, graphics, and other types of images
- JPEG files are often used on the web, where file size is a critical factor in page load times and network bandwidth usage
- JPEG is also used in many applications, such as image editing software, graphics viewers, and digital frame displays

---
<style scoped>p,li {font-size:0.88em}</style>

 # _JPEG Compression_

- JPEG compression works by dividing the image into blocks of pixels and applying a series of transformation techniques to each block
- The transformed blocks are then quantized and encoded using Huffman coding or arithmetic coding
- The resulting compressed file can be much smaller than the original image, with minimal loss of detail or artifacts

---
<style scoped>p,li {font-size:0.88em}</style>

 # **Lossless Editing**

- JPEG also supports lossless editing, where the image is compressed and decompressed without any loss of data
- This allows for efficient editing of images without sacrificing quality or detail
- Lossless JPEG compression is typically used for images that require high precision, such as scientific imaging or graphic design

---
<style scoped>p,li {font-size:0.88em}</style>

 # JPEG Files

- JPEG files have a ".jpg" or ".jpeg" filename extension
- The file format is based on the Baseline TIFF (Tagged Image File Format) standard, with additional components and syntax specific to JPEG
- JPEG files can contain multiple images, each compressed using a different set of parameters

---
<style scoped>p,li {font-size:0.88em}</style>

 # Color Profile

- JPEG supports color profiles, which define the color characteristics of the image
- Profiles can be used to convert images to different color spaces or to apply specific rendering intentions
- Color profiles are often used in professional imaging applications, where precise color reproduction is critical

---
<style scoped>p,li {font-size:0.88em}</style>

 # _Syntax and Structure_
- JPEG files consist of a series of blocks, each containing a portion of the image data
- The blocks are organized into segments, which are delimited by markers in the file
- The syntax and structure of JPEG files are defined in the ISO/IEC 10918-4 standard


---
<style scoped>p,li {font-size:0.88em}</style>

 # JPEG Codec Example
- A codec (compression-decompression) is a software implementation of the JPEG standard
- An example of a JPEG codec is libjpg, which is widely used in many applications and operating systems
- The codec takes the image data as input and produces the compressed JPEG file as output


---
<style scoped>p,li {font-size:0.88em}</style>

 # Encoding

- JPEG encoding involves the transformation and quantization of the image data, followed by Huffman or arithmetic coding
- The encoded data is then stored in the JPEG file
- The encoding process can be optimized for different applications, such as speed, size, or quality

---
<style scoped>p,li {font-size:0.88em}</style>

 # **Color Space Transformation**

- JPEG supports color space transformation, which allows images to be converted between different color models
- Common color spaces include sRGB, Adobe RGB, and CIE XYZ
- Color space transformation can be used to ensure that the image appears correctly on different devices or in different applications

---
<style scoped>p,li {font-size:0.88em}</style>

 # **Downsampling**
- JPEG supports downsampling, which allows for reduced file sizes by discarding some of the high-frequency detail in the image
- Downsampling can be applied at various levels, from individual blocks to entire images
- The amount of downsampling can be controlled using a variety of techniques, such as filtering or decimation


---
<style scoped>p,li {font-size:0.88em}</style>

 # Block Splitting
- JPEG blocks are split into smaller blocks for compression and decompression
- Block splitting allows for more efficient compression and decompression, as well as better quality retention
- The size and shape of the blocks can be controlled using a variety of techniques, such as fixed-size blocks or adaptive blocking


---
<style scoped>p,li {font-size:0.80em}</style>

 # Discrete Cosine Transform
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/JPEG_example_subimage.svg/256px-JPEG_example_subimage.svg.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Dctjpeg.png/220px-Dctjpeg.png'/>
</div>
</div>

- JPEG uses the discrete cosine transform (DCT) to convert the image data into frequency space
- The DCT is a type of Fourier transform that decomposes the image into a set of frequency components
- The DCT allows for efficient compression and decompression of images, as well as good quality retention

---
<style scoped>p,li {font-size:0.84em}</style>

 # _Quantization_
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/5/5e/Idct-animation.gif'/>
</div>
</div>

- JPEG quantization involves reducing the precision of the image data by discarding some of the frequency components
- The amount of quantization can be controlled using a variety of techniques, such as fixed-point quantization or adaptive quantization
- The choice of quantization technique and parameters can have a significant impact on the quality and size of the compressed file

---
<style scoped>p,li {font-size:0.80em}</style>

 # Entropy Coding
- JPEG uses entropy coding to compress the image data further
- Entropy coding is a form of lossless compression that takes advantage of the statistical properties of the image data
- The choice of entropy coding technique and parameters can have a significant impact on the quality and size of the compressed file
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/JPEG_ZigZag.svg/220px-JPEG_ZigZag.svg.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/JPEG_process.svg/300px-JPEG_process.svg.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.76em}</style>

 # Compression Ratio and Artifacts
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- The compression ratio is a measure of how much the image has been reduced in size during compression
- The compression ratio can be controlled using a variety of techniques, such as adjusting the amount of downsampling or quantization
- The choice of compression ratio can have a significant impact on the quality and size of the compressed file, as well as the presence of artifacts such as blockiness or ringing
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Lichtenstein_jpeg_difference.png/256px-Lichtenstein_jpeg_difference.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Lichtenstein_img_processing_test.png/256px-Lichtenstein_img_processing_test.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/1/15/Jpegvergroessert.jpg'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # Decoding
- JPEG decoding involves reversing the compression process to extract the original image data from the compressed file
- The decoding process is similar to the encoding process, but in reverse
- The decoded image can be restored to its original quality and color space using a variety of techniques, such as color profile correction or inverse conversion


---
<style scoped>p,li {font-size:0.88em}</style>

 # **Required Precision**

- JPEG supports a range of precision levels, from low-bit depth to high-bit depth
- The required precision can be controlled using a variety of techniques, such as fixed-point quantization or adaptive quantization
- The choice of required precision can have a significant impact on the quality and size of the compressed file

---
<style scoped>p,li {font-size:0.88em}</style>

 # Effects of JPEG Compression

- JPEG compression can have a number of effects on the image, including loss of detail, artifacts, and color distortion
- The specific effects of JPEG compression will depend on the amount of compression and the parameters used during encoding and decoding
- The effects of JPEG compression can be mitigated using a variety of techniques, such as adjusting the compression ratio or using lossless editing

---
<style scoped>p,li {font-size:0.84em}</style>

 # _Sample Photographs_
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Visual_impact_of_a_jpeg_compression_on_Photoshop.jpg/220px-Visual_impact_of_a_jpeg_compression_on_Photoshop.jpg'/>
</div>
</div>

- Here are some sample photographs demonstrating the effects of JPEG compression at different levels of quality and size
- The samples show the original image, as well as compressed versions with increasing amounts of artifacts and loss of detail
- The samples can be used to demonstrate the trade-offs between quality and size in JPEG compression

---
<style scoped>p,li {font-size:0.88em}</style>

 # Lossless Further Compression

- JPEG also supports lossless further compression, which allows for efficient compression of already compressed images
- Lossless further compression can be achieved using a variety of techniques, such as Huffman coding or arithmetic coding
- The choice of technique and parameters can have a significant impact on the quality and size of the compressed file

---
<style scoped>p,li {font-size:0.88em}</style>

 # Derived Formats for Stereoscopic 3D
- JPEG has also developed derived formats specifically designed for stereoscopic 3D imaging, such as JPEG Stereoscopic and JPEG Multi-Picture Format
- These formats support the encoding and decoding of stereoscopic 3D images, as well as the associated metadata and synchronization information
- The derived formats can be used for a variety of applications, including movie and video production, virtual reality, and gaming


---
<style scoped>p,li {font-size:0.88em}</style>

 # JPEG XT
- JPEG XT is a recent extension to the JPEG standard that supports high-quality compression of text and other document images
- JPEG XT uses a combination of techniques, such as sparse coding and arithmetic coding, to achieve high compression ratios with minimal loss of detail or artifacts
- JPEG XT is designed for applications where high-quality text compression is critical, such as digital publishing and document management


---
<style scoped>p,li {font-size:0.88em}</style>

 # JPEG XL
- JPEG XL is a recent extension to the JPEG standard that supports high-quality compression of images with complex structures, such as those found in medical imaging and scientific visualization
- JPEG XL uses a combination of techniques, such as wavelet transforms and adaptive quantization, to achieve high compression ratios with minimal loss of detail or artifacts
- JPEG XL is designed for applications where high-quality image compression is critical, such as medical imaging and scientific visualization


---
<style scoped>p,li {font-size:0.88em}</style>

 # Conclusion
- JPEG is a widely used and powerful image compression format that supports efficient storage and transmission of digital images
- The standard includes a range of techniques and parameters for controlling the quality and size of the compressed file, as well as support for lossless editing and derived formats for stereoscopic 3D imaging
- JPEG continues to evolve with new extensions and applications, such as JPEG XT and JPEG XL, to meet the needs of a wide range of industries and applications.
