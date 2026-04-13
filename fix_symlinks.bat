@echo off
echo Deleting symlinks
rm Y1_Kinetics/plot.py
rm Y1_Kinetics/test.py
rm Y2_Heat_Capacities/plot.py
rm Y2_Heat_Capacities/test.py
echo Configuring Git for Symlinks...
git config core.symlinks true
echo Re-linking files...
git checkout .
echo Done! If links are still text files, please run this script as an administrator.
pause
