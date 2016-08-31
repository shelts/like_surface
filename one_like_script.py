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
oneD_surface = n
twoD_surface = n

oneD_multiploter = n
plot_cost_emd = n


random_iterator = y
special_parser = n

oneD_names   = ['ft', 'bt', 'r', 'rr', 'mass', 'mr']

c          = [3.95, 0.98, 0.2, 0.2, 12, 0.2]
ft         = [3.0, 5.0, 0.1]#20
bt         = [0.8, 1.2, 0.04]#10
r          = [0.1, 1.3, 0.06]#20
r_r        = [0.1, .95, 0.05]#17
m          = [1., 120.0, 5]#23
m_r        = [.01, .95, .05]#18

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Engine Room         #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # #
#    One Dimensional Surface Sweep Func   #
# # # # # # # # # # # # # # # # # # # # # #
def oneD_data_vals():
    f = open('./1D_like_surface/parameter_data/' + oneD_names[0] + '_vals.txt', 'w')

    #  FORWARD TIME #
    counter = ft[0]
    while counter < ft[1]:
        f.write("%s \n" % counter)
        if(counter < c[0] and counter + ft[2] > c[0]):
            f.write("%s \n" % c[0])
        counter += ft[2]
    f.close()
    
    #  BACKWARD TIME  #  
    f = open('./1D_like_surface/parameter_data/' + oneD_names[1] + '_vals.txt', 'w')
    counter = bt[0]
    while counter < bt[1]:
        f.write("%s \n" % counter)
        if(counter < c[1] and counter + bt[2] > c[1]):
            f.write("%s \n" % c[1])
        counter += bt[2]
    f.close() 

    #  RADIUS  #
    f = open('./1D_like_surface/parameter_data/' + oneD_names[2] + '_vals.txt', 'w')
    counter = r[0]
    while counter < r[1]:
        f.write("%s \n" % counter)
        if(counter < c[2] and counter + r[2] > c[2]):
            f.write("%s \n" % c[2])
        counter += r[2]
    f.close()
    
    #  RADIUS RATIO  #
    f = open('./1D_like_surface/parameter_data/' + oneD_names[3] + '_vals.txt', 'w')
    counter = r_r[0]
    while counter < r_r[1]:
        f.write("%s \n" % counter)
        if(counter < c[3] and counter + r_r[2] > c[3]):
            f.write("%s \n" % c[3])
        counter += r_r[2]
    f.close()

    #  MASS  #
    f = open('./1D_like_surface/parameter_data/' + oneD_names[4] + '_vals.txt', 'w')
    counter = m[0]
    while counter < m[1]:
        f.write("%s \n" % counter)
        if(counter < c[4] and counter + m[2] > c[4]):
            f.write("%s \n" % c[4])
        counter += m[2]
    f.close()

    #  MASS RATIO  #
    f = open('./1D_like_surface/parameter_data/' + oneD_names[5] + '_vals.txt', 'w')
    counter = m_r[0]
    while counter < m_r[1]:
        f.write("%s \n" % counter)
        if(counter < c[5] and counter + m_r[2] > c[5]):
            f.write("%s \n" % c[5])
        counter += m_r[2]
    f.close()

    #    Correct Answers     #
    f = open('./1D_like_surface/parameter_data/correct.txt', 'w')
    for i in range(0, 500):
        f.write("%f \t %f \t %f \t %f \t %f \t %f \t %f\n" % (-i, c[0], c[1], c[2], c[3], c[4], c[5]))

def oneD_parser():
    for i in range(0,6):
        g = open('./1D_like_surface/parameter_sweeps/' + str(oneD_names[i]) + '.txt', 'r')
        f = open('./1D_like_surface/likelihood_data/' + str(oneD_names[i]) + '_data.txt', 'w')

        for line in g:
            if (line.startswith("<")):
                ss = line.split('<search_likelihood>')#splits the line between the two sides the delimiter
                tt = ss[1].split('</search_likelihood>')#chooses the second of the split parts and resplits
                f.write("%s \n" % tt[0])#writes the first of the resplit lines
        
    f.close()
    g.close()

