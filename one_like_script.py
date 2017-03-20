#! /usr/bin/python
#/* Copyright (c) 2016 Siddhartha Shelton */
import os
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Control Panel       #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
y = True
n = False

oneD_clean = n
twoD_clean = n

reg_iterator  = n
ran_iterator  = y

oneD_sweep = y
twoD_sweep = n

oneD_multiploter = y
plot_cost_emd = n

narrow_range = n
special_parser = n
name_of_sweeps = "_rand_iter"
oneD_names   = ['ft', 'r', 'rr', 'm', 'mr']
#oneD_names   = ['ft', 'm', 'mr']

twoD_names   = [ 'ft_bt', 'ft_rad', 'ft_rr', 'ft_m', 'ft_mr', 
                 'bt_r', 'bt_rr', 'bt_m', 'bt_mr', 
                 'r_rr', 'r_m', 'r_mr', 
                 'rr_m', 'rr_mr', 
                 'm_mr']

#twoD_names   = ['r_rr', 'r_m', 'r_mr', 'rr_m', 'rr_mr', 'm_mr']
c          = [3.95, 0.2, 0.2, 12, 0.2]
ft         = [3.0, 5.0, 0.1]#20
bt         = [0.8, 1.2, 0.04]#10
r          = [0.1, 1.3, 0.06]#20
rr         = [0.1, .95, 0.05]#17
m          = [1., 120.0, 5]#23
mr         = [.1, .95, .05]#18

if(narrow_range):
    ft         = [3.93, 3.98, 0.1]#20
    bt         = [0.96, 1.0, 0.04]#10
    r          = [0.15, .25, 0.06]#20
    rr         = [0.15, .25, 0.05]#17
    m          = [10., 14.0, 5]#23
    mr         = [.15, .25, .05]#18


if(oneD_sweep):
    N = 1
    M = 0
if(twoD_sweep):
    N = 15
    M = 9


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Engine Room         #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # #
#    One Dimensional Surface Sweep Func   #
# # # # # # # # # # # # # # # # # # # # # #
def sort(likes, vals):
    N = len(likes)
    #this sorts the random iteration sweep values from least to greatest. 
    #along with their respective likelihoods
    like_tmp = []
    val_tmp  = []
    like_new = []
    val_new  = []
    for i in range(0, N):
        like_new.append(likes[i])
        val_new.append(vals[i])
        like_tmp.append(likes[i])
        val_tmp.append(vals[i])
        
    while(1):
        for i in range(0, N - 1):
            if(val_new[i] < val_new[i + 1]):
                val_tmp[i] = val_new[i]
                val_tmp[i + 1] = val_new[i + 1]
                like_tmp[i] = like_new[i]
                like_tmp[i + 1] = like_new[i + 1]
                
            elif(val_new[i] >= val_new[i + 1]):
                val_tmp[i] = val_new[i + 1]
                val_tmp[i + 1] = val_new[i]
                like_tmp[i] = like_new[i + 1]
                like_tmp[i + 1] = like_new[i]
            for j in range(0, N):
                val_new[j] = val_tmp[j]
                like_new[j] = like_tmp[j]
        
        for i in range(0, N - 1):
            in_order = True
            diff = (val_new[i + 1]) - (val_new[i])
            if(diff > 0):
                continue
            else:
                in_order = False
                break
        if(in_order == True):
            break
    return val_new, like_new

def reliability(likes, likes_new, vals, vals_new):
    N = len(likes)
    #checks to make sure the sorting and combining put everything
    #next to the correct values
    matches = 0.0
    for i in range(0, N):
        for j in range(0, N):
            if(vals[i] == vals_new[j] and likes[i] == likes_new[j]):
                matches += 1.0
    fraction_match = 100.0 * matches / float(N)
    return fraction_match

