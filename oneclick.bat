@echo off
::set Method=MTCNN
set Method=pyface
::合并检测数据
echo %Method%
if exist %Method% ( cd %Method%/
mkdir "../evaluation/%Method%/"
copy *.txt "../evaluation/%Method%/Dets.txt"
cd .. )
::生成真值数据
if exist FDDB-folds (
cd FDDB-folds/
copy FDDB-fold-??.txt "../evaluation/imList.txt"
copy FDDB-fold-??-ellipseList.txt "../evaluation/ellipseList.txt"
cd ..
)
::进行评估和绘图
if exist evaluation (
cd evaluation/
echo evaluating
"D:/Perl/bin/perl" runEvaluate-Windows.pl %Method% 
echo ploting %Method%
"D:/Program Files/gnuplot/bin/gnuplot" "%Method%ContROC.p"
"D:/Program Files/gnuplot/bin/gnuplot" "%Method%DiscROC.p"
move %Method%DiscROC.png %Method%/%Method%DiscROC.png
move %Method%ContROC.png %Method%/%Method%ContROC.png 
cd ..
)

pause