# Networking Fundamentals

**Name:** Raghavendra

**Enrollment number:** 24BCS10250

I ran a few networking commands to check connectivity, routes, listening ports, DNS, and HTTP.

## 1. Ping

I used `ping` to check whether `google.com` was reachable and to see the response time.

```bash
ping -c 2 google.com
```

Both packets were received with `0.0%` packet loss, so the connection to Google was working.

![Ping replies from google.com](Screenshot%202026-08-31%20at%207.55.39%E2%80%AFPM.png)

![Ping statistics](Screenshot%202026-08-31%20at%207.55.50%E2%80%AFPM.png)

## 2. Traceroute

I used `traceroute` to see the first few routers between my system and Google.

```bash
traceroute -m 3 -w 1 google.com
```

Each line is one network hop. This helps find where a connection might be slow or fail.

![Traceroute output](Screenshot%202026-08-31%20at%207.56.09%E2%80%AFPM.png)

## 3. Listening TCP ports

I used `netstat` to see ports on my computer that were waiting for network connections.

```bash
netstat -an -p tcp | grep LISTEN | head -3
```

The `LISTEN` status means a program is ready to accept a connection on that port.

![Listening TCP ports](Screenshot%202026-08-31%20at%207.56.23%E2%80%AFPM.png)

## 4. DNS lookup

I used `nslookup` to check that DNS could convert `google.com` into IP addresses.

```bash
nslookup google.com | tail -6
```

The result shows the IP addresses returned for `google.com`.

![DNS lookup result](Screenshot%202026-08-31%20at%207.56.32%E2%80%AFPM.png)

## 5. HTTP check

I used `curl` to check whether an HTTPS request to Google was successful.

```bash
curl -sS -I --max-time 10 https://www.google.com | head -5
```

The `HTTP/2 200` response means the website responded successfully.

![HTTP response headers](image.png)
