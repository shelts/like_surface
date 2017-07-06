#!/bin/bash   


# cd like_surface
git status

echo 'adding:'
ls *.py *.sh
ls */*.py */*.sh

git add *.py *.sh
git add */*.py */*.sh

git commit -m "update"


git push