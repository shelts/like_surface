reset
set terminal jpeg
set key off
set output "plots/mass_precise.jpeg"
set title 'Mass'
set ylabel 'Likelihood'
set xlabel 'parameter value'
set xrange[0:191]
set yrange[-999:1]
plot "<paste data/mass_vals_precise.txt data/mass_precise_data.txt"   using 1:2 with lines
