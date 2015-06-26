#!/bin/bash          
# 	rm -r nbody
# 	mkdir nbody
	cd ~/Desktop/MW-research/like_surface/nbody
	cmake -DCMAKE_BUILD_TYPE=Release -DNBODY_GL=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON   ~/Desktop/MW-research/milkywayathome_client/
	make -j 
# 	-fopenmp
	cd ~/Desktop/MW-research/like_surface/nbody/bin
	
# 	valgrind --tool=callgrind
	
#         time  ./milkyway_nbody \
        -f ~/Desktop/MW-research/lua/EMD_10k_isotropic2_1_48.lua \
        -h ~/Desktop/MW-research/like_surface/histogram_in_seed125896_10kEMD_4_1_p5_p2_30_p2.hist \
        -o output.out \
        -z ~/Desktop/MW-research/like_surface/massratio/histogram_i_seed125896_10kEMD_4_1_p5_p2_30_p2.hist \
        -n 6 -x -e  125896 -i 4 1 .5 0.2 30 0.2 \
        2>>~/Desktop/MW-research/like_surface/out.txt
	
# 	cd ~/Desktop/MW-research/nbody_test/bin
# 	callgrind_annotate --inclusive=yes --auto=yes callgrind.out.*125896
# 654879
# 	EMD_50k_isotropic2_1_48.lua 125896
 
