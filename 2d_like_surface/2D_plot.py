#! /usr/bin/python
import os

f   = 'forward evole time'
b   = 'backward evolve time'
rad  = 'radius'
r_r = 'radius ratio'
mass  = 'mass'
m_r = 'mass ratio'


names = [ 'ft_vs_bt', 'ft_vs_rad', 'ft_vs_rr', 'ft_vs_m', 'ft_vs_mr', 'bt_vs_r', 'bt_vs_rr', 'bt_vs_m', 'bt_vs_mr', 'r_vs_rr', 'r_vs_m', 'r_vs_mr', 'rr_vs_m', 'rr_vs_mr', 'm_vs_mr']
t  = ['forward evole time', 'backward evolve time', 'radius', 'radius ratio', 'mass',  'mass ratio']
xlabels = [f, f, f, f, f, b, b, b, b, rad, rad ,rad, r_r, r_r, mass]  
ylabels = [b, rad, r_r, mass, m_r, rad, r_r, mass, m_r, r_r, mass, m_r, mass, m_r, m_r]

#ranges
ft = 3.0
bt = 2.0
r = 1.0
rr = 0.75
m = 50
mr = 0.75
xranges = [ft, ft, ft, ft, ft, bt, bt, bt, bt, r, r, r, rr, rr, m]
yranges = [bt, r, rr, m, mr, r, rr, m , mr, rr, m, mr, m, mr, mr]
N  = 15
M  = 0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data_vals = "parameter_data/"
like_data = "likelihood_data/"


f = open('2D_plot.gnuplot', 'w')
f.write("reset\n")
f.write("set terminal jpeg\n")
f.write("set key on\n")

for i in range(M, N):
    f.write("set xlabel '" + xlabels[i] + "'\n")
    f.write("set ylabel '" + ylabels[i] + "'\n")
    f.write("set zlabel 'likelihood'\n")
    f.write("set key off \n")
    f.write("set palette rgbformula -7,2,-7\n")
    f.write("set cbrange [-1000:0]\n")
    f.write("set xrange[0:" + str(xranges[i]) + "]\n")
    f.write("set yrange[0:" + str(yranges[i]) + "]\n\n\n")

    p = "<paste parameter_data/" + names[i] + ".txt likelihood_data/" + names[i] + "_data.txt"
    f.write("set output 'plots/" + names[i] + ".jpeg' \n")
    f.write("set title 'Likelihood Surface of " + str(xlabels[i]) + " vs " + str(ylabels[i]) + "' \n")
    f.write("plot '" + p + "' using 1:2:3  with image \n\n") 

    f.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # \n")
    f.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # \n")

f.close()

os.system("gnuplot 2D_plot.gnuplot 2>>piped_output.txt")
os.system("rm 2D_plot.gnuplot")