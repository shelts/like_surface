#! /usr/bin/python
import os
from subprocess import call
#--------------------------------------------------------------------------------------------------
#       PARAMETER LIBRARY       #
#--------------------------------------------------------------------------------------------------
args = [4, 1, 0.2, 0.2, 12, 0.2]
sim_time      = str(args[0])
back_time     = str(args[1])
r0            = str(args[2])
light_r_ratio = str(args[3])
mass          = str(args[4])
mass_ratio    = str(args[5])

binary        = "~/research/nbody_test/bin/milkyway_nbody"
lua           = "~/research/lua/EMD_20k_isotropic_1_54_npa3.lua"
seed          = "98213548"
input_hist    = "~/research/like_surface/histogram_in_seed"  + seed + "_20kEMD_4_1_p2_p2_12_p2.hist"
output_hist   = "~/research/like_surface/histogram_out_seed" + seed + "_20kEMD_sweep.hist"

#parameter    = [start, end, increment]
ft         = [3.9, 4.2, 0.01]#30
bt         = [0.96, 1.08, 0.005]#24
r          = [0.1, 0.8, 0.01]#80
r_r        = [0.1, 0.8, 0.01]#80
m          = [1.0, 20.0, 0.25]#80
m_r        = [0.20, 0.30, 0.001]#70

yes = True
no  = False

#choose what to run
run_forward_evole_time    = yes
run_backward_evolve_ratio = yes
run_radius                = yes
run_radius_ratio          = yes
run_mass                  = yes
run_mass_ratio            = yes
#--------------------------------------------------------------------------------------------------

#this makes a comparison histogram
os.system("rm -r ~/research/nbody_test")
os.system("mkdir ~/research/nbody_test")

os.chdir("../nbody_test")
os.system("cmake -DCMAKE_BUILD_TYPE=Release  -DNBODY_GL=OFF -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/research/milkywayathome_client/")
os.system("make -j ")
os.chdir("../like_surface")

os.system(" " + binary + " \
    -f " + lua + " \
    -z " + input_hist + " \
    -n 8 -x -e " + seed + " -i "+ sim_time + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass + " " + mass_ratio )

    #  FORWARD TIME #
if( run_forward_evole_time == True):
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
if( run_backward_evolve_ratio == True):
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
    

    #  MASS  #
if( run_mass == True):
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
if( run_mass_ratio == True):
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
        
    #  RADIUS  #
if( run_radius == True):
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
if( run_radius_ratio == True):
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
