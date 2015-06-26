#! /usr/bin/python
import os
f= open('./data/2d_mass_massratio_sweep_precise.txt', 'w')
g= open('./data/out_precise.txt', 'r')

for line in g:
  if (line.startswith("<")):
    ss=line.split('<search_likelihood>')#splits the line between the two sides the delimiter
    tt=ss[1].split('</search_likelihood>')#chooses the second of the split parts and resplits
    f.write("%s \n" % tt[0])#writes the first of the resplit lines
    
f.close()
g.close()


t= open('./data/2d_mass_massratio_sweep_precise.txt', 'r') 
h= open('./data/data_precise.dat', 'w')
mass_counter=1.0
mass=str(mass_counter)
massratio_counter=0.1
massratio=str(massratio_counter)
counter=1

s =[]

for line in t:
  s.append(line)

i=0
while mass_counter < 191:
	massratio_counter=0.1
	massratio=str(massratio_counter)
	while massratio_counter < 0.75:
	  h.write("%s \t %s \t %s" % (mass, massratio, str(s[i])))
	  i=i+1
	  counter=counter+1
	  massratio_counter=massratio_counter+0.02
	  massratio=str(massratio_counter)
	mass_counter=mass_counter+1
	mass=str(mass_counter)

t.close()
h.close()



