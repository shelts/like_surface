#! /usr/bin/python
import os
#--------------------------------------------------------------------------------------------------
#       PARAMETER LIBRARY       #
#--------------------------------------------------------------------------------------------------
#parameter    = [start, end, increment]
ft         = [3.9, 4.2, 0.01]#30
bt         = [0.96, 1.08, 0.005]#24
r          = [0.1, 0.8, 0.01]#50
r_r        = [0.1, 0.8, 0.01]#45
m          = [52.0, 72.0, 1.0]#20
m_r        = [0.17, 0.24, 0.005]#14

#--------------------------------------------------------------------------------------------------


#  FORWARD TIME #
f = open('./parameter_data/ft_vals.txt', 'w')
counter = ft[0]
while counter < ft[1]:
    f.write("%s \n" % counter)
    counter = counter + ft[2]
f.close()
  
#  BACKWARD TIME  #  
f = open('./parameter_data/bt_vals.txt', 'w')
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
f = open('./parameter_data/rr_vals.txt', 'w')
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
f = open('./parameter_data/mr_vals.txt', 'w')
counter = m_r[0]
while counter < m_r[1]:
    f.write("%s \n" % counter)
    counter = counter + m_r[2]
f.close()