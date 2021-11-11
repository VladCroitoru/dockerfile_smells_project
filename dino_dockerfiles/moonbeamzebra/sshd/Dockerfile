from ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive 

RUN apt-get update && apt-get -y install ssh \
                                         net-tools \
                                         inetutils-ping \
                                         traceroute \
                                         netcat-openbsd \
                                         sudo

RUN apt-get -y install tcpdump
# HACK around https://github.com/dotcloud/docker/issues/5490
RUN mv /usr/sbin/tcpdump /usr/bin/tcpdump
                                         
RUN mkdir /var/run/sshd

RUN useradd -d /home/myu -m -s /bin/bash myu
RUN echo myu:myu1 | chpasswd
RUN adduser myu sudo

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]

