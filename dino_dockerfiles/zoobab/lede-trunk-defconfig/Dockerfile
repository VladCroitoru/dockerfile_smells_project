FROM ubuntu:14.04
MAINTAINER Benjamin Henrion <zoobab@gmail.com>
LABEL description="A daily build of LEDE trunk"

RUN DEBIAN_FRONTEND=noninteractive apt-get update -y -q
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q --force-yes build-essential subversion git-core libncurses5-dev zlib1g-dev gawk flex quilt libssl-dev xsltproc libxml-parser-perl mercurial bzr ecj cvs unzip wget

ENV user lede

RUN useradd -d /home/$user -m -s /bin/bash $user
RUN echo "$user ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/$user
RUN chmod 0440 /etc/sudoers.d/$user

USER $user

WORKDIR /home/$user
RUN git clone --quiet https://github.com/lede-project/source.git
WORKDIR /home/$user/source
RUN make defconfig
RUN make
