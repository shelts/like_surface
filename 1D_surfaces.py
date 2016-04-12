#! /usr/bin/python
import os
from subprocess import call
#--------------------------------------------------------------------------------------------------
#       PARAMETER LIBRARY       #
#--------------------------------------------------------------------------------------------------
args = [3.95, 3.95, 0.2, 0.8, 12, 48]

sim_time      = str(args[0])
back_time     = str(args[1])
r0            = str(args[2])
light_r_ratio = str(args[3])
mass          = str(args[4])
mass_ratio    = str(args[5])

folder        = "~/research/like_surface/hists/"
binary        = "~/research/nbody_test/bin/milkyway_nbody"
lua           = "~/research/lua/EMD_20k_v158_fixed_seed_fit_parameters_directly.lua"
seed          = "98213548"

input_hist    = folder + "arg_" + sim_time + "_" + back_time + "_" + r0 + "_" + light_r_ratio + "_" + mass + "_" + mass_ratio + "_correct.hist"
output_hist   = folder + "histogram_out_20kEMD_sweep.hist"
#parameter    = [start, end, increment]
ft         = [3.85, 4.3, 0.025]#
bt         = [0.9, 1.08, 0.025]#
r          = [0.1, 3.0, 0.1]#
r_r        = [0.1, 3.0, 0.1]#
m          = [2., 120.0, 5]#
m_r        = [2., 1200.0, 23]#


y = True
n = False

#choose what to run
run_forward_evole_time    = n
run_backward_evolve_ratio = n
run_radius                = n
run_radius_ratio          = n
run_mass                  = n
run_mass_ratio            = y
#--------------------------------------------------------------------------------------------------

#os.system("rm -r ~/research/nbody_test")
#os.system("mkdir ~/research/nbody_test")

os.chdir("../nbody_test")
os.system("cmake -DCMAKE_BUILD_TYPE=Release  -DNBODY_GL=OFF -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/research/milkywayathome_client/")
os.system("make -j ")
os.chdir("../like_surface")

#this makes a comparison histogram
os.system(" " + binary + " \
    -f " + lua + " \
    -z " + input_hist + " \
    -n 8 -x -e " + seed + " -i "+ sim_time + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass + " " + mass_ratio )

    #  FORWARD TIME #
if( run_forward_evole_time == True):
    counter = ft[0]
    name = str(counter)
    while counter < ft[1]:
        output_hist = folder + "ft_hists/" + "arg_" + name + "_" + back_time + "_" + r0 + "_" + light_r_ratio + "_" + mass + "_" + mass_ratio + ".hist"
        os.system(" " + binary + " \
                -f " + lua + " \
                -h " + input_hist + " \
                -z " + output_hist + " \
                -n 8 -x -e " + seed + " -i " + name + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass + " " + mass_ratio + " \
                2>>" + folder + "parameter_sweeps/ft.txt")
        counter = counter + ft[2]
        name = str(counter)
    
    
    #  BACKWARD TIME  #
if( run_backward_evolve_ratio == True):
    counter = bt[0]
    name = str(counter)
    while counter < bt[1]:
        output_hist = folder + "arg_" + sim_time + "_" + name + "_" + r0 + "_" + light_r_ratio + "_" + mass + "_" + mass_ratio + ".hist"
        os.system(" " + binary + " \
                -f " + lua + " \
                -h " + input_hist + " \
                -z " + output_hist + " \
                -n 8 -x -e  " + seed + " -i " + sim_time + " " + name + " " + r0 + " " + light_r_ratio + " " + mass + " " + mass_ratio + " \
                2>>" + folder + "parameter_sweeps/bt.txt")
        counter = counter + bt[2]
        name = str(counter)
    

    #  MASS  #
if( run_mass == True):
    counter = m[0]
    name = str(counter)
    while counter < m[1]:
        output_hist = folder + "mass_hists/" + "arg_" + sim_time + "_" + back_time + "_" + r0 + "_" + light_r_ratio + "_" + name + "_" + mass_ratio + ".hist"
        os.system(" " + binary + " \
                -f " + lua + " \
                -h " + input_hist + " \
                -z " + output_hist + " \
                -n 8 -x -e  " + seed + " -i " + sim_time + " " + back_time + " " + r0 + " " + light_r_ratio + " " + name + " " + mass_ratio + " \
                2>>" + folder + "parameter_sweeps/mass.txt")
        counter = counter + m[2]
        name = str(counter)


    #  MASS RATIO  #
if( run_mass_ratio == True):
    counter = m_r[0]
    name = str(counter)
    while counter < m_r[1]:
        output_hist = folder + "mr_hists/" + "arg_" + sim_time + "_" + back_time + "_" + r0 + "_" + light_r_ratio + "_" + mass + "_" + name + ".hist"
        os.system(" " + binary + " \
                -f " + lua + " \
                -h " + input_hist + " \
                -z " + output_hist + " \
                -n 8 -x -e  " + seed + " -i " + sim_time + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass + " " + name + " \
                2>>" + folder + "parameter_sweeps/mr.txt")
        counter = counter + m_r[2]
        name = str(counter)
        
    #  RADIUS  #
if( run_radius == True):
    counter = r[0]
    name = str(counter)
    while counter < r[1]:
        output_hist = folder + "rad_hists/" + "arg_" + sim_time + "_" + back_time + "_" + name + "_" + light_r_ratio + "_" + mass + "_" + mass_ratio + ".hist"
        os.system(" " + binary + " \
                -f " + lua + " \
                -h " + input_hist + " \
                -z " + output_hist + " \
                -n 8 -x -e  " + seed + " -i " + sim_time + " " + back_time + " " + name + " " + light_r_ratio + " " + mass + " " + mass_ratio + " \
                2>>" + folder + "parameter_sweeps/rad.txt")
        counter = counter + r[2]
        name = str(counter)
    
    
    #  RADIUS RATIO  #
if( run_radius_ratio == True):
    counter = r_r[0]
    name = str(counter)
    while counter < r_r[1]:
        output_hist = folder + "rr_hists/" + "arg_" + sim_time + "_" + back_time + "_" + r0 + "_" + name + "_" + mass + "_" + mass_ratio + ".hist"
        os.system(" " + binary + " \
                -f " + lua + " \
                -h " + input_hist + " \
                -z " + output_hist + " \
                -n 8 -x -e  " + seed + " -i " + sim_time + " " + back_time + " " + r0 + " " + name + " " + mass + " " + mass_ratio + " \
                2>>" + folder + "parameter_sweeps/rr.txt")
        counter = counter + r_r[2]
        name = str(counter)
