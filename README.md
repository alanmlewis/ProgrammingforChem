# Programming for Chemistry

This repository contains teaching materials which using Python to teach chemistry. They follow the "strategy-first" mode of programming instruction; for more details on the pedagogical basis for these materials please refer to [A M Lewis, J. Sci. Educ. Technol. (2026)](https://doi.org/10.1007/s10956-026-10301-z). These workshops are currently delivered to undergraduate chemistry students at the University of York. More detail can be found in the JOSE paper in the `jose` branch of this repository. For questions, suggestions and corrections please contact alan.m.lewis@york.ac.uk.

## Windows Users

If cloning this repository onto a Windows machine, please run `fix_symlinks.bat` as an administrator after cloning to ensure all symlinks are created correctly.

## Content and Design

The workshops included in this resource cover a wide range of topics, which will be briefly outlined below, along with where they are delivered in the York chemistry curriculum. There are many commonalities between the workshops. In each case, students are provided with a piece of code which can be executed immediately, and runs successfully to produce an output which can be interpreted using the students' chemical knowledge. The goal of the workshop is then to adapt this code, learning the necessary syntax along the way, to produce a more sophisticated output or analysis, tackle a more complex version of the initial problem, or solve a related but distinct problem.

### Kinetics (*Year 1, script-based*)

Students are provided with `csv` files containing the absorbance of Brilliant Green dye over time as it undergoes bleaching at different temperatures, and a Python script which reads data from a `csv` file and produces a plot of the data contained in the first two columns. Since the bleaching reaction follows pseudo-first order kinetics, the absorbance is expected to change as the following function of time:

$$ \text{Abs} = e^{-k_{\text{obs}}t} .$$

Students are then guided through modifying the script to complete the following tasks:

 - Add appropriate axis labels to the graph.
 - Linearise the absorbance data.
 - Add a linear line of best fit to the plot and output the fit parameters (commented code is provided to do most of this step).
 - Process the 5 data files, corresponding to data collected at different temperatures, and collate the resulting fit parameters for each data file.
 - Create an Arrhenius plot from the collated data. The Arrhenius equation is:
 
    $$ \ln{k} = \ln{A} - \frac{E_a}{RT}. $$
    
    Students are expected to perform the appropriate data manipulation to create a plot in this form.
    
The Python script introduced in this workshop is available from the Univeristy of York [Chemistry teaching labs website](https://chemtl.york.ac.uk/data-analysis-reporting/python/graphs), and students are encouraged to use this to process data and produce graphs in the analysis of subsequent lab work.
    
### Mass Spectrometry Isotope Patterns (*Year 1, script-based*)

Students are provided with three Python files. The first contains a dictionary consisting of the isotope abundance data for the elements H, C, N and O. The second is a script which uses this data to calculate the relative abundance of the various isotopologues of a molecule whose formula is defined as a string variable, and plots these abundances as a stem graph. The third script (the "solver") takes as an argument a mass in atomic mass units, and returns a list of every "molecule" whose mass rounds to this value and can be constructed from the atoms contained in the isotope abundance data dictionary. This script assumes a mass accuracy equal to the specified number of decimal places, and performs no checks on the chemical plausibility of the returned "molecules".

During workshop, students are supported to:

 - Simulate mass spectra for the isotopologues of a molecule of their choicse, adding appropriate axis labels and scaling the peaks on the graph such that the maximum relative abundance is equal to 100%.
 - Add (at least) one element's [isotope abundance data](https://www.chem.ualberta.ca/~massspec/atomic_mass_abund.pdf) to the Python dictionary, and create an mass spectrum for the isotopologues of a molecule containing that element.
 - Differentiate between high and low resolution mass spectrometry, and use the solver to determine the advantages of high resolution data.
 - Try to find a plausible molecule which has an M+1 peak in the spectrum with a relative abundance as close to 20% as possible.
 
Students subsequently use the isotope pattern prediction script in later taught lab practicals (with a complete dictionary file of isotope abundances) and may also utilise the mass solver script in project work.

### Matrices (*Year 1, notebook*)

This workshop is not strictly strategy-first in design. It aims to teach students some fundamentals about matrices, and is delivered as part of the Maths for Chemists course alongside some pen-and-paper workshops. It illustrates coordinate transformations, matrix multiplication and matrix inversion using Python tools.

### Atmospheric Chemistry (*Year 2, script-based*)

Students are provided with a dataset containing hourly measurements of three pollutants (ozone, nitric oxide and nitrogen dioxide) taken in the centre of Stoke-on-Trent, UK, between January 2017 and December 2020. They are also provided a Python script which uses the `pandas` library to read the data, select data on a specific date, and plot the concentration of one pollutant against time for this date.

During the workshop, students:

 - Plot and label multiple data series for the three different pollutants on the same graph.
 - Use `pandas` to select different subsets of the data.
 - Use `for` loops to calculate average pollutant concentrations, firstly over days in the month and then over hours in the day.
 - Explain the trends observed using chemical cycles involving these pollutants, and students' understanding of their anthropogenic and natural sources.
 

### Non-Linear Fitting of Heat Capacities (*Year 2, script-based*)

Students are provided with data files containing the enthalpy of aluminium as a function of temperature; one file covers the range 100-900 K, the second covers the range 0-100 K. The workshop uses the same Python script as the Kinetics workshop described above, which reads data from a `csv` file, produces a plot of the data contained in the first two columns, and contains code to fit a function to the data. The goal of the workshop is to fit a function to the provided data to obtain an expression for the heat capacity as a function of temperature, using the equation:

$$ c_p = \frac{dH}{dT} .$$

To do this, students complete the following steps:

 - Plot the high-temperature enthalpy data, adding a linear line of best fit, and use the resulting equation to obtain a (constant) heat capacity.
 - Define a quartic function in Python, and fit the low-temperature enthalpy data using this function to obtain the heat capacity of aluminium as a function of temperature in this range.
 - Define a polynomial function of order 10, and fit the low-temperature enthalpy data to which noise has been added with both the quartic and polynomial function.
 - Explain the resulting root mean squared errors of each fit, and consider which fit is more appropriate for the provided data (overfitting).
 
Later in the course, students undertake a lab project which utilises non-linear fitting to determine rate constants which are combined with Hammett parameters to gain insight into a reaction mechanism. Many students modified the Python script provided in this workshop to complete this assessment.

### Introduction to Machine Learning (*Year 2, notebook*)

The notebook for this workshop begins with a brief reminder of $\text{p} K_{a}$ values, defined as $$\text{p} K_a = -\log_{10}\left({\frac{[A^-][H^+]}{[HA]}}\right).$$ It then gives an overview of what machine learning is and how it differs from traditional programming, and provides a simple example of a machine learning (ML) model using the `scikit-learn` library. The support vector regression (SVR) model uses pre-calculated Morgan fingerprints as input vectors and $\text{p} K_a$ values as targets to predict; the names of the corresponding molecules are also provided.

During the workshop, students:

 - Use their own knowledge to predict the $\text{p} K_a$ of some example molecules, and compare their predictions to that of the ML model.
 - Use the template provided and a for loop to create a learning curve showing how the machine learning model becomes more accurate when provided with more data.
 - Learn what the hyperparameters of an SVR model are, and optimise them.
 - Create a parity plot, which shows each ML predicted value against its true value.

### Design of Experiment (*Year 3, notebook*)

This workshop is very similar in structure to the Introduction Machine Learning workshop described above, but applied to a different problem - the design of synthetic experiments. This uses a dataset generated to study a palladium-catalysed cross-coupling reaction using different reagents, ligands, bases and solvents. Students follow the same steps as in the Introduction to Machine Learning workshop, and are additionally introduced to the idea of encoding categorical data for use in machine learning applications.

### Hückel Theory (*Year 3, notebook*)

This notebook introduces students to Hückel Theory, a very simple electronic structure theory. After introducing the assumptions and mathematics of the theory, students are provided with a function which creates a Hückel Hamiltonian matrix for a linear conjugated alkene, and the `numpy` function needed to diagonalise the matrix. The majority of this workshop asks students to manipulate and interpret the `numpy` arrays created by this diagonalisation:

 - identify the highest occupied and lowest unoccupied molecular orbital energies from the list of eigenvalues, and calculate the band gap and total $\pi$ energy of butadiene.
 - sketch the molecular orbitals described by the molecular orbital coefficients, and use this information justify the most likely site of electrophilic attack in butadiene.
 - use a `for` loop to calculate and plot the total $\pi$ energy and band gap of conjugated alkenes of different lengths.
 - define a function to create the Hückel Hamiltonian for cyclic conjugated molecules, and compare the total $\pi$ energies of cyclic molecules to linear molecules of the same length.

### Advanced Plotting (*Year 3, script-based*)

This workshop serves as part of students' preparation for a short research project. The goal of the workshop is to help students to think about the different ways data can be plotted, the reasons for choosing one plotting style over another, and equipping them to create a wider range of graphs. We use the `matplotlib` library throughout, but the workshop could be easily adapted to use a different library.

In the course of the workshop, students:

 - Consider a range of methods of displaying a particular dataset, evaluating the advantages and disadvantages of each.
 - Learn how to read and interpret the documentation of `matplotlib`.
 - Create scatter plots with error bars, box plots, bar charts and contour plots using a range of sample data from different areas of chemistry.
 
This repository contains example scripts and data for a number of additional types of plots not covered in this workshop, including histograms and pie charts. Students are directed to the Univeristy of York [Chemistry teaching labs website](https://chemtl.york.ac.uk/data-analysis-reporting/python/advanced-graphs) to access these scripts, and encouraged to use the relevant documentation to adapt the simple examples provided to suit the needs of their projects.

### Photometers (*Year 3, script-based*)

Unlike other workshops described here, this is a laboratory-based practical session in which students construct a simple photometer using an LED light source and a photodiode detector. Students initially record analogue voltages from the circuit using a multimeter, before adding a hardware interface (Arduino Uno) to provide analogue to digital (A2D) conversion to a computer. Students are introduced to interfacing Python with hardware using PySerial.

Using this photometer, students carry out simple photometric measurements and apply the Beer-Lambert relationship ($A=\varepsilon cl$) to determine the molar absorption coefficient of potassium permanganate solution, from a range of concentrations. Finally, students record kinetic measurements for a dye-bleaching reaction related to that analysed in the Kinetics workshop above.
