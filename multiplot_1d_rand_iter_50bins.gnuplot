reset
set terminal jpeg size 1800,1200 enhanced 
set key off
set border linewidth 2
set title font 'Times-Roman,20'
set output '1D_like_surface/plots_rand_iter_50bins/multiplot.jpeg' 
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
plot '1D_like_surface/likelihood_data_rand_iter_50bins/ft_data_vals.txt' using 1:2  with lines linecolor rgb 'blue' lw 2, '1D_like_surface/likelihood_data_rand_iter_50bins/correct.txt' using 2:1 with lines lc rgb 0,0,0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
set size ratio -1 
set size square
set ylabel 'Likelihood ' font ',26' offset -1,0
set lmargin 11
set tmargin 0
set xlabel 'Reverse Orbit Ratio (T_{f} / T_{r})' font ',26' offset 0,-1
set xtics font ', 13'
set ytics font ', 20'
set yrange [-200:0]
set xrange[0.96:1.0]
plot '1D_like_surface/likelihood_data_rand_iter_50bins/bt_data_vals.txt' using 1:2  with lines linecolor rgb 'blue' lw 2, '1D_like_surface/likelihood_data_rand_iter_50bins/correct.txt' using 3:1 with lines lc rgb 0,0,0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
set size ratio -1 
set size square
set ylabel 'Likelihood ' font ',26' offset -1,0
set lmargin 11
set tmargin 0
set xlabel 'Baryon Scale Radius (kpc)_{}' font ',26' offset 0,-1
set xtics font ', 20'
set ytics font ', 20'
set yrange [-200:0]
set xrange[0.15:0.25]
plot '1D_like_surface/likelihood_data_rand_iter_50bins/r_data_vals.txt' using 1:2  with lines linecolor rgb 'blue' lw 2, '1D_like_surface/likelihood_data_rand_iter_50bins/correct.txt' using 4:1 with lines lc rgb 0,0,0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
set size ratio -1 
set size square
set ylabel 'Likelihood ' font ',26' offset -1,0
set lmargin 11
set tmargin 0
set xlabel 'Scale Radius Ratio [R_{Stars}/(R_{Stars} + R_{Dark})]' font ',26' offset 0,-1
set xtics font ', 20'
set ytics font ', 20'
set yrange [-200:0]
set xrange[0.15:0.25]
plot '1D_like_surface/likelihood_data_rand_iter_50bins/rr_data_vals.txt' using 1:2  with lines linecolor rgb 'blue' lw 2, '1D_like_surface/likelihood_data_rand_iter_50bins/correct.txt' using 5:1 with lines lc rgb 0,0,0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
set size ratio -1 
set size square
set ylabel 'Likelihood ' font ',26' offset -1,0
set lmargin 11
set tmargin 0
set xlabel 'Baryonic Mass_{}' font ',26' offset 0,-1
set xtics font ', 20'
set ytics font ', 20'
set yrange [-200:0]
set xrange[10.0:14.0]
plot '1D_like_surface/likelihood_data_rand_iter_50bins/m_data_vals.txt' using 1:2  with lines linecolor rgb 'blue' lw 2, '1D_like_surface/likelihood_data_rand_iter_50bins/correct.txt' using 6:1 with lines lc rgb 0,0,0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
set size ratio -1 
set size square
set ylabel 'Likelihood ' font ',26' offset -1,0
set lmargin 11
set tmargin 0
set xlabel 'Mass Ratio [M_{Stars}/M_{Total}]' font ',26' offset 0,-1
set xtics font ', 20'
set ytics font ', 20'
set yrange [-200:0]
set xrange[0.15:0.25]
plot '1D_like_surface/likelihood_data_rand_iter_50bins/mr_data_vals.txt' using 1:2  with lines linecolor rgb 'blue' lw 2, '1D_like_surface/likelihood_data_rand_iter_50bins/correct.txt' using 7:1 with lines lc rgb 0,0,0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
