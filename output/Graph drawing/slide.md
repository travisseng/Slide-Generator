---
marp: true
math: katex
theme: gaia
paginate: True
style: |
   @import url('https://unpkg.com/tailwindcss@2.2.19/dist/utilities.min.css');
   :root {--color-fg-default: #FFFFFF; --color-foreground: #FFFFFF;}

   section {display: flex;flex-flow: column; font-size:35px; letter-spacing:1.4px;}

   header {overflow:visible} header > img.logo {position:absolute; right:15px;}

   header > img.logo {position:absolute; right:15px;}


---
<!-- backgroundImage: url('backgrounds/aaabstract (9).png') -->
<!-- _class: lead -->

 # Graph drawing

---
<style scoped>p,li {font-size:0.92em}</style>

 # Introduction

- Brief overview of graph drawing and its importance
- Purpose of the presentation

---
<style scoped>p,li {font-size:0.88em}</style>

 # _Graphical Conventions_
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/4node-digraph-natural.svg/110px-4node-digraph-natural.svg.png'/>
</div>
</div>

- Common notation and terminology used in graph theory
- Key components of a graph (vertices, edges, weights)

---
<style scoped>p,li {font-size:0.72em}</style>

 # Quality Measures
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Overview of different quality measures used to evaluate graph drawings
- Examples include:

+ Graph distance

+ Edge length

+ Vertex degree

+ Clustering coefficient
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/4node-digraph-embed.svg/110px-4node-digraph-embed.svg.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.72em}</style>

 # _Layout Methods_
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Social_Network_Analysis_Visualization.png/220px-Social_Network_Analysis_Visualization.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Goldner-Harary-linear.svg/220px-Goldner-Harary-linear.svg.png'/>
</div>
</div>

- Overview of popular layout methods for graph drawing, including:

+ Force-directed layout

+ Spectral layout

+ Grid-based layout

+ Spring-electrical layout

---
<style scoped>p,li {font-size:0.84em}</style>

 # Application-Specific Graph Drawings
- Examples of graph drawings tailored to specific applications, such as:

+ Web page layouts

+ Social network visualizations

+ Traffic flow maps


---
<style scoped>p,li {font-size:0.76em}</style>

 # Software
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Gephi_0.9.1_Network_Analysis_and_Visualization_Software.png/220px-Gephi_0.9.1_Network_Analysis_and_Visualization_Software.png'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Overview of popular software tools for graph drawing, including:

+ Gephi

+ NetworkX

+ Graphviz

+ Cytoscape
</div>

</div>


---
<style scoped>p,li {font-size:0.96em}</style>

 # Footnotes
- Additional resources and references for further reading on graph drawing


---
<style scoped>p,li {font-size:0.88em}</style>

 # Conclusion
- Summary of key points covered in the presentation
- Final thoughts on the importance of graph drawing in various fields

Here's a brief description of each slide:


---
<style scoped>p,li {font-size:1.00em}</style>

 # Introduction - This slide provides an overview of the presentation and its purpose. It sets the stage for the rest of the slides.


---
<style scoped>p,li {font-size:1.00em}</style>

 # Graphical Conventions - This slide covers common notation and terminology used in graph theory, as well as key components of a graph (vertices, edges, weights).


---
<style scoped>p,li {font-size:1.00em}</style>

 # Quality Measures - This slide discusses different quality measures used to evaluate graph drawings, such as graph distance, edge length, vertex degree, and clustering coefficient.


---
<style scoped>p,li {font-size:1.00em}</style>

 # _Layout Methods - This slide covers popular layout methods for graph drawing, including force-directed layout, spectral layout, grid-based layout, and spring-electrical layout._


---
<style scoped>p,li {font-size:1.00em}</style>

 # Application-Specific Graph Drawings - This slide provides examples of graph drawings tailored to specific applications, such as web page layouts, social network visualizations, and traffic flow maps.


---
<style scoped>p,li {font-size:1.00em}</style>

 # Software - This slide overviews popular software tools for graph drawing, including Gephi, NetworkX, Graphviz, and Cytoscape.


---
<style scoped>p,li {font-size:1.00em}</style>

 # Footnotes - This slide provides additional resources and references for further reading on graph drawing.


---
<style scoped>p,li {font-size:0.96em}</style>

 # Conclusion - This slide summarizes key points covered in the presentation and provides final thoughts on the importance of graph drawing in various fields.

I hope this helps! Let me know if you have any questions or need further clarification.
