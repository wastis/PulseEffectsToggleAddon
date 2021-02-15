PulseEffects Toggle addon


Purpose: toggle between PulseEffects presets

============
Installation
============

1 Requires PulseEffects from Flatpak installed

	sudo flatpak install com.github.wwmm.pulseeffects -y

2. Requires PulseEffects presets defined within PulseEffects

3. Requires PulseEffects to run as a service in backround

	vim ~/.config/autostart/PulseEffect.desktop

[Desktop Entry]
Encoding=UTF-8
Version=0.9.4
Type=Application
Name=PulseEffect
Comment=
Exec=/usr/bin/flatpak run --branch=stable --arch=x86_64 --command=pulseeffects com.github.wwmm.pulseeffects --gapplication-service
OnlyShowIn=XFCE;
RunHook=0
StartupNotify=false
Terminal=false
Hidden=false


4. Launch Kodi >> Add-ons >> Get More >> .. >> Install from zip file

See https://forum.kodi.tv/showthread.php?tid=360514

Feel free to ask any questions on the Kodi Forums.



