FROM ubuntu:16.04

RUN set -x && \
    apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install wget p7zip-full curl build-essential zlib1g-dev libcurl3 libcurl4-gnutls-dev xterm apache2 valgrind zip unzip vim

# For 10.2.0
# ADD http://altd.embarcadero.com/releases/studio/19.0/PAServer/LinuxPAServer19.0.tar.gz LinuxPAServer19.0.tar.gz

# For 10.2.3
# ADD http://altd.embarcadero.com/releases/studio/19.0/PAServer/Release3/LinuxPAServer19.0.tar.gz LinuxPAServer19.0.tar.gz

# RUN cd /root && \
#    tar zxvf /LinuxPAServer19.0.tar.gz && \
#    rm /LinuxPAServer19.0.tar.gz
