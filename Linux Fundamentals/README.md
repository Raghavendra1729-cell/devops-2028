# Linux Fundamentals

## Notes

These are the 25 Linux commands I found most useful from the class notes. I kept this list focused on files and paths, system information, processes, networking, and basic volume handling.

> The terminal blocks below are sample Ubuntu outputs. The username, AWS-style private IP, process IDs, disk names, and usage values will be different on another machine.

## Files and paths

### 1. `pwd` - show the current path

```console
ubuntu@ip-172-31-24-18:~$ pwd
/home/ubuntu
```

### 2. `ls -la` - list all files with details

```console
ubuntu@ip-172-31-24-18:~$ ls -la
drwxr-x--- 5 ubuntu ubuntu 4096 Aug 31 12:18 .
drwxr-xr-x 3 root   root   4096 Aug 31 11:40 ..
-rw-r--r-- 1 ubuntu ubuntu  220 Aug 31 11:40 .bash_logout
-rw-r--r-- 1 ubuntu ubuntu   18 Aug 31 12:18 notes.txt
```

### 3. `cd` - change the current directory

```console
ubuntu@ip-172-31-24-18:~$ cd /var/log
ubuntu@ip-172-31-24-18:/var/log$
```

### 4. `mkdir` - create a directory

```console
ubuntu@ip-172-31-24-18:~$ mkdir linux-lab
ubuntu@ip-172-31-24-18:~$ ls
linux-lab
```

### 5. `touch` - create an empty file

```console
ubuntu@ip-172-31-24-18:~/linux-lab$ touch notes.txt
ubuntu@ip-172-31-24-18:~/linux-lab$ ls -l
-rw-r--r-- 1 ubuntu ubuntu 0 Aug 31 12:24 notes.txt
```

### 6. `cp` - copy a file or directory

```console
ubuntu@ip-172-31-24-18:~/linux-lab$ cp notes.txt notes-backup.txt
ubuntu@ip-172-31-24-18:~/linux-lab$ ls
notes-backup.txt  notes.txt
```

Use `cp -r source-directory destination-directory` when copying a directory.

### 7. `mv` - move or rename a file

```console
ubuntu@ip-172-31-24-18:~/linux-lab$ mv notes-backup.txt old-notes.txt
ubuntu@ip-172-31-24-18:~/linux-lab$ ls
notes.txt  old-notes.txt
```

### 8. `rm` - remove a file

```console
ubuntu@ip-172-31-24-18:~/linux-lab$ rm -i old-notes.txt
rm: remove regular empty file 'old-notes.txt'? y
```

I use `rm -i` while practising because it asks before deleting. Deleted files do not normally go to a recycle bin.

### 9. `cat` - display a text file

```console
ubuntu@ip-172-31-24-18:~/linux-lab$ cat notes.txt
Linux commands become easier with practice.
```

## System and processes

### 10. `whoami` - show the current user

```console
ubuntu@ip-172-31-24-18:~$ whoami
ubuntu
```

### 11. `hostname` - show the machine name

```console
ubuntu@ip-172-31-24-18:~$ hostname
ip-172-31-24-18
```

### 12. `uname -a` - show kernel and system information

```console
ubuntu@ip-172-31-24-18:~$ uname -a
Linux ip-172-31-24-18 6.8.0-1024-aws #26-Ubuntu SMP x86_64 GNU/Linux
```

### 13. `date` - show the current date and time

```console
ubuntu@ip-172-31-24-18:~$ date
Mon Aug 31 12:30:18 UTC 2026
```

### 14. `uptime` - show uptime and load average

```console
ubuntu@ip-172-31-24-18:~$ uptime
12:31:02 up 2 hours, 1 user, load average: 0.03, 0.05, 0.01
```

### 15. `ps aux` - take a snapshot of running processes

```console
ubuntu@ip-172-31-24-18:~$ ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.5  21932 12840 ?        Ss   10:29   0:02 /sbin/init
ubuntu    2481  0.0  0.2  17820  6120 pts/0    Ss   12:28   0:00 -bash
```

### 16. `top` - monitor processes and resources live

```console
ubuntu@ip-172-31-24-18:~$ top
top - 12:32:11 up 2:03, 1 user, load average: 0.00, 0.03, 0.01
Tasks: 103 total, 1 running, 102 sleeping, 0 stopped, 0 zombie
%Cpu(s): 0.3 us, 0.2 sy, 99.5 id
MiB Mem :  957.4 total,  488.1 free,  173.7 used,  295.6 buff/cache
```

Press `q` to leave `top`.

### 17. `kill` - send a signal to a process

```console
ubuntu@ip-172-31-24-18:~$ kill 2481
ubuntu@ip-172-31-24-18:~$
```

The PID must belong to the process I intend to stop. A normal `kill PID` is safer than immediately forcing termination with signal 9.

