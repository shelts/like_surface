#! /usr/bin/python
import os

names   = [ 'backtime_output', 'fortime_output', 'rad_output', 'radratio_output', 'mass_output', 'massratio_output']
folders = [ 'backtime_sweep', 'fortime_sweep', 'rad_sweep', 'radratio_sweep', 'mass_sweep', 'massratio_sweep']
types   = [ 'backtime', 'fortime', 'rad', 'radratio', 'mass',  'massratio']


for i in range(0,6):
  f = open('./likelihood_data/' + str(types[i]) + '_data.txt', 'w')
  g = open('./parameter_sweeps/' + str(folders[i]) + '/' + str(names[i]) + '.txt', 'r')

  for line in g:
    if (line.startswith("<")):
      ss = line.split('<search_likelihood>')#splits the line between the two sides the delimiter
      tt = ss[1].split('</search_likelihood>')#chooses the second of the split parts and resplits
      f.write("%s \n" % tt[0])#writes the first of the resplit lines
    
  f.close()
  g.close()


