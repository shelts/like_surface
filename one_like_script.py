#! /usr/bin/python
import os
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Control Panel       #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
y = True
n = False

oneD_clean = y
twoD_clean = n
oneD_surface = n
twoD_surface = n

oneD_multiploter = n



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Engine Room         #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # #
#    One Dimensional Surface Sweep Func   #
# # # # # # # # # # # # # # # # # # # # # #
def oneD_data_vals():
    ft         = [3.9, 4.2, 0.01]#
    bt         = [0.96, 1.08, 0.005]#
    r          = [0.1, 0.8, 0.01]#
    r_r        = [0.1, 0.8, 0.01]#
    m          = [1.0, 20.0, 0.25]#
    m_r        = [0.17, 0.24, 0.001]#
    #parameter    = [start, end, increment]

    c = [4, 1, 0.2, 0.25, 60, 0.2]
    f = open('./1D_like_surface/parameter_data/ft_vals.txt', 'w')
    #  FORWARD TIME #
    counter = ft[0]
    while counter < ft[1]:
        f.write("%s \n" % counter)
        counter = counter + ft[2]
    f.close()
    
    #  BACKWARD TIME  #  
    f = open('./1D_like_surface/parameter_data/bt_vals.txt', 'w')
    counter = bt[0]
    while counter < bt[1]:
        f.write("%s \n" % counter)
        counter = counter + bt[2]
    f.close() 

    #  RADIUS  #
    f = open('./1D_like_surface/parameter_data/rad_vals.txt', 'w')
    counter = r[0]
    while counter < r[1]:
        f.write("%s \n" % counter)
        counter = counter + r[2]
    f.close()
    
    #  RADIUS RATIO  #
    f = open('./1D_like_surface/parameter_data/rr_vals.txt', 'w')
    counter = r_r[0]
    while counter < r_r[1]:
        f.write("%s \n" % counter)
        counter = counter + r_r[2]
    f.close()

    #  MASS  #
    f = open('./1D_like_surface/parameter_data/mass_vals.txt', 'w')
    counter = m[0]
    while counter < m[1]:
        f.write("%s \n" % counter)
        counter = counter + m[2]
    f.close()

    #  MASS RATIO  #
    f = open('./1D_like_surface/parameter_data/mr_vals.txt', 'w')
    counter = m_r[0]
    while counter < m_r[1]:
        f.write("%s \n" % counter)
        counter = counter + m_r[2]
    f.close()

    #    Correct Answers     #
    f = open('./1D_like_surface/parameter_data/correct.txt', 'w')
    for i in range(0, 50):
        f.write("%f \t %f \t %f \t %f \t %f \t %f \t %f\n" % (-i, c[0], c[1], c[2], c[3], c[4], c[5]))

def oneD_parser():
    names   = ['ft', 'bt',  'rad', 'rr', 'mass', 'mr']

    for i in range(0,6):
        g = open('./1D_like_surface/parameter_sweeps/' + str(names[i]) + '.txt', 'r')
        f = open('./1D_like_surface/likelihood_data/' + str(names[i]) + '_data.txt', 'w')

        for line in g:
            if (line.startswith("<")):
                ss = line.split('<search_likelihood>')#splits the line between the two sides the delimiter
                tt = ss[1].split('</search_likelihood>')#chooses the second of the split parts and resplits
                f.write("%s \n" % tt[0])#writes the first of the resplit lines
        
    f.close()
    g.close()

def oneD_plot():
    ft = [3.8, 4.2]#plot ranges
    bt = [0.95, 1.05]
    r  = [0.15, 0.8]
    rr = [0.1, 0.8]
    m  = [1.0, 20.0]
    mr = [0.15, 0.25]
    ranges_start = [ft[0], bt[0], r[0], rr[0], m[0], mr[0]]
    ranges_end   = [ft[1], bt[1], r[1], rr[1], m[1], mr[1]]
    
    #how many of the data sets are we plotting
    N  = 6
    M  = 0
    
    #f   = 'forward evole time'
    #b   = 'backward evolve time'
    #rad  = 'radius'
    #r_r = 'radius ratio'
    #mass  = 'mass'
    #m_r = 'mass ratio'

    names   = ['ft', 'bt', 'rad', 'rr', 'mass', 'mr']
    titles  = ['Forward Evolve Time', 'Reverse Orbit Ratio', 'Radius', 'Radius Ratio', 'Mass',  'Mass Ratio']
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
        f.write("set yrange [-50:0]\n")
        f.write("set xrange[" + str(ranges_start[i]) + ":" + str(ranges_end[i]) + "]\n")
        
        p = "<paste 1D_like_surface/parameter_data/" + names[i] + "_vals.txt 1D_like_surface/likelihood_data/" + names[i] + "_data.txt"
        f.write("set output '1D_like_surface/plots/" + names[i] + ".jpeg' \n")
        f.write("set title 'Likelihood Surface of " + titles[i] + "' \n")
        f.write("plot '" + p + "' using 1:2  with lines\n\n") 

        f.write("# # # # # # # # # # # # # # # # # #\n")

    f.close()

    os.system("gnuplot 1D_plot.gnuplot 2>>piped_output.txt")
    os.system("rm 1D_plot.gnuplot")

