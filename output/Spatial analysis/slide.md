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

 # _Spatial analysis_

---
<style scoped>p,li {font-size:0.92em}</style>

 # Introduction

- Brief overview of spatial analysis and its importance in various fields
- Purpose of the presentation: to provide a comprehensive understanding of spatial analysis and its applications

---
<style scoped>p,li {font-size:0.88em}</style>

 # History of Spatial Analysis

- Early beginnings in geography and cartography
- Development of statistical methods for spatial data analysis
- Emergence of geographic information systems (GIS) and remote sensing technology

---
<style scoped>p,li {font-size:0.88em}</style>

 # _Fundamental Issues in Spatial Analysis_
- Definition of space and the challenges of dealing with spatial data
- The importance of considering spatial scale and context
- Common pitfalls in spatial analysis, including the "locational fallacy," "atomic fallacy," and "ecological fallacy"


---
<style scoped>p,li {font-size:0.88em}</style>

 # Spatial Characterization
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Bubonic_plague-en.svg/240px-Bubonic_plague-en.svg.png'/>
</div>
</div>

- Overview of spatial characterization methods, including cluster analysis, discriminant analysis, and principal component analysis
- Examples of how each method can be applied in practice

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Spatial Dependence and Autocorrelation**
- Introduction to the concept of spatial dependence and autocorrelation
- Methods for measuring and modeling spatial autocorrelation, including Moran's I and Geary's C


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Spatial Association and the Second Dimension of Spatial Association**

- Overview of the different types of spatial association, including spatial independence, spatial dependence, and spatial associations
- The concept of the "second dimension of spatial association," which refers to the relationship between two or more spatial phenomena

---
<style scoped>p,li {font-size:0.92em}</style>

 # Scaling in Spatial Analysis
- Importance of scaling in spatial analysis, particularly when dealing with different spatial resolutions and levels of detail
- Examples of scaling methods, including cell size selection and mapping scales


---
<style scoped>p,li {font-size:0.92em}</style>

 # **Sampling in Spatial Analysis**
- Overview of sampling methods for spatial data, including simple random sampling, stratified sampling, and cluster sampling
- Considerations for selecting the appropriate sampling method for a given study


---
<style scoped>p,li {font-size:0.84em}</style>

 # Common Errors in Spatial Analysis

- Discussion of common errors in spatial analysis, including:

+ Locational fallacy: assuming that spatial patterns are representative of the entire area

+ Atomic fallacy: ignoring the spatial context and considering individual units as independent

+ Ecological fallacy: assuming that aggregate patterns are representative of the individuals within the area

---
<style scoped>p,li {font-size:0.84em}</style>

 # Solutions to Fundamental Issues in Spatial Analysis

- Discussion of solutions to the fundamental issues in spatial analysis, including:

+ Considering the spatial context and scale when analyzing data

+ Using appropriate methods for measuring and modeling spatial autocorrelation

+ Accounting for the limitations of spatial sampling and scaling

---
<style scoped>p,li {font-size:0.80em}</style>

 # Geographic Space and Types
- Overview of different types of geographic space, including:

+ Points: a single location on the surface of the Earth

+ Lines: a path or sequence of points in space

+ Polygons: a closed shape or area on the surface of the Earth
- Importance of considering the type of geographic space when analyzing data


---
<style scoped>p,li {font-size:0.84em}</style>

 # _Spatial Data Analysis_
- Overview of different methods for spatial data analysis, including:

+ Spatial interpolation: methods for estimating values at unsampled locations based on sampled data

+ Spatial regression: methods for modeling the relationship between a dependent variable and one or more independent variables in a spatial context

+ Spatial neural networks: methods for analyzing complex spatial patterns using artificial neural networks


---
<style scoped>p,li {font-size:0.80em}</style>

 # Spatial Heterogeneity and Interaction

- Overview of different types of spatial heterogeneity, including:

+ Spatial variability: differences in values across space and time

+ Spatial autocorrelation: the tendency for nearby locations to have similar values

+ Spatial interaction: the influence of one location on another
- Examples of how each type of spatial heterogeneity can be modeled and analyzed

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Geographic Information Systems (GIS) and Hydrospatial Analysis**

- Overview of GIS technology and its applications in spatial analysis
- Introduction to hydrospatial analysis, which involves the study of spatial patterns and processes in aquatic environments

---
<style scoped>p,li {font-size:0.84em}</style>

 # Basic Applications of Spatial Analysis

- Examples of basic applications of spatial analysis, including:

+ Mapping: creating visual representations of spatial data

+ Spatial modeling: using statistical methods to understand spatial patterns and relationships

+ Spatial prediction: using models to predict future spatial patterns or outcomes

---
<style scoped>p,li {font-size:0.84em}</style>

 # **Advanced Operations in Spatial Analysis**
- Examples of advanced operations in spatial analysis, including:

+ Spatial data mining: using machine learning algorithms to discover patterns and relationships in large datasets

+ Spatial decision support systems (SDSS): using GIS and other technologies to support decision-making processes

+ Spatial visualization: using interactive visualizations to explore and understand spatial data


---
<style scoped>p,li {font-size:0.84em}</style>

 # Mobile Geospatial and Hydrospatial Computing
- Overview of mobile geospatial and hydrospatial computing, including:

+ Location-based services (LBS): using GPS technology to provide location-specific information and services

+ Augmented reality (AR): using GPS technology and other sensors to enhance the user's experience with real-world environments

+ Hydrospatial computing: using GIS and other technologies to study and understand aquatic environments


---
<style scoped>p,li {font-size:0.92em}</style>

 # Geographic Information Science and Spatial Analysis

- Overview of geographic information science (GIScience), which involves the study of the use and impact of geospatial technology on society and the environment
- Discussion of how GIScience can inform and improve spatial analysis, including the use of new technologies and methods

---
<style scoped>p,li {font-size:0.84em}</style>

 # Future Directions in Spatial Analysis
- Overview of emerging trends and future directions in spatial analysis, including:

+ Big data analytics: using machine learning algorithms to analyze large datasets

+ Cloud computing: using cloud-based infrastructure to support geospatial analysis and data storage

+ Virtual reality (VR): using immersive technologies to enhance the user's experience with spatial data and environments
