reset
set terminal png size 1500,900 
set key off
set title font 'Times-Roman,20'
set output 'plots/like_surfaces_1d.png' 
set multiplot layout 2,3 rowsfirst
set xlabel 'Forward Evolve Time (Gyr)'
set ylabel 'Likelihood '
set yrange [-50:0]
set xrange[3.8:4.2]
set title 'Forward Evolve Time (Gyr)' 
plot '<paste parameter_data/ft_vals.txt likelihood_data/ft_data.txt' using 1:2  with lines, 'parameter_data/correct.txt' using 2:1 with lines

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
set xlabel 'Reverse Orbit Ratio'
set ylabel 'Likelihood '
set yrange [-50:0]
set xrange[0.95:1.05]
set title 'Reverse Orbit Ratio' 
plot '<paste parameter_data/bt_vals.txt likelihood_data/bt_data.txt' using 1:2  with lines, 'parameter_data/correct.txt' using 3:1 with lines

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
set xlabel 'Baryon Scale Radius (kpc)'
set ylabel 'Likelihood '
set yrange [-50:0]
set xrange[0.15:0.8]
set title 'Baryon Scale Radius (kpc)' 
plot '<paste parameter_data/rad_vals.txt likelihood_data/rad_data.txt' using 1:2  with lines, 'parameter_data/correct.txt' using 4:1 with lines

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
set xlabel 'Scale Radius Ratio (Stellar/Dark)'
set ylabel 'Likelihood '
set yrange [-50:0]
set xrange[0.1:0.8]
set title 'Scale Radius Ratio (Stellar/Dark)' 
plot '<paste parameter_data/rr_vals.txt likelihood_data/rr_data.txt' using 1:2  with lines, 'parameter_data/correct.txt' using 5:1 with lines

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
set xlabel 'Total Mass (Simulation Mass Units)'
set ylabel 'Likelihood '
set yrange [-50:0]
set xrange[1:20.0]
set title 'Total Mass (Simulation Mass Units)' 
plot '<paste parameter_data/mass_vals.txt likelihood_data/mass_data.txt' using 1:2  with lines, 'parameter_data/correct.txt' using 6:1 with lines

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
set xlabel 'Mass Ratio (Baryonic/Total)'
set ylabel 'Likelihood '
set yrange [-50:0]
set xrange[0.15:0.25]
set title 'Mass Ratio (Baryonic/Total)' 
plot '<paste parameter_data/mr_vals.txt likelihood_data/mr_data.txt' using 1:2  with lines, 'parameter_data/correct.txt' using 7:1 with lines

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
