
ABOUT THE DATASET

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
