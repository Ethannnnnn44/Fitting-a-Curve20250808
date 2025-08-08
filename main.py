# This code fits lets the user specify a .fcs file and parameter, generates a histogram
# and attempts to fit a curve. 


# PLAN  
# 1. import the .fcs file 
# 2. specify which parameter to base the plot on 
# 3. figure out how to extract the .fcs parameter from the file as an array 
# 4. plot the array
# 5. use a library to fit a curve to the data 

# 6. split the array into bins of fix size
# 7. create a scatter plot 

# 8. Create graphics overlaying the bined data and the curve. 

# maybe I can create a general function or object that extracts data from the .fcs file. 
# what labrary can you use to pull a .fcs file. 

import FlowCal
import numpy


file = FlowCal.io.FCSData('TestFile.fcs')

shape = file.shape

print(f"file shape (events, channelw): {shape}")










