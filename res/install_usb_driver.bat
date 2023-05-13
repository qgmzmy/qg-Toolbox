@ echo off
%1 %2
ver|find "5.">nul&&goto :Admin
mshta vbscript:createobject("shell.application").shellexecute("%~s0","goto :Admin","","runas",1)(window.close)&goto :eof
:Admin
color 2
echo ==============================
echo       °²×°Google USBÇý¶¯
echo ==============================
pause
cls
powershell Invoke-WebRequest -Uri "https://dl.google.com/android/repository/usb_driver_r13-windows.zip?hl=zh-cn" -OutFile "GoogleUSBDriver.zip"
mkdir C:\tr-tmp
powershell  Expand-Archive -Force -Path GoogleUSBDriver.zip -DestinationPath C:\tr-tmp
pnputil -i -a C:\tr-tmp\usb_driver\*.inf
del /f /s /q C:\tr-tmp
pause