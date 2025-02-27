@echo off

cd %~dp0  
start code .
timeout /t 2 >nul 

cd venv\Scripts
call activate
cd ../..

start cmd /k "python manage.py runserver"

exit
