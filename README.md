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
  
- [1. About The Project](#1-about-the-project)
- [2. Project Description](#2-project-description)
  * [Background](#background)
  * [Project Questions](#project-questions)
  * [QR Data](#qr-data)
- [3. Function Descriptions](#3-function-descriptions)
  * [Question 0: Calculate the length of a visit](#question-0-calculate-the-length-of-a-visit)
  * [Question 1: Determine whether two visits overlapped](#question-1-determine-whether-two-visits-overlapped)
  * [Question 2: Determine whether two individuals were in contact](#question-2-determine-whether-two-individuals-were-in-contact)
  * [Question 3: Forward contact tracing](#question-3-forward-contact-tracing)
  * [Question 4: Backward contact tracing](#question-4-backward-contact-tracing)
  
</details>

## 1. About The Project
This was the first project for COMP10001 (Foundations of Computing) at the University of Melbourne. Descriptions for various functions were provided via Grok Learning and checked against various inputs. The <a href="#project-description">Project Description</a> and <a href="#function-descriptions">Function Descriptions</a> will be below. <b> Final mark: 96% </b>

<p align="right">(<a href="#top">back to top</a>)</p>

## 2. Project Description
### Background
Contact tracing is an important measure used to control outbreaks of infectious diseases such as COVID-19.

When a person infected with the disease is detected (known as an index case), they are asked to isolate (avoid contact with others) to prevent them from infecting other people. In addition, recent contacts of the index case are traced and asked to quarantine (avoid contact with others) for a period of time, just in case they were infected by the index case.

The contacts of an index case can be identified by interview, but this can be time consuming and error prone. During COVID-19, Australia and other countries have used digital approaches to contact tracing. One such digital approach involves asking people to use QR codes to "sign in" to public locations (shops, restaurants, museums, etc) they visit. The data collected in this way can then be analysed to help public health officials find out which other people may have been potential contacts of an infected index case.

Note that while the contact tracing scenario and strategies described, accurately depict what happens in the real world, the assumptions about disease spread, the QR code data format, and the approaches to data analysis have been created for the purpose of this project. In particular, there has been considerable debate about how such data can be collected in a way that enables it to be used to help aid outbreak control, while also preserving individual privacy. While of great interest, this project does not explore these issues!

  <hr></hr>
  
### Project Questions

In this project, we will look at a number of questions relating to contact tracing and will write code to analyse (simulated) data such as might be produced by a digital contact tracing system. We will also compare two different strategies for contact tracing, known as "forward" and "backward" contact tracing.

Question 0: Calculate the length of a visit.

Question 1: Determine whether two visits overlapped.

Question 2: Determine whether two individuals were in contact.

Question 3: Forward contact tracing.

Question 4: Backward contact tracing.

<hr>

### QR Data
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

<p align="right">(<a href="#top">back to top</a>)</p>


## 3. Function Descriptions
### Question 0: Calculate the length of a visit
Write a function `visit_length(visit)` to determine the length of a person's visit to a particular location.

The function takes one argument, visit, which is a 7-tuple formatted as described above.

The function should return the length of the visit as a tuple of integer values, corresponding to hours and minutes if the visit is valid, or None if the visit is not valid. A valid visit is one with a positive length (ie, more than zero minutes).

For example,
```
visit_length(("Irene", "Skylabs", 3, 9, 15, 13, 45))

// RESULT: (4, 30)
```
which means that Irene spent 4 hours and 30 minutes at Skylabs from 9:15am to 1:45pm on the third day of the outbreak.

Assumptions:

<ul><li>You can assume that the input arguments are syntactically correct given the definitions and assumptions on the previous slides.</li></ul>

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
<hr>

### Question 1: Determine whether two visits overlapped
Write a function `contact_event(visit_a, visit_b)` to determine if two visits overlap in time and space, allowing for contact between two people to potentially occur.

The parameters of this function are as follows:

<ul><li>visit_a</li>
  <li>visit_b</li></ul>

each of which is a 7-tuple formatted as described above.

The function should return True if a contact could have occurred between two distinct people, and False otherwise. If one visit began at the exact time that the other visit ended, you may assume that a potential contact could not occur (ie, the function should return False). If either of the visits is not valid, the function should return None.

Assumptions:

<ul><li>You can assume that the input arguments are syntactically correct given the definitions and assumptions on the previous slides.</li></ul>

Here are some example calls to the function:
```
>>> print(contact_event(('Russel', 'Foodigm', 2, 9, 0, 10, 0), ('Natalya', 'Foodigm', 2, 9, 30, 9, 45)))
True

>>> print(contact_event(('Russel', 'Foodigm', 2, 9, 0, 10, 0), ('Natalya', 'Foodigm', 2, 10, 0, 10, 20)))
False

>>> print(contact_event(("Natalya", 'Foodigm', 2, 9, 30, 9, 45), ('Chihiro', 'Foodigm', 2, 8, 45, 9, 15))) # there is no time overlap
False

>>> print(contact_event(('Russel', 'Foodigm', 2, 9, 0, 10, 0), ('Aravinda', 'Afforage', 2, 9, 0, 10, 0))) # the two visit were to different locations
False

>>> print(contact_event(('Russel', 'Foodigm', 2, 9, 0, 10, 0), ('Russel', 'Foodigm', 2, 8, 30, 9, 0))) # the two visits are by the same person
False

>>> print(contact_event(('Russel', 'Foodigm', 2, 9, 0, 10, 0), ('Natalya', 'Afforage', 2, 15, 10, 14, 45))) # one of the visits is invalid
None
```

<hr>

### Question 2: Determine whether two individuals were in contact

Write a function `potential_contacts(person_a, person_b)` that identifies all of the potential contacts between two people, given data on their movement over multiple days.

The function takes the following arguments,

<ul><li>person_a </li>
<li>person_b</li></ul>

which are each lists of visits by the two people, with each visit formatted as a 7-tuple as described above.

The function should return a tuple consisting of:

<ul><li>a set of potential contact locations and times for these two people, each in the form of a 6-tuple (see below; note that the order of the items in this set does not matter, as a set does not store order); and</li>
<li>a 2-tuple containing a pair of integer values (hours and minutes) corresponding to the total duration of potential contact between these two people.</li></ul>

Note that each the potential contact locations and time in the returned set is a 6-tuple rather than a 7-tuple because it will not include the ID of an individual. It also differs from the 7-tuple described above in that the times referred to, are not the time at which a person arrived at and departed from a location, but rather the time at which the two people started being at the same location (ie, when the second person arrive) and the time at which the two people stopped being at the same location (ie, when the first person left).

For example, if the original visit 7-tuples were:
```
("Natalya", "Nutrity", 2, 10, 10, 11, 45)
```
and:
```
("Chihiro", "Nutrity", 2, 9, 45, 11, 30)
```
then the 6-tuple corresponding to the potential contact between Natalya and Chihiro would be:
```
("Nutrify", 2, 10, 10, 11, 30)
```
indicating that they were both located at Nutrity on the second day of the outbreak between 10:10am and 11:30am.

Assumptions:

<ul><li>You can assume that the input arguments are syntactically correct given the definitions and assumptions on this slide and on previous slides.</li>
<li>Any invalid visits should be ignored. Contact locations and times should only be generated for pairs of valid visits.</li></ul>

Here are some example calls to your function:
```
>>> potential_contacts([('Russel', 'Foodigm', 2, 9, 0, 10, 0), ('Russel', 'Afforage', 2, 10, 0, 11, 30), ('Russel', 'Nutrity', 2, 11, 45, 12, 0), ('Russel', 'Liberry', 3, 13, 0, 14, 15)], [('Natalya', 'Afforage', 2, 8, 15, 10, 0), ('Natalya', 'Nutrity', 4, 10, 10, 11, 45)])
(set(), (0, 0))

>>> potential_contacts([('Russel', 'Foodigm', 2, 9, 0, 10, 0), ('Russel', 'Afforage', 2, 10, 0, 11, 30), ('Russel', 'Nutrity', 2, 11, 45, 12, 0), ('Russel', 'Liberry', 3, 13, 0, 14, 15)], [('Chihiro', 'Foodigm', 2, 9, 15, 9, 30), ('Chihiro', 'Nutrity', 4, 9, 45, 11, 30), ('Chihiro', 'Liberry', 3, 12, 15, 13, 25)])
({('Foodigm', 2, 9, 15, 9, 30), ('Liberry', 3, 13, 0, 13, 25)}, (0, 40))

>>> potential_contacts([('Natalya', 'Afforage', 2, 8, 15, 10, 0), ('Natalya', 'Nutrity', 4, 10, 10, 11, 45)], [('Chihiro', 'Foodigm', 2, 9, 15, 9, 30), ('Chihiro', 'Nutrity', 4, 9, 45, 11, 30), ('Chihiro', 'Liberry', 3, 12, 15, 13, 25)])
({('Nutrity', 4, 10, 10, 11, 30)}, (1, 20))

>>> potential_contacts([('Russel', 'Foodigm', 2, 9, 0, 10, 0), ('Russel', 'Afforage', 2, 10, 0, 11, 30), ('Russel', 'Nutrity', 2, 11, 45, 12, 0), ('Russel', 'Liberry', 3, 13, 0, 14, 15)], [])  # person with no visits
(set(), (0, 0))
```

<hr>

### Question 3: Forward contact tracing

Write a function `forward_contact_trace(visits, index, day_time, second_order=False)` that identifies all potential contacts of a detected index case that occurred after the time that they were detected. These are the people who will be contacted by public health officials to ask them to quarantine until they are sure that they were not infected by the index case.

It is possible that, by the time a contact of an index case has been traced, they may have already infected other people. Therefore, public health officials may wish to be very cautious and also trace the second order contacts of the index case. That is, the contacts of the contacts of the original detected case.

The function takes the following parameters:
<ul><li>visits is a list of visits, with each visit formatted as a 7-tuple as described above;</li>
<li>index is the ID of the detected index case;</li>
<li>day_time is the day and time that the index case was detected, described as a 3-tuple containing the day, as an integer value, and time, as a pair of integer values, corresponding to hours and minutes, in 24 hour time; for example, (2, 15, 35) refers to 3:35pm on day 2 of the outbreak; and</li>
<li>second_order a Boolean flag to indicate whether second order contacts of the index case should be included.</li></ul>

The function should return an alphabetically sorted list of IDs of people who should be traced and asked to quarantine.

For example:
```
>>> visits = [('Russel', 'Nutrity', 1, 5, 0, 6, 0),
           ('Russel', 'Foodigm', 2, 9, 0, 10, 0),
           ('Russel', 'Afforage', 2, 10, 0, 11, 30),
           ('Russel', 'Nutrity', 2, 11, 45, 12, 0),
           ('Russel', 'Liberry', 3, 13, 0, 14, 15),
           ('Natalya', 'Nutrity', 1, 5, 30, 6, 45),
           ('Natalya', 'Afforage', 2, 8, 15, 10, 0),
           ('Natalya', 'Nutrity', 4, 10, 10, 11, 45),
           ('Chihiro', 'Foodigm', 2, 9, 15, 9, 30),
           ('Chihiro', 'Nutrity', 4, 9, 45, 11, 30),
           ('Chihiro', 'Liberry', 3, 12, 15, 13, 25)]

>>> forward_contact_trace(visits, 'Russel', (1, 9, 0))
['Chihiro']
```
The reasoning is as follows:

<ul><li>Russel became infectious at 9am on day 1 of the outbreak.</li>
<li>Russel visited Foodigm between 9am and 10am on day 2 of the outbreak.</li>
<li>Chihiro also visited Foodigm during this time (from 9.15am until 9.45am), during which time she could have been infected by Russel. She should be contact traced and asked to quarantine.</li>
<li>Natalya was not present in the same location at the same time as Russel after he became infectious, so she doesn't need to be contact traced.</li></ul>

On the other hand, for the same list of visit data:
```
>>> visits = [('Russel', 'Nutrity', 1, 5, 0, 6, 0),
           ('Russel', 'Foodigm', 2, 9, 0, 10, 0),
           ('Russel', 'Afforage', 2, 10, 0, 11, 30),
           ('Russel', 'Nutrity', 2, 11, 45, 12, 0),
           ('Russel', 'Liberry', 3, 13, 0, 14, 15),
           ('Natalya', 'Nutrity', 1, 5, 30, 6, 45),
           ('Natalya', 'Afforage', 2, 8, 15, 10, 0),
           ('Natalya', 'Nutrity', 4, 10, 10, 11, 45),
           ('Chihiro', 'Foodigm', 2, 9, 15, 9, 30),
           ('Chihiro', 'Nutrity', 4, 9, 45, 11, 30),
           ('Chihiro', 'Liberry', 3, 12, 15, 13, 25)]

>>> forward_contact_trace(visits, 'Russel', (1, 9, 0), second_order=True)
['Chihiro', 'Natalya']
```

The reasoning begins as above; however:

<ul><li>After being a potential contact of Russel, Chihiro visited Nutrity between 9:45am and 11:30am on day 4 of the outbreak.</li>
<li>Natalya also visited Nutrity during this time (from 10:10am until 11:45am), during which time she could have been infected by Chihiro (had she been infected). As we are now also tracing Russel's second order contacts, she should also be contact traced and asked to quarantine.</li></ul>

Hint: Start by solving the problem of first order contact tracing. Once you have written a function for this, think about how you can make use of it to solve the problem of second order contact tracing. You may wish to use a second function to manage this.

Assumptions:

<ul><li>You can assume that the input arguments are syntactically correct given the definitions and assumptions on this slide and on previous slides.</li>
<li>You are provided with a correct reference version of the function potential_contacts(person_a, person_b) from Question 3.</li></ul>


<hr>

### Question 4: Backward contact tracing

While forward contact tracing can identify other people who may have been infected by the index case, it doesn't consider where the index case themself was infected from.

Backward contact tracing can be used to identify the potential source of the index case's infection by looking back through their recent contact history. Backward contact tracing can be very effective because once this earlier source case is identified, a larger proportion of potentially infected people can be identified by forward tracing each of the source's contacts.

Write a function `backward_contact_trace(visits, index, day_time, window)` that identifies the all potential sources of the specified index case's infection.

The function takes the following parameters:

<ul><li>visits is a list of visits, with each visit formatted as a 7-tuple as described above;</li>
<li>index is the ID of the detected index case;</li>
<li>day_time is the day and time when the index case was detected, as a 3-tuple containing the day, as an integer value, and time, as a pair of integer values, corresponding to hours and minutes, in 24 hour time; for example, (2, 15, 35) refers to 3:35pm on day 2 of the outbreak; and</li>
<li>window is an integer representing the number of days prior to the detection of the index case that backward tracing will be carried out. A window of 1 indicates that all locations visited prior to the time of detection on the same day that the index case was detected will be included. A window of 2 indicates that all locations visited on the previous day will also be included, and so on.</li></ul>

The function should return an alphabetically sorted list of IDs of people who should be traced and tested to identify whether they were the potential source of the index case's infection.

For example:
```
>>> visits = [('Russel', 'Foodigm', 2, 9, 0, 10, 0),
           ('Russel', 'Afforage', 2, 10, 0, 11, 30),
           ('Russel', 'Nutrity', 2, 11, 45, 12, 0),
           ('Russel', 'Liberry', 3, 13, 0, 14, 15),
           ('Natalya', 'Afforage', 2, 8, 15, 10, 0),
           ('Natalya', 'Nutrity', 4, 10, 10, 11, 45),
           ('Chihiro', 'Foodigm', 2, 9, 15, 9, 30),
           ('Chihiro', 'Nutrity', 4, 9, 45, 11, 30),
           ('Chihiro', 'Liberry', 3, 12, 15, 13, 25)]

>>> backward_contact_trace(visits, 'Natalya', (4, 13, 0), 1)
['Chihiro']
```
The reasoning is as follows:

<ul><li>Natalya was detected at 1pm on day 4 of the outbreak, and we want to know who she could have been infected by earlier on the same day (as window=1).</li>
<li>The only location that Natalya had visited on day 4 was Nutrity, between 10:10am and 11:45am.</li>
<li>Chihiro also visited Nutrity at this time (from 9:45am until 11:30am), during which time she could have infected Natalya.</li>
<li>Chihiro should therefore be contact traced and investigated as a potential source of Natalya's infection.</li>
<li>(Additionally, outside of the scope of this problem, if Chihiro does test positive, forward contact tracing should be used to follow up on her other potential contacts!)</li></ul>

As another example:
  
```
>>> visits = [('Russel', 'Foodigm', 2, 9, 0, 10, 0),
           ('Russel', 'Afforage', 2, 10, 0, 11, 30),
           ('Russel', 'Nutrity', 2, 11, 45, 12, 0),
           ('Russel', 'Liberry', 3, 13, 0, 14, 15),
           ('Natalya', 'Afforage', 2, 8, 15, 10, 0),
           ('Natalya', 'Nutrity', 4, 10, 10, 11, 45),
           ('Chihiro', 'Foodigm', 2, 9, 15, 9, 30),
           ('Chihiro', 'Nutrity', 4, 9, 45, 11, 30),
           ('Chihiro', 'Liberry', 3, 12, 15, 13, 25)]

>>> backward_contact_trace(visits, 'Chihiro', (4, 12, 0), 2)
['Natalya', 'Russel']
```
  
The reasoning is as above; however, we are now considering visits that occurred on day 4 (up until 12pm, when Chihiro was detected), and all of day 3 (as window=2). Chihiro and Natalya both visited Nutrity on day 4, and Chihiro and Russel both visited Liberry on day 3. Chihiro may have been infected by either of them.

Assumptions:

<ul><li>You can assume that the input arguments are syntactically correct given the definitions and assumptions on this slide and on previous slides.</li>
<li>You are provided with a correct reference version of the function potential_contacts(person_a, person_b) from Question 3.</li></ul>

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/arsamsamadi/
