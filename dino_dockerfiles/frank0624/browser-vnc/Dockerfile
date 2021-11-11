
FROM ubuntu:14.04

RUN apt-get -y update
RUN apt-get -y install --no-install-recommends lubuntu-core
RUN apt-get -y install \
	lxterminal \
	vnc4server \
	fonts-droid \
	vim \
	git \
	wget \
	firefox \
	libxss1 \
	libappindicator1 \
	libindicator7 \
	fonts-liberation \
	libcurl3 \
	xdg-utils \
	libnspr4 \
	libnss3 \
	gconf-service \
	gconf-service-backend \
	gconf2-common \
	libgconf-2-4 \
	python
	
RUN apt-get clean

# Install google chrome
ADD https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb /src/google-chrome-stable_current_amd64.deb
RUN dpkg -i '/src/google-chrome-stable_current_amd64.deb' && \
	rm -rf /src/*.deb
ADD google-chrome.desktop /usr/share/applications/google-chrome.desktop
RUN mkdir ~/chrome-data

# set vncserver password
RUN /bin/echo -e "123456\n123456\n\n" | vncpasswd

# install noVNC
RUN cd /opt && git clone git://github.com/kanaka/noVNC

# vncserver port
EXPOSE 5901

# novnc port
EXPOSE 6080

ADD start.sh /opt/start.sh
RUN chmod +x /opt/start.sh

ENTRYPOINT [ "/opt/start.sh" ]
