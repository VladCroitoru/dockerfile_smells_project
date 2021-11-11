FROM ubuntu
MAINTAINER moremagic <itoumagic@gmail.com>

RUN apt-get update && apt-get install -y openssh-server openssh-client
RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd
RUN sed -i 's/PermitRootLogin .*$/PermitRootLogin yes/' /etc/ssh/sshd_config

# gauche install
RUN apt-get install -y vim curl wget gauche*

#makiki install
RUN apt-get install -y git make
WORKDIR /root
RUN git clone https://github.com/shirok/Gauche-makiki.git
WORKDIR /root/Gauche-makiki
RUN ./configure
RUN make install

# app install
RUN apt-get install -y net-tools
COPY basic.scm /root/Gauche-makiki/examples/

EXPOSE 8012 
CMD ["gosh", "/root/Gauche-makiki/examples/basic.scm"]

