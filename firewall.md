# firewall
uitzoeken welke er gebruikt wordt

firewalld // ufw // iptables  => UI voor nftables?
zien dat er maar 1 actief staat!


## systemctl status
welke service is actief?

[root@MumRa-VM01 joop]# systemctl status nftables
○ nftables.service - Netfilter Tables
     Loaded: loaded (/usr/lib/systemd/system/nftables.service; disabled; preset: disabled)

[root@MumRa-VM01 joop]# systemctl status ufw
● ufw.service - CLI Netfilter Manager
     Loaded: loaded (/usr/lib/systemd/system/ufw.service; enabled; preset: disabled)
     Active: active (exited) since Sat 2026-07-04 13:14:08 CEST; 44min ago

[root@MumRa-VM01 joop]# systemctl status firewalld
● firewalld.service - firewalld - dynamic firewall daemon
     Loaded: loaded (/usr/lib/systemd/system/firewalld.service; enabled; preset: disabled)
     Active: active (running) since Sat 2026-07-04 13:14:09 CEST; 43min ago

[root@MumRa-VM01 joop]# systemctl status iptables
○ iptables.service - IPv4 Packet Filtering Framework
     Loaded: loaded (/usr/lib/systemd/system/iptables.service; disabled; preset: disabled)
     Active: inactive (dead)



## debugging
ping tussen client en server? ok

### tcpdump ? 
pacman -S tcpdump
sudo tcpdump -i ens33 port 8000


zie je traffic als je van een andere pc stuurt? -> ja
zie je traffic op je server logs (als je de service manueel start)? -> nee

firewall issue

---------------------------------------------
# The tools I'd recommend mastering

If you become comfortable with just these, you'll solve 90% of Linux networking problems:

Purpose	Command
Interfaces	ip addr
Routes	ip route
Listening ports	ss -tlnp
Firewall services	systemctl status firewalld ufw nftables
Firewall rules	nft list ruleset
Packet capture	tcpdump
Logs	journalctl -xe
Connectivity	curl, nc, Test-NetConnection

Notice there's nothing distro-specific there.