#! /usr/bin/python
#/* Copyright (c) 2016 Siddhartha Shelton */
import os
from subprocess import call
import random
random.seed(a = 12345678)
#--------------------------------------------------------------------------------------------------
#       PARAMETER LIBRARY       #
#--------------------------------------------------------------------------------------------------
args = [3.95, 0.98, 0.2, 0.2, 12, 0.2]
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
lua           = path + "/lua/full_control.lua"
seed          = "98213548"

input_hist    = folder + "arg_" + ft_c + "_" + bt_c + "_" + r_c + "_" + rr_c + "_" + m_c + "_" + mr_c + "_correct.hist"


#parameter = [start, end, increment]
ft         = [3.0, 4.0, 0.001]#
#bt         = [0.97, 1.08, 0.02]#
bt         = [0.97, 1.08, 0.02]#
r          = [0.1, 0.4, 0.2]#
rr         = [0.1, 0.4, 0.2]#
m          = [1.0, 7.0, 2.0]#
mr         = [0.150, 0.35, 0.1]#

ft_s, ft_e, ft_in = ft[0], ft[1], ft[2]
bt_s, bt_e, bt_in = bt[0], bt[1], bt[2]
r_s,  r_e,  r_in  = r[0],  r[1],  r[2]
rr_s, rr_e, rr_in = rr[0], rr[1], rr[2]
m_s,  m_e,  m_in  = m[0],  m[1],  m[2]
mr_s, mr_e, mr_in = mr[0], mr[1], mr[2]

ft_N = 25
bt_N = 25
r_N  = 4
rr_N = 25
m_N  = 4
mr_N = 25



y = True
n  = False


#choose what to run.
make_folders              = n
rebuild_binary            = n
make_correct_answer_hist  = n
run_regular_iteration     = n
run_random_iteration      = n



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

run_m_v_mr  = n
#--------------------------------------------------------------------------------------------------


def rebuild():#rebuilds nbody
    os.chdir(".")
    #os.system("rm -r ~/research/nbody_test")
    #os.system("mkdir ~/research/nbody_test")
    os.chdir("../nbody_test")
    os.system("cmake -DCMAKE_BUILD_TYPE=Release -DBOINC_RELEASE_NAMES=OFF -DNBODY_GL=OFF -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/research/milkywayathome_client/")
    os.system("make -j ")
    os.chdir("../like_surface")

def make_correct(): #makes the correct answer histogram
    os.system(" " + binary + " \
        -f " + lua + " \
        -z " + input_hist + " \
        -b -e " + seed + " -i "+ ft_c + " " + bt_c + " " + r_c + " " + rr_c + " " + m_c + " " + mr_c )

def nbody(output_hist, ft, bt, r, rr, m, mr, file_name, sweep_name):
    os.system(" " + binary + " \
                -f " + lua + " \
                -h " + input_hist + " \
                -z " + output_hist + " \
                -n 14 -b -e " + seed + " -i " + ft + " " + bt + " " + r + " " + rr + " " + m + " " + mr + " \
                2>>" + folder + "parameter_sweeps" + sweep_name + "/" + file_name + ".txt")
    return 0

def para_init_rand(para, name, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp):
    if(para == 'ft'):#initializes the needed parameter to the value
        ft_tmp = name
    elif(para == 'bt'):
        bt_tmp = name
    elif(para == 'r'):
        r_tmp = name
    elif(para == 'rr'):
        rr_tmp = name
    elif(para == 'm'):
        m_tmp = name
    elif(para == 'mr'):
        mr_tmp = name
    
    return ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp

def para_init(para, counter, intv, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp):
    name = str(counter)
    do_correct = False
    #initializes the needed parameter to the value and also checks if the correct answer falls within the iteration interval
    #returns the full list of parameters and whether the correct answer is there.
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
    if(para == 'ft'):#writes the correct values and name to a file for the needed parameter
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

def correct_set(para, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp): 
    name = 0.0 
    #this sets the correct value for the parameter needed. returns the full list of parameters.
    if(para == 'ft'):
        ft_tmp = ft_c
        name = ft_c
    elif(para == 'bt'):
        bt_tmp = bt_c
        name = bt_c
    elif(para == 'r'):
        r_tmp  = r_c
        name = r_c
    elif(para == 'rr'):
        rr_tmp = rr_c
        name = rr_c
    elif(para == 'm'):
        m_tmp  = m_c
        name = m_c
    elif(para == 'mr'):
        mr_tmp = mr_c
        name = mr_c
        
    return ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, name
        
