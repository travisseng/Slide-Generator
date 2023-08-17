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

 # ISBN (identifier)

---
<style scoped>p,li {font-size:0.92em}</style>

 # History of ISBN
- Developed by the International Organization for Standardization (ISO) in 1967
- Initially used for books, but now used for all types of media, including audio and video recordings, e-books, and online resources


---
<style scoped>p,li {font-size:0.88em}</style>

 # Overview of ISBN
- Unique identifier assigned to each publication
- Consists of 10 or 13 digits, depending on the country of publication
- Used for tracking and identifying publications in the global supply chain


---
<style scoped>p,li {font-size:0.88em}</style>

 # _Issuing Process_
- ISBNs are issued by official agencies in each country, such as the Library of Congress in the United States
- Publishers can purchase blocks of ISBNs to assign to their publications
- Self-publishers can also obtain ISBNs directly from the official agency


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Registration Group Element**

- The first part of the ISBN, which identifies the country or region where the publication was published
- Examples include "978" for the United States and Canada, "976" for the United Kingdom, and "975" for Australia and New Zealand

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Registrant Element**

- The second part of the ISBN, which identifies the publisher or distributor of the publication
- Can be a single publisher or a group of publishers with a common prefix

---
<style scoped>p,li {font-size:0.96em}</style>

 # English Language Pattern

- The pattern for the ISBN-10 and ISBN-13 codes is different for books published in the United Kingdom and Ireland, due to the use of the "+" symbol instead of the space character

---
<style scoped>p,li {font-size:0.92em}</style>

 # Check Digits

- The check digits are calculated using a formula based on the prefix, registrant number, and country code
- Used to ensure that the ISBN is unique and valid

---
<style scoped>p,li {font-size:0.96em}</style>

 # ISBN-10 Check Digits

- Calculated using the formula: (Prefix x Registrant Number) + (Country Code x Check Character)

---
<style scoped>p,li {font-size:0.96em}</style>

 # ISBN-13 Check Digit Calculation
- Calculated using the formula: (Prefix x Registrant Number x Country Code) modulo 11


---
<style scoped>p,li {font-size:0.96em}</style>

 # ISBN-10 to ISBN-13 Conversion
- To convert an ISBN-10 to an ISBN-13, simply add a "978" prefix to the front of the ISBN-10 code


---
<style scoped>p,li {font-size:0.92em}</style>

 # Errors in Usage

- Common errors in using ISBNs include using invalid or already-assigned numbers, or omitting hyphens in the code
- These errors can cause confusion and delays in the supply chain

---
<style scoped>p,li {font-size:0.92em}</style>

 # _eISBN_

- An electronic version of the ISBN, used for digital publications such as e-books and online resources
- Similar to the traditional ISBN, but with a unique identifier for each digital publication

---
<style scoped>p,li {font-size:0.92em}</style>

 # EAN Format Used in Barcodes
- The EAN (European Article Number) format is used in barcodes for all types of products, including books and other media
- The EAN code consists of a prefix, an item number, and a check digit


---
<style scoped>p,li {font-size:0.92em}</style>

 # Upgrading
- Publishers can upgrade their existing ISBNs to ISBN-13 format to ensure compatibility with modern supply chain systems
- This process involves changing the ISBN-10 code to an ISBN-13 code by adding a "978" prefix and modifying the check digit calculation


---
<style scoped>p,li {font-size:0.92em}</style>

 # Explanatory Notes

- These additional notes provide further clarification and details on the use of ISBNs and the conversion process
- Can be useful for publishers, booksellers, and other industry professionals who need to understand the specific requirements and best practices for using ISBNs.