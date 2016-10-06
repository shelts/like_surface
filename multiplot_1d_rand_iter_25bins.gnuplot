reset
set terminal jpeg size 1800,1200 enhanced 
set key off
set border linewidth 2
set title font 'Times-Roman,20'
set output '1D_like_surface/plots_rand_iter_25bins/multiplot.jpeg' 
set multiplot layout 2,3 rowsfirst
set size ratio -1 
set size square
set ylabel 'Likelihood ' font ',26' offset -1,0
set lmargin 11
set tmargin 0
set xlabel 'Forward Evolve Time (Gyr)_{}' font ',26' offset 0,-1
set xtics font ', 13'
set ytics font ', 20'
set yrange [-200:0]
set xrange[3.93:3.98]
plot '1D_like_surface/likelihood_data_rand_iter_25bins/ft_data_vals.txt' using 1:2  with lines linecolor rgb 'blue' lw 2, '1D_like_surface/likelihood_data_rand_iter_25bins/correct.txt' using 2:1 with lines lc rgb 0,0,0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