def oneD_plot():
    ft = [3.0, 5.0]#plot ranges
    bt = [0.8, 1.2]
    r  = [0.1, 1.3]
    rr = [0.1, .95]
    m  = [1., 120.0]
    mr = [.01, .95]
    l = -200
    ranges_start = [ft[0], bt[0], r[0], rr[0], m[0], mr[0]]
    ranges_end   = [ft[1], bt[1], r[1], rr[1], m[1], mr[1]]
    
    #ranges_start = [ft[0], r[0], rr[0], m[0], mr[0]]
    #ranges_end   = [ft[1], r[1], rr[1], m[1], mr[1]]
    #how many of the data sets are we plotting
    N  = 6
    M  = 0
    
    #f   = 'forward evole time'
    #b   = 'backward evolve time'
    #rad  = 'radius'
    #r_r = 'radius ratio'
    #mass  = 'mass'
    #m_r = 'mass ratio'

    titles  = ['Forward Evolve Time', 'Reverse Orbit Time Ratio', 'Baryonic Scale Radius', 'Baryonic Scale Radius Ratio', 'Baryonic Matter Mass',  'Baryonic to Mass Ratio']
    #titles  = ['Forward Evolve Time', 'Baryonic Scale Radius', 'Dark Scale Radius', 'Baryonic Matter Mass',  'Dark Matter Mass']
    # # # # # # # # # # # # # # # # # # # # # # # # # 
    data_vals = "parameter_data/"
    like_data = "likelihood_data/"


    f = open('1D_plot.gnuplot', 'w')
    f.write("reset\n")
    f.write("set terminal jpeg\n")
    f.write("set key off\n")

    for i in range(M, N):
        f.write("set xlabel '" + titles[i] + "'\n")
        f.write("set ylabel 'likelihood'\n")
        f.write("set yrange [" + str(l) + ":0]\n")
        f.write("set xrange[" + str(ranges_start[i]) + ":" + str(ranges_end[i]) + "]\n")
        
        p = "<paste 1D_like_surface/parameter_data/" + oneD_names[i] + "_vals.txt 1D_like_surface/likelihood_data/" + oneD_names[i] + "_data.txt"
        f.write("set output '1D_like_surface/plots/" + oneD_names[i] + ".jpeg' \n")
        f.write("set title 'Likelihood Surface of " + titles[i] + "' \n")
        f.write("plot '" + p + "' using 1:2  with lines\n\n") 

        f.write("# # # # # # # # # # # # # # # # # #\n")

    f.close()

    os.system("gnuplot 1D_plot.gnuplot 2>>piped_output.txt")
    os.system("rm 1D_plot.gnuplot")
    return 0

