The mental model
Whenever something on the network doesn't work, I mentally walk the packet from client to server.

Windows application
      │
      ▼
Windows TCP/IP
      │
      ▼
VMware NAT/Bridge
      │
      ▼
Linux NIC (ens33)
      │
      ▼
Linux firewall
      │
      ▼
Application (Java/Python)

At each stage I ask:

Did the packet get this far?

Once the answer becomes "yes", I stop looking before that point.
----------------------------------------------------------------

Step 1 - Is the application running?
ss -tlnp

Result:
*:8888

----------------------------------------------------------------
Step 2 - Is the host reachable?
ping ok?

----------------------------------------------------------------
Step 3 - Can TCP connect?
Test-NetConnection

Result:

TcpTestSucceeded : False

So ICMP works, TCP doesn't.

That almost always means

firewall
service
ACL
routing
----------------------------------------------------------------
Step 4 - Does the packet arrive?
tcpdump

This is the magic tool.

You saw
SYN ->

That single line told us
Windows ✓
VMware ✓
Virtual NIC ✓
Driver ✓
Routing ✓
----------------------------------------------------------------
----------------------------------------------------------------
----------------------------------------------------------------
----------------------------------------------------------------
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
----------------------------------------------------------------