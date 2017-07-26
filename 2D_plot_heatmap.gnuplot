reset
reset
set terminal png enhanced size 1300,700
set key off
set output '2D_like_surface/plots_2d_rand_iter/rr_mr.png' 

# set multiplot layout 1,2  spacing 0.01,0
set multiplot layout 1,2 margins 0.1,0.9,.1,.95 spacing 0,0 


set dgrid3d 50,50, 10
set pm3d at t map
set pm3d interpolate 50,50
set palette model CMY rgbformulae 7,5,15
set cbrange[-50:0]
set zrange[-50:0]
set xrange[0.1:0.4]
set yrange[0.1:0.7]
set xlabel 'Scale Radius Ratio (Stellar/Dark)'
set ylabel 'Mass Ratio (Baryonic/Total)'
set cblabel 'Likelihood' 
set tics font ", 20"
set xlabel font "Times-Roman, 20"
set ylabel font "Times-Roman, 20" offset -1,0
set cblabel font "Times-Roman, 20" offset 3,0
set xtics autofreq .1, .05, .35
unset colorbox
splot './2D_like_surface/likelihood_data_2d_rand_iter/rr_mr_data_vals.txt' using 1:2:3 with image

unset ytics
set colorbox
unset ylabel
set xtics autofreq .1, .05, .4
set dgrid3d 5,5 5
plot  './2D_like_surface/likelihood_data_2d_rand_iter/cons_den.txt' using 1:2:3 with points ps 0.1 pt 5 lc 'grey', './2D_like_surface/likelihood_data_2d_rand_iter/best_fit.txt' using 2:3:1 with points ps 2 pt 11  palette, './2D_like_surface/likelihood_data_2d_rand_iter/correct_answer.txt' using 2:3:1 with points ps 5 pt 3  palette
# lc rgb 'black'


# palette model CMY rgbformulae 7,5,15