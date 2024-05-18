import os
import sys
import winreg as reg
import ctypes


def add_registry_entries(dir):
	try:
		key_path = r"Directory\shell\MoveUp"
		key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
		reg.SetValueEx(key, "", 0, reg.REG_SZ, "Move Up")
		reg.SetValueEx(key, "Icon", 0, reg.REG_SZ, os.path.join(dir, "icon.ico"))
		reg.CloseKey(key)
		
		command_key_path = key_path + r"\command"
		command_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, command_key_path)
		
		cmd = f'"{sys.executable}" "{os.path.join(dir, "move_up.py")}" "%1"'
		reg.SetValueEx(command_key, "", 0, reg.REG_SZ, cmd)
		reg.CloseKey(command_key)
	
		# If you have to run it as admin it won't show in the terminal so alert boxing instead	
		MessageBox = ctypes.windll.user32.MessageBoxW
		MessageBox(None, "Registry keys successfully added!", "Move Up", 0)
		
		# Deleting setup file / .reg
		os.remove("move_up.reg")
		os.remove(__file__)
	except Exception as e:
		print(f"Error: {e}")


# Need admin to change regedit
if ctypes.windll.shell32.IsUserAnAdmin():
	dir = os.getcwd()
	add_registry_entries(dir)	
else:
	path = os.path.abspath(sys.argv[0])
	ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, path, None, 1)
