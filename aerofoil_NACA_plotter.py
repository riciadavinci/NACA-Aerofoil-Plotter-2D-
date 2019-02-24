#---------------------------------------------------
# File Name: aerofoil_NACA_plotter.py
# Date: 22 Jan 2019
# Author: Rishikesh Nerurkar
#---------------------------------------------------

# Importing Required Modules 
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
 
# Passing the coordinate file name into our program as an argument
program_name = sys.argv[0]
argument = sys.argv[1]
arg_len = len(argument)
file_format = argument[arg_len-4:]
c_f_name = str(argument)
if(not os.path.exists(c_f_name)):
	print("Such a coordinate file does not exist")

# Ensuring that only arguments passed are python script file and coordinate file
if(len(sys.argv) != 2):
	print("Usage: python aerofoil_NACA_plotter.py coordinatefile.csv \nFor more clarification, refer the readme file\nExiting the program")
	sys.exit(1)	
elif(file_format == '.csv'):
	pass
elif(file_format == '.txt'):
	pass
else:
	print("Coordinate File must be in '.csv' or '.txt' format only\nExiting the program")
	sys.exit(1)
coordinate_file = str(argument)

# Reading Aerofoil coordinates from the csv file 
file_data = np.loadtxt(coordinate_file, dtype = float, delimiter = ',')

# Assigning Values to x and y coordinate arrays
x = file_data[:,][:,0].reshape(len(file_data),1)
y = file_data[:,][:,1].reshape(len(file_data),1)

# Appending initial x & y values to the arrays to complete the contour
x = np.append(x, x[0][0])
y = np.append(y, y[0][0])
	
# Defining min and max limits for 'matplotlib.pyplot.axis' function
x_c_max = np.amax(x) + 0.05
x_c_min = np.amin(x) - 0.05
y_c_max = np.amax(y) + 0.35
y_c_min = np.amin(y) - 0.35

# Taking aerofoil NACA code number
naca_code = input("Input Aerofoil NACA Code Number:")		#This does not make any difference to the actual working of the code.
								#It just makes it easier to save plot file name according to entere NACA Code.
	
# Adding Angle of attack
print("The angle of attack lies between 0 deg and 45 deg")
alpha_deg = float(input("Input the angle of attack (alpha) = "))
while(alpha_deg >= 0):
    if(alpha_deg <= 45):
        print("Entered Value of alpha = {0:.2f} deg".format(alpha_deg)) 
        break
    else:
        print("Alpha out of range, The angle of attack lies between 0 deg and 45 deg")
        alpha_deg = float(input("Input the angle of attack (alpha) = "))

# Converting angle of attack from degrees to radian for use in sine and cosine functions
alpha_rad = alpha_deg * np.pi / 180

# Finding Centroid
x_temp = x.copy()	#Temporary x variable to prevent changes occuring to origninal variable
y_temp = y.copy()
x_centre = (np.amax(x_temp) + np.amin(x_temp)) / 2.0
y_centre = (np.amax(y_temp) + np.amin(y_temp)) / 2.0

# Creating x and y centre arrays
x_cent_arr = np.ones(len(x))				
y_cent_arr = np.ones(len(y))
x_cent_arr = x_cent_arr * x_centre
y_cent_arr = y_cent_arr * y_centre

# Forward Translation (Translating the contour such that the centroid moves to origin)
x_o_temp = x_temp - x_cent_arr
y_o_temp = y_temp - y_cent_arr

# Rotating the new points about origin
x_rot = (x_o_temp * np.cos(alpha_rad)) + (y_o_temp * np.sin(alpha_rad))
y_rot = (x_o_temp * -1 * np.sin(alpha_rad)) + (y_o_temp * np.cos(alpha_rad))

# Back Translation
x_rotf = x_rot + x_cent_arr
y_rotf = y_rot + y_cent_arr

# Plotting the aerofoil from new x & y arrays
plot_file_name = "Plot of NACA" + naca_code + " Aerofoil"
if (not os.path.exists("plots")):
	os.makedirs("plots")
plot_file_path = str(os.getcwd()) + "/plots/"
plt.axis((x_c_min, x_c_max, y_c_min, y_c_max))
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("NACA" + naca_code + " Aerofoil plot for angle of attack " + str(alpha_deg) + "$^o$")
plt.plot(x_rotf, y_rotf, 'k')

# Saving the figures as both .png and .pdf
plt.savefig(plot_file_path + plot_file_name + ".png", bbox_inches = 'tight')
plt.savefig(plot_file_path + plot_file_name + ".pdf", bbox_inches = 'tight')
print("plots saved in folder 'plots'")
plt.show()