def make_correct(name_of_sweeps):
    if(oneD_sweep):
        data_folder = "1D_like_surface"
    if(twoD_sweep):
        data_folder = "2D_like_surface"
        
    f = open(data_folder + '/likelihood_data'  + name_of_sweeps + '/correct.txt', 'w')
    #    Correct Answers     #
    for i in range(0, 200):
        f.write("%f \t %f \t %f \t %f \t %f \t %f \n" % (-i, c[0], c[1], c[2], c[3], c[4]))
    f.close()
    return 0
    
def combine(name_of_sweeps, random_iter, names):
    if(oneD_sweep):
        data_folder = "1D_like_surface"
    if(twoD_sweep):
        data_folder = "2D_like_surface"
        
    #this combines the likelihood and data values into one file. checks for reliability
        
    for i in range(M, N):
        file_data = open('./' + data_folder + '/likelihood_data'  + name_of_sweeps + '/'  + str(names[i]) + '_data.txt', 'r')
        file_vals = open('./' + data_folder + '/parameter_sweeps' + name_of_sweeps + '/'  + str(names[i]) + '_vals.txt', 'r')
        file_comb = open('./' + data_folder + '/likelihood_data'  + name_of_sweeps + '/'  + str(names[i]) + '_data_vals.txt', 'w')
        likes = []
        vals  = []
        vals2 = [] #for 2d sweeps. they don't need to be sorted
        vals_new  = []
        likes_new = []
        
        counter_like = 0
        counter_val  = 0
        
        #make sure lists are the same length
        for line in file_data:
            l = float(line)
            likes.append(l)
            counter_like += 1
            
        for line in file_vals:
            if(oneD_sweep):#if 1d sweep, then there is only one column of data
                l = float(line)
                vals.append(l)
                
            if(twoD_sweep):
                ss = line.split('\t')
                l1 = float(ss[0])
                l2 = float(ss[1])
                vals.append(l1)
                vals2.append(l2)
            counter_val += 1
            
        #report and break if they are not
        if(counter_like != counter_val):
            print "value list length mismatch", name_of_sweeps, i
            break

        if(oneD_sweep):
            if(random_iter):#if the parameter sweep was using random iteration:
                vals_new, likes_new = sort(likes, vals)
                #sort the data values in order of least to greats with their corresponding likelihoods.
                #make sure the likelihoods were sorted correctly with the values
                reliability_of_sorting = reliability(likes, likes_new, vals, vals_new)
                
                if(reliability_of_sorting != 100.0):
                    print "HOLY FUCKING SHIT, SOMETHING IS WRONG"
                
                for j in range(0, counter_like):
                    file_comb.write("%0.15f\t%0.15f\n" % (vals_new[j], likes_new[j]))
            if(reg_iterator):
                for j in range(0, counter_like):
                    file_comb.write("%0.15f\t%0.15f\n" % (vals[j], likes[j]))
        if(twoD_sweep):#2d doesn't need to be sorted 
            for j in range(0, counter_like):
                file_comb.write("%0.15f\t%0.15f\t%0.15f\n" % (vals[j], vals2[j], likes[j]))
        
        
        if(oneD_sweep):
            os.system("rm ./" + data_folder + "/likelihood_data" + name_of_sweeps + "/" + str(oneD_names[i]) + "_data.txt")
        if(twoD_sweep):
            os.system("rm ./" + data_folder + "/likelihood_data" + name_of_sweeps + "/" + str(twoD_names[i]) + "_data.txt")
        
        file_data.close()
        file_vals.close()
        file_comb.close()
    return 0

