reset
set terminal jpeg
set key off
set output "plots/seed491349_fortime.jpeg"
set title 'Forward Evolve time'
set ylabel 'Likelihood'
set xlabel 'parameter value'
set xrange[0:6]
set yrange[-999:1]
plot "<paste data/fortime_vals.txt data/seed491349_fortime_data.txt"   using 1:2 with lines



reset
set terminal jpeg
set key off
set output "plots/seed491349_backtime.jpeg"
set title 'Backward Evolve time'
set ylabel 'Likelihood'
set xlabel 'parameter value'
set xrange[0:1]
set yrange[-999:1]
plot "<paste data/backtime_vals.txt data/seed491349_backtime_data.txt"   using 1:2 with lines



reset
set terminal jpeg
set key off
set output "plots/seed491349_rad.jpeg"
set title 'Radius'
set ylabel 'Likelihood'
set xlabel 'parameter value'
set xrange[0:0.75]
set yrange[-999:1]
plot "<paste data/rad_vals.txt data/seed491349_rad_data.txt"   using 1:2 with lines


reset
set terminal jpeg
set key off
set output "plots/seed491349_radratio.jpeg"
set title 'Radius Ratio'
set ylabel 'Likelihood'
set xlabel 'parameter value'
set xrange[0:0.75]
set yrange[-999:1]
plot "<paste data/radratio_vals.txt data/seed491349_radratio_data.txt"   using 1:2 with lines


reset
set terminal jpeg
set key off
set output "plots/seed491349_mass.jpeg"
set title 'Mass'
set ylabel 'Likelihood'
set xlabel 'parameter value'
set xrange[0:191]
set yrange[-999:1]
plot "<paste data/mass_vals.txt data/seed491349_mass_data.txt"   using 1:2 with lines


reset
set terminal jpeg
set key off
set output "plots/seed491349_massratio.jpeg"
set title 'Mass Ratio'
set ylabel 'Likelihood'
set xlabel 'parameter value'
set xrange[0:0.75]
set yrange[-999:1]
plot "<paste data/massratio_vals.txt data/seed491349_massratio_data.txt"   using 1:2 with lines