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

 # _Information visualization_

---
<style scoped>p,li {font-size:0.84em}</style>

 # Overview
- Information visualization is the process of creating visual representations of data to support decision-making and understanding.
- It involves selecting, arranging, and designing graphical displays to effectively communicate information.
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Data_visualization_process_v1.png/330px-Data_visualization_process_v1.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Internet_map_1024.jpg/240px-Internet_map_1024.jpg'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.84em}</style>

 # _Principles_
- The principles of information visualization include:

+ Perception: using knowledge of human perception and cognition to design effective visualizations.

+ Cognition: understanding how people process and understand information.

+ Affordances: designing visualizations that are intuitive and easy to use.


---
<style scoped>p,li {font-size:0.80em}</style>

 # Characteristics of Effective Graphical Displays
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Minard.png/440px-Minard.png'/>
</div>
</div>

- Effective graphical displays should have the following characteristics:

+ Clarity: the display should be clear and easy to understand.

+ Accuracy: the display should accurately represent the data.

+ Relevance: the display should only include information that is relevant to the task at hand.

---
<style scoped>p,li {font-size:0.76em}</style>

 # Quantitative Messages
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Total_Revenues_and_Outlays_as_Percent_GDP_2013.png/390px-Total_Revenues_and_Outlays_as_Percent_GDP_2013.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/U.S._Phillips_Curve_2000_to_2013.png/330px-U.S._Phillips_Curve_2000_to_2013.png'/>
</div>
</div>

- Quantitative messages are used to convey numerical information, such as trends, patterns, and relationships.
- Examples of quantitative messages include:

+ Bar charts and histograms for showing distribution of data.

+ Line charts for showing trends over time.

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Visual Perception and Data Visualization**

- Visual perception is the study of how people perceive and process visual information.
- Understanding visual perception is important for designing effective data visualizations.

---
<style scoped>p,li {font-size:0.92em}</style>

 # _Human Perception/Cognition and Data Visualization_

- Human perception and cognition are critical factors in designing effective data visualizations.
- Designers must consider how people process and understand information to create displays that are intuitive and easy to use.

---
<style scoped>p,li {font-size:0.72em}</style>

 # History
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- The history of information visualization can be traced back to the earliest forms of visual representation, such as cave paintings and diagrams.
- In the modern era, computer-based tools have made it possible to create complex and dynamic visualizations.
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/50_years_of_datavisulization_berengueres_own_work.png/220px-50_years_of_datavisulization_berengueres_own_work.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/ProductSpaceLocalization.png/220px-ProductSpaceLocalization.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Benin_English.png/250px-Benin_English.png'/>
</div>
</div>
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Mouvement_des_plan%C3%A8tes_au_cours_du_temps.png/330px-Mouvement_des_plan%C3%A8tes_au_cours_du_temps.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Playfair_TimeSeries.png/330px-Playfair_TimeSeries.png'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.84em}</style>

 # Terminology

- Key terms in information visualization include:

+ Data visualization: the process of creating visual representations of data.

+ Information architecture: the organization and structure of information.

+ User experience (UX): the way users interact with and perceive a system or product.

---
<style scoped>p,li {font-size:0.84em}</style>

 # Techniques
- Common techniques used in information visualization include:

+ Charts and graphs for showing numerical data.

+ Maps and geospatial visualizations for showing spatial data.

+ Network diagrams for showing relationships between objects.


---
<style scoped>p,li {font-size:0.84em}</style>

 # **Other Techniques**

- Other techniques used in information visualization include:

+ Interactive visualizations that allow users to explore the data in different ways.

+ Animated visualizations that show changes over time.

+ Virtual reality (VR) and augmented reality (AR) for immersive experiences.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Interactivity

- Interactivity is a critical aspect of information visualization, allowing users to explore the data in different ways and gain insights.
- Designers must consider how users will interact with the visualization and what feedback they will receive.

---
<style scoped>p,li {font-size:0.84em}</style>

 # **Other Perspectives**
- Other perspectives on information visualization include:

+ Cognitive perspective: focusing on how people process and understand information.

+ Aesthetic perspective: focusing on the beauty and design of the visualization.

+ Technical perspective: focusing on the software and tools used to create the visualization.


---
<style scoped>p,li {font-size:0.84em}</style>

 # **Applications**
- Information visualization has many applications in fields such as:

+ Business: for financial analysis, marketing, and decision-making.

+ Healthcare: for patient data analysis, medical research, and clinical decision-making.

+ Education: for student performance evaluation, curriculum development, and educational research.


---
<style scoped>p,li {font-size:0.92em}</style>

 # Organization

- Effective organization is critical to successful information visualization.
- This includes organizing the data, selecting appropriate visualizations, and designing an effective user interface.

---
<style scoped>p,li {font-size:0.88em}</style>

 # Data Presentation Architecture
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- The data presentation architecture refers to the structure and organization of the visualization.
- It should be designed to support the user's goals and tasks.
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Kencf0618FacebookNetwork.jpg/220px-Kencf0618FacebookNetwork.jpg'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.84em}</style>

 # Objectives

- The objectives of information visualization are to:

+ Support decision-making and understanding.

+ Enhance comprehension and retention of information.

+ Facilitate collaboration and communication.

---
<style scoped>p,li {font-size:0.92em}</style>

 # Scope
- The scope of an information visualization project should be defined based on the goals and objectives of the project.
- It should include all of the relevant data and stakeholders.


---
<style scoped>p,li {font-size:0.84em}</style>

 # **Related Fields**

- Other fields related to information visualization include:

+ Data science: the process of collecting, analyzing, and interpreting large amounts of data.

+ Information technology (IT): the use of computer systems and software to manage and analyze data.

+ User experience (UX) design: the process of creating user interfaces that are intuitive and easy to use.

---
<style scoped>p,li {font-size:0.80em}</style>

 # Notes

- Key considerations for effective information visualization include:

+ Clarity and accuracy of the display.

+ Relevance of the data to the task at hand.

+ User experience and interaction design.
- The field of information visualization is constantly evolving, with new techniques and tools being developed all the time.