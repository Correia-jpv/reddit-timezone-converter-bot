@ECHO OFF

Powershell.exe -executionpolicy bypass -File ./deps/windows/windows.ps1
if errorlevel 1 pause & exit 

if "%1"=="" (
  pipenv run python ./src/init.py
)

echo exiting...
pause