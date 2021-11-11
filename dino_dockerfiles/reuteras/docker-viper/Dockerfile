# This is a Docker image for Viper.
# A description of Viper from viper.li:
#   Viper is a binary management and analysis framework dedicated to malware
#   and exploit researchers.
# This Dockerfile is based on the one made by REMnux.
#   https://github.com/REMnux/docker/blob/master/viper/Dockerfile
# I created this file to be able to test later versions of Viper. I also include
# radare2 and tor.

FROM ubuntu:focal
LABEL maintainer="Coding <code@ongoing.today>"

ENV LD_LIBRARY_PATH /usr/local/lib:$LD_LIBRARY_PATH
ENV DEBIAN_FRONTEND noninteractive

USER root
## Install tools and libraries via apt
RUN sed -i -e "s/main/main non-free/" /etc/apt/sources.list && \
    apt update -yqq && \
    apt install -yqq --no-install-recommends \
        autoconf \
        automake \
        build-essential \
        ca-certificates \
        clamav-daemon \
        curl \
        exiftool \
        gcc \
        git \
        libdpkg-perl \
        libffi-dev \
        libfuzzy-dev \
        libssl-dev \
        libtool \
        libusb-1.0-0 \
        nano \
        openssh-client \
        p7zip-full \
        python3 \
        python3-dev \
        python3-pip \
        python3-setuptools \
        python3-socksipychain \
        rustc \
        ssdeep \
        sudo \ 
        swig \
        tor \
        unrar \
        wget && \
    # Add user for viper
    groupadd -r viper && \
    useradd -r -g viper -d /home/viper -s /bin/bash -c "Viper Account" viper && \
	mkdir -p /home/viper/workdir && \
	mkdir -p /home/viper/.viper && \
	sed -i "s/^.*requiretty/#Defaults requiretty/" /etc/sudoers && \
	echo "viper        ALL=(ALL)       NOPASSWD: ALL" >> /etc/sudoers && \
    # Install radare2
    cd /tmp && \
    sudo --user=viper git clone https://github.com/radare/radare2 && \
    cd radare2 && \
    SUDO_USER=viper ./sys/install.sh && \
    cd .. && \
    rm -rf radare2 && \
    ldconfig && \
    # Install PrettyTable for viper
    #python3 -m pip install PrettyTable && \
    # Support for MISP
    #python3 -m pip install pymisp && \
    cd /home/viper && \
	ln -s /home/viper/workdir/viper.conf .viper/ && \
    git clone https://github.com/viper-framework/viper-modules.git && \
    mv viper-modules /home/viper/.viper/modules && \
    cd /home/viper/.viper/modules && \
    git submodule add https://github.com/viper-framework/Mach-O.git && \
    # Install viper via pip
    python3 -m pip install --no-cache-dir viper-framework && \
    # Install dependencies
    python3 -m pip install --no-cache-dir lief && \
    sed -i -E "s/^bitstring==3.1.6/#bitstring==3.1.6/" /home/viper/.viper/modules/requirements.txt && \
    python3 -m pip install --no-cache-dir -r /home/viper/.viper/modules/requirements.txt && \
    chown -R viper:viper /home/viper && \
  	# Clean
  	apt remove -y \
  	    autoconf \
  	    automake \
  	    autotools-dev \
        build-essential \
        cpp \
        gcc \
        rustc && \
    apt autoremove -y && \
    apt clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/cache/debconf
USER viper
EXPOSE 8080
VOLUME ["/home/viper/workdir"]
WORKDIR /home/viper/
CMD ["/usr/local/bin/viper"]
