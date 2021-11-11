FROM ubuntu:16.04

MAINTAINER ijun "i@liuzhen.info"

ENV SDK lede-sdk-17.01.0-ar71xx-nand_gcc-5.4.0_musl-1.1.16.Linux-x86_64

#RUN apt-get update
RUN apt-get update && \
    apt-get install -y build-essential subversion git-core libncurses5-dev zlib1g-dev gawk flex quilt libssl-dev xsltproc libxml-parser-perl mercurial bzr ecj cvs unzip sudo wget xz-utils
RUN useradd -m mockbuilder && \
    echo 'mockbuilder ALL=NOPASSWD: ALL' > /etc/sudoers.d/mockbuilder && \
    sudo -iu mockbuilder wget -nv https://downloads.lede-project.org/releases/17.01.0/targets/ar71xx/nand/$SDK.tar.xz &&\
    sudo -iu mockbuilder tar xfa $SDK.tar.xz &&\
    sudo -iu mockbuilder rm -f $SDK.tar.xz &&\
    sudo -iu mockbuilder mv $SDK sdk

ADD package.sh /home/mockbuilder/

CMD ["sudo", "-iu", "mockbuilder", "bash"]
