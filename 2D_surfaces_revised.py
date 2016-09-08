#! /usr/bin/python
#/* Copyright (c) 2016 Siddhartha Shelton */
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

lmc_dir = '~/research/'
sid_dir = '/home/sidd/Desktop/research/'
sgr_dir = '/Users/master/sidd_research/'
path = lmc_dir


binary        = path + "nbody_test/bin/milkyway_nbody"
lua           = path + "/lua/EMD_v162.lua"
seed          = "98213548"
#input_hist    = "~/research/like_surface/histogram_in_seed"  + seed + "_20kEMD_4_1_p2_p2_12_p2.hist"
#output_hist   = "~/research/like_surface/histogram_out_seed" + seed + "_20kEMD_4_1_p2_p2_12_sweep.hist"

input_hist    = folder + "arg_" + ft_c + "_" + bt_c + "_" + r_c + "_" + rr_c + "_" + m_c + "_" + mr_c + "_correct.hist"


#parameter = [start, end, increment]
ft         = [3.9, 4.2, 0.01]#30
bt         = [0.96, 1.08, 0.005]#24
r          = [0.1, 0.8, 0.01]#80
r_r        = [0.1, 0.8, 0.01]#80
m          = [1.0, 20.0, 0.25]#80
m_r        = [0.20, 0.30, 0.001]#70

ft_N = 40
bt_N = 40
r_N  = 40
rr_N = 40
m_N  = 40
mr_N = 40



y = True
n  = False


#choose what to run
rebuild_binary            = n
make_correct_answer_hist  = y
run_regular_iteration     = y
run_random_iteration      = y



run_ft_v_bt = n
run_ft_v_r  = n
run_ft_v_rr = n
run_ft_v_m  = n
run_ft_v_mr = n

run_bt_v_r  = n
run_bt_v_rr = n
run_bt_v_m  = n
run_bt_v_mr = n

run_r_v_rr  = n
run_r_v_m   = n
run_r_v_mr  = n

run_rr_v_m  = n
run_rr_v_mr = y

run_m_v_mr  = y
#--------------------------------------------------------------------------------------------------

#this makes a comparison histogram
def rebuild():
    os.chdir(".")
    #os.system("rm -r ~/research/nbody_test")
    #os.system("mkdir ~/research/nbody_test")
    os.chdir("../nbody_test")
    os.system("cmake -DCMAKE_BUILD_TYPE=Release -DBOINC_RELEASE_NAMES=OFF -DNBODY_GL=OFF -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/research/milkywayathome_client/")
    os.system("make -j ")
    os.chdir("../like_surface")

def make_correct():
    os.system(" " + binary + " \
        -f " + lua + " \
        -z " + input_hist + " \
        -b -e " + seed + " -i "+ ft_c + " " + bt_c + " " + r_c + " " + rr_c + " " + m_c + " " + mr_c )



def nbody(output_hist, ft, bt, r, rr, m, mr, file_name, sweep_name):
    os.system(" " + binary + " \
                -f " + lua + " \
                -h " + input_hist + " \
                -z " + output_hist + " \
                -b -e " + seed + " -i " + ft + " " + bt + " " + r + " " + rr + " " + m + " " + mr + " \
                2>>" + folder + "parameter_sweeps" + sweep_name + "/" + file_name + ".txt")
    return 0
    
def para_init(para, counter):
    name = str(counter)
    do_correct == False
    ft_tmp = ft_c
    bt_tmp = bt_c
    r_tmp  = r_c
    rr_tmp = rr_c
    m_tmp  = m_c
    mr_tmp = mr_c
    
    if(para == 'ft'):
            ft_tmp = name
        if(counter < args[0] and counter + intv > args[0]):
            do_correct = True
    elif(para == 'bt'):
        bt_tmp = name
        if(counter < args[1] and counter + intv > args[1]):
            do_correct = True
    elif(para == 'r'):
        r_tmp = name
        if(counter < args[2] and counter + intv > args[2]):
            do_correct = True
    elif(para == 'rr'):
        rr_tmp = name
        if(counter < args[3] and counter + intv > args[3]):
            do_correct = True
    elif(para == 'm'):
        m_tmp = name
        if(counter < args[4] and counter + intv > args[4]):
            do_correct = True
    elif(para == 'mr'):
        mr_tmp = name
        if(counter < args[5] and counter + intv > args[5]):
            do_correct = True
    
    return ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, do_correct
            