def oneD_multiplot():
    f   = 'forward evole time'
    b   = 'backward evolve time'
    rad  = 'radius'
    r_r = 'radius ratio'
    mass  = 'mass'
    m_r = 'mass ratio'

    names   = ['ft', 'bt', 'rad', 'rr', 'mass', 'mr']
    titles  = ['Forward Evolve Time (Gyr)', 'Reverse Orbit Ratio', 'Baryon Scale Radius (kpc)', 'Scale Radius Ratio (Stellar/Dark)', 'Total Mass (Simulation Mass Units)',  'Mass Ratio (Baryonic/Total)']

    #correct answers:
    correct = [4, 1, 0.2, 0.25, 60, 0.2]

    #ranges
    ft = [3.8, 4.2]
    bt = [0.95, 1.05]
    r  = [0.15, 0.8]
    rr = [0.1, 0.8]
    m  = [1, 20.0]
    mr = [0.15, 0.25]
    ranges_start = [ft[0], bt[0], r[0], rr[0], m[0], mr[0]]
    ranges_end   = [ft[1], bt[1], r[1], rr[1], m[1], mr[1]]
    N  = 6
    M  = 0

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    data_vals = "parameter_data/"
    like_data = "likelihood_data/"


    f = open('multiplot_1d.gnuplot', 'w')
    f.write("reset\n")
    f.write("set terminal png size 1500,900 \n")
    f.write("set key off\n")
    f.write("set title font 'Times-Roman,20'\n")
    f.write("set output '1D_like_surface/plots/like_surfaces_1d.png' \n")
    f.write("set multiplot layout 2,3 rowsfirst\n")
    for i in range(M, N):
        f.write("set xlabel '" + titles[i] + "'\n")
        f.write("set ylabel 'Likelihood '\n")
        f.write("set yrange [-50:0]\n")
        f.write("set xrange[" + str(ranges_start[i]) + ":" + str(ranges_end[i]) + "]\n")
        #f.write("set parametric\n")
        p = "<paste 1D_like_surface/parameter_data/" + names[i] + "_vals.txt 1D_like_surface/likelihood_data/" + names[i] + "_data.txt"
        f.write("set title '" + titles[i] + "' \n")
        f.write("plot '" + p + "' using 1:2  with lines, 'parameter_data/correct.txt' using " + str(i + 2) + ":1 with lines\n\n") 

        f.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # \n")
        f.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # \n")

    f.close()

    os.system("gnuplot multiplot_1d.gnuplot 2>>piped_output.txt")
    os.system("rm multiplot_1d.gnuplot")
# # # # # # # # # # # # # # # # # # # # # #
#    Two Dimensional Surface Sweep Func   #
# # # # # # # # # # # # # # # # # # # # # #
def twoD_data_vals():
    ft         = [0.25, 3.0, 0.05]
    bt         = [0.25, 2.0, 0.05]
    r          = [0.1, 1.0, 0.05]
    r_r        = [0.1, 0.75, 0.05]
    m          = [2.0, 50.0, 1.0]
    m_r        = [0.1, 0.75, 0.05]
    #parameter = [start, end, increment]
    #--------------------------------------------------------------------------------------------------

    #  FORWARD TIME VS BACKTIME #
    f = open('./2D_like_surface/parameter_data/ft_vs_bt.txt', 'w')
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

def twoD_cleanse():
    os.system("rm -r 2D_like_surface/likelihood_data")
    os.system("mkdir 2D_like_surface/likelihood_data")

    os.system("rm -r 2D_like_surface/plots")
    os.system("mkdir 2D_like_surface/plots")

    os.system("rm -r 2D_like_surface/parameter_data")
    os.system("mkdir 2D_like_surface/parameter_data")


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
        oneD_parser()
        oneD_plot()
    
    if(oneD_multiploter == True):
        oneD_multiplot()

        
        
        
    if(twoD_surface == True):
        twoD_data_vals()
        twoD_parser()
        twoD_plot()
        
main()    