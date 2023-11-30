# CMP-120 Intro to Programming Study Guide

This repository contains a series of challenges which will help you to learn / practice your python skills. It is intended to be used as a study guide for our Final Exam / Interviews, to be held in room **309A of the Jennie King Mellon Library.** You should have received an invitation to attend this; let me know if you did not or if the time will not work for you.

# Topics which are in bounds for the Final

* modules and import statements
* defining and calling functions
  * parameters
  * docstrings
  * type hints
* if statements
* loops
  * for
  * while
  * break (not a type of loop, but something you can do within one)
* strings
  * formatting them (for example, with f-strings)
  * splitting, parsing them
  * accessing individual letters with e.g. my_string[4]
* Graphics libraries
  * [CMU Graphics](https://academy.cs.cmu.edu)
  * [Processing](https://py.processing.org)
* Lists
  * Creating / declaring them  
  * iterating through them
  * append()
  * getting the length
* Dictionaries
  * Creating / declaring them
  * iterating through the (by key)
  * getting the length
  * adding items into them
  * retrieveing items from them
* Classes
  * Defining them
  * Adding and calling methods
  * Adding and referencing data properties
* Operators
  * arithmetic: + - / * // % **
  * assignment: =
  * comparison: == < > <= >=
* Common library functions
  * print()
  * len()
  * help()
  * round()
  * abs()
* Basic mathematical concepts
  * factors, modulo division
  * basic trigonometric functions (sine and cosine should suffice)
  * prime numbers
 
# Sample Questions
Here are the questions we have worked on in class

## Is this list sorted?
Write a python function which can accept a list and returns True if the list is in order, and False if it is not.

## Duck-Duck-Goose
Please write a function in Python which will accept an integer *N*,
and return a string which has N copies of the word "duck" followed
by a single "goose".

## Modeling a Company
You are in charge of building a system to model the growth of small businesses for a research project.

The research project is concerned with studying the effects of increased education rates among the general population, and how that affects their employability.

I want you to design a python class which represents a company/business to be used in a simulation.

Your company will probably need to express adding and removing employees, earning revenue, taking on debt, and any of the other basic properties of a business.

You do not need to provide an implementation for any methods, just list them. 

### Company Initializer
Write the `__init__()` method for your class

## Is this a Palindrome?
I need you to write a function which accepts a string and returns True if that string is a palindrome, otherwise return False.

A palindrome is a string which is the same forwards and backwards:

|If I pass: |   Function should return: |
|---|---|
|RADAR |        True|
|COMBAT |        False|
|SEES |         True|
|DOSE |         False|

For bonus, what if I asked you to ignore case? Or punctuation?
|Radar |        True|

### a few helpful hints:
* `len("twice")` is 5
* `"brine"[1]` is "r"
* `"slips"[0]` is "s"
* `"epidural"[20]` is None

## 