def oneD_multiplot():
    titles  = ['Forward Evolve Time (Gyr)_{}', 'Reverse Orbit Ratio (T_{f} / T_{r})', 'Baryon Scale Radius (kpc)_{}', 'Scale Radius Ratio [R_{Stars}/(R_{Stars} + R_{Dark})]', 'Baryonic Mass_{}',  'Mass Ratio [M_{Stars}/M_{Total}]']
    labels  = ['Forward Evolve Time (Gyr)', 'Reverse Orbit Ratio', 'Baryon Scale Radius (kpc)', 'Scale Radius Ratio', 'Baryonic Mass (Sim Mass Units)',  'Mass Ratio']
    #titles  = ['Forward Evolve Time (Gyr)',  'Baryon Scale Radius (kpc)', 'Scale Radius Ratio (Stellar/Dark)', 'Total Mass (Simulation Mass Units)',  'Mass Ratio (Baryonic/Total)']
    #ranges
    ft = [3.0, 5.0]#plot ranges
    bt = [0.8, 1.2]
    r  = [0.1, 1.3]
    rr = [0.1, .95]
    m  = [1., 120.0]
    mr = [.01, .95]
    l = -200
    ranges_start = [ft[0], bt[0], r[0], rr[0], m[0], mr[0]]
    ranges_end   = [ft[1], bt[1], r[1], rr[1], m[1], mr[1]]
    #ranges_start = [ft[0], r[0], rr[0], m[0], mr[0]]
    #ranges_end   = [ft[1], r[1], rr[1], m[1], mr[1]]
    N  = 6
    M  = 0

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    data_vals = "parameter_data/"
    like_data = "likelihood_data/"


    f = open('multiplot_1d.gnuplot', 'w')
    f.write("reset\n")
    f.write("set terminal png size 1800,1200 enhanced \n")
    f.write("set key off\n")
    f.write("set border linewidth 2\n")
    f.write("set title font 'Times-Roman,20'\n")
    f.write("set output '1D_like_surface/plots/like_surfaces_1d.png' \n")
    f.write("set multiplot layout 2,3 rowsfirst\n")
    for i in range(M, N):
        f.write("set size ratio -1 \n")
        f.write("set size square\n")
        f.write("set ylabel 'Likelihood ' font ',26' offset -1,0\n")
        f.write("set lmargin 11\n")
        f.write("set tmargin 0\n")
        f.write("set xlabel '" + titles[i] + "' font ',26' offset 0,-1\n")
        #f.write("set tics scale 0.5\n")
        f.write("set xtics font ', 20'\n")
        f.write("set ytics font ', 20'\n")
        f.write("set yrange [" + str(l) + ":0]\n")
        f.write("set xrange[" + str(ranges_start[i]) + ":" + str(ranges_end[i]) + "]\n")
        #f.write("set parametric\n")
        p = "<paste 1D_like_surface/parameter_data/" + oneD_names[i] + "_vals.txt 1D_like_surface/likelihood_data/" + oneD_names[i] + "_data.txt"
        #f.write("set title '" + titles[i] + "' font ',22'\n")
        f.write("plot '" + p + "' using 1:2  with lines linecolor rgb 'blue' lw 2, '1D_like_surface/parameter_data/correct.txt' using " + str(i + 2) + ":1 with lines lc rgb 0,0,0\n\n") 

        f.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # \n")
        f.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # \n")

    f.close()

    os.system("gnuplot multiplot_1d.gnuplot 2>>piped_output.txt")
    os.system("rm multiplot_1d.gnuplot")
    return 0

def oneD_cost_emd_parser():
    for i in range(0,5):
        g = open('./1D_like_surface/parameter_sweeps/' + str(oneD_names[i]) + '.txt', 'r')
        f = open('./1D_like_surface/cost_emd_data/' + str(oneD_names[i]) + '_cost_data.txt', 'w')
        d = open('./1D_like_surface/cost_emd_data/' + str(oneD_names[i]) + '_emd_data.txt', 'w')
        for line in g:
            if (line.startswith("log(EMDComponent)")):
                ss = line.split('log(EMDComponent) = ')#splits the line between the two sides the delimiter
                d.write("%f\n" % (float(ss[1])))#writes the first of the resplit lines
                
            if (line.startswith("log(CostComponent)")):
                tt = line.split('log(CostComponent) = ')#chooses the second of the split parts and resplits
                f.write("%s" % (tt[1]))#writes the first of the resplit lines
        
    f.close()
    g.close()
    d.close()

