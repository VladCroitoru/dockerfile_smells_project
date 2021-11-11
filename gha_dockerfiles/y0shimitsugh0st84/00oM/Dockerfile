
FROM ubuntu:20.04
RUN apt-get update

ENV DISPLAY=:1 \
    VNC_PORT=5901 \
    NO_VNC_PORT=6901 \
    SSH_PORT=22 \
    SUPER_VISOR__PORT=9001 \
    DEBIAN_FRONTEND=noninteractive
###########################################################################
ENV HOME=/headless \
    TERM=xterm \
    STARTUPDIR=/dockerstartup \
    INST_SCRIPTS=/headless/install \
    ADD_SCRIPTS=/root/install_add \
    NO_VNC_HOME=/usr/share/novnc \
    DEBIAN_FRONTEND=noninteractive \
    VNC_COL_DEPTH=24 \
    VNC_RESOLUTION=1360x768 \
    VNC_PW=vncpassword \
    VNC_VIEW_ONLY=false
### Envrionment config

RUN whoami

###########################################################################
################################## ADD FILES ##################################
ADD ./bidoon/ $ADD_SCRIPTS/
ADD ./src/ $INST_SCRIPTS/
ADD ./addon/ $INST_SCRIPTS/
RUN find $INST_SCRIPTS -name '*.sh' -exec chmod a+x {} +
################## Envrionment config ##########################################
WORKDIR $HOME
RUN $INST_SCRIPTS/package.sh
RUN $INST_SCRIPTS/package_2.sh
ADD ./etc/ /etc/
#######################  SSH ###########################################
RUN mkdir -p ~/.ssh
RUN rm /etc/ssh/sshd_config
RUN cp $INST_SCRIPTS/sshd_config /etc/ssh/
###########################################################################

RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G sudo -u 1000 test 

RUN  echo 'test:test' | chpasswd

RUN service ssh start

############################ ADD ROOT PASSWORD ###########################
RUN ssh-keygen -q -t rsa -N '' -f /id_rsa

RUN echo "root:1" | /usr/sbin/chpasswd


#########################################################################




RUN echo -e \
"<!DOCTYPE html>\n" \
"<html>\n" \
"    <head>\n" \
"        <title>noVNC</title>\n" \
"        <meta charset=\"utf-8\"/>\n" \
"    </head>\n" \
"    <body>\n" \
"        <p><a href=\"vnc_lite.html\">noVNC Lite Client</a></p>\n" \
"        <p><a href=\"vnc.html\">noVNC Full Client</a></p>\n" \
"    </body>\n" \
"</html>" \
> "${NO_VNC_HOME}"/index.html
#################################################################################
COPY ./src/xfce-startup "${STARTUPDIR}"/
COPY ./xfce/src/home/config /root/.config/
COPY ./xfce/src/home/Desktop /root/Desktop/
COPY ./xfce/src/home/readme*.md "${HOME}"/
RUN chmod 755 -R "${STARTUPDIR}" \
    && "${STARTUPDIR}"/set_user_permissions.sh "${STARTUPDIR}" "${HOME}"
RUN /headless/install/tun_setup.sh
#####################################
EXPOSE $VNC_PORT $NO_VNC_PORT $SSH_PORT $SUPER_VISOR__PORT








RUN addgroup headless
RUN useradd -m -s /bin/bash -g root headless
RUN echo "headless:1" | /usr/sbin/chpasswd
RUN echo "headless    ALL=(ALL) ALL" >> /etc/sudoers
RUN echo "export PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '" >> /root/.bashrc

#
#USER root
#USER 0
#CMD ["/usr/sbin/sshd","-D"]
#ENTRYPOINT [ "/usr/bin/tini", "--", "/dockerstartup/startup.sh" ]
CMD ["/bin/bash", "/dockerstartup/startup.sh"]

#RUN python --version
#RUN python3.9 --version
#COPY requirements.txt .
#RUN --mount=type=cache,mode=0755,target=/root/.cache pip3 install -r requirements.txt 111
#COPY . .

#CMD ["python3", " --version"]
#CMD ["--wait"]