def run_sweep(start1, end1, intv1, para1, start2, end2, intv2, para2):
    counter1 = start1
    counter2 = start2
    name1 = str(counter1)
    name2 = str(counter2)
   
    sweep_name = ""  #sweep name
    
    pipe_name = para1 + "_" + para2  #name of the files
    
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
    
    while counter1 < end1 + intv1:  #this iterates over one parameter on the outside and another on the inside
        counter2 = start2  #restart the inner parameter iteration from beginning
        name2 = str(counter2)
        
        #checks which parameter needs to be updated for the outside loop and updates it
        #also checks to see if the correct answer for the outside lies between current val and next increment, if so it sets do_correct1 to true
        ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, do_correct1 = para_init(para1, counter1, intv1, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp )
        
        
        while counter2 < end2 + intv2:  #inner loop.
            output_hist = folder + pipe_name + "_hists/" + "arg_"  #resets the output hist name
           
            #checks which parameter needs to be updated for the inner loop and updates it
            #also checks if the correct answer for the inner lies between current val and next increment, if so sets do_correct2
            ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, do_correct2 = para_init(para2, counter2, intv2, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp )
            
            
            output_hist += ft_tmp + "_" + bt_tmp + "_" + r_tmp + "_" + rr_tmp + "_" + m_tmp + "_" + mr_tmp + ".hist"  #appends the current parameters to the output hist name
            
            nbody(output_hist, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, pipe_name, sweep_name)  #runs the sim with these parameters
            
            f.write("%s\t%s\n" % (name1, name2))  #writes the value to the value files.
            
            
            if(do_correct2 == True):  #if the correct answer is between the interval for the inner loop, run the correct answer
                write_correct(f, para2, name1)  #writes the correct answers to the value file
                
                output_hist = folder + pipe_name + "_hists/" + "arg_" + ft_tmp + "_" + bt_tmp + "_" + r_tmp + "_" + rr_tmp + "_" + m_tmp + "_" + mr_tmp + ".hist"  #sets the output hist name
                nbody(output_hist, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, pipe_name, sweep_name)
                
                do_correct2 = False  #resets do_correct2
            
            
            counter2 += intv2  #increment the inner loop value
            name2 = str(counter2)
        
        
        if(do_correct1 == True):  #if the outer loop correct answer was found in the interval
            name1_save = name1  #save the current iterated value for the outer loop
            
            ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, name1 = correct_set(para1, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp)  #set the correct values for the outer loop
                
            
            counter2 = start2  #run the same inner loop as above
            name2 = str(counter2)
            while counter2 < end2 + intv2:
                output_hist = folder + pipe_name + "_hists/" + "arg_"  #resets the output hist name
                
                #checks which parameter needs to be updated for the inner loop and updates it
                #also checks if the correct answer for the inner lies between current val and next increment, if so sets do_correct2
                ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, do_correct2 = para_init(para2, counter2, intv2, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp )
                
                
                output_hist += ft_tmp + "_" + bt_tmp + "_" + r_tmp + "_" + rr_tmp + "_" + m_tmp + "_" + mr_tmp + ".hist"  #appends the current parameters to the output hist name
                nbody(output_hist, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, pipe_name, sweep_name)
                
                f.write("%s\t%s\n" % (name1, name2))  #writes the correct values to the value file
                
                
                if(do_correct2 == True):  #if the correct answer for the inner loop was found 
                    write_correct(f, para2, name1)  #write the correct answers to the value file
                    
                    output_hist = folder + pipe_name + "_hists/" + "arg_" + ft_c + "_" + bt_c + "_" + r_c + "_" + rr_c + "_" + m_c + "_" + mr_c + ".hist"  #sets the output hist name
                    nbody(output_hist, ft_c, bt_c, r_c, rr_c, m_c, mr_c, pipe_name, sweep_name)
                    do_correct2 = False  #resets do_correct2

                
                counter2 += intv2  #iterates the inner loop value
                name2 = str(counter2)
            
            name1 = name1_save  #once the correct value was put in, reset the counter to previous value so that iteration continues
            do_correct1 = False  #reset do_correct1
        
        counter1 += intv1  #iterates the outer loop value
        name1 = str(counter1)
    f.close()#close the files
    return 0

