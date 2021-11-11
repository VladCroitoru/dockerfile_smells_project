FROM ubuntu:bionic
ENV DEBIAN_FRONTEND noninteractive 

# update the system, install dependencies
RUN apt-get update -y && \
    apt-get upgrade -y && \
	apt-get install -y --no-install-recommends \
		x11vnc \
		net-tools \
		ca-certificates \
		curl \
		python \
		python-numpy \
		python-xdg \
		xvfb \
		xdg-utils \
		openbox \
		menu && \
	apt autoclean && \
    apt autoremove -y && \
    rm -rf /var/lib/apt/lists/* && \
	echo fs.inotify.max_user_watches=100000 | \
	tee -a /etc/sysctl.conf; sysctl -p

# copy startup script
ADD startup.sh /startup.sh
RUN chmod 0755 /startup.sh

# create the user
RUN useradd --create-home --shell /bin/bash --user-group --groups adm,sudo tresorit
USER tresorit
WORKDIR /home/tresorit

# install noVNC and tresorit, create some folders
RUN curl -L https://github.com/novnc/noVNC/archive/master.tar.gz | tar xzv && \
	mv noVNC-master noVNC && \
	rm -r ./noVNC/tests && \
	ln -s ./vnc.html ./noVNC/index.html && \
	cd noVNC/utils && \
	curl -L https://github.com/novnc/websockify/archive/master.tar.gz | tar xzv && \
	mv websockify-master websockify && \
	rm -r ./websockify/tests ./websockify/Windows && \
	cd /home/tresorit && \
	curl -LO https://installerstorage.blob.core.windows.net/public/install/tresorit_installer.run && \
    chmod +x ./tresorit_installer.run && \
	echo "N " | ./tresorit_installer.run --update-v2 . && \
	rm ./tresorit_installer.run && \
	mkdir -p /home/tresorit/Profiles \
			 /home/tresorit/external \
			 /home/tresorit/.x11vnc

VOLUME /home/tresorit/Profiles /home/tresorit/external
USER root
EXPOSE 6080
CMD ["/startup.sh"]
