# Linux Fundamentals

**Name:** Raghavendra

**Enrollment number:** 24BCS10250

I kept the commands grouped by the part of Linux I was practising.

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

The `-i` flag prompts for confirmation before deleting files. Deleted files do not go to a recycle bin.

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

## More Linux notes

### Understanding Soft and Hard Links

A hard link is another name for the same inode. The data is still available through the hard link if the original name is removed. A symbolic link stores a path instead, so it breaks if that target is removed. Symbolic links can also point to directories or cross filesystems.

Commands I tried:

```console
# 1. Create a file
ubuntu@ip-172-31-24-18:~$ echo "Hello World" > target.txt

# 2. Create links
ubuntu@ip-172-31-24-18:~$ ln target.txt hard-link.txt
ubuntu@ip-172-31-24-18:~$ ln -s target.txt soft-link.txt

# 3. Verify inodes (notice target.txt and hard-link.txt share the same inode number)
ubuntu@ip-172-31-24-18:~$ ls -li

# 4. Delete the original and see what happens (soft link breaks, hard link survives)
ubuntu@ip-172-31-24-18:~$ rm target.txt
ubuntu@ip-172-31-24-18:~$ cat hard-link.txt  # Succeeds
ubuntu@ip-172-31-24-18:~$ cat soft-link.txt  # Fails: No such file or directory
```

### User Management: `adduser` vs `useradd`

On Ubuntu, `useradd` is the lower-level command and needs flags for things such as a home directory or shell. `adduser` is interactive and creates the usual home-directory setup by default.

```console
# Create a test user interactively on Ubuntu
ubuntu@ip-172-31-24-18:~$ sudo adduser testuser

# Verify the user was created successfully
ubuntu@ip-172-31-24-18:~$ id testuser
uid=1001(testuser) gid=1001(testuser) groups=1001(testuser)
```

### Viewing Logs with `journalctl`

I used `journalctl` to read logs collected by `systemd-journald`.

```console
# View all logs from the current boot
ubuntu@ip-172-31-24-18:~$ journalctl -b

# View logs for a specific service (e.g., SSH)
ubuntu@ip-172-31-24-18:~$ journalctl -u ssh

# Follow/tail logs live for a service (like 'tail -f')
ubuntu@ip-172-31-24-18:~$ journalctl -u ssh -f

# View logs from a specific time frame
ubuntu@ip-172-31-24-18:~$ journalctl --since "1 hour ago"
```