def parser(name_of_sweeps, random_iter, names):
    if(oneD_sweep):
        data_folder = "1D_like_surface"
    if(twoD_sweep):
        data_folder = "2D_like_surface"
    
    for i in range(M, N):
        g = open('./' + data_folder + '/parameter_sweeps' + name_of_sweeps + '/' + str(names[i]) + '.txt', 'r')
        f = open('./' + data_folder + '/likelihood_data'  + name_of_sweeps + '/' + str(names[i]) + '_data.txt', 'w')

        for line in g:
            if (line.startswith("<search_likelihood")):
                ss = line.split('<search_likelihood>')#splits the line between the two sides the delimiter
                tt = ss[1].split('</search_likelihood>')#chooses the second of the split parts and resplits
                f.write("%s \n" % tt[0])#writes the first of the resplit lines
        
    f.close()
    g.close()
    combine(name_of_sweeps, random_iter, names)
    make_correct(name_of_sweeps)#make a file with the correct answers. 
    return 0 

def oneD_plot(name_of_sweeps):
    l = -200
    #ranges_start = [ft[0], bt[0], r[0], rr[0], m[0], mr[0]]
    #ranges_end   = [ft[1], bt[1], r[1], rr[1], m[1], mr[1]]
    
    ranges_start = [ft[0], r[0], rr[0], m[0], mr[0]]
    ranges_end   = [ft[1], r[1], rr[1], m[1], mr[1]]
    
    #ranges_start = [ft[0],  m[0], mr[0]]
    #ranges_end   = [ft[1],  m[1], mr[1]]
    #how many of the data sets are we plotting
    

    #titles  = ['Forward Evolve Time', 'Reverse Orbit Time Ratio', 'Baryonic Scale Radius', 'Baryonic Scale Radius Ratio', 'Baryonic Matter Mass',  'Baryonic to Mass Ratio']
    titles  = ['Forward Evolve Time', 'Baryonic Scale Radius', 'Baryonic Scale Radius Ratio', 'Baryonic Matter Mass',  'Baryonic to Mass Ratio']
    #titles  = ['Forward Evolve Time', 'Baryonic Matter Mass',  'Mass Ratio']
    # # # # # # # # # # # # # # # # # # # # # # # # # 
    data_vals = "parameter_data/"
    like_data = "likelihood_data/"


    f = open('1D_plot' + name_of_sweeps + '.gnuplot', 'w')
    f.write("reset\n")
    f.write("set terminal jpeg\n")
    f.write("set key off\n")

    for i in range(M, N):
        f.write("set xlabel '" + titles[i] + "'\n")
        f.write("set ylabel 'likelihood'\n")
        f.write("set yrange [" + str(l) + ":0]\n")
        f.write("set xrange [" + str(ranges_start[i]) + ":" + str(ranges_end[i]) + "]\n")
        
        #p = "<paste 1D_like_surface/parameter_data/" + oneD_names[i] + "_vals.txt 1D_like_surface/likelihood_data/" + oneD_names[i] + "_data.txt"
        p = "1D_like_surface/likelihood_data" + name_of_sweeps + "/" + oneD_names[i] + "_data_vals.txt"
        f.write("set output '1D_like_surface/plots" + name_of_sweeps + "/" + oneD_names[i] + ".jpeg' \n")
        f.write("set title 'Likelihood Surface of " + titles[i] + "' \n")
        f.write("plot '" + p + "' using 1:2  with lines\n\n") 

        f.write("# # # # # # # # # # # # # # # # # #\n")

    f.close()

    os.system("gnuplot 1D_plot" + name_of_sweeps + ".gnuplot 2>>piped_output.txt")
    os.system("rm 1D_plot" + name_of_sweeps + ".gnuplot")
    return 0

