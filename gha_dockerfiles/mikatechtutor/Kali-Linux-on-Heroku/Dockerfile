FROM kalilinux/kali

LABEL AboutImage "Kali_Linux_Novnc"

LABEL Maintainer "Howtotech"

ARG DEBIAN_FRONTEND=noninteractive

ENV DEBIAN_FRONTEND=noninteractive \
#VNC Server Password
	VNC_PASS="samplepass" \
#VNC Server Title(w/o spaces)
	VNC_TITLE="Kali_Linux" \
#VNC Resolution(720p is preferable)
	VNC_RESOLUTION="1280x720" \
#Local Display Server Port
	DISPLAY=:1 \
#NoVNC Port
	NOVNC_PORT=5900 \
#PORT
        PORT=80 \
#Locale
	LANG=en_US.UTF-8 \
	LANGUAGE=en_US.UTF-8 \
	LC_ALL=C.UTF-8 \
	TZ="Asia/Kolkata" \
#StartXfce4
        UI_COMMAND=/usr/bin/startxfce4

COPY . /app
RUN     echo 'Installing desktop files, this may take a few minutes...' && \
        apt-get update && \
	apt-get install -y \
#Desktop Installation
        xfce4 \
	dbus-x11
	
RUN	echo 'Installing base files, this may take a few minutes...' && \
# Packages Installation, You Can Edit Here (Personal Preferences)
# WARN!!!Don't Remove (sudo,nodejs,npm,x1vnc,xvfb,supervisor,build-essential,software-properties-common,apt-transport-https,pcmanfm) or the kali linux will be unstable
# Thank you For Using My Repo :D
	apt-get install -y \
	tzdata \
	software-properties-common \
	apt-transport-https \
	wget \
	git \
	curl \
	vim \
	zip \
	sudo \
	net-tools \
	iputils-ping \
	firefox-esr \
	build-essential \
	ssh \
	nodejs \
	npm \
	vim-gtk3 \
	nano \
	mousepad \
	pcmanfm \
	terminator \
	screen \
	supervisor \
	x11vnc \
	xvfb \
	gnupg \
	alacarte \
	dirmngr \
	gdebi-core \
	nginx \
	novnc \
	ffmpeg \
	pluma
	
#Install Websockify To Run Novnc
WORKDIR /usr/app
COPY ./ /usr/app
#Websockify
RUN	npm i websockify

WORKDIR /app
#Install Heroku CLI
RUN curl https://cli-assets.heroku.com/install.sh | sh
#Install Kali Tools Top 10
RUN echo 'Installing additional packages...' && \
	export DEBIAN_FRONTEND=noninteractive && \
	apt-get update && \
	apt-get install \
	kali-tools-top10 \
	-y --show-progress && \
#TimeZone
	ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
	echo $TZ > /etc/timezone && \
#NoVNC
	cp /usr/share/novnc/vnc.html /usr/share/novnc/index.html && \
	openssl req -new -newkey rsa:4096 -days 36500 -nodes -x509 -subj "/C=IN/ST=Maharastra/L=Private/O=Dis/CN=www.google.com" -keyout /etc/ssl/novnc.key  -out /etc/ssl/novnc.cert
ENTRYPOINT ["supervisord", "-l", "/app/supervisord.log", "-c"]
EXPOSE 22000/tcp

CMD ["/app/supervisord.conf"]
