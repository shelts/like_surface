#! /usr/bin/python
import os

f   = 'forward evole time'
b   = 'backward evolve time'
rad  = 'radius'
r_r = 'radius ratio'
mass  = 'mass'
m_r = 'mass ratio'

names   = ['ft', 'bt', 'rad', 'rr', 'mass', 'mr']
titles  = ['Forward Evolve Time', 'Backward Evolve Time', 'Radius', 'Radius Ratio', 'Mass',  'Mass Ratio']

#ranges
ft = [3.0, 5.0]
bt = [0.8, 1.2]
r = [0.1, 0.3]
rr = [0.1, 0.35]
m = [2.0, 120.0]
mr = [0.1, 0.35]
ranges_start = [ft[0], bt[0], r[0], rr[0], m[0], mr[0]]
ranges_end   = [ft[1], bt[1], r[1], rr[1], m[1], mr[1]]
N  = 6
M  = 0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data_vals = "parameter_data/"
like_data = "likelihood_data/"


f = open('1D_plot.gnuplot', 'w')
f.write("reset\n")
f.write("set terminal jpeg\n")
f.write("set key off\n")

for i in range(M, N):
    f.write("set xlabel '" + titles[i] + "'\n")
    f.write("set ylabel 'likelihood'\n")
    f.write("set yrange [-200:0]\n")
    f.write("set xrange[" + str(ranges_start[i]) + ":" + str(ranges_end[i]) + "]\n")

    p = "<paste parameter_data/" + names[i] + "_vals.txt likelihood_data/" + names[i] + "_data.txt"
    f.write("set output 'plots/" + names[i] + ".jpeg' \n")
    f.write("set title 'Likelihood Surface of " + titles[i] + "' \n")
    f.write("plot '" + p + "' using 1:2  with points \n\n") 

    f.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # \n")
    f.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # \n")

f.close()

os.system("gnuplot 1D_plot.gnuplot 2>>piped_output.txt")
#os.system("rm 1D_plot.gnuplot")