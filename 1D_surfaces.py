#! /usr/bin/python
import os
from subprocess import call
#--------------------------------------------------------------------------------------------------
#       PARAMETER LIBRARY       #
#--------------------------------------------------------------------------------------------------
args = [2, 1, 0.5, 0.2, 30, 0.2]
sim_time      = str(args[0])
back_time     = str(args[1])
r0            = str(args[2])
light_r_ratio = str(args[3])
mass          = str(args[4])
mass_ratio    = str(args[5])

binary        = "~/research/nbody_test/bin/milkyway_nbody"
lua           = "~/research/lua/EMD_20k_isotropic_1_52.lua"
seed          = "98213548"
input_hist    = "~/research/like_surface/histogram_in_seed"  + seed + "_20kEMD_2_1_p5_p2_30_p2.hist"
output_hist   = "~/research/like_surface/histogram_out_seed" + seed + "_20kEMD_2_1_p5_p2_30_sweep.hist"

#parameter    = [start, end, increment]
ft            = [0.25, 3.0, 0.25]
bt            = [0.1, 2.0, 0.05]
r             = [0.1, 0.75, 0.02]
r_r           = [0.06, 0.75, 0.02]
m             = [2, 100, 2]
m_r           = [0.1, 0.75, 0.02]

#--------------------------------------------------------------------------------------------------

#this makes a comparison histogram
os.system("rm -r ~/research/nbody_test")
os.system("mkdir ~/research/nbody_test")

os.chdir("../nbody_test")
os.system("cmake -DCMAKE_BUILD_TYPE=Release  -DNBODY_GL=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/research/milkywayathome_client/")
os.system("make -j ")
os.chdir("../like_surface")

os.system(" " + binary + " \
    -f " + lua + " \
    -z " + input_hist + " \
    -n 8 -x -e " + seed + " -i "+ sim_time + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass + " " + mass_ratio )


#  FORWARD TIME #
counter = ft[0]
name = str(counter)
while counter < ft[1]:
  os.system(" " + binary + " \
        -f " + lua + " \
        -h " + input_hist + " \
        -z " + output_hist + " \
        -n 8 -x -e " + seed + " -i " + name + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass + " " + mass_ratio + " \
        2>>~/research/like_surface/parameter_sweeps/ft.txt")
  counter = counter + ft[2]
  name = str(counter)
  
  
#  BACKWARD TIME  #  
counter = bt[0]
name = str(counter)
while counter < bt[1]:
  os.system(" " + binary + " \
        -f " + lua + " \
        -h " + input_hist + " \
        -z " + output_hist + " \
        -n 8 -x -e  " + seed + " -i " + sim_time + " " + name + " " + r0 + " " + light_r_ratio + " " + mass + " " + mass_ratio + " \
        2>>~/research/like_surface/parameter_sweeps/bt.txt")
  counter = counter + bt[2]
  name = str(counter)
 

#  RADIUS  #
counter = r[0]
name = str(counter)
while counter < r[1]:
  os.system(" " + binary + " \
        -f " + lua + " \
        -h " + input_hist + " \
        -z " + output_hist + " \
        -n 8 -x -e  " + seed + " -i " + sim_time + " " + back_time + " " + name + " " + light_r_ratio + " " + mass + " " + mass_ratio + " \
        2>>~/research/like_surface/parameter_sweeps/rad.txt")
  counter = counter + r[2]
  name = str(counter)
 
 
 #  RADIUS RATIO  #
counter = r_r[0]
name = str(counter)
while counter < r_r[1]:
  os.system(" " + binary + " \
        -f " + lua + " \
        -h " + input_hist + " \
        -z " + output_hist + " \
        -n 8 -x -e  " + seed + " -i " + sim_time + " " + back_time + " " + r0 + " " + name + " " + mass + " " + mass_ratio + " \
        2>>~/research/like_surface/parameter_sweeps/rr.txt")
  counter = counter + r_r[2]
  name = str(counter)


#  MASS  #
counter = m[0]
name = str(counter)
while counter < m[1]:
  os.system(" " + binary + " \
        -f " + lua + " \
        -h " + input_hist + " \
        -z " + output_hist + " \
        -n 8 -x -e  " + seed + " -i " + sim_time + " " + back_time + " " + r0 + " " + light_r_ratio + " " + name + " " + mass_ratio + " \
        2>>~/research/like_surface/parameter_sweeps/mass.txt")
  counter = counter + m[2]
  name = str(counter)


#  MASS RATIO  #
counter = m_r[0]
name = str(counter)
while counter < m_r[1]:
  os.system(" " + binary + " \
        -f " + lua + " \
        -h " + input_hist + " \
        -z " + output_hist + " \
        -n 8 -x -e  " + seed + " -i " + sim_time + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass + " " + name + " \
        2>>~/research/like_surface/parameter_sweeps/mr.txt")
  counter = counter + m_r[2]
  name = str(counter)