def oneD_cost_emd_plot():
    ft = [3.8, 4.3]#plot ranges
    bt = [3.8, 4.3]
    r  = [0.1, 4.0]
    rr = [0.7, 4.0]
    m  = [2.0, 120.0]
    mr = [2, 1200]
    l = -100
    #ranges_start = [ft[0], bt[0], r[0], rr[0], m[0], mr[0]]
    #ranges_end   = [ft[1], bt[1], r[1], rr[1], m[1], mr[1]]
    ranges_start = [ft[0], r[0], rr[0], m[0], mr[0]]
    ranges_end   = [ft[1], r[1], rr[1], m[1], mr[1]]
    #how many of the data sets are we plotting
    N  = 5
    M  = 0
    
    #titles  = ['Forward Evolve Time', 'Reverse Orbit Time', 'Baryonic Scale Radius', 'Dark Scale Radius', 'Baryonic Matter Mass',  'Dark Matter Mass']
    titles  = ['Forward Evolve Time', 'Baryonic Scale Radius', 'Dark Scale Radius', 'Baryonic Matter Mass',  'Dark Matter Mass']
    # # # # # # # # # # # # # # # # # # # # # # # # # 
    data_vals = "parameter_data/"
    like_data = "likelihood_data/"


    f = open('1D_plot.gnuplot', 'w')
    f.write("reset\n")
    f.write("set terminal jpeg\n")
    f.write("set key on\n")

    for i in range(M, N):
        f.write("set xlabel '" + titles[i] + "'\n")
        f.write("set ylabel 'likelihood'\n")
        f.write("set yrange [" + str(l) + ":0]\n")
        f.write("set xrange[" + str(ranges_start[i]) + ":" + str(ranges_end[i]) + "]\n")
        
        p = "<paste 1D_like_surface/parameter_data/" + oneD_names[i] + "_vals.txt 1D_like_surface/cost_emd_data/" + oneD_names[i] + "_cost_data.txt"
        q = "<paste 1D_like_surface/parameter_data/" + oneD_names[i] + "_vals.txt 1D_like_surface/cost_emd_data/" + oneD_names[i] + "_emd_data.txt"
        w = "<paste 1D_like_surface/parameter_data/" + oneD_names[i] + "_vals.txt 1D_like_surface/likelihood_data/" + oneD_names[i] + "_data.txt"
        f.write("set output '1D_like_surface/cost_emd_plots/" + oneD_names[i] + "_cost.jpeg' \n")
        f.write("set title 'Cost and EMD Surface of " + titles[i] + "' \n")
        f.write("plot '" + p + "' using 1:2  with lines title 'Cost', '" + q + "' using 1:2  with lines title 'EMD', '" + w + "' using 1:2  with lines title 'Likelihood'\n  \n") 
        
        #p = "<paste 1D_like_surface/parameter_data/" + oneD_names[i] + "_vals.txt 1D_like_surface/cost_emd_data/" + oneD_names[i] + "_emd_data.txt"
        #f.write("set output '1D_like_surface/cost_emd_plots/" + oneD_names[i] + "_emd.jpeg' \n")
        #f.write("set title 'EMD Surface of " + titles[i] + "' \n")
        #f.write("plot '" + p + "' using 1:2  with lines\n\n") 

        f.write("# # # # # # # # # # # # # # # # # #\n")

    f.close()

    os.system("gnuplot 1D_plot.gnuplot 2>>piped_output.txt")
    os.system("rm 1D_plot.gnuplot")

def sort(likes, vals):
    N = len(likes)
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
    matches = 0.0
    for i in range(0, N):
        for j in range(0, N):
            if(vals[i] == vals_new[j] and likes[i] == likes_new[j]):
                matches += 1.0
    fraction_match = 100.0 * matches / float(N)
    return fraction_match

