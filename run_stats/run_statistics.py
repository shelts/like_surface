#! /usr/bin/python
#/* Copyright (c) 2016 Siddhartha Shelton */
import os
import statistics 
import math as mt
folder = 'runs_5_23_17/'
run_names = ['de_nbody_5_23_17_v164_20k_1', 'de_nbody_5_23_17_v164_20k_2', 'de_nbody_5_23_17_v164_20k_3', 'ps_nbody_5_23_17_v164_20k__1', 'ps_nbody_5_23_17_v164_20k__2']

class stats:
    def __init__(self, vals):
        self.median                = self.get_median(vals)
        self.mean                  = self.get_mean(vals)
        self.maximum, self.minimum = self.get_max_min(vals)
        self.std                   = self.get_std(vals)
        
    def get_median(self, vals):
        return statistics.median(vals)
    
    def get_mean(self, vals):
        val_sum = 0
        for i in range(0, len(vals)):
            val_sum += vals[i]
        return val_sum / len(vals)
    
    def get_max_min(self, vals):
        tmp_max = vals[0]
        tmp_min = vals[0]
        for i in range(0, len(vals)):
            if(vals[i] <= tmp_min):
                tmp_min = vals[i]
            if(vals[i] >= tmp_max):
                tmp_max = vals[i]
        
        return tmp_max, tmp_min
    
    def get_std(self, vals):
        tmp_sum = 0
        for i in range(0, len(vals)):
            diff = vals[i] - self.mean
            tmp_sum += diff * diff
            
        tmp_sum = mt.sqrt(tmp_sum / (len(vals)- 1))
        return tmp_sum

class run:
    def __init__(self, run_name):
        self.run_name = run_name
        self.get_data(run_name)
        self.ls; self.ft; self.rl; self.rr; self.ml; self.mr
        
    def get_data(self, run_name):
        likes = []; fts = []; rls = []; rrs = []; mls = []; mrs = []
    
        f = open(folder + run_name, 'r')
        starting_line = 1
        for line in f:
            if(line.startswith("The best")):
                break
            else:
                starting_line += 1

        f.seek(0)
        line_number = 1
        for line in f:
            if(line_number > starting_line):
                line = line.replace('[', '')
                line = line.replace(']', '')
                line = line.replace('\t', '')
                line = line.replace('\n', '')
                ss = line.split(',')
                
                likes.append(float(ss[1]))
                fts.append(float(ss[2]))
                rls.append(float(ss[4]))
                rrs.append(float(ss[5]))
                mls.append(float(ss[6]))
                mrs.append(float(ss[7]))
            line_number += 1
        
        self.ls = stats(likes)
        self.ft = stats(fts)
        self.rl = stats(rls)
        self.rr = stats(rrs)
        self.ml = stats(mls)
        self.mr = stats(mrs)
        
    def write_stats(self, file_name, run_name):
        file_name.write("RUN NAME: %s \t\t BEST LIKELIHOOD: %f \t WORST LIKELIHOOD: %f\n" %(run_name, self.ls.maximum, self.ls.minimum))
        file_name.write("\t FORWARD TIME \n \t\t MEAN:\t %f \n \t\t STDEV\t %f \n \t\t MEDIAN\t %f\n \t\t MAX\t %f \n \t\t MIN\t %f \n" % (self.ft.mean, self.ft.std, self.ft.median, self.ft.maximum, self.ft.minimum))
        file_name.write("\t BARYON RADIUS\n \t\t MEAN:\t %f \n \t\t STDEV\t %f \n \t\t MEDIAN\t %f\n \t\t MAX\t %f \n \t\t MIN\t %f \n" % (self.rl.mean, self.rl.std, self.rl.median, self.rl.maximum, self.rl.minimum))
        file_name.write("\t RADIUS RATIO \n \t\t MEAN:\t %f \n \t\t STDEV\t %f \n \t\t MEDIAN\t %f\n \t\t MAX\t %f \n \t\t MIN\t %f \n" % (self.rr.mean, self.rr.std, self.rr.median, self.rr.maximum, self.rr.minimum))
        file_name.write("\t BARYON MASS  \n \t\t MEAN:\t %f \n \t\t STDEV\t %f \n \t\t MEDIAN\t %f\n \t\t MAX\t %f \n \t\t MIN\t %f \n" % (self.ml.mean, self.ml.std, self.ml.median, self.ml.maximum, self.ml.minimum))
        file_name.write("\t MASS RATIO   \n \t\t MEAN:\t %f \n \t\t STDEV\t %f \n \t\t MEDIAN\t %f\n \t\t MAX\t %f \n \t\t MIN\t %f \n" % (self.mr.mean, self.mr.std, self.mr.median, self.mr.maximum, self.mr.minimum))
        file_name.write("\n\n")
        
        
def main():
    g = open('run_statistics.txt', 'w')
   
    runs = []
    for i in range(0,len(run_names)):
        tmp = run(run_names[i])
        runs.append(tmp)
        runs[i].write_stats(g, run_names[i])
        
    g.close()
    
main()