def tmp_sweep_correction(start1, end1, N1, para1, start2, end2, N2, para2):
    counter = 0
    rrs = [0.4170584501, 
           0.2107946813, 
           0.3575861589, 
           0.3758760553, 
           0.0230560377, 
           0.1799287515,
           0.1314197617,
           0.4534621829,
           0.2953949994,
           0.4302072331,
           0.084536664,
           0.303708456,
           0.040928522,
           0.2885632999,
           0.2928602405,
           0.497721423,
           0.2935240269,
           0.2482222544,
           0.286666601,
           0.2877686545,
           0.2803815874,
           0.0482648795,
           0.078455945,
           0.4939880484,
           0.3552749709]

    sweep_name = "_2d_rand_iter"
    pipe_name = para1 + "_" + para2 + "_correction"
    data_vals   = folder + "parameter_sweeps" + sweep_name + "/" + pipe_name + "_vals.txt"
    f = open(data_vals, 'w')
    
    output_hist = 'tmp.hist'
    nbody(output_hist, ft_c, bt_c, r_c, str(0.41705845006 ), m_c,  str(0.935116486918), pipe_name, sweep_name)
    f.write("%s\t%s\n" % (str(0.41705845006 ), str(0.935116486918)))  #write values to value file
    
    
    
    for i in range(0, len(rrs)):
        name1 = str(rrs[i])
        nbody(output_hist, ft_c, bt_c, r_c, name1, m_c, mr_c, pipe_name, sweep_name)
    
    f.close()
    
    
def random_iteration_sweep(start1, end1, N1, para1, start2, end2, N2, para2):
    counter1 = 0.0
    counter2 = 0.0
    #sweep name
    sweep_name = "_2d_rand_iter"
    #name of the files
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
    
     #this iterates over one parameter on the outside and another on the inside
    while counter1 < N1:
        if(counter1 == 0.0):#since this has random iteration, put the correct value first
            ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, name1 = correct_set(para1, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp)  #sets the correct value for the outerloop

            counter2 = 0.0#reset the inner loop counter
            while counter2 < N2:#runs the inner loop iteration
                if(counter2 == 0.0):#put the correct value for the inner loop first
                    ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, name2 = correct_set(para2, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp)  #sets the correct value for the inner loop
                    output_hist = folder + pipe_name + "_hists/" + "arg_" + ft_c + "_" + bt_c + "_" + r_c + "_" + rr_c + "_" + m_c + "_" + mr_c + ".hist"  #sets the name of the output hist
                    nbody(output_hist, ft_c, bt_c, r_c, rr_c, m_c, mr_c, pipe_name, sweep_name)
                    f.write("%s\t%s\n" % (name1, name2))  #write values to value file
                
                output_hist = folder + pipe_name + "_hists/" + "arg_"  #reset output file name
                
                name2 = random.uniform(0.0, 1.0) * (end2 - start2) + start2  #randomly select a value in the sweep range of inner loop parameter
                name2 = str(name2)
                
                ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp = para_init_rand(para2, name2, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp )  #set the values for the correct parameter for the inner loop
                
                output_hist += ft_tmp + "_" + bt_tmp + "_" + r_tmp + "_" + rr_tmp + "_" + m_tmp + "_" + mr_tmp + ".hist" #append the values to the hist name
                nbody(output_hist, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, pipe_name, sweep_name)
                f.write("%s\t%s\n" % (name1, name2)) #write values to value file
                
                counter2 += 1 #iterate counter. want a certain number of points
        
        name1 = random.uniform(0.0, 1.0) * (end1 - start1) + start1  #after putting correct answer, randomly select value from sweep range for outer loop parameter
        name1 = str(name1)
        
        ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp = para_init_rand(para1, name1, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp )  #set the values for the correct parameter for the inner loop
        
        counter2 = 0.0  #reset the counter for the inner loop
        while counter2 < N2:
            if(counter2 == 0.0):#put the correct value for the inner loop first
                ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, name2 = correct_set(para2, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp)
                
                output_hist = folder + pipe_name + "_hists/" + "arg_" + ft_tmp + "_" + bt_tmp + "_" + r_tmp + "_" + rr_tmp + "_" + m_tmp + "_" + mr_tmp + ".hist" #set the hist name
                nbody(output_hist, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, pipe_name, sweep_name)
                
                f.write("%s\t%s\n" % (name1, name2)) #write values to value file
                
            
            output_hist = folder + pipe_name + "_hists/" + "arg_" #reset the name of the hists
            
            name2 = random.uniform(0.0, 1.0) * (end2 - start2) + start2 #randomly select a value within the sweep range for the inner loop
            name2 = str(name2)
           
            ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp = para_init_rand(para2, name2, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp )  #assign values to the correct parameter for the inner loop
                
            output_hist += ft_tmp + "_" + bt_tmp + "_" + r_tmp + "_" + rr_tmp + "_" + m_tmp + "_" + mr_tmp + ".hist"
            nbody(output_hist, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, pipe_name, sweep_name)
            f.write("%s\t%s\n" % (name1, name2))
            counter2 += 1
        counter1 +=1
        
    f.close()
    return 0
    
