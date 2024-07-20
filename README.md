# macchanger
application that can  change mac addres
in windows
in above code you just need to change ssid name of the wifi which is nothing but name of the wifi in place of MIT.Test and path to the text file in which  mac addres or list of mac address is present 
the mac address shoud be a plane string without (:) and if you want to try list of mac then each mac should be on new line
you can get mac address of the devices connnected to the network with the help of this https://github.com/systematicat/hack-captive-portals.git tool.This tool only works on linux sou can download wsl(windows subsystem for linux)

place where mac address of the windows is stored

we need to create a string file first in registry editor
the path is 
 Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4d36e972-e325-11ce-bfc1-08002be10318}\0003
create a new string file by left click then new and string and name the file as NetworkAddress

run the application as administrator