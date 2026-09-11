Set WshShell = CreateObject("WScript.Shell")

WshShell.CurrentDirectory = "C:\Users\PC_User\terminal_search_app"

WshShell.Run "pythonw app2.py", 0, False

WScript.Sleep 2000

WshShell.Run "http://127.0.0.1:5000", 1, False