def oneD_multiplot(name_of_sweeps):
    l = -200
    titles  = ['Forward Evolve Time (Gyr)',  'Baryon Scale Radius (kpc)', 'Scale Radius Ratio (Stellar/Dark)', 'Baryonic Mass (SMU)',  'Mass Ratio (Baryonic/Total)']
    #titles  = ['Forward Evolve Time (Gyr)', 'Baryonic Mass (SMU)',  'Mass Ratio (Baryonic/Total)']
    #labels  = ['Forward Evolve Time (Gyr)', 'Baryon Scale Radius (kpc)', 'Scale Radius Ratio', 'Baryonic Mass (Sim Mass Units)',  'Mass Ratio']
    #titles  = ['Forward Evolve Time (Gyr)_{}', 'Reverse Orbit Ratio (T_{f} / T_{r})', 'Baryon Scale Radius (kpc)_{}', 'Scale Radius Ratio [R_{Stars}/(R_{Stars} + R_{Dark})]', 'Baryonic Mass_{}',  'Mass Ratio [M_{Stars}/M_{Total}]']
    #labels  = ['Forward Evolve Time (Gyr)', 'Reverse Orbit Ratio', 'Baryon Scale Radius (kpc)', 'Scale Radius Ratio', 'Baryonic Mass (Sim Mass Units)',  'Mass Ratio']
    #ranges

    #ranges_start = [ft[0], bt[0], r[0], rr[0], m[0], mr[0]]
    #ranges_end   = [ft[1], bt[1], r[1], rr[1], m[1], mr[1]]
    ranges_start = [ft[0], r[0], rr[0], m[0], mr[0]]
    ranges_end   = [ft[1], r[1], rr[1], m[1], mr[1]]

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    data_vals = "parameter_data/"
    like_data = "likelihood_data/"


    f = open('multiplot_1d' + name_of_sweeps + '.gnuplot', 'w')
    f.write("reset\n")
    f.write("set terminal png size 1800,1200 enhanced \n")
    f.write("set key off\n")
    f.write("set border linewidth 2\n")
    f.write("set title font 'Times-Roman,20'\n")
    f.write("set output '1D_like_surface/plots" + name_of_sweeps + "/multiplot.png' \n")
    f.write("set multiplot layout 2,3 rowsfirst\n")
    for i in range(M, N):
        f.write("set size ratio -1 \n")
        f.write("set size square\n")
        if(i == 0 or i == 3):
            f.write("set ylabel 'Likelihood ' font ',26' offset -1,0\n")
        else:
            f.write("set ylabel '' font ',26' offset -1,0\n")
            
        f.write("set lmargin 11\n")
        f.write("set tmargin 0\n")
        f.write("set xlabel '" + titles[i] + "' font ',26' offset 0,-1\n")
        #f.write("set tics scale 0.5\n")
        if(i <= 1):
            f.write("set xtics font ', 24' offset 0,-0.5\n")
        elif(i == 2 or i == 4):
            f.write("set xtics 0.1, 0.2, 0.9 font ', 24' offset 0,-0.5\n")
        elif(i == 3):
            f.write("set xtics 0, 20, 120 font ', 24' offset 0,-0.5\n")
        f.write("set ytics font ', 24'\n")
        f.write("set yrange [" + str(l) + ":0]\n")
        f.write("set xrange[" + str(ranges_start[i]) + ":" + str(ranges_end[i]) + "]\n")
        #f.write("set parametric\n")
        p = "1D_like_surface/likelihood_data" + name_of_sweeps + "/" + oneD_names[i] + "_data_vals.txt"
        #f.write("set title '" + titles[i] + "' font ',22'\n")
        f.write("plot '" + p + "' using 1:2  with lines linecolor rgb 'blue' lw 2, '1D_like_surface/likelihood_data" + name_of_sweeps + "/correct.txt' using " + str(i + 2) + ":1 with lines lc rgb 0,0,0\n\n") 

        f.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # \n")
        f.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # \n")

    f.close()

    os.system("gnuplot multiplot_1d" + name_of_sweeps + ".gnuplot 2>>piped_output.txt")
    os.system("rm multiplot_1d" + name_of_sweeps + ".gnuplot")
    return 0

