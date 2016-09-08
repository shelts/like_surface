#! /usr/bin/python
#/* Copyright (c) 2016 Siddhartha Shelton */
import os
from subprocess import call
#--------------------------------------------------------------------------------------------------
#       PARAMETER LIBRARY       #
#--------------------------------------------------------------------------------------------------
args = [3.95, 0.98, 0.2, 0.2, 6, 0.2]
ft_cn  = (args[0])#cn for correct number
bt_cn  = (args[1])
r_cn   = (args[2])
rr_cn  = (args[3])
m_cn   = (args[4])
mr_cn  = (args[5])



ft_c  = str(args[0])
bt_c  = str(args[1])
r_c   = str(args[2])
rr_c  = str(args[3])
m_c   = str(args[4])
mr_c  = str(args[5])



lmc_dir = '~/research/'
sid_dir = '/home/sidd/Desktop/research/'
sgr_dir = '/Users/master/sidd_research/'
path = sid_dir

folder        = path + "like_surface/2d_sweep_hists/"
binary        = path + "nbody_test/bin/milkyway_nbody"
lua           = path + "/lua/EMD_v162.lua"
seed          = "98213548"
#input_hist    = "~/research/like_surface/histogram_in_seed"  + seed + "_20kEMD_4_1_p2_p2_12_p2.hist"
#output_hist   = "~/research/like_surface/histogram_out_seed" + seed + "_20kEMD_4_1_p2_p2_12_sweep.hist"

input_hist    = folder + "arg_" + ft_c + "_" + bt_c + "_" + r_c + "_" + rr_c + "_" + m_c + "_" + mr_c + "_correct.hist"


#parameter = [start, end, increment]
ft         = [3.92, 4.0, 0.02]#30
bt         = [0.97, 1.08, 0.02]#24
r          = [0.1, 0.4, 0.2]#80
rr         = [0.1, 0.4, 0.2]#80
m          = [1.0, 7.0, 2.0]#80
mr         = [0.150, 0.35, 0.1]#70

ft_s, ft_e, ft_in = ft[0], ft[1], ft[2]
bt_s, bt_e, bt_in = bt[0], bt[1], bt[2]
r_s,  r_e,  r_in  = r[0],  r[1],  r[2]
rr_s, rr_e, rr_in = rr[0], rr[1], rr[2]
m_s,  m_e,  m_in  = m[0],  m[1],  m[2]
mr_s, mr_e, mr_in = mr[0], mr[1], mr[2]

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



run_ft_v_bt = y
run_ft_v_r  = y
run_ft_v_rr = y
run_ft_v_m  = y
run_ft_v_mr = y

run_bt_v_r  = y
run_bt_v_rr = y
run_bt_v_m  = y
run_bt_v_mr = y

run_r_v_rr  = y
run_r_v_m   = y
run_r_v_mr  = y

run_rr_v_m  = y
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
    
def para_init(para, counter, intv, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp):
    name = str(counter)
    do_correct = False

    if(para == 'ft'):
        ft_tmp = name
        if(counter < ft_cn and counter + intv > ft_cn):
            do_correct = True
    elif(para == 'bt'):
        bt_tmp = name
        if(counter < bt_cn and counter + intv > bt_cn):
            do_correct = True
    elif(para == 'r'):
        r_tmp = name
        if(counter < r_cn and counter + intv > r_cn):
            do_correct = True
    elif(para == 'rr'):
        rr_tmp = name
        if(counter < rr_cn and counter + intv > rr_cn):
            do_correct = True
    elif(para == 'm'):
        m_tmp = name
        if(counter < m_cn and counter + intv > m_cn):
            do_correct = True
    elif(para == 'mr'):
        mr_tmp = name
        if(counter < mr_cn and counter + intv > mr_cn):
            do_correct = True
    
    return ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, do_correct

def write_correct(f, para, name):
    if(para == 'ft'):
        ft_tmp = ft_c
        f.write("%s\t%s \n" % (name, ft_c))
    elif(para == 'bt'):
        bt_tmp = bt_c
        f.write("%s\t%s \n" % (name, bt_c))
    elif(para == 'r'):
        r_tmp  = r_c
        f.write("%s\t%s \n" % (name, r_c))
    elif(para == 'rr'):
        rr_tmp = rr_c
        f.write("%s\t%s \n" % (name, rr_c))
    elif(para == 'm'):
        m_tmp  = m_c
        f.write("%s\t%s \n" % (name, m_c))
    elif(para == 'mr'):
        mr_tmp = mr_c
        f.write("%s\t%s \n" % (name, mr_c))
    return 0

def correct_set(para, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp) 
    if(para == 'ft'):
        ft_tmp = ft_c
        name = ft_c
    elif(para == 'bt'):
        bt_tmp = bt_c
        name1 = bt_c
    elif(para == 'r'):
        r_tmp  = r_c
        name = r_c
    elif(para == 'rr'):
        rr_tmp = rr_c
        name = rr_c
    elif(para == 'm'):
        m_tmp  = m_c
        name1 = m_c
    elif(para == 'mr'):
        mr_tmp = mr_c
        name = mr_c
        
    return ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, name
        
