![](https://i.imgur.com/oQSlTX0.png)

# About

This is a little script that allows you to change your desktop wallpaper to a different video depending on the time of day and the weather.
It requires python, and Lively Wallpaper and the command utility.

When you install python, make sure you add it to PATH.

You will also need an API key from OpenWeather.
Full instructions are included.

Premade videos of a scene in Skyrim can be downloaded [here](https://drive.google.com/drive/folders/1xF0Iz6BP_f_UGSkXBAFqbQ5xHxR2msvC?usp=share_link).

## Known Issues

If your wallpaper isn't updating, open the current_wallpaper.txt file, delete everything in it, save it, and run the task. This happens when the script runs before lively opens, and it thinks it already has the correct wallpaper set so it doesn't change it. Delay the task in task scheduler to prevent this.

---

Thanks to rocksdanister and the [Lively](https://github.com/rocksdanister/lively) contributors for making Lively and the command utility that my script relies on.



<a href="https://www.buymeacoffee.com/BiomeBits" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/guidelines/download-assets-sm-3.svg" alt="Buy Me A Coffee" height="41" width="174"></a>
