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
output_hist   = "~/research/like_surface/histogram_out_seed" + seed + "_20kEMD_4_1_p2_p2_12_sweep.hist"

#parameter = [start, end, increment]
ft         = [3.9, 4.2, 0.01]#30
bt         = [0.96, 1.08, 0.005]#24
r          = [0.1, 0.8, 0.01]#80
r_r        = [0.1, 0.8, 0.01]#80
m          = [1.0, 20.0, 0.25]#80
m_r        = [0.20, 0.30, 0.001]#70


yes = True
no  = False

run_ft_v_bt = no
run_ft_v_r  = no
run_ft_v_rr = no
run_ft_v_m  = no
run_ft_v_mr = no
run_bt_v_r  = no
run_bt_v_rr = no
run_bt_v_m  = no
run_bt_v_mr = no
run_r_v_rr  = no
run_r_v_m   = no
run_r_v_mr  = no
run_rr_v_m  = no
run_rr_v_mr = yes
run_m_v_mr  = yes
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


#  FORWARD TIME VS BACKTIME #
if(run_ft_v_bt == True):
    fwt_counter = ft[0]
    fwt = str(fwt_counter)
    while fwt_counter < ft[1]:
        bwt_counter = bt[0]
        bwt = str(bwt_counter)
        while bwt_counter < bt[1]:
            os.system(" " + binary + " \
                    -f " + lua + " \
                    -h " + input_hist + " \
                    -z " + output_hist + " \
                    -n 10 -x -e  " + seed + " -i " + fwt + " " + bwt + " " + r0 + " " + light_r_ratio + " " + mass + " " + mass_ratio + " \
                    2>>~/research/like_surface/2d_parameter_sweeps/ft_vs_bt.txt")
            bwt_counter = bwt_counter + bt[2]
            bwt = str(bwt_counter)
        fwt_counter = fwt_counter + ft[2]
        fwt = str(fwt_counter)
  
  
#  FORWARD TIME VS RAD #
if(run_ft_v_r == True):
    fwt_counter = ft[0]
    fwt = str(fwt_counter)
    while fwt_counter < ft[1]:
        rad_counter = r[0]
        rad = str(rad_counter)
        while rad_counter < r[1]:
            os.system(" " + binary + " \
                    -f " + lua + " \
                    -h " + input_hist + " \
                    -z " + output_hist + " \
                    -n 10 -x -e  " + seed + " -i " + fwt + " " + back_time + " " + rad + " " + light_r_ratio + " " + mass + " " + mass_ratio + " \
                    2>>~/research/like_surface/2d_parameter_sweeps/ft_vs_rad.txt")
            rad_counter = rad_counter + r[2]
            rad = str(rad_counter)
        fwt_counter = fwt_counter + ft[2]
        fwt = str(fwt_counter)
  
#  FORWARD TIME VS RAD RATIO #
if(run_ft_v_rr == True):
    fwt_counter = ft[0]
    fwt = str(fwt_counter)
    while fwt_counter < ft[1]:
        rr_counter = r_r[0]
        rr = str(rr_counter)
        while rr_counter < r_r[1]:
            os.system(" " + binary + " \
                    -f " + lua + " \
                    -h " + input_hist + " \
                    -z " + output_hist + " \
                    -n 10 -x -e  " + seed + " -i " + fwt + " " + back_time + " " + r0 + " " + rr + " " + mass + " " + mass_ratio + " \
                    2>>~/research/like_surface/2d_parameter_sweeps/ft_vs_rr.txt")
            rr_counter = rr_counter + r_r[2]
            rr = str(rr_counter)
        fwt_counter = fwt_counter + ft[2]
        fwt = str(fwt_counter)


#  FORWARD TIME VS MASS #
if(run_ft_v_m == True):
    fwt_counter = ft[0]
    fwt = str(fwt_counter)
    while fwt_counter < ft[1]:
        m_counter = m[0]
        ms = str(m_counter)
        while m_counter < m[1]:
            os.system(" " + binary + " \
                    -f " + lua + " \
                    -h " + input_hist + " \
                    -z " + output_hist + " \
                    -n 10 -x -e  " + seed + " -i " + fwt + " " + back_time + " " + r0 + " " + light_r_ratio + " " + ms + " " + mass_ratio + " \
                    2>>~/research/like_surface/2d_parameter_sweeps/ft_vs_m.txt")
            m_counter = m_counter + m[2]
            ms = str(m_counter) 
        fwt_counter = fwt_counter + ft[2]
        fwt = str(fwt_counter)
    
    
