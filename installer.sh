#!/bin/bash

# By SkylineIsBack

if [ "$(id -u)" -ne 0 ]; then
        echo 'This installer script must be run as root.'
        exit 1
fi

echo "Starting installation"
echo""
sudo apt install python-tk
sudo apt install python3-tk
sudo mv WebAppManager.py /usr/bin/
sudo mv WAM /usr/bin/
sudo chmod +x /usr/bin/WebAppManager.py
sudo chmod +x /usr/bin/WAM/WAM-create.py
sudo chmod +x /usr/bin/WAM/WAM-delete.py
sudo mv WAM.png /usr/share/icons/
sudo mv WAM.desktop /usr/share/applications/
sudo chmod +x /usr/share/applications/WAM.desktop
if [[ -f /usr/bin/firefox ]];
then
    echo ""
    echo "Installing Firefox WebApp profile"
    user="$(cat /etc/passwd | grep '/home' | cut -d':' -f1)"
    cd /home/$user/.mozilla/firefox/
    mkdir webapp-profile && cd webapp-profile
    echo 'user_pref("toolkit.legacyUserProfileCustomizations.stylesheets", true);' >> "user.js"
    mkdir chrome && cd chrome
    echo '#nav-bar, #TabsToolbar, #tabbrowser-tabs {
	visibility: collapse !important;
}' >> "userChrome.css"
    echo ""
    echo "Successfully created Firefox WebApp profile"
fi
echo ""
echo "Successfully installed"