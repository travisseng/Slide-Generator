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

 # Manifest covariance

---
<style scoped>p,li {font-size:0.92em}</style>

 # Introduction

- Brief overview of Manifest Covariance
- Importance of understanding this concept in software development

---
<style scoped>p,li {font-size:0.92em}</style>

 # Definition of Manifest Covariance

- Definition: "the degree to which two types are related, as measured by the number of common subtypes they have."
- Explanation of how this definition applies to software development

---
<style scoped>p,li {font-size:0.92em}</style>

 # Types of Covariance
- Declared Covariance: when a type parameter is declared as a supertype of another type parameter
- Inferred Covariance: when a type parameter is inferred as a supertype of another type parameter based on the context of the program


---
<style scoped>p,li {font-size:0.92em}</style>

 # Examples of Manifest Covariance

- Example 1: Using declared covariance to define a generic class with a type parameter that can be used as either a supertype or a subtype
- Example 2: Using inferred covariance to define a generic method that can work with different types of collections

---
<style scoped>p,li {font-size:0.88em}</style>

 # **Benefits of Manifest Covariance**

- Allows for more flexible and modular code design
- Enables the use of generic classes and methods with a wider range of type arguments
- Improves the readability and maintainability of code by reducing the need for explicit type casts and checks

---
<style scoped>p,li {font-size:0.88em}</style>

 # Challenges of Manifest Covariance
- Can lead to more complex and difficult-to-understand code if not used carefully
- Requires a good understanding of the concept and its implications in order to use effectively
- Can be challenging to debug and diagnose issues that arise from manifest covariance


---
<style scoped>p,li {font-size:0.88em}</style>

 # _Best Practices for Manifest Covariance_
- Use declared covariance when possible, as it is easier to understand and debug
- Use inferred covariance only when necessary, and with careful consideration of the potential implications
- Document all uses of manifest covariance in the code, to make it clear and understandable for other developers


---
<style scoped>p,li {font-size:0.88em}</style>

 # Conclusion
- Manifest covariance is a powerful concept that can improve the flexibility and modularity of software systems
- However, it requires careful consideration and use in order to avoid potential issues and challenges
- By understanding and applying manifest covariance effectively, developers can write more maintainable, flexible, and efficient code.