def random_iterator_sweep():
    N = 3
    M = 0
    #parse the data
    for i in range(0, N):
        g = open('./1D_like_surface/parameter_sweeps/' + str(oneD_names[i]) + '.txt', 'r')
        f = open('./1D_like_surface/parameter_sweeps/' + str(oneD_names[i]) + '_data.txt', 'w')

        for line in g:
            if (line.startswith("<")):
                ss = line.split('<search_likelihood>')#splits the line between the two sides the delimiter
                tt = ss[1].split('</search_likelihood>')#chooses the second of the split parts and resplits
                f.write("%s \n" % tt[0])#writes the first of the resplit lines
        
    f.close()
    g.close()
    
    
    
    for i in range(0, N):
        likes = []
        vals  = []
        vals_new = []
        likes_new = []
        
        f = open('./1D_like_surface/parameter_sweeps/' + str(oneD_names[i]) + '_data.txt', 'r')
        g = open('./1D_like_surface/parameter_sweeps/' + str(oneD_names[i]) + '_vals.txt', 'r')
        h = open('./1D_like_surface/parameter_data/' + str(oneD_names[i]) + '_sorted_data_vals.txt', 'w')
        counter_like = 0
        counter_val  = 0
        
        #make sure lists are the same length
        for line in f:
            l = float(line)
            likes.append(l)
            counter_like += 1
        for line in g:
            l = float(line)
            vals.append(l)
            counter_val += 1
            
        #report and break if they are not
        if( counter_like != counter_val):
            print "value list length mismatch"
            break

        #sort the data values in order of least to greats with their corresponding likelihoods.
        vals_new, likes_new = sort(likes, vals)
        #make sure the likelihoods were sorted correctly with the values
        reliability_of_sorting = reliability(likes, likes_new, vals, vals_new)
        
        if(reliability_of_sorting != 100.0):
            print "HOLY FUCKING SHIT, SOMETHING IS WRONG"
        
        for j in range(0, counter_like):
            h.write("%0.15f %0.15f\n" % (vals_new[j], likes_new[j]))
        
        os.system("rm ./1D_like_surface/parameter_sweeps/" + str(oneD_names[i]) + "_data.txt")
        f.close()
        g.close()
        h.close()
        
        
    ft = [3.0, 5.0]#plot ranges
    bt = [0.8, 1.2]
    r  = [0.1, 1.3]
    rr = [0.1, .95]
    m  = [1., 120.0]
    mr = [.01, .95]
    l = -200
    ranges_start = [ft[0], bt[0], r[0], rr[0], m[0], mr[0]]
    ranges_end   = [ft[1], bt[1], r[1], rr[1], m[1], mr[1]]
    

    titles  = ['Forward Evolve Time', 'Reverse Orbit Time Ratio', 'Baryonic Scale Radius', 'Baryonic Scale Radius Ratio', 'Baryonic Matter Mass',  'Baryonic to Mass Ratio']
    # # # # # # # # # # # # # # # # # # # # # # # # # 
    data_vals = "parameter_data/"
    like_data = "likelihood_data/"


    f = open('1D_plot_rani.gnuplot', 'w')
    f.write("reset\n")
    f.write("set terminal jpeg\n")
    f.write("set key off\n")

    for i in range(M, N):
        f.write("set xlabel '" + titles[i] + "'\n")
        f.write("set ylabel 'likelihood'\n")
        f.write("set yrange [" + str(l) + ":0]\n")
        f.write("set xrange[" + str(ranges_start[i]) + ":" + str(ranges_end[i]) + "]\n")
        
        p = "1D_like_surface/parameter_data/" + oneD_names[i] + "_sorted_data_vals.txt"
        f.write("set output '1D_like_surface/plots/" + oneD_names[i] + ".jpeg' \n")
        f.write("set title 'Likelihood Surface of " + titles[i] + "' \n")
        f.write("plot '" + p + "' using 1:2  with lines\n\n") 

        f.write("# # # # # # # # # # # # # # # # # #\n")

    f.close()

    os.system("gnuplot 1D_plot_rani.gnuplot 2>>piped_output.txt")
    os.system("rm 1D_plot_rani.gnuplot")
    return 0
