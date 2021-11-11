# This Dockerfile is used to build an headless Ubuntu with OBS

FROM ubuntu:16.04

MAINTAINER potsky <potsky@me.com>

LABEL io.k8s.description="Headless Container with MonaServer2, FFMPEG, VNC, XFCE Window Manager, Chromium, GIT" \
      io.k8s.display-name="Headless Container based on Ubuntu 16"

### Env
ENV DEBIAN_FRONTEND=noninteractive
ENV DISPLAY=:1
ENV HOME=/root
ENV HTTP_PORT=80
ENV HTTPS_PORT=443
ENV INST_SCRIPTS=$HOME/install
ENV NO_VNC_HOME=$HOME/noVNC
ENV NO_VNC_PORT=6901
ENV RTMP_PORT=1935
ENV SSH_PORT=22
ENV STARTUPDIR=$HOME/startup
ENV TERM=xterm
ENV VERSION_GIT=2.14.1
ENV VNC_COL_DEPTH=24
ENV VNC_PORT=5901
ENV VNC_PW=vncpwd
ENV VNC_RESOLUTION=1280x1024
ENV VNC_VIEW_ONLY=false

### Add install scripts
ADD ./install/ $INST_SCRIPTS/
RUN find $INST_SCRIPTS -name '*.sh' -exec chmod a+x {} +

### Install common tools
RUN $INST_SCRIPTS/tools.sh
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

### Install softwares
RUN $INST_SCRIPTS/tigervnc.sh
RUN $INST_SCRIPTS/no_vnc.sh
RUN $INST_SCRIPTS/chrome.sh
RUN $INST_SCRIPTS/xfce_ui.sh
RUN $INST_SCRIPTS/system.sh
RUN $INST_SCRIPTS/ffmpeg.sh
RUN $INST_SCRIPTS/mona.sh

### Docker config
EXPOSE $SSH_PORT $VNC_PORT $NO_VNC_PORT $HTTP_PORT $HTTPS_PORT $RTMP_PORT
WORKDIR $HOME/MonaServer2/MonaTiny/www

### Copy assets
ADD ./runtime/home/ $HOME/
ADD ./runtime/system/vimrc /root/.vimrc
ADD ./runtime/system/motd /etc/motd
ADD ./runtime/system/zsh_history /root/.zsh_history

### Startup
ADD ./runtime/scripts $STARTUPDIR
RUN find $STARTUPDIR -name '*.sh' -exec chmod a+x {} +

CMD [ "/root/startup/run.sh" ]
