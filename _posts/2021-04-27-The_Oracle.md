---
layout: post
author: James Skripchuk
title: "SCP-320505: The Oracle Machine"
excerpt: "REQUIRED SECURITY CLEARANCE: LEVEL RHO"
---

**Item #**: SCP-320505

**Object Class**: Safe

**Special Containment Procedures**: SCP-320505 is contained in room B-███ at the Foundation technology center, blocked by security level Rho access. SCP-320505 must be air-gapped and not be connected to any sort of internal or external Foundation network. Any sort of interaction with SCP-320505 must take place physically using the system's default I/O, and transferring files must take place over removable USB.

**Description**: Item SCP-320505 is a Gateway GT5034 Media Center Desktop Computer, manufactured sometime around 2006. SCP-320505 has the following hardware:

- AMD Athlon 64 X2 4200+ 
- 2 GB DDR SRAM
- 320GB HDD
- NVIDIA GeForce 6100

SCP-320505 runs off of Windows XP, and is mostly stock in terms of installed programs. However, the main difference is an installed program titled "Sudoku World 1999" (SCP-320505-A). Cross-referencing this across the known list of Foundation software yields no matches.

<div>
   <img class="image" src="/assets/gateway_pc_2.jpg" >
  <p style="text-align: center;"><em>Fig 1. A Gateway GT5034 Media Center Desktop Computer (Not SCP-320505) </em></p>
</div>

***SCP-320505-A***:

At first glance, SCP-320505-A seems like an ordinary computer sudoku game. It has a collection of preset sudoku puzzles, a puzzle generator, and a way for users to create puzzles. The object of interest in SCP-320505-A is the puzzle creation suite. Once a user creates a puzzle, there is an option for the program to attempt to solve the puzzle.

The puzzle solving algorithm is abnormally fast. Extended empirical testing by Foundation computer scientists imply that the time complexity of the solving algorithm is O(n^█), where *n*×*n* is the size of the sudoku board. Since sudoku solving can be reduced to the [exact cover problem](https://en.wikipedia.org/wiki/Exact_cover), this implies that SCP-320505-A can solve problems within NP in Polynomial time, thus possibly implying [P=NP](https://en.wikipedia.org/wiki/P_versus_NP_problem).

Any attempt to reverse engineer the code for SCP-320505-A have failed. Any sort of decompilation (e.g. using [Ghidra](https://ghidra-sre.org/) and in-house foundation tools) results in undecipherable and intractable results.

**History**: SCP-320505 was found at a used technology shop in Seattle sometime in the Summer of 2007. The owners of the shop have no logs or recollection of how SCP-320505 appeared in their stock.

---

**Experimental Logs**

Foundation Computer Scientists have constructed various reductions of common NP problems to Sudoku puzzles in order to test the efficiency of SCP-320505-A.


---

**Test ███-██████**

**Name**: Dr. ███████

**Date**: ██-██-██

**Problem**: Boolean satisfiability problem (SAT). Using Benchmarks from the [2018 SAT Solving Competition](http://www.satcompetition.org/) run by Helsinki University.

**Results**: Using ███ benchmarks in total, final average score of ████████ On par with gold main-track winners using modern hardware.

---
**Test ███-██████**

**Name**: Dr. ███

**Date**: ██-██-██

**Problem**: Protein Folding. Using the [CASP Dataset](https://predictioncenter.org/). Using classical methods previously thought intractable given input size.

**Results**: Final result gives a median free-modelling accuracy with a Global Distance Test of 8█, comparable with [AlphaFold](https://deepmind.com/blog/article/AlphaFold-Using-AI-for-scientific-discovery) results without the heavy training cost of deep-learning.

**Experimenter's Note**: Trying to figure out how to represent protein mechanics as a sudoku puzzle was challenging, but the results are outstanding. SCP-320505 could be a game changer if we find a way to contract it out for bioinformatics research. Think of the possible medicines that could come out of this.

---

**Test ███-██████**

**Name**: Dr. █████

**Date**: ██-██-██

**Problem**: AES Encryption (256-bit)

**Results**: The encoded string was cracked in a total compute time of █ months. Compare that to the theoretical limit of 1 billion *billion* years for standard brute-force algorithms.

**Experimenter's Note**: In *no way* can this SCP-320505 make contact with the outside world without a high amount of foundation security. Essentially, every cryptosystem in the world we know today would be rendered useless. Banks will crumble, and nation state secrets will be all but useless. We need to get serious about quantum cryptography *now*.



