FROM paddlepaddle/paddle:latest-dev
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -y
RUN apt-get install -y openssh-server lxde software-properties-common python-software-properties
RUN add-apt-repository ppa:x2go/stable
RUN apt-get update -y
RUN apt-get install x2goserver x2goserver-xsession x2golxdebindings pwgen firefox pulseaudio libcurl3 libappindicator1 -y
RUN add-apt-repository ppa:nightuser/qtcreator
RUN add-apt-repository ppa:gophers/archive
RUN apt-get update
RUN apt-get install qtcreator golang-1.8 fish vim nano ccache htop byobu -y
RUN mkdir -p /var/run/sshd && sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config && sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config
RUN sed -i "s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config
RUN sed -i "s/#PasswordAuthentication/PasswordAuthentication/g" /etc/ssh/sshd_config
ADD set_root_pw.sh /set_root_pw.sh
ADD run.sh /run.sh
RUN echo "export PATH=/usr/local/nvidia/bin:/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin" >> /etc/profile &&\
    echo 'export LD_LIBRARY_PATH=/usr/local/nvidia/lib:/usr/local/nvidia/lib64:$LD_LIBRARY_PATH' >> /etc/profile &&\
    echo "export LIBRARY_PATH=/usr/local/cuda/lib64/stubs"  >> /etc/profile
RUN chsh -s /usr/bin/fish
RUN chmod +x /*.sh

EXPOSE 22
CMD ["/run.sh"]
