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
#    orcid: 0000-0003-0872-7098
    affiliation: 1
  - name: David Pugh
#    orcid: 0000-0003-0872-7098
    affiliation: 1
  - name: Alan M. Lewis
    orcid: 0000-0002-3296-7203
    affiliation: 1
affiliations:
 - name: Department of Chemistry, University of York, Heslington, York, YO10 5DD
   index: 1
# - name: Institution 2
#   index: 2
date: 4 March 2026
bibliography: paper.bib

# Optional fields if submitting to a AAS journal too, see this blog post:
# https://blog.joss.theoj.org/2018/12/a-new-collaboration-with-aas-publishing
# aas-doi: 10.3847/xxxxx <- update this with the DOI from AAS once you know it.
# aas-journal: Astrophysical Journal <- The name of the AAS journal.
---

# Overview and Origin

These educational resources teach undergraduate students a range of chemical concepts using Python programming as a means to exploring chemical data and simulation, and follow the recently introduced "strategy-first" method to programming instruction [@Lewis2026]. This pedagogical approach begins with code which can be applied to chemical problems students are expected to be familiar with from other parts of the undergraduate course, and teaches only the syntax needed to carry out the goals of the workshop. In practice, this involves providing students with pre-written code and asking them to modify and improve subsections of it, without expecting them to understand every line provided, even by the end of the workshop. This allows programming novices to engage with the programming content of the workshop while always working within a familiar chemical context. This helps the students to see the relevance of the programming to their chemical interests, improving student engagement and outcomes.

These materials were developed over the last three years for delivery to all undergraduate chemistry students at the University of York, and all of the materials provided are now regularly delivered as part of the skills modules in each year of study. Some workshops employ Jupyter notebooks, which at York were hosted on Google Colab but could could equally be delivered through local Jupyter installations; in these cases the code and instructions are included together in the same document. For other workshops students are provided with plain-text Python scripts and are guided through a series of modifications and improvements using a PowerPoint presentation, which has also been included in this resource. The workshops will be outlined later, with a note for each indicating the mode of Python usage.

# Statement of Need

Programming skills are increasing desired by students and expected by employers, especially amongst STEM graduates [@?]. Furthermore, some chemistry concepts can be taught and illustrated through programming workshops in ways which would be impossible the context of a flat lecture or teaching laboratory. Therefore, a number of examples of programming workshops and curricula for chemistry students have been published [@?], including in this journal [@?]. The workshops presented here follow a newly introduced approach to programming instruction called "strategy-first teaching". The advantages of strategy-first teaching are outlined in [@Lewis2026], which also highlights the current lack of publicly available teaching resources in that style. This paper aims to provide both off-the-shelf workshops in a range of chemical disciplines for educators to use and adapt, and to serve as a template for this style of programming instruction for educators to follow to develop their own resources.

# Content and Design

The workshops included in this resource cover a wide range of topics, which will be briefly outlined below along with where they are delivered in the York chemistry curriculum. There are many commonalities between the workshops. In each case, students are provided with a piece of code which can be executed immediately, and runs successfully to produce an output which can be interpreted using students chemical knowledge. The goal of the workshop is then to modify and improve this code, learning the necessary syntax along the way, to produce a more sophisticated output or analysis, tackle a more complex version of the initial problem, or solve a related but distinct problem. Each workshop concludes with an open-ended challenge or extension material, designed to stretch the programming and/or chemical knowledge of students who complete the main tasks of the workshop quickly.

The workshops are designed to be delivered with support from demonstrating staff. In addition, students are encouraged to engage in peer teaching and learning; this allows students with previous programming experience to support those without that prior knowledge and, thanks to the strategy-first design of the workshops, students with strong chemistry knowledge can also support their peers regardless of their knowledge of Python, which helps avoids peer interactions feeling one-sided.

## Kinetics (*Year 1, script-based*)

Students are provided with some files showing the absorbance of Brilliant Green dye as it undergoes bleaching at different temperatures [@], and a Python script which reads data from a `csv` file and produces a plot of the data contained in the first two columns. The absorbance is expected to change as the following function of time:

$$ \text{Abs} = e^{-k_{\text{obs}}t} $$.

Students are then guided through modifying the script to complete the following tasks:

 - Add appropriate axis labels to the graph.
 - Linearise the absorbance data.
 - Add a linear line of best fit to the plot and output the fit parameters (code is provided to do most of this step).
 - Process 5 data files, corresponding to data collected at different temperatures, using the script to collate the fit parameters for each data file.
 - Create an Arrhenius plot from the collated data. The Arrhenius equation is
    $$ \ln{k} = \ln{A} - \frac{E_a}{RT}; $$
    students are expected to perform the appropriate data manipulation to create a plot in this form.
    
## Mass Spectrometry Isotope Patterns (*Year 1, script-based*)

Students are provided with three Python files. The first contains a dictionary consisting of the isotope abundance data for the elements H, C, N and O. The second uses this data to calculate the relative abundance of the various isotopes of a molecule whose formula is defined as a string variable, and plots these abundances as a stem graph. The third script (the "solver") takes a mass in atomic mass units, and returns a list of every "molecule" whose mass rounds to this value and can be constructed from the atoms contained in the isotope abundance data dictionary. This script assumes a mass accuracy equal to the specified number of decimal places, and performs no checks on the chemical plausibility of the returned "molecules".

