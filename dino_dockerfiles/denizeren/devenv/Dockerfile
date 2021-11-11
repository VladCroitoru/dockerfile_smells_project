FROM ubuntu

MAINTAINER Deniz Eren

### INSTALL
RUN apt-get update
RUN apt-get install -y openssh-server
RUN apt-get install -y tmux
RUN apt-get install -y git
RUN apt-get install -y vim
RUN apt-get install -y curl
RUN apt-get install -y zsh
RUN apt-get install -y golang-go
RUN apt-get install -y gcc
RUN apt-get install -y g++
RUN apt-get install -y cgdb
RUN apt-get install -y python-pudb
RUN apt-get install -y exuberant-ctags
RUN apt-get install -y sshfs
RUN apt-get install -y man


### CONFIGURE
RUN mkdir /root/go

# SSH Stuff
RUN mkdir /var/run/sshd
RUN echo 'root:deniz' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
EXPOSE 22

# rc
RUN cd /root; git clone https://github.com/denizeren/rc.git; bash rc/install.sh


### START
CMD ["/usr/sbin/sshd", "-D"]