# # # # # # # # # # # # # # # # # # # # # #
#    Two Dimensional Surface Sweep Func   #
# # # # # # # # # # # # # # # # # # # # # #
def twoD_data_vals():
    f = open('./2D_like_surface/parameter_data/ft_vs_bt.txt', 'w')

    #parameter = [start, end, increment]
    #--------------------------------------------------------------------------------------------------

    #  FORWARD TIME VS BACKTIME #
    fwt_counter = ft[0]
    fwt = str(fwt_counter)
    while fwt_counter < ft[1]:
        bwt_counter = bt[0]
        bwt = str(bwt_counter)
        while bwt_counter < bt[1]:
            f.write("%s \t %s \n" % (fwt_counter, bwt_counter))
            bwt_counter = bwt_counter + bt[2]
            bwt = str(bwt_counter)
        fwt_counter = fwt_counter + ft[2]
        fwt = str(fwt_counter)
    f.close()
    
    #  FORWARD TIME VS RAD #
    f = open('./2D_like_surface/parameter_data/ft_vs_rad.txt', 'w')
    fwt_counter = ft[0]
    fwt = str(fwt_counter)
    while fwt_counter < ft[1]:
        rad_counter = r[0]
        rad = str(rad_counter)
        while rad_counter < r[1]:
            f.write("%s \t %s \n" % (fwt_counter, rad_counter))
            rad_counter = rad_counter + r[2]
            rad = str(rad_counter)
        fwt_counter = fwt_counter + ft[2]
        fwt = str(fwt_counter)
    f.close()


    #  FORWARD TIME VS RAD RATIO #
    f = open('./2D_like_surface/parameter_data/ft_vs_rr.txt', 'w')
    fwt_counter = ft[0]
    fwt = str(fwt_counter)
    while fwt_counter < ft[1]:
        rr_counter = r_r[0]
        rr = str(rr_counter)
        while rr_counter < r_r[1]:
            f.write("%s \t %s \n" % (fwt_counter, rr_counter))
            rr_counter = rr_counter + r_r[2]
            rr = str(rr_counter)
        fwt_counter = fwt_counter + ft[2]
        fwt = str(fwt_counter)
    f.close()

    #  FORWARD TIME VS MASS #
    f = open('./2D_like_surface/parameter_data/ft_vs_m.txt', 'w')
    fwt_counter = ft[0]
    fwt = str(fwt_counter)
    while fwt_counter < ft[1]:
        m_counter = m[0]
        ms = str(m_counter)
        while m_counter < m[1]:
            f.write("%s \t %s \n" % (fwt_counter, m_counter))
            m_counter = m_counter + m[2]
            ms = str(m_counter) 
        fwt_counter = fwt_counter + ft[2]
        fwt = str(fwt_counter)
    f.close()   
        
    #  FORWARD TIME VS MASS RATIO #
    f = open('./2D_like_surface/parameter_data/ft_vs_mr.txt', 'w')
    fwt_counter = ft[0]
    fwt = str(fwt_counter)
    while fwt_counter < ft[1]:
        mr_counter = m_r[0]
        mr = str(mr_counter)
        while mr_counter < m_r[1]:
            f.write("%s \t %s \n" % (fwt_counter, mr_counter))
            mr_counter = mr_counter + m_r[2]
            mr = str(mr_counter) 
        fwt_counter = fwt_counter + ft[2]
        fwt = str(fwt_counter)
    f.close()    
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    #  BACKWARD TIME VS RAD #
    f = open('./2D_like_surface/parameter_data/bt_vs_r.txt', 'w')
    bwt_counter = bt[0]
    bwt = str(bwt_counter)
    while bwt_counter < bt[1]:
        rad_counter = r[0]
        rad = str(rad_counter)
        while rad_counter < r[1]:
            f.write("%s \t %s \n" % (bwt_counter, rad_counter))
            rad_counter = rad_counter + r[2]
            rad = str(rad_counter)
        bwt_counter = bwt_counter + bt[2]
        bwt = str(bwt_counter)
    f.close()

    #  BACKWARD TIME VS RAD RATIO #
    f = open('./2D_like_surface/parameter_data/bt_vs_rr.txt', 'w')
    bwt_counter = bt[0]
    bwt = str(bwt_counter)
    while bwt_counter < bt[1]:
        rr_counter = r_r[0]
        rr = str(rr_counter)
        while rr_counter < r_r[1]:
            f.write("%s \t %s \n" % (bwt_counter, rr_counter))
            rr_counter = rr_counter + r_r[2]
            rr = str(rr_counter)
        bwt_counter = bwt_counter + bt[2]
        bwt = str(bwt_counter)
    f.close()

    #  BACKWARD TIME VS MASS #
    f = open('./2D_like_surface/parameter_data/bt_vs_m.txt', 'w')
    bwt_counter = bt[0]
    bwt = str(bwt_counter)
    while bwt_counter < bt[1]:
        m_counter = m[0]
        ms = str(m_counter)
        while m_counter < m[1]:
            f.write("%s \t %s \n" % (bwt_counter, m_counter))
            m_counter = m_counter + m[2]
            ms = str(m_counter) 
        bwt_counter = bwt_counter + bt[2]
        bwt = str(bwt_counter) 
    f.close()

    #  BACKWARDS TIME VS MASS RATIO #
    f = open('./2D_like_surface/parameter_data/bt_vs_mr.txt', 'w')
    bwt_counter = bt[0]
    bwt = str(bwt_counter)
    while bwt_counter < bt[1]:
        mr_counter = m_r[0]
        mr = str(mr_counter)
        while mr_counter < m_r[1]:
            f.write("%s \t %s \n" % (bwt_counter, mr_counter))
            mr_counter = mr_counter + m_r[2]
            mr = str(mr_counter) 
        bwt_counter = bwt_counter + bt[2]
        bwt = str(bwt_counter)
    f.close()
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    #  RAD VS RAD RATIO #
    f = open('./2D_like_surface/parameter_data/r_vs_rr.txt', 'w')
    r_counter = r[0]
    rad = str(r_counter)
    while r_counter < r[1]:
        rr_counter = r_r[0]
        rr = str(rr_counter)
        while rr_counter < r_r[1]:
            f.write("%s \t %s \n" % (r_counter, rr_counter))
            rr_counter = rr_counter + r_r[2]
            rr = str(rr_counter)
        r_counter = r_counter + r[2]
        rad = str(r_counter)
    f.close()

    #  RAD VS MASS #
    f = open('./2D_like_surface/parameter_data/r_vs_m.txt', 'w')
    r_counter = r[0]
    rad = str(r_counter)
    while r_counter < r[1]:
        m_counter = m[0]
        ms = str(m_counter)
        while m_counter < m[1]:
            f.write("%s \t %s \n" % (r_counter, m_counter))
            m_counter = m_counter + m[2]
            ms = str(m_counter) 
        r_counter = r_counter + r[2]
        rad = str(r_counter)
    f.close()

    #  RAD VS MASS RATIO #
    f = open('./2D_like_surface/parameter_data/r_vs_mr.txt', 'w')
    r_counter = r[0]
    rad = str(r_counter)
    while r_counter < r[1]:
        mr_counter = m_r[0]
        mr = str(mr_counter)
        while mr_counter < m_r[1]:
            f.write("%s \t %s \n" % (r_counter, mr_counter))
            mr_counter = mr_counter + m_r[2]
            mr = str(mr_counter) 
        r_counter = r_counter + r[2]
        rad = str(r_counter)
    f.close()
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    #  RAD RATIO VS MASS #
    f = open('./2D_like_surface/parameter_data/rr_vs_m.txt', 'w')
    rr_counter = r_r[0]
    rr = str(rr_counter)
    while rr_counter < r_r[1]:
        m_counter = m[0]
        ms = str(m_counter)
        while m_counter < m[1]:
            f.write("%s \t %s \n" % (rr_counter, m_counter))
            m_counter = m_counter + m[2]
            ms = str(m_counter) 
        rr_counter = rr_counter + r_r[2]
        rr = str(rr_counter)
    f.close()

    #  RAD RATIO VS MASS RATIO #
    f = open('./2D_like_surface/parameter_data/rr_vs_mr.txt', 'w')
    rr_counter = r_r[0]
    rr = str(rr_counter)
    while rr_counter < r_r[1]:
        mr_counter = m_r[0]
        mr = str(mr_counter)
        while mr_counter < m_r[1]:
            f.write("%s \t %s \n" % (rr_counter, mr_counter))
            mr_counter = mr_counter + m_r[2]
            mr = str(mr_counter) 
        rr_counter = rr_counter + r_r[2]
        rr = str(rr_counter)
    f.close()
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    #  MASS VS MASS RATIO #
    f = open('./2D_like_surface/parameter_data/m_vs_mr.txt', 'w')
    m_counter = m[0]
    ms = str(m_counter)
    while m_counter < m[1]:
        mr_counter = m_r[0]
        mr = str(mr_counter)
        while mr_counter < m_r[1]:
            f.write("%s \t %s \n" % (m_counter, mr_counter))
            mr_counter = mr_counter + m_r[2]
            mr = str(mr_counter) 
        m_counter = m_counter + m[2]
        ms = str(m_counter)
    f.close()

