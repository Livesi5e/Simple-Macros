import os
import winreg as reg

def enableReg():
    pth = os.getcwd()
    name = 'main.exe'
    adress = os.path.join(pth, name)
    key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
    open = reg.OpenKey(reg.HKEY_CURRENT_USER, key_value, 0, reg.KEY_ALL_ACCESS)
    reg.SetValueEx(open,"SimpleMacros",0,reg.REG_SZ, adress)
    reg.CloseKey(open)

def disableReg():
    with reg.OpenKeyEx(reg.HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Run', access=reg.KEY_ALL_ACCESS) as open:
        reg.SetValueEx(open, 'SimpleMacros',0,reg.REG_SZ,'deactivated')