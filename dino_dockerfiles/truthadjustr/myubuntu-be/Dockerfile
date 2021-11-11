FROM ubuntu:latest
MAINTAINER truthadjustr@gmail.com

RUN apt-get update && apt-get install -y --no-install-recommends apt-transport-https\
    ca-certificates\
    build-essential\
    cgdb\
    vim\
    bc\
    hexedit\
    valgrind\
    less\
    openssh-client\
    manpages-dev\
    manpages-posix-dev\
    dos2unix\
    automake\
    ncurses-dev\
    flex\
    texinfo\
    libreadline6 libreadline6-dev\
    file\
    inotify-tools\
    git

WORKDIR /root/
RUN mkdir /root/src && cd /root/src && git clone https://github.com/syscools/commandline.git\
    && cd commandline && ./setup.sh
