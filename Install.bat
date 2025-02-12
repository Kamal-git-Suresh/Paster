:start
echo off	
cls

call "python_install.bat"
call "pack_install.bat"
copy paster.exe "C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
echo "install complete"
cmd /k "paster.exe"
pause
exit

