import xbmcaddon
import xbmcgui
import os, subprocess

 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')


def run(cmd):
	ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	output = ps.communicate()[0].decode('utf8').split('\n')
	return output
	

result = run("/usr/bin/flatpak run com.github.wwmm.pulseeffects -p")

if(result[0].find("com.github.wwmm.pulseeffects") != -1): 

	xbmcgui.Dialog().textviewer("PulseEffects", "Error with PulseEffects, please refer Kodi log.", False) 
	xbmc.log('\n'.join(result) , xbmc.LOGERROR) 
	
	
else:

	profile_list = result[0].split(':')[1].strip().split(',')[:-1]
	
	if(len(profile_list)<1):
	
		xbmcgui.Dialog().textviewer("PulseEffects", "No profile defined. Please define profile in PulseEffects.", False) 
	else:

		dialog = xbmcgui.Dialog()
		ret = dialog.contextmenu(profile_list)
		
		
		result = run("/usr/bin/flatpak run com.github.wwmm.pulseeffects -l "+profile_list[ret])
