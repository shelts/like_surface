#! /usr/bin/python
import os



f=open('./data/backtime_vals.txt', 'w')
counter=0.1
while counter < 2:
  f.write("%s \n" % counter)
  counter=counter+0.05
  
f.close()


f=open('./data/fortime_vals.txt', 'w')
counter=0.25
while counter < 6.0:
  f.write("%s \n" % counter)
  counter=counter+0.25
  
f.close()


f=open('./data/rad_vals.txt', 'w')
counter=0.1
while counter < 0.75:
  f.write("%s \n" % counter)
  counter=counter+0.02
  
f.close()


f=open('./data/radratio_vals.txt', 'w')
counter=0.06
while counter < 0.75:
  f.write("%s \n" % counter)
  counter=counter+0.02
  
f.close()


f=open('./data/mass_vals.txt', 'w')
counter=2
while counter < 100:
  f.write("%s \n" % counter)
  counter=counter+2
  
f.close()

f=open('./data/massratio_vals.txt', 'w')
counter=0.1
while counter < 0.75:
  f.write("%s \n" % counter)
  counter=counter+0.02
  
f.close()