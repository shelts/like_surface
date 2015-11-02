reset
set terminal jpeg
set key off
set output "plots/fortime.jpeg"
set title 'Forward Evolve time'
set ylabel 'Likelihood'
set xlabel 'parameter value'
set xrange[0:6]
set yrange[-999:1]
plot "<paste parameter_data/fortime_vals.txt likelihood_data/fortime_data.txt"   using 1:2 title 'seed 125868' with lines



reset
set terminal jpeg
set key off 
set output "plots/backtime.jpeg"
set title 'Backward Evolve time'
set ylabel 'Likelihood'
set xlabel 'parameter value'
set xrange[0:2]
set yrange[-999:1]
plot "<paste parameter_data/backtime_vals.txt likelihood_data/backtime_data.txt"   using 1:2 title 'seed 125868' with lines



reset
set terminal jpeg
set key off
set output "plots/rad.jpeg"
set title 'Radius'
set ylabel 'Likelihood'
set xlabel 'parameter value'
set xrange[0:0.75]
set yrange[-999:1]
plot "<paste parameter_data/rad_vals.txt likelihood_data/rad_data.txt"   using 1:2 title 'seed 125868' with lines

reset
set terminal jpeg
set key off
set output "plots/radratio.jpeg"
set title 'Radius Ratio'
set ylabel 'Likelihood'
set xlabel 'parameter value'
# set xrange[0:0.75]
# set yrange[-999:1]
plot "<paste parameter_data/radratio_vals.txt likelihood_data/radratio_data.txt"   using 1:2 title 'seed 125868' with lines


reset
set terminal jpeg
set key off
set output "plots/mass.jpeg"
set title 'Mass'
set ylabel 'Likelihood'
set xlabel 'parameter value'
set xrange[0:120]
set yrange[-999:1]
plot "<paste parameter_data/mass_vals.txt likelihood_data/mass_data.txt"   using 1:2 title 'seed 125868' with lines


reset
set terminal jpeg
set key off
set output "plots/massratio.jpeg"
set title 'Mass Ratio'
set ylabel 'Likelihood'
set xlabel 'parameter value'
set xrange[0:0.75]
set yrange[-200:1]
plot "<paste parameter_data/massratio_vals.txt likelihood_data/massratio_data.txt"   using 1:2 title 'seed 125868' with lines