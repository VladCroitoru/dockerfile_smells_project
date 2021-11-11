# {Linux Wine XPRA} based dockerfile (test version)
#
# 1. Copy tnfFOnlineServer.cfg to FOnlineServer.cfg and configure it.
# 2. Copy default.web_server_config.toml to web_server_config.toml and configure it.
#
# TODO: 
# - Replace base image with alpine instead of ubuntu.
FROM ubuntu
VOLUME /tmp/.X11-unix
RUN apt update \
 && DEBIAN_FRONTEND=noninteractive apt install -y wget gnupg xvfb x11-xserver-utils python3-pip \
 #&& pulseaudio lxterminal \
 && pip3 install pyinotify \
 && echo "deb [arch=amd64] https://xpra.org/ focal main" > /etc/apt/sources.list.d/xpra.list \
 && wget -q https://xpra.org/gpg.asc -O- | apt-key add - \
 && apt update \
 && DEBIAN_FRONTEND=noninteractive apt install -y xpra \
 && mkdir -p /run/user/0/xpra
RUN apt-get install xterm
RUN apt-get install software-properties-common -y
RUN dpkg --add-architecture i386
RUN wget -nc https://dl.winehq.org/wine-builds/winehq.key
RUN gpg -o /etc/apt/trusted.gpg.d/winehq.key.gpg --dearmor winehq.key
RUN add-apt-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ focal main'
RUN apt update
RUN apt install --install-recommends winehq-stable winetricks -y
RUN wget -P /mono http://dl.winehq.org/wine/wine-mono/4.9.4/wine-mono-4.9.4.msi

RUN echo "..."
RUN wineboot -u && msiexec /i /mono/wine-mono-4.9.4.msi
RUN rm -rf /mono/wine-mono-4.9.4.msi
RUN rm /winehq.key

RUN apt-get install locales
RUN locale-gen ru_RU.CP1251
ENV LANG ru_RU.CP1251
ENV LANGUAGE ru_RU.ru
ENV LC_ALL ru_RU.CP1251
#RUN adduser app
#RUN usermod -aG sudo app
#USER app

RUN apt-get install git -y
RUN git clone https://github.com/fonline-roleplay/rust_workspace.git /var/rust_workspace

#RUN echo -n "yourenvvariablehere" > /home/password.txt

RUN mkdir /app

ENV XDG_RUNTIME_DIR /var/app
CMD ["cp", "/var/app/web_server_config.toml", "/var/rust_workspace/web_server/config.toml"]
#ENTRYPOINT ["xpra", "start", ":80", "--bind-tcp=0.0.0.0:4020,auth=file:filename=/home/password.txt", "--mdns=no", "--html=on", "--clipboard=on", "--webcam=no", "--no-daemon", "--start-child=wine /app/FOnlineServer.exe -start", "--exit-with-children"] 
ENTRYPOINT ["xpra", "start", ":80", "--bind-tcp=0.0.0.0:4020", "--mdns=no", "--html=on", "--clipboard=on", "--webcam=no", "--no-daemon", "--start-child=wine /var/app/FOnlineServer.exe -start", "--start-child=xterm", "--exit-with-children"] 