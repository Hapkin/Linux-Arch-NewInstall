Manual packages installed:
# welcome screen
set local repositories


## Maintenance! older install
sudo pacman -Syy reflector
sudo reflector --country Belgium,Netherlands,Germany --latest 20 --protocol https --sort rate --save /etc/pacman.d/mirrorlist

### updateDB 
sudo pacman -Syyu




### install additional software -> commonly installed 
-> VScode
-> sudo pacman -S gnome-keyring
-> sudo pacman -S libsecret

create service for keyring
-> systemctl --user enable --now gnome-keyring-daemon.service







# now and then do to keep your system clean!
## check for unused packages
sudo pacman -Rns $(pacman -Qdtq)
