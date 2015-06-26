#! /usr/bin/python
import os
f= open('./data/seed125896_backtime_data.txt', 'w')
g= open('./seed_125896/backtime_sweep/backtime_output.txt', 'r')

for line in g:
  if (line.startswith("<")):
    ss=line.split('<search_likelihood>')#splits the line between the two sides the delimiter
    tt=ss[1].split('</search_likelihood>')#chooses the second of the split parts and resplits
    f.write("%s \n" % tt[0])#writes the first of the resplit lines
    
f.close()
g.close()
########  


f= open('./data/seed125896_fortime_data.txt', 'w')
g= open('./seed_125896/fortime_sweep/fortime_output.txt', 'r')

for line in g:
  if (line.startswith("<")):
    ss=line.split('<search_likelihood>')
    tt=ss[1].split('</search_likelihood>')
    f.write("%s \n" % tt[0])
    
f.close()
g.close()
########  

#f= open('./data/seed125896_rad_data.txt', 'w')
#g= open('./seed_125896/rad_sweep/rad_output.txt', 'r')

#for line in g:
  #if (line.startswith("<")):
    #ss=line.split('<search_likelihood>')
    #tt=ss[1].split('</search_likelihood>')
    #f.write("%s \n" % tt[0])
    
#f.close()
#g.close()
########  

f= open('./data/seed125896_radratio_data.txt', 'w')
g= open('./seed_125896/radratio_sweep/radratio_output.txt', 'r')

for line in g:
  if (line.startswith("<")):
    ss=line.split('<search_likelihood>')
    tt=ss[1].split('</search_likelihood>')
    f.write("%s \n" % tt[0])
    
f.close()
g.close()
########  

#f= open('./data/seed125896_mass_data.txt', 'w')
#g= open('./seed_125896/mass_sweep/mass_output.txt', 'r')

#for line in g:
  #if (line.startswith("<")):
    #ss=line.split('<search_likelihood>')
    #tt=ss[1].split('</search_likelihood>')
    #f.write("%s \n" % tt[0])
    
#f.close()
#g.close()
########  

f= open('./data/seed125896_massratio_data.txt', 'w')
g= open('./seed_125896/massratio_sweep/massratio_output.txt', 'r')

for line in g:
  if (line.startswith("<")):
    ss=line.split('<search_likelihood>')
    tt=ss[1].split('</search_likelihood>')
    f.write("%s \n" % tt[0])
    
f.close()
g.close()
########  