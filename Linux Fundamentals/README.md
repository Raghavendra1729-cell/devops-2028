# Linux Fundamentals

**Name:** Raghavendra
**Enrollment number:** 24BCS10250

## Soft links and hard links

A hard link is another filename for the same inode. Removing the original name does not remove the data while another hard link still exists. A symbolic link stores a target path, so it becomes broken when that target disappears. Soft links can cross filesystems and point to directories; ordinary hard links cannot.

```bash
echo "Hello links" > original.txt
ln original.txt hard.txt
ln -s original.txt soft.txt
ls -li original.txt hard.txt soft.txt
rm original.txt
cat hard.txt
cat soft.txt
rm hard.txt soft.txt
```

The original and hard link had the same inode. After deleting the original, the hard link still returned the text and the soft link failed. These are the main points I would explain in an interview. The [Linux practice output](outputs/linux-practice.txt) records creation, inspection and deletion.

## adduser and useradd

`useradd` is a lower-level command. Flags such as `-m` and `-s` control the home directory and login shell. On Ubuntu, `adduser` is usually easier for creating a normal user because it provides the usual home directory and interactive setup.

I created a test user in a disposable Ubuntu 24.04 container. The exercise used a disabled password because the test user did not need to log in.

```bash
adduser --disabled-password --gecos "Course practice" course-test
id course-test
ls -ld /home/course-test
deluser course-test
```

The [Ubuntu output](ubuntu-user-output.txt) shows the new UID, group and home directory. The user was removed, and deleting the disposable container removed its home directory.

## journalctl

`journalctl` reads logs collected by systemd-journald. I used the local Minikube Linux node, which runs systemd, for this exercise.

```bash
sudo journalctl -b -n 5 --no-pager
sudo journalctl -u kubelet -n 5 --no-pager
sudo journalctl -u kubelet --since "10 minutes ago" --no-pager
sudo journalctl -u kubelet -f
```

`-b` selects this boot, `-u` selects a service, `--since` limits the time, and `-f` follows new entries until Ctrl+C. The captured boot and kubelet logs are at the end of the [practice output](outputs/linux-practice.txt). Some kubelet errors came from the intentionally broken Pod exercises.

## Command cheat sheet

| Commands | What I used them for |
|---|---|
| `pwd`, `ls -la`, `cd` | Check paths and move between directories |
| `mkdir`, `rmdir` | Create and remove directories |
| `touch`, `cp`, `mv`, `rm` | Create, copy, rename and remove files |
| `cat`, `head`, `tail`, `grep`, `find` | Read files and find text or filenames |
| `chmod`, `chown` | Change permissions and ownership |
| `whoami`, `id`, `date` | Inspect the current identity and date |
| `df -h`, `du -sh`, `free -h` | Check filesystem, directory and memory usage |
| `ps`, `top`, `uptime` | Inspect processes and resource usage |
| `kill PID` | Stop a selected process; I used a temporary sleep process |
| `ip addr`, `ip route`, `ss -tuln` | Inspect interfaces, routes and listening sockets |
| `lsblk`, `findmnt` | Inspect devices and mounted filesystems |
| `mount`, `umount` | Attach or detach a filesystem when needed |
| `journalctl` | Read system and service logs |

For permissions, `640` means owner read/write, group read, and no access for others. I worked in a temporary directory and removed the exercise files afterwards. Network practice is in the [networking notes](../Networking/README.md).

[Additional permissions and mount practice](outputs/permissions-and-mount.txt) includes touch, ownership, executable permissions, directory size, time-filtered service logs and a temporary tmpfs mount.

![Ubuntu test user creation](images/ubuntu-user.jpg)
