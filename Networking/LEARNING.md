# What I Learned from the Networking Resources

## How a request travels

When I open a website, DHCP first gives my device an IP address, subnet mask, gateway, and DNS server. DNS converts the website name into an IP address. Switches forward frames inside the local network using MAC addresses, while routers forward packets between networks using IP addresses. TCP or UDP then carries data to the correct port.

## OSI model

- Layer 1 moves signals through cable, fibre, or Wi-Fi.
- Layer 2 uses frames and MAC addresses; switches work here.
- Layer 3 uses IP addresses and routing; routers work here.
- Layer 4 uses TCP/UDP and port numbers.
- Layers 5-7 handle sessions, data format, encryption, and application protocols such as DNS and HTTPS.

## IP addressing and subnetting

An IPv4 address has a network part and a host part. CIDR notation such as `/24` tells how many bits belong to the network. The first address is normally the network address and the last is the broadcast address. Subnetting divides one network into smaller networks and reduces the number of usable hosts in each subnet.

## DHCP, monitoring, and troubleshooting

DHCP follows DORA: Discover, Offer, Request, and Acknowledgement. IPFIX and NetFlow record traffic-flow details for monitoring, while NTP keeps device clocks synchronized so timestamps can be compared correctly. For troubleshooting, I should check connectivity, route, ports, DNS, and finally the application instead of guessing.

## Resources

- [Network Troubleshooting](https://github.com/Nency-Ravaliya/Network-Troubleshooting)
- [OSI Network Devices](https://github.com/Nency-Ravaliya/OSI-Network-devices)
- [Networking](https://github.com/Nency-Ravaliya/Networking)
- [Subnetting](https://github.com/Nency-Ravaliya/Subnetting)
- [IP Questions](https://github.com/Nency-Ravaliya/IP-quest)
- [IPFIX, NetFlow, and NTP](https://github.com/Nency-Ravaliya/IPFIX-NETFLOW-NTP)
- [How DHCP Works](https://github.com/Nency-Ravaliya/How-DHCP-Works)
