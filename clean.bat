@echo off
rd labels /s /q
rd images /s /q
rd Annotations /s /q
rd "ImageSets/Main" /s /q
mkdir images
mkdir labels
mkdir Annotations
pause