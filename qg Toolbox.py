import os
os.system("title qg Toolbox by-qgmzmy")
while True:
    os.system("echo off")
    os.system("cls")
    os.system("cd /d res/adb")
    print('''============================
         qg Toolbox
        作者：qgmzmy
============================''')
    print(''' 1.打开cmd命令行
 2.从payload.bin提取img映像
 3.打开adb shell
 4.重启选项
 5.应用管理
 6.退出''')
    ipt = input("请输入序号：")
    os.system("cls")
    if ipt == "1":
        os.system("echo on")
        print("输入'exit'返回主页")
        os.system("cmd /k")
    elif ipt == "2":
        print('请将payload.bin放在payload-dumper-go目录下')
        os.system("pause")
        print('''1.提取所有
2.提取boot
3.提取init_boot
4.返回主页''')
        ipt = input("请输入序号：")
        os.system("cls")
        if ipt == "1":
            os.system("cd /d payload-dumper-go&payload-dumper-go.exe -o .\img .\payload.bin")
        elif ipt == "2":
            os.system("cd /d payload-dumper-go&payload-dumper-go.exe -p boot -o .\img .\payload.bin")
        elif ipt == "3":
            os.system("cd /d payload-dumper-go&payload-dumper-go.exe -p init_boot -o .\img .\payload.bin")
        elif ipt == "4":
            continue
        else:
            print('请正确输入...')
            os.system("pause")
            os.system("cls")
    elif ipt == "3":
        print("输入'exit'返回主页")
        os.system("adb shell")
        os.system("cls")
    elif ipt == "4":
        print('''1.重启到system
2.重启到system（fastboot）
3.重启到recovery
4.重启到bootloader
5.重启到bootloader（fastboot）
6.重启到fastbootd
7.重启到fastbootd（fastboot）
8.重启到sideload（若设备支持）
9。重启到sideload（fastboot）（若设备支持）
10.关机
11.返回主页''')
        ipt = input("请输入序号：")
        if ipt == "1":
            os.system("adb reboot")
            os.system("cls")
        elif ipt == "2":
            os.system("fastboot reboot")
            os.system("cls")
        elif ipt == "3":
            os.system("adb reboot recovery")
            os.system("cls")
        elif ipt == "4":
            os.system("adb reboot bootloader")
            os.system("cls") 
        elif ipt == "5":
            os.system("fastboot reboot bootloader")
            os.system("cls")
        elif ipt == "6":
            os.system("adb reboot fastboot")
            os.system("cls")
        elif ipt == "7":
            os.system("fastboot reboot fastboot")
            os.system("cls")
        elif ipt == "8":
            os.system("adb reboot sideload")
            os.system("cls")
        elif ipt == "9":
            os.system("fastboot reboot sideload")
            os.system("cls")
        elif ipt == "10":
            os.system("adb shell reboot -p")
            os.system("cls")
        elif ipt == "11":
            os.system("cls")
        else:
            print('请正确输入...')
            os.system("pause")
            os.system("cls")
    elif ipt == "5":
        print('''1.安装应用
2.列出所有包名
3.卸载应用
4.返回主页''')
        ipt = input("请输入序号：")
        os.system("cls")
        if ipt == "1":
            apk = input("请拖入apk文件：")
            os.system("adb install "+apk)
            os.system("pause")
        elif ipt == "2":
            os.system("adb shell pm list package")
            os.system("pause")
        elif ipt == "3":
            package = input("请输入要卸载的应用的包名（系统应用可能无效）（查看包名请输入'package'）：")
            if package == "package":
                os.system("adb shell pm list package")
                package = input("请输入要卸载的应用的包名（系统应用可能无效）：")
                os.system("cls")
                os.system("adb uninstall "+package)
                os.system("pause")
            else:
                os.system("adb uninstall "+package)
                os.system("pause")
        elif ipt == "4":
            continue
        else:
            print('请正确输入...')
            os.system("pause")
    elif ipt == "6" or ipt == "exit":
        break
        os.system("taskkill /f /im cmd.exe")
    else:
        print('请正确输入...')
        os.system("pause")