reset
set terminal jpeg
set key off
set output "plots/fortime.jpeg"
set title 'Forward Evolve time'
set ylabel 'Likelihood'
set xlabel 'parameter value'
set xrange[0:6]
set yrange[-999:1]
plot "<paste data/fortime_vals.txt data/fortime_data.txt"   using 1:2 title 'seed 125868' with lines



reset
set terminal jpeg
set key off 
set output "plots/backtime.jpeg"
set title 'Backward Evolve time'
set ylabel 'Likelihood'
set xlabel 'parameter value'
set xrange[0:2]
set yrange[-999:1]
plot "<paste data/backtime_vals.txt data/backtime_data.txt"   using 1:2 title 'seed 125868' with lines



reset
set terminal jpeg
set key off
set output "plots/rad.jpeg"
set title 'Radius'
set ylabel 'Likelihood'
set xlabel 'parameter value'
set xrange[0:0.75]
set yrange[-999:1]
plot "<paste data/rad_vals.txt data/rad_data.txt"   using 1:2 title 'seed 125868' with lines

reset
set terminal jpeg
set key off
set output "plots/radratio.jpeg"
set title 'Radius Ratio'
set ylabel 'Likelihood'
set xlabel 'parameter value'
set xrange[0:0.75]
set yrange[-999:1]
plot "<paste data/radratio_vals.txt data/radratio_data.txt"   using 1:2 title 'seed 125868' with lines


reset
set terminal jpeg
set key off
set output "plots/mass.jpeg"
set title 'Mass'
set ylabel 'Likelihood'
set xlabel 'parameter value'
set xrange[0:191]
set yrange[-999:1]
plot "<paste data/mass_vals.txt data/mass_data.txt"   using 1:2 title 'seed 125868' with lines


reset
set terminal jpeg
set key off
set output "plots/massratio.jpeg"
set title 'Mass Ratio'
set ylabel 'Likelihood'
set xlabel 'parameter value'
set xrange[0:0.75]
set yrange[-200:1]
plot "<paste data/massratio_vals.txt data/massratio_data.txt"   using 1:2 title 'seed 125868' with lines