def mk_dirs():
    names = [ 'ft_bt', 'ft_rad', 'ft_rr', 'ft_m', 'ft_mr', 'bt_r', 'bt_rr', 'bt_m', 'bt_mr', 'r_rr', 'r_m', 'r_mr', 'rr_m', 'rr_mr', 'm_mr']
    os.system("mkdir 2d_sweep_hists")
    for i in range(0, len(names)):
        os.system("mkdir 2d_sweep_hists/" + names[i] + "_hists")
    return 0


def main():
    if(make_folders):
        mk_dirs()
        
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
    
    if(run_random_iteration):
        if(run_ft_v_bt):
            random_iteration_sweep(ft_s, ft_e, ft_N, 'ft', bt_s, bt_e, bt_N, 'bt')
        if(run_ft_v_r ):
            random_iteration_sweep(ft_s, ft_e, ft_N, 'ft', r_s,  r_e,  r_N,  'r')
        if(run_ft_v_rr):
            random_iteration_sweep(ft_s, ft_e, ft_N, 'ft', rr_s, rr_e, rr_N, 'rr')
        if(run_ft_v_m ):
            random_iteration_sweep(ft_s, ft_e, ft_N, 'ft', m_s,  m_e,  m_N,  'm')
        if(run_ft_v_mr):
            random_iteration_sweep(ft_s, ft_e, ft_N, 'ft', mr_s, mr_e, mr_N, 'mr')
            
        if(run_bt_v_r  ):
            random_iteration_sweep(bt_s, bt_e, bt_N, 'bt', r_s,  r_e,  r_N,  'r')
        if(run_bt_v_rr ):
            random_iteration_sweep(bt_s, bt_e, bt_N, 'bt', rr_s, rr_e, rr_N, 'rr')
        if(run_bt_v_m  ):
            random_iteration_sweep(bt_s, bt_e, bt_N, 'bt', m_s,  m_e,  m_N,  'm')
        if(run_bt_v_mr ):
            random_iteration_sweep(bt_s, bt_e, bt_N, 'bt', mr_s, mr_e, mr_N, 'mr')
            
            
        if(run_r_v_rr  ):
            random_iteration_sweep(r_s,  r_e,  r_N,  'r',  rr_s, rr_e, rr_N, 'rr')
        if(run_r_v_m   ):
            random_iteration_sweep(r_s,  r_e,  r_N,  'r',  m_s,  m_e,  m_N,  'm')
        if(run_r_v_mr  ):
            random_iteration_sweep(r_s,  r_e,  r_N,  'r',  mr_s, mr_e, mr_N, 'mr')
            
        if(run_rr_v_m  ):
            random_iteration_sweep(rr_s, rr_e, rr_N, 'rr', m_s,  m_e,  m_N,  'm')
        if(run_rr_v_mr ):
            random_iteration_sweep(rr_s, rr_e, rr_N, 'rr', mr_s, mr_e, mr_N, 'mr')
            
        if(run_m_v_mr  ):
            random_iteration_sweep(m_s,  m_e,  m_N,  'm',  mr_s, mr_e, mr_N, 'mr')
            
    tmp_sweep_correction(r_s,  r_e,  r_N,  'r',  mr_s, mr_e, mr_N, 'mr')
main()
            
        