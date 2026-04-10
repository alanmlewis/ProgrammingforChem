@echo off
echo Deleting symlinks
rm Y1_Kinetics/plot.py
rm Y2_Heat_Capacities/plot.py
echo Configuring Git for Symlinks...
git config core.symlinks true
echo Re-linking files...
git checkout .
echo Done! If links are still text files, ensure Developer Mode is ON, or run "sudo .\setup.bat".
pause