def run_sweep(start1, end1, intv1, start2, end2, intv2, para1, para2):
    counter1 = start1
    counter2 = start2
    name1 = str(counter1)
    name2 = str(counter2)
    sweep_name = ""
    os.system("mkdir hists/parameter_sweeps" + sweep_name)
    data_vals   = "hists/parameter_sweeps" + sweep_name + "/" + para + "_vals.txt"
    f = open(data_vals, 'a')
    
    ft_tmp = ft_c
    bt_tmp = bt_c
    r_tmp  = r_c
    rr_tmp = rr_c
    m_tmp  = m_c
    mr_tmp = mr_c
    do_correct1 = False
    do_correct2 = False
    pipe_name = para1 + "_" + para2
    
    while counter1 < end1:
        counter2 = start2
        name2 = str(counter2)
        output_hist = folder + para + "_hists/" + "arg_"
        
        #ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, do_correct1 = para_init(para1, counter1)
        
        if(para1 == 'ft'):
            ft_tmp = name1
            if(counter1 < args[0] and counter1 + intv1 > args[0]):
                do_correct1 = True
        elif(para1 == 'bt'):
            bt_tmp = name1
            if(counter1 < args[1] and counter1 + intv1 > args[1]):
                do_correct1 = True
        elif(para1 == 'r'):
            r_tmp = name1
            if(counter1 < args[2] and counter1 + intv1 > args[2]):
                do_correct1 = True
        elif(para1 == 'rr'):
            rr_tmp = name1
            if(counter1 < args[3] and counter1 + intv1 > args[3]):
                do_correct1 = True
        elif(para1 == 'm'):
            m_tmp = name1
            if(counter1 < args[4] and counter1 + intv1 > args[4]):
                do_correct1 = True
        elif(para1 == 'mr'):
            mr_tmp = name1
            if(counter1 < args[5] and counter1 + intv1 > args[5]):
                do_correct1 = True
            
        while counter2 < end2:
            if(para2 == 'ft'):
                ft_tmp = name2
                if(counter2 < args[0] and counter2 + intv2 > args[0]):
                    do_correct2 = True
            elif(para2 == 'bt'):
                bt_tmp = name2
                if(counter2 < args[0] and counter2 + intv2 > args[0]):
                    do_correct2 = True
            elif(para2 == 'r'):
                r_tmp = name2
                if(counter2 < args[0] and counter2 + intv2 > args[0]):
                    do_correct2 = True
            elif(para2 == 'rr'):
                rr_tmp = name2
                if(counter2 < args[0] and counter2 + intv2 > args[0]):
                    do_correct2 = True
            elif(para2 == 'm'):
                m_tmp = name2
                if(counter2 < args[0] and counter2 + intv2 > args[0]):
                    do_correct2 = True
            elif(para2 == 'mr'):
                mr_tmp = name2
                if(counter2 < args[0] and counter2 + intv2 > args[0]):
                    do_correct2 = True
            
            
            output_hist += ft_tmp + "_" + bt_tmp + "_" + r_tmp + "_" + rr_tmp + "_" + m_tmp + "_" + mr_tmp + ".hist"
            nbody(output_hist, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, pipe_name, sweep_name)
            f.write("%s\t%s  \n" % (name1, name2))
            
            if(do_correct2 == True):
                
                if(para2 == 'ft'):
                    ft_tmp = ft_c
                    f.write("%s\t%s \n" % (name1, ft_c))
                elif(para2 == 'bt'):
                    bt_tmp = bt_c
                    f.write("%s\t%s \n" % (name1, bt_c))
                elif(para2 == 'r'):
                    r_tmp  = r_c
                    f.write("%s\t%s \n" % (name1, r_c))
                elif(para2 == 'rr'):
                    rr_tmp = rr_c
                    f.write("%s\t%s \n" % (name1, rr_c))
                elif(para2 == 'm'):
                    m_tmp  = m_c
                    f.write("%s\t%s \n" % (name1, m_c))
                elif(para2 == 'mr'):
                    mr_tmp = mr_c
                    f.write("%s\t%s \n" % (name1, mr_c))
                    
                output_hist = folder + para + "_hists/" + "arg_" + ft_tmp + "_" + bt_tmp + "_" + r_tmp + "_" + rr_tmp + "_" + m_tmp + "_" + mr_tmp + ".hist"
                nbody(output_hist, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, pipe_name, sweep_name)
                do_correct2 = False
                
            counter2 += intv2
            name2 = str(counter2)
        
        if(do_correct1 == True):
            if(para1 == 'ft'):
                ft_tmp = ft_c
                name_tmp = ft_c
            elif(para1 == 'bt'):
                bt_tmp = bt_c
                name_tmp = bt_c
            elif(para1 == 'r'):
                r_tmp  = r_c
                name_tmp = r_c
            elif(para1 == 'rr'):
                rr_tmp = rr_c
                name_tmp = rr_c
            elif(para1 == 'm'):
                m_tmp  = m_c
                name_tmp = m_c
            elif(para1 == 'mr'):
                mr_tmp = mr_c
                name_tmp = mr_c
                
            while counter2 < end2:
                if(para2 == 'ft'):
                    ft_tmp = name2
                    if(counter2 < args[0] and counter2 + intv2 > args[0]):
                        do_correct2 = True
                elif(para2 == 'bt'):
                    bt_tmp = name2
                    if(counter2 < args[0] and counter2 + intv2 > args[0]):
                        do_correct2 = True
                elif(para2 == 'r'):
                    r_tmp = name2
                    if(counter2 < args[0] and counter2 + intv2 > args[0]):
                        do_correct2 = True
                elif(para2 == 'rr'):
                    rr_tmp = name2
                    if(counter2 < args[0] and counter2 + intv2 > args[0]):
                        do_correct2 = True
                elif(para2 == 'm'):
                    m_tmp = name2
                    if(counter2 < args[0] and counter2 + intv2 > args[0]):
                        do_correct2 = True
                elif(para2 == 'mr'):
                    mr_tmp = name2
                    if(counter2 < args[0] and counter2 + intv2 > args[0]):
                        do_correct2 = True
                
                
                output_hist += ft_tmp + "_" + bt_tmp + "_" + r_tmp + "_" + rr_tmp + "_" + m_tmp + "_" + mr_tmp + ".hist"
                nbody(output_hist, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, pipe_name, sweep_name)
                f.write("%s\t%s  \n" % (name_tmp, name2))
                
                if(do_correct2 == True):
                    output_hist = folder + para + "_hists/" + "arg_" + ft_c + "_" + bt_c + "_" + r_c + "_" + rr_c + "_" + m_c + "_" + mr_c + ".hist"
                    nbody(output_hist, ft_c, bt_c, r_c, rr_c, m_c, mr_c, para, sweep_name)
                    do_correct1 = False
                    do_correct2 = False        
                    
                    
                    if(para2 == 'ft'):
                        ft_tmp = ft_c
                        f.write("%s\t%s \n" % (name_tmp, ft_c))
                    elif(para2 == 'bt'):
                        bt_tmp = bt_c
                        f.write("%s\t%s \n" % (name_tmp, bt_c))
                    elif(para2 == 'r'):
                        r_tmp  = r_c
                        f.write("%s\t%s \n" % (name_tmp, r_c))
                    elif(para2 == 'rr'):
                        rr_tmp = rr_c
                        f.write("%s\t%s \n" % (name_tmp, rr_c))
                    elif(para2 == 'm'):
                        m_tmp  = m_c
                        f.write("%s\t%s \n" % (name_tmp, m_c))
                    elif(para2 == 'mr'):
                        mr_tmp = mr_c
                        f.write("%s\t%s \n" % (name_tmp, mr_c))
        
        counter1 += intv1
        name1 = str(counter1)
    f.close()
    return 0