#! /usr/bin/python
#/* Copyright (c) 2016 Siddhartha Shelton */
import os
import statistics 
import math as mt
folder = 'runs_5_23_17/'
run_names = ['de_nbody_5_23_17_v164_20k_1', 'de_nbody_5_23_17_v164_20k_2', 'de_nbody_5_23_17_v164_20k_3', 'ps_nbody_5_23_17_v164_20k__1', 'ps_nbody_5_23_17_v164_20k__2']

class stats:#for doing the stats on an input list of numbers. 
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

class run:#class for doing stats on each individual run
    def __init__(self, run_name):
        self.run_name = run_name#getting the name of the run
        
        
    def get_data(self):#pulls the data from the file and does the stats on them
        likes = []; fts = []; rls = []; rrs = []; mls = []; mrs = []
    
        f = open(folder + self.run_name, 'r')
        read_data = False

        for line in f:
            if (line.startswith("The best")):
                read_data = True
                continue
            if(read_data):
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
        
        self.ls = stats(likes)
        self.ft = stats(fts)
        self.rl = stats(rls)
        self.rr = stats(rrs)
        self.ml = stats(mls)
        self.mr = stats(mrs)
        
        self.best_ls = likes[len(likes) - 1]
        self.best_ft = fts[len(likes) - 1]
        self.best_rl = rls[len(likes) - 1]
        self.best_rr = rrs[len(likes) - 1]
        self.best_ml = mls[len(likes) - 1]
        self.best_mr = mrs[len(likes) - 1]
        
    def write_stats(self, file_name):#for writing the stats to a file
        file_name.write("RUN NAME: %s \t\t BEST LIKELIHOOD: %f \t WORST LIKELIHOOD: %f\n" %(self.run_name, self.ls.maximum, self.ls.minimum))
        file_name.write("\t FORWARD TIME \n \t\t MEAN:\t %f \n \t\t STDEV\t %f \n \t\t MEDIAN\t %f\n \t\t MAX\t %f \n \t\t MIN\t %f \n" % (self.ft.mean, self.ft.std, self.ft.median, self.ft.maximum, self.ft.minimum))
        file_name.write("\t BARYON RADIUS\n \t\t MEAN:\t %f \n \t\t STDEV\t %f \n \t\t MEDIAN\t %f\n \t\t MAX\t %f \n \t\t MIN\t %f \n" % (self.rl.mean, self.rl.std, self.rl.median, self.rl.maximum, self.rl.minimum))
        file_name.write("\t RADIUS RATIO \n \t\t MEAN:\t %f \n \t\t STDEV\t %f \n \t\t MEDIAN\t %f\n \t\t MAX\t %f \n \t\t MIN\t %f \n" % (self.rr.mean, self.rr.std, self.rr.median, self.rr.maximum, self.rr.minimum))
        file_name.write("\t BARYON MASS  \n \t\t MEAN:\t %f \n \t\t STDEV\t %f \n \t\t MEDIAN\t %f\n \t\t MAX\t %f \n \t\t MIN\t %f \n" % (self.ml.mean, self.ml.std, self.ml.median, self.ml.maximum, self.ml.minimum))
        file_name.write("\t MASS RATIO   \n \t\t MEAN:\t %f \n \t\t STDEV\t %f \n \t\t MEDIAN\t %f\n \t\t MAX\t %f \n \t\t MIN\t %f \n" % (self.mr.mean, self.mr.std, self.mr.median, self.mr.maximum, self.mr.minimum))
        file_name.write("\n\n")
   
    def print_bests(self):#prints out the parameters associated with the best likelihood
       print(self.best_ls, self.best_ft, self.best_rl , self.best_rr , self.best_ml , self.best_mr )
       