## Networking

### 18. `ip addr` - show network interfaces and addresses

```console
ubuntu@ip-172-31-24-18:~$ ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 state UNKNOWN
    inet 127.0.0.1/8 scope host lo
2: ens5: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9001 state UP
    inet 172.31.24.18/20 scope global dynamic ens5
```

### 19. `ip route` - show the routing table

```console
ubuntu@ip-172-31-24-18:~$ ip route
default via 172.31.16.1 dev ens5 proto dhcp src 172.31.24.18
172.31.16.0/20 dev ens5 proto kernel scope link src 172.31.24.18
```

### 20. `ping` - test reachability and latency

```console
ubuntu@ip-172-31-24-18:~$ ping -c 3 8.8.8.8
64 bytes from 8.8.8.8: icmp_seq=1 ttl=113 time=1.82 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=113 time=1.77 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=113 time=1.79 ms
--- 8.8.8.8 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss
```

### 21. `ss -tulnp` - inspect listening sockets

```console
ubuntu@ip-172-31-24-18:~$ sudo ss -tulnp
Netid State  Local Address:Port  Peer Address:Port Process
tcp   LISTEN 0.0.0.0:22          0.0.0.0:*         users:(("sshd",pid=922,fd=3))
```

The flags show TCP, UDP, listening sockets, numeric addresses, and process information.

### 22. `curl -I` - fetch only HTTP response headers

```console
ubuntu@ip-172-31-24-18:~$ curl -I https://example.com
HTTP/2 200
content-type: text/html
content-length: 1256
```

This is useful for checking whether a web server responds without downloading the full page.

## Basic volumes

### 23. `lsblk` - list block devices

```console
ubuntu@ip-172-31-24-18:~$ lsblk
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
nvme0n1     259:0    0    8G  0 disk
└─nvme0n1p1 259:1    0    8G  0 part /
nvme1n1     259:2    0   10G  0 disk
```

### 24. `mount` - show or attach mounted filesystems

```console
ubuntu@ip-172-31-24-18:~$ sudo mount /dev/nvme1n1 /mnt/data
ubuntu@ip-172-31-24-18:~$ mount
/dev/nvme0n1p1 on / type ext4 (rw,relatime)
/dev/nvme1n1 on /mnt/data type ext4 (rw,relatime)
```

The target directory and filesystem must already be prepared before mounting a real device.

### 25. `umount` - detach a mounted filesystem

```console
ubuntu@ip-172-31-24-18:~$ sudo umount /mnt/data
ubuntu@ip-172-31-24-18:~$
```

I first make sure no program is using files inside the mount point.

## What I learned

- Linux paths start from `/`, while `~` represents my home directory.
- File commands become safer when I check the current path before copying, moving, or deleting anything.
- `ps` gives a process snapshot, while `top` keeps updating the information.
- `ip addr`, `ip route`, `ping`, and `ss` answer different networking questions.
- A block device is not the same as a mounted filesystem. `lsblk` shows devices, while `mount` and `umount` attach or detach filesystems.

## Short homework notes

### Soft link and hard link

- A **hard link** is another name for the same file. Both names share the same inode, so the data remains available if one name is deleted. It normally cannot cross filesystems or link directories.
- A **soft link**, or symbolic link, stores the path of another file. It can cross filesystems and link directories, but it becomes broken if its target is removed.
- `ln original.txt hard-link.txt` creates a hard link, while `ln -s original.txt soft-link.txt` creates a soft link. `ls -li` can be used to compare inode numbers.

### `adduser` and `useradd`

- `useradd` is the lower-level, distribution-independent command. Its behaviour depends on options and system defaults, so administrators often specify the home directory and shell explicitly.
- On Debian and Ubuntu, `adduser` is normally preferred for creating a regular user manually. It is a friendlier wrapper that creates the home directory, copies default files, and asks for the required details.
- Therefore, there is no single preferred command for every Linux distribution: use `adduser` for interactive Debian/Ubuntu administration and `useradd` when a portable or scripted low-level command is required.

### `journalctl`

`journalctl` reads logs collected by `systemd-journald`. It is useful for checking boot problems, service failures, and recent system events. Useful forms include `journalctl -b` for the current boot, `journalctl -u nginx` for one service, and `journalctl -f` to follow new entries.

### Cheat-sheet revision

The command cheat sheet is a quick revision tool, but I should understand what a command changes before running it. Commands involving deletion, processes, users, networking, or mounted filesystems should be checked carefully instead of copied blindly.

## Class material

These notes were prepared after reviewing the PDFs shared in the class repository:

- [Session 2 - Linux](https://github.com/Nency-Ravaliya/devops-heros/tree/main/session2-linux)
- Linux basic commands
- Advanced Linux commands
- Linux networking cheat sheet