# # # # # # # # # # # # # # # # # # # # # #
#    Two Dimensional Surface Sweep Func   #
# # # # # # # # # # # # # # # # # # # # # #
def twoD_plot():
    ft  = [1.0, 3.0]
    bt  = [0.8, 1.2]
    r   = [0.1, 0.9]
    rr  = [0.1, 0.7]
    m   = [2.0, 45]
    mr  = [0.1, 0.55]
    #starts, ends
    
    f   = 'Forward Evolve Time'
    b   = 'Reverse Orbit Ratio'
    rad  = 'Radius'
    r_r = 'Radius Ratio'
    mass  = 'Mass'
    m_r = 'Mass Ratio'


    names = [ 'ft_vs_bt', 'ft_vs_rad', 'ft_vs_rr', 'ft_vs_m', 'ft_vs_mr', 'bt_vs_r', 'bt_vs_rr', 'bt_vs_m', 'bt_vs_mr', 'r_vs_rr', 'r_vs_m', 'r_vs_mr', 'rr_vs_m', 'rr_vs_mr', 'm_vs_mr']
    xlabels = [f, f, f, f, f, b, b, b, b, rad, rad ,rad, r_r, r_r, mass]  
    ylabels = [b, rad, r_r, mass, m_r, rad, r_r, mass, m_r, r_r, mass, m_r, mass, m_r, m_r]

    xranges_start = [ft[0], ft[0], ft[0], ft[0], ft[0], bt[0], bt[0], bt[0], bt[0], r[0], r[0], r[0], rr[0], rr[0], m[0]]
    yranges_start = [bt[0], r[0], rr[0], m[0], mr[0], r[0], rr[0], m [0], mr[0], rr[0], m[0], mr[0], m[0], mr[0], mr[0]]

    xranges = [ft[1], ft[1], ft[1], ft[1], ft[1], bt[1], bt[1], bt[1], bt[1], r[1], r[1], r[1], rr[1], rr[1], m[1]]
    yranges = [bt[1], r[1], rr[1], m[1], mr[1], r[1], rr[1], m [1], mr[1], rr[1], m[1], mr[1], m[1], mr[1], mr[1]]

    color_cutoff = -200

    N  = 15
    M  = 0

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    data_vals = "parameter_data/"
    like_data = "likelihood_data/"


    f = open('2D_plot.gnuplot', 'w')
    f.write("reset\n")
    f.write("set terminal png\n")
    f.write("set key off\n")
    f.write("set pm3d interpolate 50,50\n")
    for i in range(M, N):
        f.write("set xlabel '" + xlabels[i] + "'\n")
        f.write("set ylabel '" + ylabels[i] + "'\n")
        f.write("set zlabel 'likelihood'\n")
        #f.write("set palette  maxcolors 1000\n")
        #f.write("set palette rgbformulae \n")
        #f.write("set palette gray \n")
        f.write("set cbrange[" + str(color_cutoff) + ":0]\n")
        f.write("set xrange[" + str(xranges_start[i]) + ":" + str(xranges[i]) + "]\n")
        f.write("set yrange[" + str(yranges_start[i]) + ":" + str(yranges[i]) + "]\n\n\n")

        p = "<paste 2D_like_surface/parameter_data/" + names[i] + ".txt 2D_like_surface/likelihood_data/" + names[i] + "_data.txt"
        f.write("set output '2D_like_surface/plots/" + names[i] + ".png' \n")
        f.write("set title 'Likelihood Surface of " + str(xlabels[i]) + " vs " + str(ylabels[i]) + "' \n")
        f.write("plot '" + p + "' using 1:2:3  with image \n\n") 

        f.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # \n")
        f.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # \n")

    f.close()

    os.system("gnuplot 2D_plot.gnuplot 2>>piped_output.txt")
    os.system("rm 2D_plot.gnuplot")

