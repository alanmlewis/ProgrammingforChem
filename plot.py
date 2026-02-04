# These libraries contain useful tools we will use to load, processes and plot data
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from os.path import splitext
from inspect import getfullargspec

# This allows us to pass arguments to our program
from sys import argv

# ----------------------------- FITTING OPTIONS --------------------------------------------

# Set fit to True to calculate a fit to the (possibly manipulated) data
fit = True

# Define the form of the function to be fit to the data (default: linear a*x+b)
def linear(x,m,c):
    return m*x+c
    
# For a quadratic fit 
def quad(x,a,b,c):
    return a*x**2 + b*x + c
    
# ------------------------------------------------------------------------------------------

# ----------------------------- HANDLE RUN-TIME ARGUMENTS ----------------------------------

# The first argument is always the name of the program; we will remove it
args = argv[1:]

# The last argument tells us which fitting function (defined above) to use.
func_name = args[-1]

try:
	func = eval(func_name)
	suffix = '_'+func_name
	print(f'A best fit to the data will be calculated using the function \"{func_name}\"')
except:
	print('You have either not provided a fitting function, or provided the incorrect name for a fitting function. No line of best fit will be plotted.')
	fit = False
	suffix = ''

# ----------------------------- OUTPUT OPTIONS --------------------------------------------
# Set output to True to write the parameters of the line of best fit
# of every processed data file to a single external file.
output = True

# Set the name of this external file
output_fname = 'fit_parameters'

# If we are not performing a fit, there will be nothing to output!
if fit == False:
    output = False

# Add a unique suffix to the name of each output file
# By default this is the name of the fitting function
# Uncomment the line below to override this
# suffix = '"suffix"'
# ------------------------------------------------------------------------------------------


# We need to collect the fit data for each file we process
if output:
    fit_data = []
    data_fnames = []

# We will create a plot from every csv file passed to the program
for fname in args:
    # If the filename is not a csv file, it will be skipped
    if fname[-4:] != '.csv': continue

    # Load the x and y data from the csv file. Note that the column indexes start from 0, not 1.
    try:
        data = np.loadtxt(fname,delimiter=",",skiprows=0)
    except:
        print("Could not process file",fname,". This is probably because it contains text outside of the header line. It has been skipped.")
        continue
    x = data[:,0]
    y = data[:,1]
    
    # Add the name of each file we will process to a list
    if output: data_fnames.append(fname)


    # --------------------------------------------------------------------------------------

    # Calculate a line of best fit, if fit is true. The best fit parameters are stored in variable p.
    if fit:
        p,pcov = curve_fit(func,x,y)
        if output: fit_data.append(p)
    
    # Create the figure
    fig = plt.figure()
    # Create the "Axes", which contains information for the graph
    ax = plt.axes()

    # This creates a line graph, adding a straight line between each point
    # in the input data file
    ax.plot(x,y,label='Data')

    # Add a line of best fit to the plot, if fit is true
    if fit: ax.plot(x,func(x,*p),label='Line of best fit')

    # ----- PLOTTING DETAILS ---------------------------------------------------------------
    # Modify the following lines to be appropriate for the graph you are currently plotting

    # Add labels to the x and y axes
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    
    # Set the maximum values of the x and y axes
    # ax.set_xlim([0,200])
    # ax.set_ylim([0.0,1.0])

    # Show a legend
    ax.legend()

    # Add a title to the graph; by default this is the
    # name of the input data file
    ax.set_title("Title")

    #----- CALCULATE MEAN SQUARE ERROR------------------------------------------------------


    # Make a list of "best fit" values which each correspond to a temperature value   
    if fit:
        bestfit = []

        for temperature in x:
            bestfit.append(func(temperature,*p))

        # Make a list which contains the error for each datapoint (i.e. the difference between the experimental value and our model's prediction)
        # len(y) is the number of values in the list of datapoints y
        errors = []
        
        for i in range(0,len(y)):
            errors.append(bestfit[i]-y[i])

        # Calculate the mean square error by squaring each "error" value and taking the mean of those squares
        
        total = 0
        
        for i in errors:
            total = total + i**2

        mean_square_error = total/len(y)

        print("The mean square error for this fit is", mean_square_error)
    

    # --------------------------------------------------------------------------------------

    fig.savefig(splitext(fname)[0]+suffix+".png")
    plt.close()

    # Output the parameters of the line of best fit for every file processed
    if output and len(data_fnames)>0:
        params = getfullargspec(func)[0][1:]
        np.savetxt(output_fname+suffix+'.csv',np.vstack((data_fnames,np.array(fit_data).T)).T,delimiter=',',header='File Name,'+','.join(params),comments='',fmt="%s")
