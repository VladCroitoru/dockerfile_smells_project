FROM ubuntu:15.04
MAINTAINER Franck Besnard <franck@besnard.mobi>

ENV DEBIAN_FRONTEND noninteractive
ENV HOME /root

RUN apt-get update \
        && apt-get install -y --force-yes --no-install-recommends \
                supervisor openssh-server pwgen sudo vim-tiny net-tools \
                lxde x11vnc xvfb gtk2-engines-murrine ttf-ubuntu-font-family lxterminal \
		firefox owncloud-client filezilla xpdf gimp \
        && apt-get autoclean \
        && apt-get autoremove \
        && rm -rf /var/lib/apt/lists/*

ADD panel /root/
ADD lxde-x-terminal-emulator.desktop /root/

ADD startup.sh /
ADD desktop.conf /etc/supervisor/conf.d/
ADD sshd.conf /etc/supervisor/conf.d/

RUN chmod +x /startup.sh

RUN mkdir -p /var/run/sshd &&\
        sed -i -e 's/PermitRootLogin without-password/PermitRootLogin yes/g' /etc/ssh/sshd_config &&\
        sed -i -e 's/^session    required     pam_loginuid.so$/session    optional     pam_loginuid.so/g' /etc/pam.d/sshd &&\
        echo 'root:passw0rd' | chpasswd &&\
        useradd -d /home/default -m default &&\	
	mkdir -p /home/default/Documents &&\
        echo 'default:passw0rd' | chpasswd &&\
        echo "default ALL = (root) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/default &&\
        chmod 0440 /etc/sudoers.d/default

EXPOSE 5900 22
WORKDIR /root
CMD ["/startup.sh"]

