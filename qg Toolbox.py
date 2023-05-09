import os,time
os.system("echo off")
os.system("title qg Toolbox by-qgmzmy")
while True:
    os.system("cd /d res/adb")
    print('''============================
         qg Toolbox
        作者：qgmzmy
============================''')
    print(''' 1.打开cmd命令行
 2.从payload.bin提取img映像
 3.打开adb shell
 4.退出''')
    ipt = input("请输入序号：")
    os.system("cls")
    if ipt == "1":
        os.system("echo on")
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
            time.sleep(1.5)
            os.system("cls")
    elif ipt == "3":
        os.system("adb shell")
        os.system("cls")