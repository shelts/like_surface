#! /usr/bin/python
import os

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
f.write("set output 'plots/like_surfaces_1d.png' \n")
f.write("set multiplot layout 2,3 rowsfirst\n")
for i in range(M, N):
    f.write("set xlabel '" + titles[i] + "'\n")
    f.write("set ylabel 'Likelihood '\n")
    f.write("set yrange [-50:0]\n")
    f.write("set xrange[" + str(ranges_start[i]) + ":" + str(ranges_end[i]) + "]\n")
    #f.write("set parametric\n")
    p = "<paste parameter_data/" + names[i] + "_vals.txt likelihood_data/" + names[i] + "_data.txt"
    f.write("set title '" + titles[i] + "' \n")
    f.write("plot '" + p + "' using 1:2  with lines, 'parameter_data/correct.txt' using " + str(i + 2) + ":1 with lines\n\n") 

    f.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # \n")
    f.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # \n")

f.close()

os.system("gnuplot multiplot_1d.gnuplot 2>>piped_output.txt")
#os.system("rm 1D_plot.gnuplot")