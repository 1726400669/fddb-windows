@echo off
cd MTCNN/
copy *.txt "../evaluation/MTCNN/Dets.txt"
cd ..

cd FDDB-folds/
copy FDDB-fold-??.txt "../evaluation/MTCNN/imList.txt"
copy FDDB-fold-??-ellipseList.txt "../evaluation/MTCNN/ellipseList.txt"
cd ..

cd evaluation/

"D:/Perl/bin/perl" runEvaluate.pl

plot.bat
cd ..

pause