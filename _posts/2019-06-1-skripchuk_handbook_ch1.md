---
layout: post
author: James Skripchuk
title: "SHoCHoCER: Ch1"
excerpt: "TLDR: I'm going to be going through the The Cambridge Handbook of Computing Education Research and I'm taking all of you along for the ride."
---

# **Meta: What is all this about?**

Recently I've been wanting to pivot my career into research in Computing Education and Educational Data Mining. After finding Andrew Ko's [cheatsheet](https://faculty.washington.edu/ajko/cer) on computing education research, I decided to impulse buy [The Cambridge Handbook of Computing Education Research](https://www.cambridge.org/core/books/cambridge-handbook-of-computing-education-research/F8CFAF7B81A8F6BF5C663412BA0A943D) to get an overview of the field.

I decided that I'll post my notes here, but they're no substitution for reading the book itself! [Go get it!](https://www.amazon.com/Cambridge-Computing-Education-Handbooks-Psychology/dp/1108721893)

**SHoCHoCER** stands for *The Skripchuk Handbook of the Cambridge Handbook of Computing Education Research*. I like to pronounce it *Show Choker*.

---
---


# **The Scope of CER**

What **tools** can we design and use to help further computing education?

What are the **objectives** of teaching computing?

How can we **evaluate** the effectiveness of teaching computing?


---

# **Early History (1960s-1980s)**


Before the dawn of the PC. No mice, no GUI.

Early Question:
***Why is programming difficult to learn?***


## **Miller (1975)**

Many beginners have trouble with **translation**.

**Translation** - Turning a problem statement into a format more suitable for code. 

An example of translation would be turning the problem statement of *"Put red things into Box 1"* into *"IF THING IS RED PUT IN BOX 1"*

Beginners tended to start with specific instances of a problem rather than the general case.

## **Youngs (1974)**
Novice's errors were based more around a language's syntax and quirks. 

*"Many syntax errors arose from novices overgeneralizing the syntactic rules of the language."*

**Can we design programming languages that are easier to learn?**


## **Other Early Studies**

Many studies on how beginners parse conditional statements.

Tested two different facets:

**Sequence Information** - Given a set of conditions, what will a program do?

**Taxon Information** - What set of conditions will cause a program to reach a certain point?

Novices look at "surface form" of the code, while experts look at the underlying structure. (Common across novices and experts of all disciplines)

---

# **Learning Programming**

Two main camps:
* Learning something else through programming to
facilitate a deeper understanding of other subjects (such as math or science)

Early languages such as Logo and Solo.

* Learning Programming for the Sake of Programming

Early languages such as AID and Pascal were designed for novices. *(TIL Pascal was the language of the first APCS exam)*

Across many languages, novices would assume the computer would "figure out what they had meant to say" (The **Superbug**)

---

# **Research on Teaching Methods**

How low-level should we start students? Teach them on a high-level language or an assembler?

Use flow charts as a learning aid? Brooks (1978) found that a variable dictionary (an annotated list of variables in a program) provided more effective assistance than a flowchart.

Group and pair programming produced more favorable attitudes towards programming.

---

# **Redesigning the Learner's interface**

The way programming is presented to a learner dramatically affects their capabilities.

Smalltalk started the trend with multiple fonts, windows, and a mouse pointer. Smalltalk was used for kids to program music and animations.

Boxer used boxes to represent data and procedures. References to variables and argument bindings were now concrete boxes with visible values. (Great granddaddy of block based languages today such as Scratch)

**Physical Programming** - Real world robots/toys that can be programmed.

---

# **Education Research Begins**

Research shifts from *small-scale lab settings* to *long term evaluations of educational cohorts*.

A study of 8-10 year old children learning Logo over a year, they found that children were *no better at a planning task* at the end of a year than children who had not learned Logo. (Pea, Kurland, Hawkins, 1985)

**Above study is debated**: might have been too early in the field to make solid conclusions.

*Should teaching programming improve the classroom, or transform it into something different?*

*Should we use traditional methods of education research, or do we need new methods for computing education research?*

## **Knowledge Transfer**

*"Knowledge transfer occurs when a transferable skill was made explicit, rather than hoping it would be learned passively"* (Carver, 1986)

---

# **The Role of Cognitive Science**

**Phenomenography** - The qualitatively different ways people think and experience something. (Programming Qualia?)


---
# **Research Questions**

*Developing a mental model of what a computer is doing when it executes a program*

**Beacons** - Lines of code which serve as typical indicators of a particular structure or operation. Assisted experts better than novices to recall programs they have studied (Wiedenbeck 1986)

**Tutors** - Error diagnostic systems. Able to guide students step by step. Helped learners to master simple programming more quickly than other methods. (Research idea?)

**Superbug** - The false idea that a computer will "just know" what you're trying to do.

**Procedural Literacy** - The ability to explain a problem in a simple structured manner so that it can be implemented by a machine.

## **The Role of GUIs**

GUIs and Physical interfaces might have counterintuitively increased complexity. 

Students don't know what their programs did or where their programs were stored. (Don't program in a void?)

## **Programming as a notation for thinking**

Human language dramatically changed society and how we act, so what's to say computer languages will be any different. (Computational Thinking gang!)

Programming could lead to different kinds of understanding in the maths and sciences, rather than pen and paper methods.

## **Graphical Languages**
Write programs sooner

Less conditional and iteration errors

Block based languages can transfer knowledge to more text based languages

## **Representing Execution**
Does animation of algorithms make it easier to understand?

Objectives:
Provide new insight? Support debugging?

Sorva (2012)

*"In general, there is little evidence that viewing algorithm animations leads to improved learning about the animations."* pg. 28 (Possible typo? Should the last word 'animations' be algorithms?)

---

# **Conclusions**

Not enough work done on minority students, different genders, socioeconomic status, and learning disabilities.

---
---

# **My Thoughts**

Lots of interesting stuff here. One of the most interesting things is the distinction between **Sequence Information** and **Taxon Information**. I feel like a good understanding of these two concepts leads to a successful software engineer and debugger, so I'm glad to see someone already codified those ideas.

I've already seen the idea that novice's only look at the surface form of a problem while the experts only look at the underlying structure. I remember reading a book on education where they gave physics problems to students and physics teachers. Students would classify them on the surface features (box on a plane, rolling ball, lifting weights), while the physics teachers would classify them on what physics concepts were used to solve them (work-energy theorem, kinematic equations, etc.)

I took a cognitive science class my Freshman year, so I was really surprised to see it show up in here. But after thinking about it for a while, I really shouldn't be surprised due to the very nature of that field. In that class we talked a lot about how information is represented and such, which seems right at place.

I'm bummed that it says that viewing animations doesn't seem to help that much when learning algorithms. I'm a big fan of highly visual explanation series like [3blue1brown's fantastic series on linear algebra](https://www.youtube.com/watch?v=kjBOesZCoqc). Part of me thinks this has to due with a lack of interactivity. Possible research topic?




