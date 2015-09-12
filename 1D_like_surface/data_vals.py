#! /usr/bin/python
import os
#--------------------------------------------------------------------------------------------------
#       PARAMETER LIBRARY       #
#--------------------------------------------------------------------------------------------------
#parameter    = [start, end, increment]
ft            = [0.25, 3.0, 0.25]
bt            = [0.1, 2.0, 0.05]
r             = [0.1, 0.75, 0.02]
r_r           = [0.06, 0.75, 0.02]
m             = [2, 100, 2]
m_r           = [0.1, 0.75, 0.02]

#--------------------------------------------------------------------------------------------------


#  FORWARD TIME #
f = open('./parameter_data/fortime_vals.txt', 'w')
counter = ft[0]
while counter < ft[1]:
    f.write("%s \n" % counter)
    counter = counter + ft[2]
f.close()
  
#  BACKWARD TIME  #  
f = open('./parameter_data/backtime_vals.txt', 'w')
counter = bt[0]
while counter < bt[1]:
    f.write("%s \n" % counter)
    counter = counter + bt[2]
f.close() 

#  RADIUS  #
f = open('./parameter_data/rad_vals.txt', 'w')
counter = r[0]
while counter < r[1]:
    f.write("%s \n" % counter)
    counter = counter + r[2]
f.close()
 
 #  RADIUS RATIO  #
f = open('./parameter_data/radratio_vals.txt', 'w')
counter = r_r[0]
while counter < r_r[1]:
    f.write("%s \n" % counter)
    counter = counter + r_r[2]
f.close()

#  MASS  #
f = open('./parameter_data/mass_vals.txt', 'w')
counter = m[0]
while counter < m[1]:
    f.write("%s \n" % counter)
    counter = counter + m[2]
f.close()

#  MASS RATIO  #
f = open('./parameter_data/massratio_vals.txt', 'w')
counter = m_r[0]
while counter < m_r[1]:
    f.write("%s \n" % counter)
    counter = counter + m_r[2]
f.close()