mkdir lmc
mkdir tel

cd lmc
scp -r $lmc:~/research/like_surface/hists/parameter_sweeps_rand_iter ./
cd ..


cd tel
scp -r $teletraan:~/research/like_surface/hists/parameter_sweeps_rand_iter ./

cd ..
mkdir parameter_sweeps_rand_iter

./combine_multi_server_sweeps.py