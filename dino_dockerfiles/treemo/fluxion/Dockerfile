FROM debian


# install
RUN mkdir /home/fluxion
ADD . /home/fluxion
WORKDIR /home/fluxion


# install dependancy (in Installer.sh)
RUN apt update
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys ED444FF07D8D0BF6
RUN echo '# Kali linux repositories' >> /etc/apt/sources.list
RUN echo 'deb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list
RUN echo 'deb http://repo.kali.org/kali kali-bleeding-edge main' >> /etc/apt/sources.list
RUN apt-get update -m
RUN apt install -y xterm software-properties-common aircrack-ng gawk bully curl isc-dhcp-server hostapd wireless-tools lighttpd mdk3 nmap openssl php-cgi pyrit python reaver rfkill unzip zenity binutils psmisc
RUN export DEBIAN_FRONTEND=noninteractive && apt install -y macchanger 


# clean / optimise docker size
RUN apt remove --purge -y git
RUN apt-get autoremove -y
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*
RUN rm -rf /tmp/* /var/tmp/*


# running
ENTRYPOINT ./fluxion && sysctl -w net.ipv4.ip_forward=1