#  FORWARD TIME VS MASS RATIO #
if(run_ft_v_mr == True):
    fwt_counter = ft[0]
    fwt = str(fwt_counter)
    while fwt_counter < ft[1]:
        mr_counter = m_r[0]
        mr = str(mr_counter)
        while mr_counter < m_r[1]:
            os.system(" " + binary + " \
                    -f " + lua + " \
                    -h " + input_hist + " \
                    -z " + output_hist + " \
                    -n 10 -x -e  " + seed + " -i " + fwt + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass + " " + mr + " \
                    2>>~/research/like_surface/2d_parameter_sweeps/ft_vs_mr.txt")
            mr_counter = mr_counter + m_r[2]
            mr = str(mr_counter) 
        fwt_counter = fwt_counter + ft[2]
        fwt = str(fwt_counter)
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#  BACKWARD TIME VS RAD #
if(run_bt_v_r == True):
    bwt_counter = bt[0]
    bwt = str(bwt_counter)
    while bwt_counter < bt[1]:
        rad_counter = r[0]
        rad = str(rad_counter)
        while rad_counter < r[1]:
            os.system(" " + binary + " \
                    -f " + lua + " \
                    -h " + input_hist + " \
                    -z " + output_hist + " \
                    -n 10 -x -e  " + seed + " -i " + sim_time + " " + bwt + " " + rad + " " + light_r_ratio + " " + mass + " " + mass_ratio + " \
                    2>>~/research/like_surface/2d_parameter_sweeps/bt_vs_r.txt")
            rad_counter = rad_counter + r[2]
            rad = str(rad_counter)
        bwt_counter = bwt_counter + bt[2]
        bwt = str(bwt_counter)
  
#  BACKWARD TIME VS RAD RATIO #
if(run_bt_v_rr == True):
    bwt_counter = bt[0]
    bwt = str(bwt_counter)
    while bwt_counter < bt[1]:
        rr_counter = r_r[0]
        rr = str(rr_counter)
        while rr_counter < r_r[1]:
            os.system(" " + binary + " \
                    -f " + lua + " \
                    -h " + input_hist + " \
                    -z " + output_hist + " \
                    -n 10 -x -e  " + seed + " -i " + sim_time + " " + bwt + " " + r0 + " " + rr + " " + mass + " " + mass_ratio + " \
                    2>>~/research/like_surface/2d_parameter_sweeps/bt_vs_rr.txt")
            rr_counter = rr_counter + r_r[2]
            rr = str(rr_counter)
        bwt_counter = bwt_counter + bt[2]
        bwt = str(bwt_counter)


#  BACKWARD TIME VS MASS #
if(run_bt_v_m == True):
    bwt_counter = bt[0]
    bwt = str(bwt_counter)
    while bwt_counter < bt[1]:
        m_counter = m[0]
        ms = str(m_counter)
        while m_counter < m[1]:
            os.system(" " + binary + " \
                    -f " + lua + " \
                    -h " + input_hist + " \
                    -z " + output_hist + " \
                    -n 10 -x -e  " + seed + " -i " + sim_time + " " + bwt + " " + r0 + " " + light_r_ratio + " " + ms + " " + mass_ratio + " \
                    2>>~/research/like_surface/2d_parameter_sweeps/bt_vs_m.txt")
            m_counter = m_counter + m[2]
            ms = str(m_counter) 
        bwt_counter = bwt_counter + bt[2]
        bwt = str(bwt_counter) 
 
#  BACKWARDS TIME VS MASS RATIO #
if(run_bt_v_mr == True):
    bwt_counter = bt[0]
    bwt = str(bwt_counter)
    while bwt_counter < bt[1]:
        mr_counter = m_r[0]
        mr = str(mr_counter)
        while mr_counter < m_r[1]:
            os.system(" " + binary + " \
                    -f " + lua + " \
                    -h " + input_hist + " \
                    -z " + output_hist + " \
                    -n 10 -x -e  " + seed + " -i " + sim_time + " " + bwt + " " + r0 + " " + light_r_ratio + " " + mass + " " + mr + " \
                    2>>~/research/like_surface/2d_parameter_sweeps/bt_vs_mr.txt")
            mr_counter = mr_counter + m_r[2]
            mr = str(mr_counter) 
        bwt_counter = bwt_counter + bt[2]
        bwt = str(bwt_counter)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#  RAD VS RAD RATIO #
