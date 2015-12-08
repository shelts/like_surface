reset
set terminal jpeg
set key off
set xlabel 'Forward Evolve Time'
set ylabel 'likelihood'
set yrange [-200:0]
set xrange[3.0:5.0]
set output 'plots/ft.jpeg' 
set title 'Likelihood Surface of Forward Evolve Time' 
plot '<paste parameter_data/ft_vals.txt likelihood_data/ft_data.txt' using 1:2  with points 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
set xlabel 'Backward Evolve Time'
set ylabel 'likelihood'
set yrange [-200:0]
set xrange[0.8:1.2]
set output 'plots/bt.jpeg' 
set title 'Likelihood Surface of Backward Evolve Time' 
plot '<paste parameter_data/bt_vals.txt likelihood_data/bt_data.txt' using 1:2  with points 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
set xlabel 'Radius'
set ylabel 'likelihood'
set yrange [-200:0]
set xrange[0.1:0.3]
set output 'plots/rad.jpeg' 
set title 'Likelihood Surface of Radius' 
plot '<paste parameter_data/rad_vals.txt likelihood_data/rad_data.txt' using 1:2  with points 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
set xlabel 'Radius Ratio'
set ylabel 'likelihood'
set yrange [-200:0]
set xrange[0.1:0.35]
set output 'plots/rr.jpeg' 
set title 'Likelihood Surface of Radius Ratio' 
plot '<paste parameter_data/rr_vals.txt likelihood_data/rr_data.txt' using 1:2  with points 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
set xlabel 'Mass'
set ylabel 'likelihood'
set yrange [-200:0]
set xrange[2.0:120.0]
set output 'plots/mass.jpeg' 
set title 'Likelihood Surface of Mass' 
plot '<paste parameter_data/mass_vals.txt likelihood_data/mass_data.txt' using 1:2  with points 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
set xlabel 'Mass Ratio'
set ylabel 'likelihood'
set yrange [-200:0]
set xrange[0.1:0.35]
set output 'plots/mr.jpeg' 
set title 'Likelihood Surface of Mass Ratio' 
plot '<paste parameter_data/mr_vals.txt likelihood_data/mr_data.txt' using 1:2  with points 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
