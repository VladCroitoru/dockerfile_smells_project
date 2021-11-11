FROM debian:stretch
MAINTAINER Guillaume Gauvrit <guillaume@gauvr.it> 


# Dockerfile that contains stuff to build and host .deb packages
# This is lots of copy paste from


# https://registry.hub.docker.com/u/mikepurvis/aptly/dockerfile/
# https://registry.hub.docker.com/u/tianon/debian-devel/dockerfile/

RUN  apt-get update && \
     apt-get install -y gnupg2 && \
     mkdir ~/.gnupg && \
     echo "disable-ipv6" >> ~/.gnupg/dirmngr.conf && \
     echo "deb http://repo.aptly.info/ squeeze main" > /etc/apt/sources.list.d/aptly.list

# Instructions from: https://www.aptly.info/download/
RUN apt-key adv --keyserver pool.sks-keyservers.net --recv-keys ED75B5A4483DA07C

RUN apt-get update && apt-get install -y \
        aptly \
        bash-completion curl less rsync vim wget \
        build-essential \
        devscripts \
        dh-make \
        dh-virtualenv \
        equivs \
        git bzr mercurial subversion \
        git-buildpackage svn-buildpackage \
        libcrypt-ssleay-perl \
        libdistro-info-perl \
        libfile-fcntllock-perl \
        libwww-perl \
        openssh-client \
        python-distro-info \
        python-debian \
        python3-venv \
        quilt \
        --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# need deb-src for compiling packages
RUN find /etc/apt/sources.list* -type f -exec sed -i 'p; s/^deb /deb-src /' '{}' +

# let's make apt list package versions, since those are handy during devel
RUN echo 'APT::Get::Show-Versions "1";' > /etc/apt/apt.conf.d/verbose

# for ssh to debian hosts, let's make sure we know their fingerprints <3
RUN mkdir -p ~/.ssh && chmod 700 ~/.ssh \
    && wget -O ~/.ssh/known_hosts https://db.debian.org/debian_known_hosts \
    && chmod 644 ~/.ssh/known_hosts

# make sure things are pretty
ENV LANG C.UTF-8
ENV TERM xterm-256color
RUN cp /etc/skel/.bashrc ~/ \
    && sed -ri 's/^#(force_color_prompt=yes)/\1/' ~/.bashrc

# quilt is much amaze: https://wiki.debian.org/UsingQuilt#Using_quilt_with_Debian_source_packages
ENV QUILT_PATCHES debian/patches
ENV QUILT_REFRESH_ARGS -p ab --no-timestamps --no-index


ADD gen-key-script /etc/gen-key-script
ADD aptly.conf /etc/aptly.conf
ADD entrypoint.sh /entrypoint.sh
ADD makedeb /bin/makedeb 

RUN chmod u+x /entrypoint.sh
RUN chmod u+x /bin/makedeb


ENTRYPOINT ["/entrypoint.sh"]

VOLUME ["/aptly"]
VOLUME ["/root"]
EXPOSE 8765

WORKDIR /mnt

