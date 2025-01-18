XCOPY "main\seznam.xls" .
XCOPY "main\config.xls" .
XCOPY "main\templates" ".\templates\" /E

ECHO START /B main\main.exe>launch.bat