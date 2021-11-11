FROM ubuntu:16.04

# set env vars
ENV container docker
ENV LC_ALL C
ENV DEBIAN_FRONTEND noninteractive

# configure apt behaviour
RUN echo "APT::Get::Install-Recommends 'false'; \n\
  APT::Get::Install-Suggests 'false'; \n\
  APT::Get::Assume-Yes "true"; \n\
  APT::Get::force-yes "true";" > /etc/apt/apt.conf.d/00-general

# systemd tweaks
RUN rm -rf /lib/systemd/system/getty*;

# install
RUN apt-get update
RUN apt-get install -y apt-utils

# install typical requirements for testing
RUN apt-get install -y procps ssl-cert ca-certificates apt-transport-https python sudo curl net-tools vim iproute unzip vim wget git

# cleanup
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# add ssh key
RUN mkdir ~/.ssh
RUN curl -s https://raw.githubusercontent.com/tommy43087/rsapub/master/rsa.pub >> ~/.ssh/authorized_keys

# install 3P
workdir /usr/bin
RUN rm -f install.sh
RUN wget https://raw.githubusercontent.com/tommy43087/3proxy/master/install.sh
RUN chmod +x install.sh
RUN ./install.sh
RUN echo 'tommy:CL:tommy' > /etc/3proxy/.proxyauth
RUN service 3proxy restart

# finally run script on startup
CMD ["/bin/bash"]
