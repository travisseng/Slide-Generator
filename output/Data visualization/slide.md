---
marp: true
math: katex
theme: gaia
paginate: True
style: |
   @import url('https://unpkg.com/tailwindcss@2.2.19/dist/utilities.min.css');
   section {display: flex;flex-flow: column; font-size:35px; letter-spacing:1.4px;}

   header {overflow:visible} header > img.logo {position:absolute; right:15px;}

   header > img.logo {position:absolute; right:15px;}


---
<!-- backgroundColor: white -->
<!-- _class: lead -->

 # Data visualization

---
<style scoped>p,li {font-size:0.80em}</style>

 # Overview
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Data_visualization_process_v1.png/330px-Data_visualization_process_v1.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Internet_map_1024.jpg/240px-Internet_map_1024.jpg'/>
</div>
</div>

</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Definition of data visualization
- Importance of data visualization in today's data-driven world
- Brief history of data visualization
</div>

</div>


---
<style scoped>p,li {font-size:0.88em}</style>

 # Principles

- Key principles of effective data visualization
- Clarity, simplicity, and precision
- Avoid 3D and unnecessary embellishments

---
<style scoped>p,li {font-size:0.80em}</style>

 # **Characteristics of Effective Graphical Displays**
- Visual encoding (using color, shape, size)
- Labeling and annotation
- Scales and granularity
- Overall design and aesthetics
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Minard.png/440px-Minard.png'/>
</div>
</div>


---
<style scoped>p,li {font-size:0.80em}</style>

 # _Quantitative Messages_
<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Total_Revenues_and_Outlays_as_Percent_GDP_2013.png/390px-Total_Revenues_and_Outlays_as_Percent_GDP_2013.png'/>
</div>
<div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/U.S._Phillips_Curve_2000_to_2013.png/330px-U.S._Phillips_Curve_2000_to_2013.png'/>
</div>
</div>

- Charts and graphs for numerical data
- Bar charts, line charts, scatter plots
- Interpreting trends and patterns

---
<style scoped>p,li {font-size:0.88em}</style>

 # Visual Perception and Data Visualization
- Human visual perception limitations
- Importance of color, typography, and layout
- Using white space effectively


---
<style scoped>p,li {font-size:0.88em}</style>

 # Human Perception/Cognition and Data Visualization
- Cognitive processes involved in data visualization
- Attention, comprehension, retention
- Designing for user needs and goals


---
<style scoped>p,li {font-size:0.72em}</style>

 # **History**
- Early history of data visualization (e.g., Florence Nightingale's rose diagram)
- Evolution of data visualization tools and techniques
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


---
<style scoped>p,li {font-size:0.92em}</style>

 # Terminology
- Common terms in data visualization (e.g., "dataviz," "infographic")
- Distinguishing between different types of visualizations (e.g., bar chart, heatmap)


---
<style scoped>p,li {font-size:0.92em}</style>

 # Techniques
- Overview of popular data visualization techniques (e.g., scatter plots, Sankey diagrams)
- When to use each technique


---
<style scoped>p,li {font-size:0.92em}</style>

 # Other Techniques
- Advanced and specialized data visualization techniques (e.g., Gauge charts, Treemaps)
- Tools and software for creating these visualizations


---
<style scoped>p,li {font-size:0.92em}</style>

 # Interactivity

- Importance of interactivity in modern data visualization
- Using interactive elements like filters, drill-downs, and animations

---
<style scoped>p,li {font-size:0.88em}</style>

 # Other Perspectives

- Data visualization as a form of storytelling
- Visualizing non-quantitative data (e.g., text, images)
- Integrating data visualization into presentations and reports

---
<style scoped>p,li {font-size:0.92em}</style>

 # Applications

- Real-world applications of data visualization in various fields (e.g., business, healthcare, sports)
- Examples of effective data visualizations in action

---
<style scoped>p,li {font-size:0.92em}</style>

 # **Organization**

- Importance of organization in data visualization
- Creating a clear and logical structure for your visualization

---
<style scoped>p,li {font-size:0.88em}</style>

 # Data Presentation Architecture
<div style='flex:1 1 auto; min-height:0;' class="grid grid-cols-8 gap-4">
<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

- Overview of data presentation architecture components (e.g., header, body, footer)
- Best practices for designing a visually appealing and functional data presentation architecture
</div>

<div style='display:flex; flex-flow:column; min-height:0;' class="col-span-4">

<div style="display: flex; flex: 1 1 auto; flex-flow: row; min-height: 0"><div style="display: flex; flex: 1 1 auto; justify-content: center;min-height:0;min-width:0; margin-bottom:0.1em;;margin-right:0.15em">
<img style='object-fit: contain; max-height:100%; max-width:100%; background-color: rgba(0,0,0,0);' src='https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Kencf0618FacebookNetwork.jpg/220px-Kencf0618FacebookNetwork.jpg'/>
</div>
</div>

</div>

</div>


---
<style scoped>p,li {font-size:0.92em}</style>

 # Objectives
- Defining clear objectives for your data visualization project
- Ensuring your visualization effectively communicates your message


---
<style scoped>p,li {font-size:0.92em}</style>

 # Scope
- Determining the scope of your data visualization project
- Identifying the key stakeholders and their needs


---
<style scoped>p,li {font-size:0.92em}</style>

 # Related Fields
- Other fields related to data visualization (e.g., information design, human-computer interaction)
- How these fields contribute to the broader field of data visualization


---
<style scoped>p,li {font-size:0.92em}</style>

 # Notes

- Summary of key takeaways from the presentation
- Additional resources for further learning and exploration

---
<style scoped>p,li {font-size:0.92em}</style>

 # _References_

- List of sources used in the presentation (e.g., books, articles, websites)

I hope this slide presentation helps you learn more about data visualization!