class all_runs:#class for doing stats on all the best fit from all the runs
    def __init__(self):
        self.fts = []; self.rls = []; self.rrs = []; self.mls = []; self.mrs = []
        self.ft_r = []; self.rl_r = []; self.rr_r = []; self.ml_r = []; self.mr_r = []
        
    def add_run(self, run):#stores the parameters associated with the best likelihood 
        self.fts.append(run.best_ft)
        self.rls.append(run.best_rl)
        self.rrs.append(run.best_rr)
        self.mls.append(run.best_ml)
        self.mrs.append(run.best_mr)
        
    def print_runs(self):#prints out the parameters associated with the best likelihood for all the runs. for debugging
        print self.fts, '\n', self.rls, '\n', self.rrs, '\n', self.mls, '\n', self.mrs
        
    def do_stats(self):#does the stat calcs. for after it gets the parameters from all runs
        self.ft = stats(self.fts)
        self.rl = stats(self.rls)
        self.rr = stats(self.rrs)
        self.ml = stats(self.mls)
        self.mr = stats(self.mrs)
        
    def write_search_stats(self, file_name):
        file_name.write("FOR BEST OF ALL REPORTED RUNS:\n")
        file_name.write("\t FORWARD TIME \n \t\t MEAN:\t %f \n \t\t STDEV\t %f \n \t\t MEDIAN\t %f\n \t\t MAX\t %f \n \t\t MIN\t %f \n" % (self.ft.mean, self.ft.std, self.ft.median, self.ft.maximum, self.ft.minimum))
        file_name.write("\t BARYON RADIUS\n \t\t MEAN:\t %f \n \t\t STDEV\t %f \n \t\t MEDIAN\t %f\n \t\t MAX\t %f \n \t\t MIN\t %f \n" % (self.rl.mean, self.rl.std, self.rl.median, self.rl.maximum, self.rl.minimum))
        file_name.write("\t RADIUS RATIO \n \t\t MEAN:\t %f \n \t\t STDEV\t %f \n \t\t MEDIAN\t %f\n \t\t MAX\t %f \n \t\t MIN\t %f \n" % (self.rr.mean, self.rr.std, self.rr.median, self.rr.maximum, self.rr.minimum))
        file_name.write("\t BARYON MASS  \n \t\t MEAN:\t %f \n \t\t STDEV\t %f \n \t\t MEDIAN\t %f\n \t\t MAX\t %f \n \t\t MIN\t %f \n" % (self.ml.mean, self.ml.std, self.ml.median, self.ml.maximum, self.ml.minimum))
        file_name.write("\t MASS RATIO   \n \t\t MEAN:\t %f \n \t\t STDEV\t %f \n \t\t MEDIAN\t %f\n \t\t MAX\t %f \n \t\t MIN\t %f \n" % (self.mr.mean, self.mr.std, self.mr.median, self.mr.maximum, self.mr.minimum))
        file_name.write("\n\n")
        
        file_name.write("BEST SEARCH RANGE:\n")
        file_name.write("\t FORWARD TIME \n \t\t LOWER:\t %f \n \t\t UPPER:\t %f \n" % (self.ft_r[0], self.ft_r[1]))
        file_name.write("\t BARYON RADIUS\n \t\t LOWER:\t %f \n \t\t UPPER\t %f  \n" % (self.rl_r[0], self.rl_r[1]))
        file_name.write("\t RADIUS RATIO \n \t\t LOWER:\t %f \n \t\t UPPER\t %f  \n" % (self.rr_r[0], self.rr_r[1]))
        file_name.write("\t BARYON MASS  \n \t\t LOWER:\t %f \n \t\t UPPER\t %f  \n" % (self.ml_r[0], self.ml_r[1]))
        file_name.write("\t MASS RATIO   \n \t\t LOWER:\t %f \n \t\t UPPER\t %f  \n" % (self.mr_r[0], self.mr_r[1]))
        file_name.write("\n\n")
    def best_search_range(self):
        self.ft_r = [self.ft.mean - self.ft.std, self.ft.mean + self.ft.std]
        self.rl_r = [self.rl.mean - self.rl.std, self.rl.mean + self.rl.std]
        self.rr_r = [self.rr.mean - self.rr.std, self.rr.mean + self.rr.std]
        self.ml_r = [self.ml.mean - self.ml.std, self.ml.mean + self.ml.std]
        self.mr_r = [self.mr.mean - self.mr.std, self.mr.mean + self.mr.std]
       
def main():
    g = open('run_statistics.txt', 'w')
    
    runs = []
    all_run_stats = all_runs()
    for i in range(0,len(run_names)):
        tmp = run(run_names[i])
        tmp.get_data()
        runs.append(tmp)
        runs[i].write_stats(g)
        #runs[i].print_bests()
        
        all_run_stats.add_run(runs[i])
        
    all_run_stats.do_stats()    
    all_run_stats.best_search_range()
    #all_run_stats.print_runs()
        
    g.close()
    
    g = open('search_stats', 'w')
    all_run_stats.write_search_stats(g)
    g.close()
main()