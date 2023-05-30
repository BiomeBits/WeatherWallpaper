Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "X:\filepath\WeatherWallpaper\Task_Scheduler_File.bat" & Chr(34), 0
Set WshShell = Nothing