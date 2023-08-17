---
marp: true
math: katex
theme: uncover
style: |
   @import url('https://unpkg.com/tailwindcss@2.2.19/dist/utilities.min.css');
   section {display: flex;flex-flow: column; font-size:35px; letter-spacing:1.4px;}

   header {overflow:visible} header > img.logo {position:absolute; right:15px;}

   header > img.logo {position:absolute; right:15px;}


---
<!-- backgroundColor: white -->
<!-- _class: lead -->

 # TIFF

---
<style scoped>p,li {font-size:0.92em}</style>

 # _History_
- TIFF (Tagged Image File Format) was developed by Aldus Corporation (now Adobe Systems) in the mid-1980s as a standard file format for computer graphics and image processing.
- It was designed to be a flexible, versatile format that could handle a wide range of image types and sizes.


---
<style scoped>p,li {font-size:0.88em}</style>

 # Overview
- TIFF is a raster graphics file format that supports color images, grayscale images, and black-and-white images.
- It uses tag-based storage to store metadata and image data, which makes it highly customizable and flexible.
- TIFF is widely used in industries such as photography, graphic design, publishing, and medical imaging.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Internet Media Type
- TIFF is registered as an internet media type (image/tiff) by the Internet Assigned Numbers Authority (IANA).
- This means that web browsers and other software can automatically recognize and handle TIFF files without the need for additional plugins or codecs.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Digital Preservation
- TIFF is widely used in digital preservation due to its ability to store high-quality images with embedded metadata and other information.
- Many libraries, archives, and museums use TIFF as a standard format for digitizing and preserving printed materials, photographs, and other types of visual media.


---
<style scoped>p,li {font-size:0.88em}</style>

 # Details
- TIFF files can contain multiple subfiles, which allows users to store different types of data (such as image data, metadata, and other information) in separate files that can be accessed and managed independently.
- TIFF supports a variety of compression methods, including lossless and lossy compression, which can help reduce file size and improve storage efficiency.
- TIFF also supports a range of image types, including grayscale, RGB, CMYK, and others.


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Part 1 - Baseline TIFF_

- Baseline TIFF is the core set of features and functionality that all TIFF files must support.
- This includes features such as image data, metadata, and other information stored in tag-based storage.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Multiple Subfiles
- In addition to the main image data, TIFF files can contain multiple subfiles that store additional information such as metadata, thumbnails, and other data.
- These subfiles are typically stored in a separate directory or file and can be accessed and managed independently of the main image data.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Strips

- TIFF supports the use of strips, which are sequences of images that are stored together in a single file.
- This allows users to store and manage large sets of images more efficiently than storing each image as a separate file.

---
<style scoped>p,li {font-size:0.88em}</style>

 # Compression
- TIFF supports a variety of compression methods, including lossless and lossy compression.
- Some common lossless compression methods used in TIFF include Huffman coding and run-length encoding.
- Some common lossy compression methods used in TIFF include JPEG (Joint Photographic Experts Group) and Discrete Cosine Transform (DCT).


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Image Types**

- In addition to the standard grayscale, RGB, and CMYK image types, TIFF also supports a range of other image types.
- These may include specialized image types such as multispectral, hyperspectral, and medical imaging data.

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Byte Order**

- TIFF files can store images with a variety of byte orders, including little-endian and big-endian.
- The byte order determines the order in which the bytes of the image data are stored in the file.

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Other TIFF Fields_
- In addition to the main image data and metadata, TIFF files can contain a variety of other fields and information.
- These may include thumbnails, audio and video data, and other types of media.


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Part 2 - TIFF Extensions_
- TIFF extensions are additional features and functionality that can be added to the baseline TIFF format.
- These may include features such as support for new image types, additional metadata fields, and other types of data.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Image Trees
- TIFF supports the use of image trees, which are hierarchical structures that allow users to store and manage large sets of images more efficiently than storing each image as a separate file.
- Image trees can be used to store and manage images at multiple levels of detail, with higher-level nodes representing coarser resolutions and lower-level nodes representing finer resolutions.


---
<style scoped>p,li {font-size:0.92em}</style>

 # _Tiles_
- TIFF also supports the use of tiles, which are rectangular blocks of image data that can be stored separately from the main image file.
- This allows users to store and manage large images more efficiently than storing the entire image as a single file.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Other Extensions
- In addition to TIFF extensions, there are also other formats that support TIFF-like functionality.
- These may include formats such as Exif (Exchangeable Image File Format), which is widely used in digital photography, and IPTC (International Press and Telecommunications Council), which is used in publishing and other industries.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Private Tags

- TIFF supports the use of private tags, which are custom metadata fields that can be defined by the user to store information specific to their application or industry.
- Private tags can be used to store a wide range of information, including image data, metadata, and other types of data.

---
<style scoped>p,li {font-size:0.92em}</style>

 # TIFF Compression Tag

- The TIFF compression tag is a specialized field that allows users to specify the type of compression used in the file.
- This can be useful for applications that require specific compression methods or that need to support multiple compression methods.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Related Formats
- TIFF is related to other image formats such as JPEG, PNG (Portable Network Graphics), and GIF (Graphics Interchange Format).
- These formats share some similarities with TIFF but have different strengths and weaknesses depending on the specific application or use case.


---
<style scoped>p,li {font-size:0.92em}</style>

 # _BigTIFF_

- BigTIFF is a variant of TIFF that supports larger file sizes and more advanced features such as multithreaded compression and image pyramids.
- BigTIFF is widely used in applications such as medical imaging, geospatial analysis, and other types of visual data processing.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Exif

- Exif (Exchangeable Image File Format) is a format that supports many of the same features as TIFF but is more specifically designed for digital photography.
- Exif includes features such as image metadata, thumbnails, and other information that are commonly used in digital photography.

---
<style scoped>p,li {font-size:0.92em}</style>

 # TIFF/IT

- TIFF/IT (Tagged Image File Format/Information Technology) is a variant of TIFF that is specifically designed for use in the IT industry.
- It includes features such as IT-specific metadata fields, improved compression methods, and other advanced functionality.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Conclusion

- TIFF is a versatile and widely used image format that supports a range of applications and industries.
- Its ability to store high-quality images with embedded metadata and other information makes it an ideal choice for digital preservation, publishing, and other applications where image quality and accuracy are critical.