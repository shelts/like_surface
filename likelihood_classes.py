import os
import subprocess
from subprocess import call
import math as mt
# # # # # # # # # # # # # # # # # # # # # #
#        USEFUL CLASSES                   #
# # # # # # # # # # # # # # # # # # # # # #

class nbody_running_env:
    def __init__(self, lua_file, version, path):
        self.lua_file      = lua_file
        self.version       = version
        self.path          = path
    
    def build(self, scratch = None):#function for rebuilding nbody. it will build it in a seperate folder from the client directory
        os.chdir("./")
        
        if(scratch):
            os.system("rm -r nbody_test")  
            os.system("mkdir nbody_test")  
        
        os.chdir("../nbody_test")

        #following are fairly standard cmake commands
        os.system("cmake -DCMAKE_BUILD_TYPE=Release -DNBODY_DEV_OPTIONS=ON -DBOINC_RELEASE_NAMES=OFF -DNBODY_GL=OFF -DNBODY_STATIC=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    " + self.path + "milkywayathome_client/")
        
        #making the binaries. the -j is for multithreaded build/
        os.system("make -j ")
        os.chdir("../like_surface")
    
    
    def run(self, parameters, simulation_hist, comparison_hist = None, pipe = None):#running function. 2 optional parameters. 
        ft    = str(parameters[0])
        bt    = str(parameters[1])
        rl    = str(parameters[2])
        rr    = str(parameters[3])
        ml    = str(parameters[4])
        mr    = str(parameters[5])
        print('running nbody')
        os.chdir(self.path + "nbody_test/bin/")
        
        #below is a standard example of running nbody's binary
        #it is incomplete. It has the lua file flag, the output hist flag, and outfile flag
        run_command  = "./milkyway_nbody" + self.version + " \
                         -f " + self.lua_file + " \
                         -z " + simulation_hist + ".hist \
                         -o " + simulation_hist + ".out "
        
        #final piece to the run command. includes the number of threads, output format, and visualizer args
        end_piece = "-n 10  -b  --visualizer-bin=" + self.path + "nbody_test/bin/milkyway_nbody_graphics -i " + (ft) + " " + bt + " " + rl + " " + rr + " " + ml + " " + mr
        
        if(not comparison_hist): ##this willl produce a single run of nbody, without comparing the end result to anything
            run_command += end_piece #completing the run command
       
        elif(comparison_hist):#this willl produce a single run of nbody, comparing the end result to given histogram
            compare_hist_flag = " -h " + self.path + "quick_plots/hists/" + comparison_hist + ".hist  " #adding the input argument flag
            run_command +=  compare_hist_flag + end_piece
       
         
        if(pipe): 
            piping = " 2>> " + pipe #adding the piping piece to the command
            os.system(run_command + piping)
        else:
            os.system(run_command)
   
   
   
    def match_hists(self, hist1, hist2, pipe = None):#will compare to hist without running nbody simulation.
        print "matching histograms: "
        command = " " + self.path + "nbody_test/bin/milkyway_nbody" + self.version \
                + " -h " + self.path + "quick_plots/hists/" + hist1 + '.hist' \
                + " -D " + self.path + "quick_plots/hists/" + hist2 + '.hist'
        
        #using call here instead so the format of using it is on record
        if(pipe):#produces the comparison to stdout
            call([command + " 2>>" + pipe ], shell=True)
            
        else:#will pipe the result of the comparison to a file
            call([command], shell=True)
        
        print hist1, "\n", hist2
        print "\n"
        return 0
