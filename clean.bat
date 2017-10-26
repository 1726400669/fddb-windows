@echo off
rd evaluation\x64 /s /q
del evaluation\*.ilk /s /q
del evaluation\*.pdb /s /q
rd labels /s /q
rd images /s /q
mkdir images
mkdir labels
pause