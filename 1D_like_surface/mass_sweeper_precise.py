#! /usr/bin/python
import os


f= open('./data/mass_precise_data.txt', 'w')
g= open('.//mass_sweep_precise/mass_output.txt', 'r')

for line in g:
  if (line.startswith("<")):
    ss=line.split('<search_likelihood>')
    tt=ss[1].split('</search_likelihood>')
    f.write("%s \n" % tt[0])
    
f.close()
g.close()


f=open('./data/mass_vals_precise.txt', 'w')
counter=1
while counter < 191:
  f.write("%s \n" % counter)
  counter=counter+1
  
f.close()