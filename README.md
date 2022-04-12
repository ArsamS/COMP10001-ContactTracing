<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">COMP10001 Contact Tracing</h3>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This was the first project for COMP10001 (Foundations of Computing) at the University of Melbourne. Descriptions for various functions were provided via Grok Learning and checked against various inputs. The <a href="#project-description">Project Description</a> and <a href="#function-descriptions">Function Descriptions</a> will be below.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Project Description

Contact tracing is an important measure used to control outbreaks of infectious diseases such as COVID-19.

When a person infected with the disease is detected (known as an index case), they are asked to isolate (avoid contact with others) to prevent them from infecting other people. In addition, recent contacts of the index case are traced and asked to quarantine (avoid contact with others) for a period of time, just in case they were infected by the index case.

The contacts of an index case can be identified by interview, but this can be time consuming and error prone. During COVID-19, Australia and other countries have used digital approaches to contact tracing. One such digital approach involves asking people to use QR codes to "sign in" to public locations (shops, restaurants, museums, etc) they visit. The data collected in this way can then be analysed to help public health officials find out which other people may have been potential contacts of an infected index case.

Note that while the contact tracing scenario and strategies described, accurately depict what happens in the real world, the assumptions about disease spread, the QR code data format, and the approaches to data analysis have been created for the purpose of this project. In particular, there has been considerable debate about how such data can be collected in a way that enables it to be used to help aid outbreak control, while also preserving individual privacy. While of great interest, this project does not explore these issues!

  <hr>
In this project, we will look at a number of questions relating to contact tracing and will write code to analyse (simulated) data such as might be produced by a digital contact tracing system. We will also compare two different strategies for contact tracing, known as "forward" and "backward" contact tracing.

Question 0: Calculate the length of a visit.

Question 1: Determine whether two visits overlapped.

Question 2: Determine whether two individuals were in contact.

Question 3: Forward contact tracing.

Question 4: Backward contact tracing.
  <hr>
  Each visit by a person to a location results in the following data being generated when they scan a QR code with their phone:
  <ul><li>an ID associated with that person</li>
  <li>an ID associated with the location</li>
  <li>an integer value corresponding to the day (note that this is not a calendar date, but rather increments from "day zero" of the outbreak)</li>
  <li>a pair of integer values, corresponding to the time (hours and minutes, in 24 hour time) that the person arrived at the location</li>
  <li>a pair of integer values corresponding to the time (hours and minutes, in 24 hour time) that the person departed from the location</li></ul>

In this project, we will represent this data in a 7-tuple. For example, the tuple:
```
("Irene", "Skylabs", 3, 9, 15, 13, 45)
```
tells us that Irene visited Skylabs on day 3 of the outbreak, arriving at 9:15am and departing at 1:45pm (ie, 13:45 in 24 hour time).

Another example, the tuple:
```
("Xaiton", "CoffeX", 10, 2, 5, 23, 59)
```
tells us that Xaiton visited CoffeX on day 10 of the outbreak, arriving at 2:05am and departing at 11:59pm. If Xaoitan had stayed past midnight, there would be another entry for day 11, starting at 00:00am.

In this project, you may always assume that these 7-tuples are correctly formatted; that is, they will consist of two strings followed by five non-negative integers. The two values corresponding to hours (indices 3 and 5) will be in the range [0, 23], and the two values corresponding to minutes (indices 4 and 6) will be in the range [0, 59]. Please note: 2am is recorded as 2 rather than 02, and 5 minutes is recorded as 5 rather than 05.

You may assume that all visits are syntactically valid and that no visits for a single person are overlapping in time, although a successive visits may end and start at the same time



## Function Descriptions
### 
Write a function visit_length(visit) to determine the length of a person's visit to a particular location.

The function takes one argument, visit, which is a 7-tuple formatted as described above.

The function should return the length of the visit as a tuple of integer values, corresponding to hours and minutes if the visit is valid, or None if the visit is not valid. A valid visit is one with a positive length (ie, more than zero minutes).

For example,
```
visit_length(("Irene", "Skylabs", 3, 9, 15, 13, 45))

// RESULT: (4, 30)
```
which means that Irene spent 4 hours and 30 minutes at Skylabs from 9:15am to 1:45pm on the third day of the outbreak.

Assumptions:

You can assume that the input arguments are syntactically correct given the definitions and assumptions on the previous slides.

Here are some example calls to the function:
```
>>> print(visit_length(('Russel', 'Foodigm', 2, 9, 0, 10, 0)))
(1, 0)

>>> print(visit_length(('Natalya', 'Foodigm', 2, 9, 30, 9, 45)))
(0, 15)

>>> print(visit_length(('Chihiro', 'Foodigm', 2, 8, 45, 9, 15)))
(0, 30)

>>> print(visit_length(('Aravinda', 'Afforage', 2, 9, 0, 10, 0)))
(1, 0)

>>> print(visit_length(('Chihiro', 'Foodigm', 2, 8, 30, 9, 0)))
(0, 30)

>>> print(visit_length(('Natalya', 'Afforage', 2, 15, 10, 14, 45)))  # the length of the visit is negative
None

>>> print(visit_length(('Aravinda', 'Nutrity', 2, 15, 10, 15, 10)))  # the length of the visit is zero
None
```




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/arsamsamadi/
