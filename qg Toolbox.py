import os
os.system("title qg Toolbox by-qgmzmy")
while True:
    print('若不正确使用此软件可以导致数据丢失、无法开机等情况，若已知晓请输入“know”进行确认。开发者不会对使用此软件产生的任何后果负责。')
    ipt = input('''
按回车确定：''')
    os.system("cls")
    if ipt == "know":
        while True:
            os.system("echo off")
            os.system("cls")
            os.system("cd /d adb")
            print('''  ____   _____   _______          _ _               
 / __ \ / ____| |__   __|        | | |              
| |  | | |  __     | | ___   ___ | | |__   _____  __		
| |  | | | |_ |    | |/ _ \ / _ \| | '_ \ / _ \ \/ /
| |__| | |__| |    | | (_) | (_) | | |_) | (_) >  < 
 \___\_\\\_____|    |_|\___/ \___/|_|_.__/ \___/_/\_\  作者：qgmzmy''')
            print(''' 1.打开cmd命令行
 2.从payload.bin提取img映像
 3.打开adb shell
 4.重启选项
 5.应用管理
 6.刷入img映像
 7.安装Google USB驱动
 8.获取设备信息
 9.文件管理
 10.退出''')
            ipt = input("请输入序号：")
            os.system("cls")
            if ipt == "1":
                os.system("echo on")
                print("输入'exit'返回主页")
                os.system("cmd /k")
            elif ipt == "2":
                print('''1.提取所有
2.提取boot
3.提取init_boot
4.返回主页''')
                ipt = input("请输入序号：")
                if ipt == "1" or ipt == "2" or ipt == "3":
                    payload = input("请拖入payload.bin：")
                if ipt == "1":
                    os.system("cd /d payload-dumper-go&payload-dumper-go.exe -o .\img "+payload)
                    print('提取完成，请在payload-dumper-go/img中查看')
                    os.system("pause")
                    os.system("start payload-dumper-go\img")
                    os.system("cls")
                elif ipt == "2":
                    os.system("cd /d payload-dumper-go&payload-dumper-go.exe -p boot -o .\img "+payload)
                    print('提取完成，请在payload-dumper-go/img中查看')
                    os.system("pause")
                    os.system("start payload-dumper-go\img")
                    os.system("cls")
                elif ipt == "3":
                    os.system("cd /d payload-dumper-go&payload-dumper-go.exe -p init_boot -o .\img "+payload)
                    print('提取完成，请在payload-dumper-go/img中查看')
                    os.system("pause")
                    os.system("start payload-dumper-go/img")
                    os.system("cls")
                elif ipt == "4":
                    continue
                else:
                    print('请正确输入...')
                    os.system("pause")
                    os.system("cls")
            elif ipt == "3":
                print("按'ctrl'+'d'返回主页")
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
4.查找apk安装位置
5.返回主页''')
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
                    package = input("请输入应用包名：")
                    os.system("adb shell pm path "+package)
                    os.system("pause")
                elif ipt == "5":
                    continue
                else:
                    print('请正确输入...')
                    os.system("pause")
            elif ipt == "6":
                print('''1.刷入boot
2.刷入init_boot
3.刷入system
4.刷入recovery
5.自定义刷入
6.返回主页''')
                ipt = input("请输入序号：")
                os.system("cls")
                if ipt == "1":
                    print('''1.刷入boot
2.刷入boot_a
3.刷入boot_b
4.返回主页''')
                    ipt = input("请输入序号：")
                    if ipt == "1":
                        img = input("请拖入img映像：")
                        os.system("fastboot flash boot "+img)
                        os.system("pause")
                    elif ipt == "2":
                        img = input("请拖入img映像")
                        os.system("fastboot flash boot_a "+img)
                        os.system("pause")
                    elif ipt == "3":
                        img = input("请拖入img映像")
                        os.system("fastboot flash boot_b "+img)
                        os.system("pause")
                    elif ipt == "4":
                        continue
                    else:
                        print('请正确输入...')
                        os.system("pause")
                elif ipt == "2":
                    print('''1.刷入init_boot
2.刷入init_boot_a
3.刷入init_boot_b
4.返回主页''')
                    ipt = input("请输入序号：")
                    if ipt == "1":
                        img = input("请拖入img映像：")
                        os.system("fastboot flash init_boot "+img)
                        os.system("pause")
                    elif ipt == "2":
                        img = input("请拖入img映像：")
                        os.system("fastboot flash init_boot_a "+img)
                        os.system("pause")
                    elif ipt == "3":
                        img = input("请拖入img映像：")
                        os.system("fastboor flash init_boot_b "+img)
                        os.system("pause")
                    elif ipt == "4":
                        continue
                    else:
                        print('请正确输入...')
                        os.system("pause")
                elif ipt == "3":
                    print('''1.刷入system
2.刷入system_a
3.刷入system_b
4.返回主页''')
                    ipt = input("请输入序号：")
                    if ipt == "1":
                        img = input("请拖入img映像：")
                        os.system("fastboot flash system "+img)
                        os.system("pause")
                    elif ipt == "2":
                        img = input("请拖入img映像：")
                        os.system("fastboot flash system_a "+img)
                        os.system("pause")
                    elif ipt == "3":
                        img = input("请拖入img映像：")
                        os.system("fastboor flash system_b "+img)
                        os.system("pause")
                    elif ipt == "4":
                        continue
                    else:
                        print('请正确输入...')
                        os.system("pause")
                elif ipt == "2":
                    print('''1.刷入recovery
