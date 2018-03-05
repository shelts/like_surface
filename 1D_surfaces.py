#! /usr/bin/python
#/* Copyright (c) 2016 Siddhartha Shelton */
import os
from subprocess import call
import random
random.seed(a = 12345678)#lmc
#random.seed(a = 687651463)#teletraan
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

lmc_dir = '/home/shelts/research/'
sid_dir = '/home/sidd/Desktop/research/'
sgr_dir = '/Users/master/sidd_research/'
path = lmc_dir

folder        = path + "like_surface/hists/"
binary        = path + "nbody_test/bin/milkyway_nbody"
lua           = path + "lua/full_control.lua"

input_hist    = folder + "arg_" + ft_c + "_" + bt_c + "_" + r_c + "_" + rr_c + "_" + m_c + "_" + mr_c + "_correct.hist"

correct = [3.95, 0.2, 0.2, 12, 0.2]
parameters_names = ['ft', 'r', 'rr', 'm', 'mr']
ranges  = [ [3.0, 5.0],  \
            [0.05, 0.5],  \
            [0.05, 0.5],  \
            [1., 60.0,], \
            [.01, .95,],   \
          ]   
search_N = [50, 50, 50, 50, 50]
y = True
n = False

#choose what to run
make_folders              = y
rebuild_binary            = n
make_correct_answer_hist  = y
run_regular_iteration     = n
run_random_iteration      = y

run_forward_evole_time    = y
run_backward_evolve_ratio = n
run_radius                = y
run_radius_ratio          = y
run_mass                  = y
run_mass_ratio            = y
#--------------------------------------------------------------------------------------------------

    
class sweep:
    def __init__(self, parameter, nbody):
        os.system("mkdir " + path + "like_surface/hists/parameter_sweeps")
        
        self.parameter = parameter #parameter index
        self.data_vals = []
        self.data_val_file = path + "like_surface/hists/parameter_sweeps" + sweep_name + "/" + para + "_vals.txt"
        
        self.get_data_vals()
        self.run_sweep(nbody)
        
        def get_data_vals(self):
            if(random_iter):
                self.data_vals.append(args[self.parameter]) #correct value
            else:
                val = ranges[self.parameter][0] # lower range
                dN = (ranges[self.parameter][1] - ranges[self.parameter][0]) / search_N[self.parameter]
                self.data_vals.append(val)
                
            for i in range(0, search_N[self.parameter]):
                if(random_iter):
                    val = random.uniform(0.0, 1.0) * (ranges[self.parameter][1] - ranges[self.parameter][0]) + ranges[self.parameter][0]
                else:
                    val += dN
                
                self.data_vals.append(val)
                
        def run_sweep(self, nbody):
            paras = list(args)
            for i range(0, search_N[self.parameter]):
                paras[self.parameter] = self.data_vals[i]
                output_hist = folder + para + "_hists/" + "arg_" + paras[0] + "_" + paras[1] + "_" + paras[2] + "_" + paras[3] + "_" + paras[4] + ".hist"
                pipe_name = folder + "parameter_sweeps/" + parameters_names[self.parameter] + ".txt"
                nbody.run(paras, input_hist, output_hist, pipe_name)
        
        def write_data_vals(self):
            f = open(self.data_val_file, 'w')
            for i in range(0, len(self.data_vals)):
                f.write("%0.15f\n" % self.data_vals[i])
            f.close()
        
def mk_dirs():
    names   = ['ft', 'bt', 'r', 'rr', 'm', 'mr']
    os.chdir(path + "like_surface")
    os.system("mkdir hists")
    for i in range(0, len(names)):
        os.system("mkdir hists/" + names[i] + "_hists")
    return 0

def main():
    nbody = nbody_running_env(lua, version, path)
    
    if(make_folders):
        mk_dirs()
    
    if(rebuild_binary):
        nbody.build(False)
        
    if(make_correct_answer_hist):
        nbody.run(args, input_hist)
    
    
            
    return 0
    
main()