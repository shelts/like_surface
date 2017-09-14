#!/bin/bash   


rm 2D_like_surface/parameter_sweeps_2d_rand_iter/rr_mr_corrected.txt
rm 2D_like_surface/parameter_sweeps_2d_rand_iter/rr_mr_vals_corrected.txt

./recalc_like_from_hists.py
./one_like_script.py
gnuplot 2D_plot_heatmap.gnuplot 
