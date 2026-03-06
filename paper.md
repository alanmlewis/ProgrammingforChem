---
title: 'Strategy-first Programming Resources: Teaching Chemistry Using Python'
tags:
  - Python
  - chemistry education
  - kinetics
  - green chemistry
  - machine learning
  - physical chemistry
authors:
  - name: Annika Ankersen
    orcid: 0000-0003-0872-7098
    affiliation: 1
  - name: David Pugh
    affiliation: 1
  - name: Alan M. Lewis
    orcid: 0000-0002-3296-7203
    affiliation: 1
affiliations:
 - name: Department of Chemistry, University of York, York, YO
   index: 1
 - name: Institution 2
   index: 2
date: 4 March 2026
bibliography: paper.bib

# Optional fields if submitting to a AAS journal too, see this blog post:
# https://blog.joss.theoj.org/2018/12/a-new-collaboration-with-aas-publishing
aas-doi: 10.3847/xxxxx <- update this with the DOI from AAS once you know it.
aas-journal: Astrophysical Journal <- The name of the AAS journal.
---

# Overview and Origin

These educational resources teach undergraduate students a range of chemical concepts using Python programming as a means to exploring chemical data and simulation, and follow the recently introduced "strategy-first" method to programming instruction [@Lewis2026]. This pedagogical approach begins with code which can be applied to chemical problems students are expected to be familiar with from other parts of the undergraduate course, and teaches only the syntax needed to carry out the goals of the workshop. In practice, this involves providing students with pre-written code and asking them to modify and improve subsections of it, without expecting them to understand every line provided, even by the end of the workshop. This allows programming novices to engage with the programming content of the workshop while always working within a familiar chemical context. This helps the students to see the relevance of the programming to their chemical interests, improving student engagement and outcomes.

These materials were developed over the last three years for delivery to all undergraduate chemistry students at the University of York, and all of the materials provided are now regularly delivered as part of the skills modules in each year of study. Some workshops employ Jupyter notebooks, which at York were hosted on Google Colab but could could equally be delivered through local Jupyter installations; in these cases the code and intructions are included together in the same document. For other workshops students are provided with plain-text Python scripts and are guided through a series of modifications and improvements using a PowerPoint presentation, which has also been included in this resource. The workshops will be outlined later, with a note for each indicating the mode of Python usage.

# Statement of Need

The advantages of strategy-first teaching are outlined in [@Lewis2026], which also highlights the current lack of publicly available teaching resources in that style. This paper aims to provide both off-the-shelf workshops in a range of chemical disciplines for educators to use and adapt, and to serve as a template for this style of programming instruction for educators to follow to develop their own resources.

# Content and Design

The workshops included in this resource cover a wide range of topics, which will be briefly outlined below along with where they are delivered in the York chemistry curriculum. There are many commonalities 

They are designed to be delivered with support from demonstrating staff. In addition, students are encouraged to engage in peer teaching and learning; this allows students with previous programming experience to support those without that prior knowledge, and thanks to the strategy-first design of the workshops students with strong chemistry knowledge can also support their peers regardless of their knowledge of Python, which avoids peer interactions feeling one-sided.


# Mathematics

Single dollars ($) are required for inline mathematics e.g. $f(x) = e^{\pi/x}$

Double dollars make self-standing equations:

$$\Theta(x) = \left\{\begin{array}{l}
0\textrm{ if } x < 0\cr
1\textrm{ else}
\end{array}\right.$$


# Citations

Citations to entries in paper.bib should be in
[rMarkdown](http://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html)
format.

For a quick reference, the following citation commands can be used:
- `@author:2001`  ->  "Author et al. (2001)"
- `[@author:2001]` -> "(Author et al., 2001)"
- `[@author1:2001; @author2:2001]` -> "(Author1 et al., 2001; Author2 et al., 2002)"

# Figures

Figures can be included like this: ![Example figure.](figure.png)

# Acknowledgements

We acknowledge contributions from Brigitta Sipocz, Syrtis Major, and Semyeong
Oh, and support from Kathryn Johnston during the genesis of this project.

# References
