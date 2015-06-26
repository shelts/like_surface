#! /usr/bin/python
import os
#from subprocess import call

counter=0.1
name=str(counter)
while counter < 2:
  os.system(" ~/research/nbody_test_10k/bin/milkyway_nbody \
        -f ~/research/lua/EMD_10k_isotropic2_1_48.lua \
        -h ~/research/like_surface/histogram_in_seed125896_10kEMD_4_1_p5_p2_30_p2.hist \
        -o ~/research/nbody_test_10k/bin/output.out \
        -z ~/research/like_surface/histogram_out_seed125896_1kEMD_4_1_p5_p2_30_sweep.hist \
        -n 6 -x -e  125896 -i 4 "+ name +" 0.5 0.2 30 0.2 \
        2>>~/research/like_surface/backtime_sweep/backevotime_output.txt")
  counter=counter+0.05
  name=str(counter)
 
counter=0.25
name=str(counter)
while counter < 6.0:
  os.system(" ~/research/nbody_test_10k/bin/milkyway_nbody \
        -f ~/research/lua/EMD_10k_isotropic2_1_48.lua \
        -h ~/research/like_surface/histogram_in_seed125896_10kEMD_4_1_p5_p2_30_p2.hist \
        -o ~/research/nbody_test_10k/bin/output.out \
        -z ~/research/like_surface/histogram_out_seed125896_1kEMD_4_1_p5_p2_30_sweep.hist \
        -n 6 -x -e  125896 -i " + name +" 1 0.5 0.2 30 0.2 \
        2>>~/research/like_surface/fortime_sweep/forwardevotime_output.txt")
  counter=counter+0.25
  name=str(counter)




print 'new seed time'

#new seed
counter=0.1
name=str(counter)
while counter < 2:
  os.system(" ~/research/nbody_test_10k/bin/milkyway_nbody \
        -f ~/research/lua/EMD_10k_isotropic2_1_48.lua \
        -h ~/research/like_surface/histogram_in_seed125896_10kEMD_4_1_p5_p2_30_p2.hist \
        -o ~/research/nbody_test_10k/bin/output.out \
        -z ~/research/like_surface/histogram_out_seed491349_1kEMD_4_1_p5_p2_30_sweep.hist \
        -n 6 -x -e  491349 -i 4 "+ name +" 0.5 0.2 30 0.2 \
        2>>~/research/like_surface/seed_491349/backtime_sweep/backevotime_output.txt")
  counter=counter+0.05
  name=str(counter)
 
counter=0.25
name=str(counter)
while counter < 6.0:
  os.system(" ~/research/nbody_test_10k/bin/milkyway_nbody \
        -f ~/research/lua/EMD_10k_isotropic2_1_48.lua \
        -h ~/research/like_surface/histogram_in_seed125896_10kEMD_4_1_p5_p2_30_p2.hist \
        -o ~/research/nbody_test_10k/bin/output.out \
        -z ~/research/like_surface/histogram_out_seed491349_1kEMD_4_1_p5_p2_30_sweep.hist \
        -n 6 -x -e  491349 -i " + name +" 1 0.5 0.2 30 0.2 \
        2>>~/research/like_surface/seed_491349/fortime_sweep/forwardevotime_output.txt")
  counter=counter+0.25
  name=str(counter)

print 'finished the times'

counter=0.02
name=str(counter)
while counter < 0.75:
  os.system(" ~/research/nbody_test_10k/bin/milkyway_nbody \
        -f ~/research/lua/EMD_10k_isotropic2_1_48.lua \
        -h ~/research/like_surface/histogram_in_seed125896_10kEMD_4_1_p5_p2_30_p2.hist \
        -o ~/research/nbody_test_10k/bin/output.out \
        -z ~/research/like_surface/histogram_out_seed491349_1kEMD_4_1_p5_p2_30_sweep.hist \
        -n 6 -x -e  491349 -i 4 1 "+ name +" 0.2 30 0.2 \
        2>>~/research/like_surface/seed_491349/rad_sweep/rad_output.txt")
  counter=counter+0.02
  name=str(counter)
 
counter=0.06
name=str(counter)
while counter < 0.75:
  os.system(" ~/research/nbody_test_10k/bin/milkyway_nbody \
        -f ~/research/lua/EMD_10k_isotropic2_1_48.lua \
        -h ~/research/like_surface/histogram_in_seed125896_10kEMD_4_1_p5_p2_30_p2.hist \
        -o ~/research/nbody_test_10k/bin/output.out \
        -z ~/research/like_surface/histogram_out_seed491349_1kEMD_4_1_p5_p2_30_sweep.hist \
        -n 6 -x -e  491349 -i 4 1 0.5 " + name +" 30 0.2 \
        2>>~/research/like_surface/seed_491349/radratio_sweep/radratio_output.txt")
  counter=counter+0.02
  name=str(counter)


print 'finished radii'


counter=1
name=str(counter)
while counter < 191:
  os.system(" ~/research/nbody_test_10k/bin/milkyway_nbody \
        -f ~/research/lua/EMD_10k_isotropic2_1_48.lua \
        -h ~/research/like_surface/histogram_in_seed125896_10kEMD_4_1_p5_p2_30_p2.hist \
        -o ~/research/nbody_test_10k/bin/output.out \
        -z ~/research/like_surface/histogram_out_seed491349_1kEMD_4_1_p5_p2_30_sweep.hist \
        -n 6 -x -e  491349 -i 4 1 0.5 0.2 "+ name +" 0.2 \
        2>>~/research/like_surface/seed_491349/mass_sweep/mass_output.txt")
  counter=counter+10
  name=str(counter)

counter=0.1
name=str(counter)
while counter < 0.75:
  os.system(" ~/research/nbody_test_10k/bin/milkyway_nbody \
        -f ~/research/lua/EMD_10k_isotropic2_1_48.lua \
        -h ~/research/like_surface/histogram_in_seed125896_10kEMD_4_1_p5_p2_30_p2.hist \
        -o ~/research/nbody_test_10k/bin/output.out \
        -z ~/research/like_surface/histogram_out_seed491349_1kEMD_4_1_p5_p2_30_sweep.hist \
        -n 6 -x -e  491349 -i 4 1 0.5 0.2 30 " + name +"  \
        2>>~/research/like_surface/seed_491349/massratio_sweep/massratio_output.txt")
  counter=counter+0.02
  name=str(counter)


print 'finished masses'
