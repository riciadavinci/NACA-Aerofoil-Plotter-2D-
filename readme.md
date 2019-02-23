# NACA Aerofoil Plotter (2D) - Readme

__Author:__ Rishikesh Nerurkar

__Date:__ 23-02-2019

___
## Description
This project contains a python script file named **‘aerofoil_NACA_plotter.py’**. The script loads x and y coordinates from the coordinate file and also asks for NACA aerofoil code and angle of attack (alpha). The script does nothing more than generate 2D plot of the aerofoil cross section. By default the project contains coordinate files of **‘NACA 2412 Aerofoil’** and **‘NACA 1410 Aerofoil’** taken from the website http://airfoiltools.com/airfoil/naca4digit . You can select any other aerofoil from the website and copy their coordinates, although the script has been tested only on the above mentioned aerofoils. The script has been tested on a PC running Windows 8.1 using python 3.7.1.

___

## Instructions before running the script
Copy the x and y coordinates of the aerofoil from the above website, either overwriting the default coordinates or into a new text file. Make sure to separate the x and y coordinates with commas in each row (i.e., comma is the delimiter). Once this is done save the file as **‘.csv’** or **‘.txt’** format only.

___

## Running the script
To run the script, navigate to the script file directory using any shell of your choice (cmd, shell, bash, etc.)

The python script requires **2 system arguments**, **the script name* and **the coordinate file name**.

__Usage :__
```
python aerofoil_NACA_plotter.py aerofoil_coordinates.csv
```

After running the script the plots are saved in ‘.png’ format as well as ‘.pdf’ format. The image in ‘.png’ format is pixel-based while that in ‘.pdf’ format is vector-based.

___

## Future Work
Some ideas to expand on the current work:
1. Plotter that inputs name (ex: - NACA 2424) and plots the cross-section by retrieving the coordinates stored either in an offline database or by parsing an online source/webpage.
2. Plotter that works on taking input parameters for solving equation that generates the coordinates for aerofoil contour.

___