#! /usr/bin/python
import os
f= open('./data/seed491349_backtime_data.txt', 'w')
g= open('./seed_491349/backtime_sweep/backtime_output.txt', 'r')

for line in g:
  if (line.startswith("<")):
    ss=line.split('<search_likelihood>')
    tt=ss[1].split('</search_likelihood>')
    f.write("%s \n" % tt[0])
    
f.close()
g.close()
########  


f= open('./data/seed491349_fortime_data.txt', 'w')
g= open('./seed_491349/fortime_sweep/fortime_output.txt', 'r')

for line in g:
  if (line.startswith("<")):
    ss=line.split('<search_likelihood>')
    tt=ss[1].split('</search_likelihood>')
    f.write("%s \n" % tt[0])
    
f.close()
g.close()
########  

f= open('./data/seed491349_rad_data.txt', 'w')
g= open('./seed_491349/rad_sweep/rad_output.txt', 'r')

for line in g:
  if (line.startswith("<")):
    ss=line.split('<search_likelihood>')
    tt=ss[1].split('</search_likelihood>')
    f.write("%s \n" % tt[0])
    
f.close()
g.close()
########  

f= open('./data/seed491349_radratio_data.txt', 'w')
g= open('./seed_491349/radratio_sweep/radratio_output.txt', 'r')

for line in g:
  if (line.startswith("<")):
    ss=line.split('<search_likelihood>')
    tt=ss[1].split('</search_likelihood>')
    f.write("%s \n" % tt[0])
    
f.close()
g.close()
########  

f= open('./data/seed491349_mass_data.txt', 'w')
g= open('./seed_491349/mass_sweep/mass_output.txt', 'r')

for line in g:
  if (line.startswith("<")):
    ss=line.split('<search_likelihood>')
    tt=ss[1].split('</search_likelihood>')
    f.write("%s \n" % tt[0])
    
f.close()
g.close()
########  

f= open('./data/seed491349_massratio_data.txt', 'w')
g= open('./seed_491349/massratio_sweep/massratio_output.txt', 'r')

for line in g:
  if (line.startswith("<")):
    ss=line.split('<search_likelihood>')
    tt=ss[1].split('</search_likelihood>')
    f.write("%s \n" % tt[0])
    
f.close()
g.close()
########  