DES-Simulation-for-simple-Quese:

A Discrete Event Simulation model based on SimPy¹ to determine the effectiveness and 
influence of two variables: "Patient per day" and "Cure Duration" in "Hospital Load" 
and "Failure Rates" alongside other parameters.

about the model itself, I should mention it's a queueing model with a choice of leaving 
for participants in the queue (or just passing away) and a common process which is
applied to every demand possible.

although it is applied to a healthcare system problem but, is not limited to that field 
and can be used to describe any service system which has common inner nature and some turns 
and twists in parameters.

I hope the description in the jupyter notebook is sufficient and the bulk python file 
does its purpose of creating 2-dimensional data points for interpolating and 
estimating the original unknown function which governs the original problem.

if I'm missing any essential description, please note me at:
eftekhari.meftekhari.mohamad-at-gmail.com
to be added to this ReadMe file and appreciated as well.

______________________________________________________________________________
1. https://simpy.readthedocs.io/en/latest/index.html