if(run_r_v_rr == True):
    r_counter = r[0]
    rad = str(r_counter)
    while r_counter < r[1]:
        rr_counter = r_r[0]
        rr = str(rr_counter)
        while rr_counter < r_r[1]:
            os.system(" " + binary + " \
                    -f " + lua + " \
                    -h " + input_hist + " \
                    -z " + output_hist + " \
                    -n 10 -x -e  " + seed + " -i " + sim_time + " " + back_time + " " + rad + " " + rr + " " + mass + " " + mass_ratio + " \
                    2>>~/research/like_surface/2d_parameter_sweeps/r_vs_rr.txt")
            rr_counter = rr_counter + r_r[2]
            rr = str(rr_counter)
        r_counter = r_counter + r[2]
        rad = str(r_counter)


#  RAD VS MASS #
if(run_r_v_m == True):
    r_counter = r[0]
    rad = str(r_counter)
    while r_counter < r[1]:
        m_counter = m[0]
        ms = str(m_counter)
        while m_counter < m[1]:
            os.system(" " + binary + " \
                    -f " + lua + " \
                    -h " + input_hist + " \
                    -z " + output_hist + " \
                    -n 10 -x -e  " + seed + " -i " + sim_time + " " + back_time + " " + rad + " " + light_r_ratio + " " + ms + " " + mass_ratio + " \
                    2>>~/research/like_surface/2d_parameter_sweeps/r_vs_m.txt")
            m_counter = m_counter + m[2]
            ms = str(m_counter) 
        r_counter = r_counter + r[2]
        rad = str(r_counter)
 
#  RAD VS MASS RATIO #
if(run_r_v_mr == True):
    r_counter = r[0]
    rad = str(r_counter)
    while r_counter < r[1]:
        mr_counter = m_r[0]
        mr = str(mr_counter)
        while mr_counter < m_r[1]:
            os.system(" " + binary + " \
                    -f " + lua + " \
                    -h " + input_hist + " \
                    -z " + output_hist + " \
                    -n 10 -x -e  " + seed + " -i " + sim_time + " " + back_time + " " + rad + " " + light_r_ratio + " " + mass + " " + mr + " \
                    2>>~/research/like_surface/2d_parameter_sweeps/r_vs_mr.txt")
            mr_counter = mr_counter + m_r[2]
            mr = str(mr_counter) 
        r_counter = r_counter + r[2]
        rad = str(r_counter)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#  RAD RATIO VS MASS #
if(run_rr_v_m == True):
    rr_counter = r_r[0]
    rr = str(rr_counter)
    while rr_counter < r_r[1]:
        m_counter = m[0]
        ms = str(m_counter)
        while m_counter < m[1]:
            os.system(" " + binary + " \
                    -f " + lua + " \
                    -h " + input_hist + " \
                    -z " + output_hist + " \
                    -n 10 -x -e  " + seed + " -i " + sim_time + " " + back_time + " " + r0 + " " + rr + " " + ms + " " + mass_ratio + " \
                    2>>~/research/like_surface/2d_parameter_sweeps/rr_vs_m.txt")
            m_counter = m_counter + m[2]
            ms = str(m_counter) 
        rr_counter = rr_counter + r_r[2]
        rr = str(rr_counter)
 
#  RAD RATIO VS MASS RATIO #
if(run_rr_v_mr == True):
    rr_counter = r_r[0]
    rr = str(rr_counter)
    while rr_counter < r_r[1]:
        mr_counter = m_r[0]
        mr = str(mr_counter)
        while mr_counter < m_r[1]:
            os.system(" " + binary + " \
                    -f " + lua + " \
                    -h " + input_hist + " \
                    -z " + output_hist + " \
                    -n 10 -x -e  " + seed + " -i " + sim_time + " " + back_time + " " + r0 + " " + rr + " " + mass + " " + mr + " \
                    2>>~/research/like_surface/2d_parameter_sweeps/rr_vs_mr.txt")
            mr_counter = mr_counter + m_r[2]
            mr = str(mr_counter) 
        rr_counter = rr_counter + r_r[2]
        rr = str(rr_counter)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#  MASS VS MASS RATIO #
if(run_m_v_mr == True):
    m_counter = m[0]
    ms = str(m_counter)
    while m_counter < m[1]:
        mr_counter = m_r[0]
        mr = str(mr_counter)
        while mr_counter < m_r[1]:
            os.system(" " + binary + " \
                    -f " + lua + " \
                    -h " + input_hist + " \
                    -z " + output_hist + " \
                    -n 10 -x -e  " + seed + " -i " + sim_time + " " + back_time + " " + r0 + " " + light_r_ratio + " " + ms + " " + mr + " \
                    2>>~/research/like_surface/2d_parameter_sweeps/m_vs_mr.txt")
            mr_counter = mr_counter + m_r[2]
            mr = str(mr_counter) 
        m_counter = m_counter + m[2]
        ms = str(m_counter)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
