import os
import zipfile
import time
numberText = "请输入序号："
os.system("title root 专区")
while True:
    os.system("cls")
    productName = os.popen("adb shell getprop ro.product.name")
    productName = productName.readlines()
    productName = productName[0]
    print(''' 1.线刷 root
 2.退出''')
    number = input(numberText)
    os.system("cls")
    if number == "1":
        print("正在安装 Magisk...")
        os.system('cmd /c "adb install Magisk.apk" >nul 2>&1')
        print("安装完成")
        os.system("pause")
        print('''请选择品牌：
 1.小米/红米
 2.Google''')
        number = input(numberText)
        os.system("cls")
        if number == "1":
            print('''使用本软件 root 前请前往 https://unlock.update.miui.com 下载 miflash_unlock 解锁您的设备。
本软件的作者不会对使用后产生的任何后果负任何责任。''')
            os.system("pause")
            os.system("start https://xiaomirom.com/series/"+productName)
            os.system("cls")
            print("请在弹出的浏览器窗口中下载您当前版本的“Recovery 卡刷包”")
            xiaomiOtaRom = input("请拖入下载的文件：")
            print("正在创建目录...")
            if os.path.isdir("C:\\QG-Toolbox\\temp") == False:
                os.mkdir("C:\\QG-Toolbox\\temp")
            if os.path.isdir("C:\\QG-Toolbox\\boot") == False:
                os.mkdir("C:\\QG-Toolbox\\boot")
            print("创建完成")
            print("正在解压文件...")
            with zipfile.ZipFile(xiaomiOtaRom, 'r') as zip_ref:
                zip_ref.extractall("C:\\QG-Toolbox\\temp")
            print("解压完成")
            
            if os.path.exists("C:\\QG-Toolbox\\temp\\boot.img"):
                print("正在复制文件...")
                os.system("copy C:\\QG-Toolbox\\temp\\boot.img C:\\QG-Toolbox\\boot")
                print("复制完成")
            else:
                print("正在提取映像...")
                os.system('cmd /c "payload-dumper-go.exe -p boot -o C:\\QG-Toolbox\\boot C:\\QG-Toolbox\\temp\\payload.bin" >nul 2>&1')
                if os.path.exists("C:\\QG-Toolbox\\boot\\boot.img") == False:
                    os.system('cmd /c "payload-dumper-go.exe -p init_boot -o C:\\QG-Toolbox\\boot C:\\QG-Toolbox\\temp\\payload.bin" >nul 2>&1')
                    print("提取完成")
                    print("正在修补映像...")
                    
            os.system("pause")
        elif number == "2":
            print("正在重启到 sideload...")
            os.system("adb reboot sideload")
            time.sleep(30)
            print("重启完成")
            print("正在重命名文件...")
            os.rename("Magisk.apk", "Magisk.zip")
            print("重命名完成")
            print("正在推送 Magisk...")
            os.system("adb sideload Magisk.zip")
            time.sleep(5)
            print("推送完成")
            print("正在重启...")
            os.system("adb reboot")
            print("重启完成")
            print("正在恢复文件...")
            os.rename("Magisk.zip", "Magisk.apk")
            print("恢复完成")
            os.system("pause")
            os.system("taskkill /f /im cmd.exe")
    elif number == "2":
        os.system("taskkill /f /im cmd.exe")
        break
    else:
        print("请正确输入")
        os.system("pause")