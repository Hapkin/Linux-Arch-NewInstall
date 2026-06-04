
# folder location
/home/joop/.config/systemd/user


# emoji-daemon.service
[Unit]
Description=Emoji Daemon

[Service]
### new location for the script...
ExecStart=/usr/bin/python /home/joop/.local/bin/emoji-daemon.py
Restart=always

[Install]
WantedBy=default.target