def twoD_parser():
    names   = [ 'ft_vs_bt', 'ft_vs_rad', 'ft_vs_rr', 'ft_vs_m', 'ft_vs_mr', 'bt_vs_r', 'bt_vs_rr', 'bt_vs_m', 'bt_vs_mr', 'r_vs_rr', 'r_vs_m', 'r_vs_mr', 'rr_vs_m', 'rr_vs_mr', 'm_vs_mr']
    N  = 15
    M  = 0

    for i in range(M,N):
        g = open('./2D_like_surface/2d_parameter_sweeps/' + str(names[i]) + '.txt', 'r')
        f = open('./2D_like_surface/likelihood_data/' + str(names[i]) + '_data.txt', 'w')

        for line in g:
            if (line.startswith("<")):
                ss = line.split('<search_likelihood>')#splits the line between the two sides the delimiter
                tt = ss[1].split('</search_likelihood>')#chooses the second of the split parts and resplits
                f.write("%s \n" % tt[0])#writes the first of the resplit lines
        
    f.close()
    g.close()

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
    
# # # # # # # # # #
#     Cleaners    #
# # # # # # # # # #


def oneD_cleanse():
    os.system("rm -r 1D_like_surface/likelihood_data")
    os.system("mkdir 1D_like_surface/likelihood_data")

    os.system("rm -r 1D_like_surface/plots")
    os.system("mkdir 1D_like_surface/plots")

    os.system("rm -r 1D_like_surface/parameter_data")
    os.system("mkdir 1D_like_surface/parameter_data")
    
    os.system("rm -r 1D_like_surface/cost_emd_data")
    os.system("mkdir 1D_like_surface/cost_emd_data")
    
    os.system("rm -r 1D_like_surface/cost_emd_plots")
    os.system("mkdir 1D_like_surface/cost_emd_plots")

def twoD_cleanse():
    os.system("rm -r 2D_like_surface/likelihood_data")
    os.system("mkdir 2D_like_surface/likelihood_data")

    os.system("rm -r 2D_like_surface/plots")
    os.system("mkdir 2D_like_surface/plots")

    os.system("rm -r 2D_like_surface/parameter_data")
    os.system("mkdir 2D_like_surface/parameter_data")

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
    if(oneD_clean == True):
        oneD_cleanse()
    
    if(twoD_clean == True):
        twoD_cleanse()
    
    if(oneD_surface == True):
        oneD_data_vals()
        #oneD_parser()
        oneD_plot()
    
    if(oneD_multiploter == True):
        oneD_multiplot()

    if(plot_cost_emd == True):
        oneD_cost_emd_parser()
        oneD_cost_emd_plot()
        
        
    if(twoD_surface == True):
        twoD_data_vals()
        twoD_parser()
        twoD_plot()
        
    if(random_iterator == True):
        random_iterator_sweep()
    
    if(special_parser == True):
        all_hists_in_one_file_parser()
main()    