During workshop, students are supported to:

 - Add appropriate axis labels to the graph, and scale the peaks on the graph such that the maximum relative abundance is equal to 100%.
 - Add (at least) one element's isotope abundance data to the Python dictionary, and create an mass spectrum for a molecule containing that element.
 - Differentiate between high and low resolution mass spectrometry, and use the solver to determine the advantages of high resolution data.
 - Try to find a plausible molecule which has an M+1 peak in the spectrum with a relative abundance as close to 20% as possible.
 
## Matrices (*Year 1, notebook*)

## Atmospheric Chemistry (*Year 2, script-based*)

Students are provided with a dataset containing hourly measurements of three pollutants (ozone, nitric oxide and nitrogen dioxide) taken in the centre of Stoke-on-Trent, UK, between January 2017 and December 2020. They are also provided a Python script which uses the pandas library to read the data, select data on a specific date, and plot the concentration of one pollutant against time for this date.

During the workshop, students:

 - Plot and label multiple data series on the same graph, in this case for the three different pollutants.
 - Use pandas to select different subsets of the data.
 - Use for loops to calculate averages over first days in the month and then hours in the day.
 - Explain the trends observed using chemical cycles involving these pollutants, and their understand of their anthropogenic and natural sources.
 

## Non-Linear Fitting of Heat Capacities (*Year 2, script-based*)

Students are provided with data files containing the enthalpy of aluminium as a function of temperature; one file covers the range 100-900 K, the second covers the range 0-100 K. They are also provided with the same script used in the Kinetics workshop described above, which reads data from a `csv` file and produces a plot of the data contained in the first two columns, and contains code to fit a function to the data. The goal of the workshop is to fit a function to the provided data to obtain an expression for the heat capacity as a function of temperature, using the equation:

$$ c_p = \frac{dH}{dT} $$

To do this, students complete the following steps:

 - Add a linear line of best to the high-temperature enthalpy data, and use the resulting equation to obtain a (constant) heat capacity.
 - Define a quartic function in Python, and fit the low-temperature enthalpy data using this function to obtain the low-T heat capacity of aluminium as a function of temperature.
 - Define a polynomial function of order 10, and fit the low-temperature enthalpy data to which noise has been added with both the quartic and polynomial function.
 - Explain the resulting root mean squared errors of each fit, and consider which fit is more appropriate for the provided data (overfitting).

## Introduction to Machine Learning (*Year 2, notebook*)

The notebook for this workshop begins with a brief reminder of pKa values, defined as $$\text{p} K_a = -\log_{10}\left({\frac{[A^-][H^+]}{[HA]}}\right).$$ It then gives an overview of what machine learning is and how it differs from tradational programming, and provides a simple example of a machine learning model using the scikit-learn library. The support vector regression (SVR) model uses pre-calculated Morgan fingerprints as input vectors and $\text{p} K_a$s as targets to predict; the names of the corresponding molecules are also provided.

During the workshop, students:

 - Use their own knowledge to predict the $\text{p} K_a$ of some example molecules, and compare their predictions to that of the ML model.
 - Use the template provided and a for loop to create a learning curve showing how the machine learning model becomes more accurate when provided with more data.
 - Learn what the hyperparameters of an SVR model are, and optimise them.
 - Create a parity plot, which shows each ML predicted value against its true value.

## Design of Experiment (*Year 3, notebook*)

This workshop is very similar in structure to the Introduction Machine Learning workshop described above, but applied to a different problem - the design of synthetic experiments. This uses a dataset generated to study a palladium-catalysed cross-coupling reaction using different reagents, ligands, bases and solvents [@?]. Students follow the same steps as in the Introduction to Machine Learning workshop, and are additionally introduced to the idea of encoding categorical data for use in machine learning applications.

## Hückel Theory (*Year 3, notebook*)

This notebook introduces students to Hückel Theory, a very simple electronic structure theory [@?]. After introducing the assumptions and mathematics of the theory, students are provided with a function which creates a Hückel Hamiltonian matrix for a linear molecule, and the numpy function needed to diagonalise the matrix. The majority of this workshop asks students to manipulate and interpret the numpy arrays created by this diagonalisation:

 - identify the HOMO and LUMO energies from the list of eigenavalues, and calculate the band gap and total $\pi$ energy of butadiene.
 - use the molecular orbital cofficients to sketch the corresponding molecular orbitals, identify the most likely site of electrophilic attack.
 - use a for loop to calculate and plot the total energy of conjugate alkenes of different lengths.
 - define a function to create the Hückel Hamiltonian for cyclic conjugated molecules, and compare the total energies of cyclic molecules to linear molecules of the same length.

## Advanced Plotting (*Year 3, script-based*)



# Acknowledgements

We are grateful for feedback on and support in delivering these workshops from Dr. Pete Edwards, Dr. Lizzie Wheeldon, Dr. Angelo Frei, and Dr. Nick Wood.

# References
