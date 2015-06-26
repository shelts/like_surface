reset
set terminal wxt persist
set key off
# set output "./mass_massratio_precise.jpeg"
set title 'Likelihood Surface of Mass vs Mass Ratio'
set xlabel 'Mass value'
set ylabel 'Mass Ratio'
set zlabel 'Likelihood'
# set xrange[0:6]
# set yrange[0:.5]
# set contour surface
# set dgrid3d 30,30
# set hidden3d
splot "./data/data_precise.dat"   using 1:2:3 with points pointtype 7 pointsize .2

