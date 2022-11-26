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
    key_value = "Software\Microsoft\Windows\CurrentVersion\Run\SimpleMacros"
    open = reg.OpenKey(reg.HKEY_CURRENT_USER, key_value, 0, reg.KEY_ALL_ACCESS)
    reg.DeleteKey(open)
    reg.CloseKey(open)