def reg_iterator_sweep(name_of_sweeps):
    random_iter = False
    
    if(oneD_sweep):
        oneD_cleanse(name_of_sweeps)
        parser(name_of_sweeps, random_iter, oneD_names)
        oneD_plot(name_of_sweeps)
        
        if(oneD_multiploter):
            oneD_multiplot(name_of_sweeps)
    
    if(twoD_sweep):
        twoD_cleanse(name_of_sweeps)
        parser(name_of_sweeps, random_iter, twoD_names)
        twoD_plot(name_of_sweeps)
    return 0

def random_iterator_sweep(name_of_sweeps):
    random_iter = True
    
    #parse the data
    #this will also put the likelihoods and data values in one file
    #if it is a random iteration sweep it will sort the data values with their respective
    #likelihoods from least to greatest
    if(oneD_sweep):
        oneD_cleanse(name_of_sweeps)
        parser(name_of_sweeps, random_iter, oneD_names)
        oneD_plot(name_of_sweeps)
        
        if(oneD_multiploter):
            oneD_multiplot(name_of_sweeps)
            
    if(twoD_sweep):
        twoD_cleanse(name_of_sweeps)
        parser(name_of_sweeps, random_iter, twoD_names)
        #twoD_plot(name_of_sweeps)
        
    return 0

# # # # # # # # # #
#     Cleaners    #
# # # # # # # # # #
def oneD_cleanse(name_of_sweeps):
    os.system("rm -r 1D_like_surface/likelihood_data" + name_of_sweeps)
    os.system("mkdir 1D_like_surface/likelihood_data" + name_of_sweeps)

    #os.system("rm -r 1D_like_surface/plots" + name_of_sweeps)
    #os.system("mkdir 1D_like_surface/plots" + name_of_sweeps)

    #os.system("rm -r 1D_like_surface/parameter_data")
    #os.system("mkdir 1D_like_surface/parameter_data")
    
    #os.system("rm -r 1D_like_surface/cost_emd_data")
    #os.system("mkdir 1D_like_surface/cost_emd_data")
    
    #os.system("rm -r 1D_like_surface/cost_emd_plots")
    #os.system("mkdir 1D_like_surface/cost_emd_plots")
    return 0

def twoD_cleanse(name_of_sweeps):
    os.system("rm -r 2D_like_surface/likelihood_data" + name_of_sweeps)
    os.system("mkdir 2D_like_surface/likelihood_data" + name_of_sweeps)

    os.system("rm -r 2D_like_surface/plots" + name_of_sweeps)
    os.system("mkdir 2D_like_surface/plots" + name_of_sweeps)
    return 0
# # # # # # # # # # # 
#    Misc parsers   #
# # # # # # # # # # # 

def all_hists_in_one_file_parser():
    g = open('./all_in_one_mr.txt', 'r')
    l = open('./like_data', 'w')
    #this function is for parsing a file which has all the histograms and likelihood_data dumped one after the other. 
    #which happens if you mess up the output file directory
    for line in g:
        if(line.startswith("Error opening")):
            ss = line.split("Error opening histogram 'mr_hists/~/research/like_surface/hists/")
            tt = ss[1].split("'. Using default output instead. (2): No such file or directory")
            f = open('./parsed_hists/' + tt[0], 'w')
            continue
        if(line.startswith("nSim:") or line.startswith("log") or line.startswith("<search_likelihood") or line.startswith("Using OpenMP")):
            l.write(line)
        else:
            f.write(line)
# # # # # # # 
#    Main   #
# # # # # # #    
def main():
    if(oneD_clean):
        oneD_cleanse()
    
    if(twoD_clean):
        twoD_cleanse()
    
    #if(multi_server_combo_switch):
        #multi_server_combo_switch()
    
    if(reg_iterator):
        reg_iterator_sweep(name_of_sweeps)

    if(ran_iterator):
        random_iterator_sweep(name_of_sweeps)
        
        
    #if(twoD_surface):
        #twoD_data_vals()
        #twoD_parser()
        #twoD_plot()
        
    
    if(special_parser):
        all_hists_in_one_file_parser()

main()    