FROM ubuntu:17.10

# inspired by webanck/docker-wine-steam

# preparations
ENV DEBIAN_FRONTEND noninteractive

	# activate i386 arch for Wine and install stuff we need
RUN dpkg --add-architecture i386 && \
	apt-get update && \
	apt-get -qy upgrade && apt-get -o Dpkg::Options::="--force-overwrite" -qy install wget software-properties-common apt-transport-https openssh-server xauth cabextract winbind squashfs-tools pulseaudio sudo x11-apps xfce4 cups joe xfce4-terminal xrdp xorgxrdp xvfb socat x11vnc firefox locales && \
	
	# install latest Wine
	wget -qO- https://dl.winehq.org/wine-builds/Release.key | apt-key add - && \
	apt-add-repository https://dl.winehq.org/wine-builds/ubuntu/ && \
	apt-get update && apt-get -o Dpkg::Options::="--force-overwrite" -qy install --install-recommends winehq-devel && \

	# make sshd work and enable X11 forwarding
	mkdir /var/run/sshd && \
	sed -i 's/session    required     pam_loginuid.so/#session    required     pam_loginuid.so/g' /etc/pam.d/sshd && \
	echo "X11Forwarding yes\n" >> /etc/ssh/ssh_config && \
	echo "ForwardX11Trusted yes\n" >> /etc/ssh/ssh_config && \

	# create our user for Wine
	useradd -m -s /bin/bash -G sudo,tty,video,dialout wineuser && echo 'wineuser:remotex11' | chpasswd && \

	# winetricks
	wget https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks -O /tmp/winetricks && \
	chmod +x /tmp/winetricks && \
	cd /tmp && \
	su -l wineuser -c 'WINEDEBUG=-all WINEPREFIX=/home/wineuser/.wine WINEARCH=win32 winecfg' && \
	su -l wineuser -c 'WINEDEBUG=-all WINEPREFIX=/home/wineuser/.wine WINEARCH=win32 xvfb-run -a /tmp/winetricks -q corefonts dotnet462 vcrun2013' && \
	
	# replace wine-devel for wine-staging
	apt-get -qy purge winehq-devel && \
	apt-get -o Dpkg::Options::="--force-overwrite" -qy install --install-recommends winehq-staging && \
	
	# install Gecko
	wget http://dl.winehq.org/wine/wine-gecko/2.47/wine_gecko-2.47-x86_64.msi -O /tmp/wine_gecko-x86_64.msi && \
	su -l wineuser -c 'WINEDEBUG=-all WINEPREFIX=/home/wineuser/.wine WINEARCH=win32 xvfb-run -a wine start /wait msiexec /i /tmp/wine_gecko-x86_64.msi /qn' && \
	
	# cleaning up
	apt-get autoremove -y --purge software-properties-common && \
	apt-get autoremove -y --purge && \
	apt-get clean -y && \
	rm -rf /home/wine/.cache && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

USER root
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
