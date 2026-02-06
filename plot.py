# These libraries contain useful tools we will use to load, processes and plot data
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from os.path import splitext
from inspect import getfullargspec
from glob import glob

# This allows us to pass arguments to our program
from sys import argv

# ----------------------------- FITTING OPTIONS --------------------------------------------

# Set fit to True to calculate a fit to the (possibly manipulated) data
fit = False

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
	# Since you've provided an acceptable fitting function, we assume you want to fit
	fit = True
	suffix = '_'+func_name
	print(f'A best fit to the data will be calculated using the function \"{func_name}\"')
except:
	if fit == True:
	    print("You have either not provided a fitting function, or provided the incorrect name for a fitting function.")
	    print("Since you've requested a fit (fit = True), we default to a linear line of best fit.")
	    func_name = "linear"
	    func = eval(func_name)
	    suffix = '_'+func_name
	else:
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
# If you are fitting the data, this is the name of the fitting function by default
# Uncomment the line below to override this

# suffix = "_suffix"

# ------------------------------------------------------------------------------------------

# We need to collect the fit data for each file we process
if output:
    fit_data = []
    data_fnames = []

# The first argument is always the name of the program; we will remove it
# If the filename is not a csv file, it will be skipped
args = [f for l in argv[1:] for f in glob(l) if f[-4:] == '.csv']
nfiles=len(args)
print('A total of '+str(nfiles)+' csv files will be processed. Any other files will be ignored.')

# We will create a plot from every csv file passed to the program
i = 0
for fname in args:
    i=i+1
    print(f"Processing file {i} of {nfiles} - {fname}")
    
    # Load the data from the csv file. 
    try:
        data = np.loadtxt(fname,delimiter=",",skiprows=1)
    except Exception as error:
        print("Could not process file",fname,". It has been skipped.\nThe error from Python is:")
        print(error.args[0])
        continue
    
    # Choose which columns of data we want to use as our x and y values.
    # Note that the column indexes start from 0, not 1.    
    x = data[:,0]
    y = data[:,1]
    
    # Add the name of each file we will process to a list
    if output: data_fnames.append(fname)

    # ----- DATA MANIPULATION --------------------------------------------------------------
    # Uncomment the relevent line from this section or add your own code

    # Example: Convert time from minutes to seconds
    # x = x*60

    # Example: Convert y to ln(y)
    # y = np.log(y) 

    # --------------------------------------------------------------------------------------

    # Calculate a line of best fit, if fit is true. The best fit parameters are stored in variable fit_params.
    if fit:
        try:
            fit_params, pcov = curve_fit(func,x,y)
            if output: fit_data.append(fit_params)
        except Exception as error:
            print("Could not fit a curve to your data. Check the form of func, and your data. \nThe error from Python is:")
            print(error.args[0])
            fit = False
    
    # Create the figure
    fig = plt.figure()
    # Create the "Axes", which contains information for the graph
    ax = plt.axes()

    # This creates a line graph, adding a straight line between each point
    # in the input data file
    ax.plot(x,y,label='Data')

    # Add a line of best fit to the plot, if fit is true
    if fit: ax.plot(x,func(x,*fit_params),label='Line of best fit')

    # ----- PLOTTING DETAILS ---------------------------------------------------------------
    # Modify the following lines to be appropriate for the graph you are currently plotting

    # Add labels to the x and y axes
    ax.set_xlabel("X axis / units")
    ax.set_ylabel("Y axis / units")
    
    # Set the maximum values of the x and y axes
    # ax.set_xlim([0,200])
    # ax.set_ylim([0.0,1.0])

    # Show a legend
    ax.legend()

    # Add a title to the graph
    ax.set_title("Title")

    #----- CALCULATE MEAN SQUARE ERROR------------------------------------------------------

    # Make a list of "best fit" values which each correspond to a temperature value   
    if fit:
    
        # Calculate the value of the line of the best fit at every value of x
        y_fit = func(x,*fit_params)
        # Calculate the root mean square error in the line of best fit.
        rmse = np.square(y-yfit)
        rmse = np.average(rmse)
        rmse = np.sqrt(rmse)

        print("The root mean square error for this fit is", rmse)

    # --------------------------------------------------------------------------------------

    fig.savefig(splitext(fname)[0]+suffix+".png")
    plt.close()

# Output the parameters of the line of best fit for every file processed
if output and len(data_fnames)>0:
    params = getfullargspec(func)[0][1:]
    np.savetxt(output_fname+suffix+'.csv',np.vstack((data_fnames,np.array(fit_data).T)).T,delimiter=',',header='File Name,'+','.join(params),comments='',fmt="%s")
if nfiles > 0: print('All files processed')