def run_sweep(start1, end1, intv1, para1, start2, end2, intv2, para2):
    counter1 = start1
    counter2 = start2
    name1 = str(counter1)
    name2 = str(counter2)
    sweep_name = ""
    pipe_name = para1 + "_" + para2
    
    os.system("mkdir " + folder + "parameter_sweeps" + sweep_name)
    data_vals   = folder + "parameter_sweeps" + sweep_name + "/" + pipe_name + "_vals.txt"
    f = open(data_vals, 'w')
    
    ft_tmp = ft_c
    bt_tmp = bt_c
    r_tmp  = r_c
    rr_tmp = rr_c
    m_tmp  = m_c
    mr_tmp = mr_c
    do_correct1 = False
    do_correct2 = False
    
    while counter1 < end1 + intv1:
        counter2 = start2
        name2 = str(counter2)
        
        ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, do_correct1 = para_init(para1, counter1, intv1, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp )
            
        while counter2 < end2 + intv2:
            output_hist = folder + pipe_name + "/" + "arg_"
            ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, do_correct2 = para_init(para2, counter2, intv2, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp )
            
            
            output_hist += ft_tmp + "_" + bt_tmp + "_" + r_tmp + "_" + rr_tmp + "_" + m_tmp + "_" + mr_tmp + ".hist"
            nbody(output_hist, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, pipe_name, sweep_name)
            f.write("%s\t%s  \n" % (name1, name2))
            
            if(do_correct2 == True):
                write_correct(f, para2, name1)
                    
                output_hist = folder + pipe_name + "/" + "arg_" + ft_tmp + "_" + bt_tmp + "_" + r_tmp + "_" + rr_tmp + "_" + m_tmp + "_" + mr_tmp + ".hist"
                nbody(output_hist, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, pipe_name, sweep_name)
                do_correct2 = False
                
            counter2 += intv2
            name2 = str(counter2)
            
        if(do_correct1 == True):
            name1_save = name1
            ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, name1 = correct_set(para1, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp)
                
            counter2 = start2
            name2 = str(counter2)
            while counter2 < end2 + intv2:
                output_hist = folder + pipe_name + "/" + "arg_"
                ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, do_correct2 = para_init(para2, counter2, intv2, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp )
                
                
                output_hist += ft_tmp + "_" + bt_tmp + "_" + r_tmp + "_" + rr_tmp + "_" + m_tmp + "_" + mr_tmp + ".hist"
                nbody(output_hist, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, pipe_name, sweep_name)
                f.write("%s\t%s  \n" % (name1, name2))
                
                if(do_correct2 == True):
                    output_hist = folder + pipe_name + "/" + "arg_" + ft_c + "_" + bt_c + "_" + r_c + "_" + rr_c + "_" + m_c + "_" + mr_c + ".hist"
                    nbody(output_hist, ft_c, bt_c, r_c, rr_c, m_c, mr_c, pipe_name, sweep_name)
                    do_correct2 = False
                    
                    write_correct(f, para2, name1)

                        
                counter2 += intv2
                name2 = str(counter2)
            name1 = name1_save
            do_correct1 = False        
        counter1 += intv1
        name1 = str(counter1)
    f.close()
    return 0



def main():
    if(rebuild_binary):
        rebuild()
        
    if(make_correct_answer_hist):
        make_correct()
    
    
    if(run_regular_iteration):
        if(run_ft_v_bt):
            run_sweep(ft_s, ft_e, ft_in, 'ft', bt_s, bt_e, bt_in, 'bt')
        if(run_ft_v_r ):
            run_sweep(ft_s, ft_e, ft_in, 'ft', r_s,  r_e,  r_in,  'r')
        if(run_ft_v_rr):
            run_sweep(ft_s, ft_e, ft_in, 'ft', rr_s, rr_e, rr_in, 'rr')
        if(run_ft_v_m ):
            run_sweep(ft_s, ft_e, ft_in, 'ft', m_s,  m_e,  m_in,  'm')
        if(run_ft_v_mr):
            run_sweep(ft_s, ft_e, ft_in, 'ft', mr_s, mr_e, mr_in, 'mr')
            
        if(run_bt_v_r  ):
            run_sweep(bt_s, bt_e, bt_in, 'bt', r_s,  r_e,  r_in,  'r')
        if(run_bt_v_rr ):
            run_sweep(bt_s, bt_e, bt_in, 'bt', rr_s, rr_e, rr_in, 'rr')
        if(run_bt_v_m  ):
            run_sweep(bt_s, bt_e, bt_in, 'bt', m_s,  m_e,  m_in,  'm')
        if(run_bt_v_mr ):
            run_sweep(bt_s, bt_e, bt_in, 'bt', mr_s, mr_e, mr_in, 'mr')
            
            
        if(run_r_v_rr  ):
            run_sweep(r_s,  r_e,  r_in,  'r',  rr_s, rr_e, rr_in, 'rr')
        if(run_r_v_m   ):
            run_sweep(r_s,  r_e,  r_in,  'r',  m_s,  m_e,  m_in,  'm')
        if(run_r_v_mr  ):
            run_sweep(r_s,  r_e,  r_in,  'r',  mr_s, mr_e, mr_in, 'mr')
            
        if(run_rr_v_m  ):
            run_sweep(rr_s, rr_e, rr_in, 'rr', m_s,  m_e,  m_in,  'm')
        if(run_rr_v_mr ):
            run_sweep(rr_s, rr_e, rr_in, 'rr', mr_s, mr_e, mr_in, 'mr')
            
        if(run_m_v_mr  ):
            run_sweep(m_s,  m_e,  m_in,  'm',  mr_s, mr_e, mr_in, 'mr')
            
            
            
main()
            
        