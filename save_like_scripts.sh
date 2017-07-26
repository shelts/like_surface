#!/bin/bash   


# cd like_surface
git status

echo 'adding:'
ls *.py *.sh
ls */*.py */*.sh

git add *.py *.sh
git add */*.py */*.sh

git add *.gnuplot 
git add */*.gnuplot 

git commit -m "update"


git push