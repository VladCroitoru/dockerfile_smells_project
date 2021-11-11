# This Dockerfile is used to build an headles vnc image based on Centos

FROM centos:7

ENV REFRESHED_AT 2018-03-31

LABEL maintainer "nancheald@gmail.com"

## Connection ports for controlling the UI:
# VNC port:5901
ENV DISPLAY=:1 \
    VNC_PORT=5901 \
    BURP_PORT=6901
EXPOSE $VNC_PORT $BURP_PORT

### Envrionment config
ENV HOME=/headless \
    TERM=xterm \
    STARTUPDIR=/dockerstartup \
    INST_SCRIPTS=/headless/install \
    VNC_COL_DEPTH=24 \
    VNC_RESOLUTION=1280x800 \
    VNC_PW=vncpassword \
    VNC_VIEW_ONLY=false
WORKDIR $HOME

### Add all install scripts for further steps
ADD ./src/common/install/ $INST_SCRIPTS/
ADD ./src/centos/install/ $INST_SCRIPTS/
RUN find $INST_SCRIPTS -name '*.sh' -exec chmod a+x {} +

### Install some common tools
RUN $INST_SCRIPTS/tools.sh
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

### Install xvnc-server
RUN $INST_SCRIPTS/tigervnc.sh


### Install xfce UI
RUN $INST_SCRIPTS/xfce_ui.sh
ADD ./src/common/xfce/ $HOME/

### Install burpsuite pro
RUN $INST_SCRIPTS/burpsuite_pro.sh

### configure startup
RUN $INST_SCRIPTS/libnss_wrapper.sh
ADD ./src/common/scripts $STARTUPDIR
RUN $INST_SCRIPTS/set_user_permission.sh $STARTUPDIR $HOME

# USER 1984

ENTRYPOINT ["/dockerstartup/vnc_startup.sh"]
CMD ["--tail-log"]
