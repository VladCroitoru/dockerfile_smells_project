FROM ubuntu:14.04

# env vars
ENV HOME /root
ENV GOPATH /root/go
ENV PATH /root/go/bin:/usr/local/go/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games

# GOPATH
RUN mkdir -p /root/go

# apt
RUN echo "deb mirror://mirrors.ubuntu.com/mirrors.txt trusty main restricted universe multiverse" > /etc/apt/sources.list
RUN echo "deb-src mirror://mirrors.ubuntu.com/mirrors.txt trusty main restricted universe multiverse" >> /etc/apt/sources.list

RUN echo "deb mirror://mirrors.ubuntu.com/mirrors.txt trusty-updates main restricted universe multiverse" >> /etc/apt/sources.list
RUN echo "deb-src mirror://mirrors.ubuntu.com/mirrors.txt trusty-updates main restricted universe multiverse" >> /etc/apt/sources.list

RUN echo "deb mirror://mirrors.ubuntu.com/mirrors.txt trusty-backports main restricted universe multiverse" >> /etc/apt/sources.list
RUN echo "deb-src mirror://mirrors.ubuntu.com/mirrors.txt trusty-backports main restricted universe multiverse" >> /etc/apt/sources.list

RUN echo "deb mirror://mirrors.ubuntu.com/mirrors.txt trusty-security main restricted universe multiverse" >> /etc/apt/sources.list
RUN echo "deb-src mirror://mirrors.ubuntu.com/mirrors.txt trusty-security main restricted universe multiverse" >> /etc/apt/sources.list

RUN echo "deb http://archive.canonical.com/ubuntu trusty partner" >> /etc/apt/sources.list
RUN echo "deb http://extras.ubuntu.com/ubuntu trusty main" >> /etc/apt/sources.list
RUN echo "deb-src http://extras.ubuntu.com/ubuntu trusty main" >> /etc/apt/sources.list

RUN apt-get update
RUN apt-get install -y build-essential mercurial git-core subversion wget

# go 1.3 tarball
RUN wget -qO- http://golang.org/dl/go1.3.linux-amd64.tar.gz | tar -C /usr/local -xzf -
