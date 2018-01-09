#! /usr/bin/python
#/* Copyright (c) 2018 Siddhartha Shelton */
import os
from subprocess import call




class reval:
    def __init__(self, folder_name, sweeps):
        self.folder_name        = folder_name
        self.sweeps             = sweeps

    def get_likes(self):
        for i in range(0,len(self.sweeps)):
            sweep = self.sweeps[i]
            #get_likes(sweeps[i])
            f = open(self.folder_name + sweep + "_hist_names.txt", 'r')
            data = self.folder_name + 'data_hist_fall_2017.hist'
            for line in f:
                line = line.split("\n")
                hist = self.folder_name + sweep + "_hists/" + line[0]
                call(["~/Desktop/research/nbody_test/bin/milkyway_nbody" +
                    " -h " + data +
                    " -S " + hist 
                    + " 2>>" + self.folder_name + "new_vals/" + sweep + "_data_vals.txt"], shell=True)
            
    def clear_data(self):
        os.system('rm -r ' +  self.folder_name + "new_vals/")
        os.system('mkdir ' +  self.folder_name + "new_vals/")

def main():
    folder_name = 'parameter_sweeps_actual_data_hists_24dec2017_nbody_version166_theoretical_vel_error_2/'
    sweeps = ['ft', 'r', 'rr', 'm', 'mr']
    
    new = reval(folder_name, sweeps)
    
    new.clear_data()
    new.get_likes()
    
main()