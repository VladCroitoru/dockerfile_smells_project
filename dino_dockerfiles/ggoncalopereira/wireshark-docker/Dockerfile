FROM ubuntu:latest

ENV INSTALLER_DIR_MININET mininet/util/install.sh
ENV REPOSITORY_DIR_MININET https://github.com/mininet/mininet.git

RUN apt-get update && apt-get install -y \
    git \
    tcpdump \
    sudo

RUN DEBIAN_FRONTEND=noninteractive apt-get install wireshark -y

RUN git clone $REPOSITORY_DIR_MININET

RUN chmod +x $INSTALLER_DIR_MININET
RUN ./$INSTALLER_DIR_MININET -fnv

RUN rm -rf /tmp/mininet
RUN rm -rf /tmp/openflow

EXPOSE 6653 6633

VOLUME /home/mininetdir
WORKDIR /home/mininetdir

CMD ["bash"]
