![](https://i.imgur.com/oQSlTX0.png)

# About

This is a little script that allows you to change your desktop wallpaper to a different video depending on the time of day and the weather.
It requires Lively Wallpaper, and the command utility.
You will also need an API key from OpenWeather.
Full instructions are included.

Premade videos of a scene in Skyrim can be downloaded [here](https://drive.google.com/drive/folders/1xF0Iz6BP_f_UGSkXBAFqbQ5xHxR2msvC?usp=share_link).

Thanks to rocksdanister and the [Lively](https://github.com/rocksdanister/lively) contributors for making Lively and the command utility that my script relies on.

## Known Issues
Sometimes task scheduler causes a cmd terminal to pop up and minimise full screen games. The solution is to run the batch file via a vbs script like so:

Set WshShell = CreateObject("WScript.Shell")

WshShell.Run chr(34) & "C:\path\to\WeatherWallpaper\Task_Scheduler_File.bat" & Chr(34), 0

Set WshShell = Nothing

Save as .vbs and run this through task scheduler instead of the .bat file directly

Task Scheduler is a pain. Sometimes it just won't run the batch file even when you can run it yourself fine. Try unticking 'run whether use is logged on or not' if you have problems. Also make sure that when you are troubleshooting, you change the current_wallpaper.txt file to something wrong, otherwise the wallpaper won't update.


<a href="https://www.buymeacoffee.com/BiomeBits" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/guidelines/download-assets-sm-3.svg" alt="Buy Me A Coffee" height="41" width="174"></a>
