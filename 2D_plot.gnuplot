reset
set terminal png enhanced size 2600,1400
set palette defined ( 20 "#101010", 30 "#ff0000", 40 "#00ff00", 50 "#e0e0e0" ) 
set key off
set xlabel 'Scale Radius Ratio (Stellar/Dark)'
set ylabel 'Mass Ratio (Baryonic/Total)' 
set zlabel 'likelihood' 
set cbrange[-50:0]
set zrange[-50:0]
set xrange[0.1:0.4]
set yrange[0.1:0.4]
set output '2D_like_surface/plots_2d_rand_iter/rr_mr_1.png' 
set title 'Likelihood Surface of Scale Radius Ratio (Stellar/Dark) vs Mass Ratio (Baryonic/Total)' 
plot './2D_like_surface/likelihood_data_2d_rand_iter/rr_mr_data_vals.txt' using 1:2:3  with points palette  ps 5 pt 7, './2D_like_surface/likelihood_data_2d_rand_iter/best_fit2.txt' using 2:3 with points ps 5 pt 11 


reset
set terminal wxt persist
set key off
reset
set terminal png enhanced size 1300,700
set key off
set output '2D_like_surface/plots_2d_rand_iter/rr_mr.png' 
set multiplot layout 1,2 margins 0.05,0.9,.1,.99 spacing 0.01,0
set dgrid3d 50,50, 10
set pm3d at t map
set pm3d interpolate 50,50
set palette model CMY rgbformulae 7,5,15
set zlabel 'likelihood' 
set zrange[-50:0]
set xrange[0.1:0.4]
set yrange[0.1:0.4]
set size square
set origin 0,0
splot './2D_like_surface/likelihood_data_2d_rand_iter/rr_mr_data_vals.txt' using 1:2:3 with image
set size square
plot './2D_like_surface/likelihood_data_2d_rand_iter/best_fit.txt' using 2:3:(0.0) with points ps 1 pt 5 lc rgb 'black'
