#! /usr/bin/python
#/* Copyright (c) 2016 Siddhartha Shelton */
import os
from subprocess import call
import random
#--------------------------------------------------------------------------------------------------
#       PARAMETER LIBRARY       #
#--------------------------------------------------------------------------------------------------
args = [3.95, 0.98, 0.2, 0.2, 12, 0.2]

ft_c  = str(args[0])
bt_c  = str(args[1])
r_c   = str(args[2])
rr_c  = str(args[3])
m_c   = str(args[4])
mr_c  = str(args[5])

folder        = "~/research/like_surface/hists/"
binary        = "~/research/nbody_test/bin/milkyway_nbody"
lua           = "~/research/lua/EMD_v162.lua"
seed          = "98213548"

input_hist    = folder + "arg_" + ft_c + "_" + bt_c + "_" + r_c + "_" + rr_c + "_" + m_c + "_" + mr_c + "_correct.hist"
#output_hist   = folder + "histogram_out_20kEMD_sweep.hist"
#parameter    = [start, end, number of points]
ft_rg         = [3.0, 5.0, 20]#20
bt_rg         = [0.8, 1.2, 20]#10
r_rg          = [0.1, 1.3, 20]#20
rr_rg         = [0.1, .95, 20]#17
m_rg          = [1., 120.0, 20]#23
mr_rg         = [.01, .95, 20]#18


y = True
n = False
random.seed(a = 12345678)

#choose what to run
rebuild_binary            = n
make_correct_answer_hist  = n

run_forward_evole_time    = y
run_backward_evolve_ratio = y
run_radius                = y
run_radius_ratio          = y
run_mass                  = y
run_mass_ratio            = y
#--------------------------------------------------------------------------------------------------

def rebuild():
    os.chdir(".")
    #os.system("rm -r ~/research/nbody_test")
    #os.system("mkdir ~/research/nbody_test")
    os.chdir("../nbody_test")
    os.system("cmake -DCMAKE_BUILD_TYPE=Release -DBOINC_RELEASE_NAMES=OFF -DNBODY_GL=OFF -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/research/milkywayathome_client/")
    os.system("make -j ")
    os.chdir("../like_surface")

#this makes a comparison histogram
def make_correct():
    os.system(" " + binary + " \
        -f " + lua + " \
        -z " + input_hist + " \
        -b -e " + seed + " -i "+ ft_c + " " + bt_c + " " + r_c + " " + rr_c + " " + m_c + " " + mr_c )

def nbody(output_hist, ft, bt, r, rr, m, mr, file_name):
    os.system(" " + binary + " \
                -f " + lua + " \
                -h " + input_hist + " \
                -z " + output_hist + " \
                -b -e " + seed + " -i " + ft + " " + bt + " " + r + " " + rr + " " + m + " " + mr + " \
                2>>" + folder + "parameter_sweeps/" + file_name + ".txt")
    return 0
    
def run_sweep(start, end, N, para):
    counter = 0.0
    data_vals   = "hists/parameter_sweeps/" + para + "_vals.txt"
    f = open(data_vals, 'a')
    
    #get the correct answer hist
    output_hist = folder + para + "_hists/" + "arg_" + ft_c + "_" + bt_c + "_" + r_c + "_" + rr_c + "_" + m_c + "_" + mr_c + ".hist"
    nbody(output_hist, ft_c, bt_c, r_c, rr_c, m_c, mr_c, para)
    
    while counter < N:
        output_hist = folder + para + "_hists/" + "arg_"
        name = random.uniform(0.0, 1.0) * (end - start) + start
        name = str(name)
        
        if(para == 'ft'):
            if(counter == 0.0):
                f.write("%s \n" % ft_c)
            output_hist += name + "_" + bt_c + "_" + r_c + "_" + rr_c + "_" + m_c + "_" + mr_c + ".hist"
            nbody(output_hist, name, bt_c, r_c, rr_c, m_c, mr_c, para)
            
            
        elif(para == 'bt'):
            if(counter == 0.0):
                f.write("%s \n" % bt_c)
            output_hist += ft_c + "_" + name + "_" + r_c + "_" + rr_c + "_" + m_c + "_" + mr_c + ".hist"
            nbody(output_hist, ft_c, name, r_c, rr_c, m_c, mr_c, para)
            
        
        elif(para == 'r'):
            if(counter == 0.0):
                f.write("%s \n" % r_c)
            output_hist += ft_c + "_" + bt_c + "_" + name + "_" + rr_c + "_" + m_c + "_" + mr_c + ".hist"
            nbody(output_hist, ft_c, bt_c, name, rr_c, m_c, mr_c, para)
            
        
        elif(para == 'rr'):
            if(counter == 0.0):
                f.write("%s \n" % rr_c)
            output_hist += ft_c + "_" + bt_c + "_" + r_c + "_" + name + "_" + m_c + "_" + mr_c + ".hist"
            nbody(output_hist, ft_c, bt_c, r_c, name, m_c, mr_c, para)
            
        
        elif(para == 'm'):
            if(counter == 0.0):
                f.write("%s \n" % m_c)
            output_hist += ft_c + "_" + bt_c + "_" + r_c + "_" + rr_c + "_" + name + "_" + mr_c + ".hist"
            nbody(output_hist, ft_c, bt_c, r_c, rr_c, name, mr_c, para)
            
        
        elif(para == 'mr'):
            if(counter == 0.0):
                f.write("%s \n" % mr_c)
            output_hist += ft_c + "_" + bt_c + "_" + r_c + "_" + rr_c + "_" + m_c + "_" + name + ".hist"
            nbody(output_hist, ft_c, bt_c, r_c, rr_c, m_c, name, para)
            
          
        f.write("%s \n" % name)
        counter += 1
    f.close()    
    return 0
        
        
        
def main():
    if(rebuild_binary == True):
        rebuild()
        
    if(make_correct_answer_hist == True):
        make_correct()
        
    if(run_forward_evole_time == True):
         run_sweep(ft_rg[0], ft_rg[1], ft_rg[2], 'ft')
    
    if(run_backward_evolve_ratio == True):
         run_sweep(bt_rg[0], bt_rg[1], bt_rg[2], 'bt')
         
    if(run_radius == True):
         run_sweep(r_rg[0], r_rg[1], r_rg[2], 'r')
         
    if(run_radius_ratio == True):
         run_sweep(rr_rg[0], rr_rg[1], rr_rg[2], 'rr')
         
    if(run_mass == True):
         run_sweep(m_rg[0], m_rg[1], m_rg[2], 'm')
         
    if(run_mass_ratio == True):
         run_sweep(mr_rg[0], mr_rg[1], mr_rg[2], 'mr')
    
    return 0
    
main()