FROM debian:stable

LABEL author=ChrisBinnie
LABEL version=120517

RUN apt update && \ 
    apt install -y dnsutils netcat telnet traceroute libcap-ng-utils curl wget tcpdump ssldump \
    rsync procps fping lsof nmap htop strace net-tools vim nano iftop && \
    apt-get clean

CMD bash