2.刷入recovery_a
3.刷入recovery_b
4.临时启动
5.返回主页''')
                    ipt = input("请输入序号：")
                    if ipt == "1":
                        img = input("请拖入img映像：")
                        os.system("fastboot flash recovery "+img)
                        os.system("pause")
                    elif ipt == "2":
                        img = input("请拖入img映像：")
                        os.system("fastboot flash recovery_a "+img)
                        os.system("pause")
                    elif ipt == "3":
                        img = input("请拖入img映像：")
                        os.system("fastboot flash recovery_b "+img)
                        os.system("pause")
                    elif ipt == "4":
                        img = input("请拖入img映像：")
                        os.system("fastboot boot "+img)
                        os.system("pause")
                    elif ipt == "5":
                        continue
                    else:
                        print('请正确输入...')
                        os.system("pause")
                elif ipt == "5":
                    ipt = input("请输入分区名称：")
                    img = input("请拖入img映像:")
                    os.system("fastboot flash "+ipt+" "+img)
                    os.system("pause")
                elif ipt == "6":
                    continue
                else:
                    print('请正确输入...')
                    os.system("pause")
            elif ipt == "7":
                os.system("start res\install_usb_driver.bat")
            elif ipt == "8":
                os.system("adb devices")
                os.system('echo|set /p="型号：           "')
                os.system("adb -d shell getprop ro.product.model")
                os.system('echo|set /p="厂商：           "')
                os.system("adb -d shell getprop ro.product.brand")
                os.system('echo|set /p="Android 版本：   "')
                os.system("adb shell getprop ro.build.version.release")
                os.system('echo|set /p="系统版本：       "')
                os.system("adb shell getprop ro.system.build.id")
                os.system('echo|set /p="API 版本：       "')
                os.system("adb shell getprop ro.build.version.sdk")
                os.system('echo|set /p="内核版本：       "')
                os.system("adb shell getprop ro.kernel.version")
                os.system('echo|set /p="Bootloader 版本："')
                os.system("adb shell getprop ro.bootloader")
                os.system('echo|set /p="代号：           "')
                os.system("adb shell getprop ro.product.name")
                os.system('echo|set /p="架构：           "')
                os.system("adb shell getprop ro.product.cpu.abi")
                os.system('echo|set /p="ROM 构建者：     "')
                os.system("adb shell getprop ro.build.user")
                os.system('echo|set /p="Android ID：     "')
                os.system("adb shell settings get secure android_id")
                os.system('echo|set /p="A/B Update：     "')
                os.system("adb shell getprop ro.build.ab_update")
                os.system('echo|set /p="SoC：            "')
                os.system("adb shell getprop ro.soc.model")
                os.system("pause")
            elif ipt == "9":
                print('''1.传输
2.移动
3.复制
4.删除
5.新建
6.返回主页''')
                ipt = input("请输入序号：")
                os.system("cls")
                if ipt == "1":
                    os.system("cls")
                    print('''1.传输文件至Android
2.传输文件至PC
3.返回主页''')
                    ipt = input("请输入序号：")
                    os.system("cls")
                    if ipt == "1":
                        src = input("请拖入文件：")
                        os.system("adb push "+src+" /sdcard/Download/")
                        print('传输完成，请在/sdcard/Download中查看')
                        os.system("pause")
                    elif ipt == "2":
                        src = input("请输入文件路径：")
                        os.system("adb pull / "+src+" %userprofile%\Downloads")
                        print('传输完成，请在Downloads中查看')
                        os.system("pause")
                        os.system("start %userprofile%\Downloads")
                    elif ipt == "3":
                        continue
                    else:
                        print('请正确输入...')
                        os.system("pause")
                elif ipt == "2":
                    src = input("请输入文件原路径：")
                    dest = input("请输入移动路径：")
                    os.system("adb shell mv /"+src+" /"+dest)
                    print('移动完成')
                    os.system("pause")
                elif ipt == "3":
                    src = input("请输入文件原路径：")
                    dest = input("请输入复制路径：")
                    os.system("adb shell cp /"+src+" /"+dest)
                    print('复制完成')
                    os.system("pause")
                elif ipt == "4":
                    src = input("请输入需要删除的文件路径：")
                    os.system("adb shell rm -f /"+src)
                    print('删除完成')
                    os.system("pause")
                elif ipt == "5":
                    print('''1.新建文件
2.新建文件夹
3.返回主页''')
                    ipt = input("请输入序号：")
                    os.system("cls")
                    if ipt == "1":
                        file = input("请输入要创建的文件路径：")
                        os.system("adb shell touch /"+file)
                        print('创建完成')
                        os.system("pause")
                    elif ipt == "2":
                        dir = input("请输入要创建的文件夹路径：")
                        os.system("adb shell mkdir /"+dir)
                        print('创建完成')
                        os.system("pause")
                    elif ipt == "3":
                        continue
                    else:
                        print('请正确输入...')
                        os.system("pause")
            elif ipt == "10" or ipt == "exit":
                os.system("taskkill /f /im cmd.exe")
                break
            else:
                print('请正确输入...')
                os.system("pause")
        break
    else:
        os.system("pause")
        os.system("cls")