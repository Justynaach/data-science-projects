# ABOUT THE DATASET

The dataset has 10 000 data points stored as rows with 14 features in column.

UID is an unique identifier (this is the index of the data frame)
Product ID contains data like L, M and H. It refers to the quality variants of the machine and serial number.
There is also other column which has only quality level without serial number and its called Type. 
Air temperature [K] is an ambient temperature around the machine.
Process temperature [K] is a temperature of the specific manufacturing process.
Rotational speed [rpm] The speed at which the machine operates.
Torque [Nm] The rotational force applied by the machine.

Tool wear [min] The amount of time the tool has been in use. (this is what we want to predict in our project)

Machine Failure (bool):
TWF Tool Wear Failure
HDF Heat Dissipation Failure
PWF Power Failure
OSF Overstrain Failure
RNF Random Failures 

# MACHINES PROJECT

The project focuses on the prediction on Tool wear (min). The goal is to estimate the amount of time the machine would work before failure based on operational parameters like temperature, torque, and rotational speed.

Language:
Python
Libraries:
Seaborn and Matplotlib (Vizualization)
Sklearn ( One Hot Encoding, )
....


## Key Points:
Outliers in Torque and Rotational Speed were retained after analysis, as they represent critical operational extremes rather than data errors.

All failure-related columns were dropped from the feature set (X).

Used One-Hot Encoding for machine types, dropping the Type_L column to avoid the Dummy Variable Trap.
