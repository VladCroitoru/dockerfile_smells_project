FROM ubuntu:bionic

ARG DEBIAN_FRONTEND=noninteractive
ENV TERM=xterm-256color LANG=en_US.UTF-8
RUN apt-get update \
    && apt-get install -y locales \
    && locale-gen $LANG \
    && apt-get install -y --no-install-recommends apt-utils \
    && echo reconfig locales: \
    && dpkg-reconfigure locales \
    && apt-get install -y \
        lxc \
        iptables \
        expect \
        lsb \
        man \
        git \
        autoconf \
        autopoint \
        automake \
        autotools-dev \
        libtool \
        telnet \
        vim \
        curl \
        wget \
        zsh \
        make \
        bzip2 \
        mtr \
        nmap \
        netcat-openbsd \
        openssh-server \
        iputils-ping \
        httping \
        dnsutils \
        libnet-ifconfig-wrapper-perl \
        apt-transport-https \
        ca-certificates \
        software-properties-common \
        supervisor \
        supervisor-doc \
        launchtool \
        python \
        python-pip \
        python3 \
        python3-pip \
        command-not-found \
        megatools \
    && curl -fsSL get.docker.com | bash -s \
    && apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* \
    && rm -f /etc/ssh/ssh_host_*_key

RUN wget -O dircolors "https://raw.githubusercontent.com/seebi/dircolors-solarized/master/dircolors.ansi-light" \
    && dircolors -b dircolors > /root/.dircolors_source \
    && rm -f dircolors \
    && curl -fsSL "https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh" | bash -s \
    && chsh -s /bin/zsh
COPY zshrc /root/.zshrc
COPY sources.list.* /etc/apt/
COPY dubuntu.zsh-theme /root/.oh-my-zsh/custom/dubuntu.zsh-theme
COPY vimrc /root/.vimrc
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY entrypoint.sh /entrypoint.sh

# VOLUME /shared    commented out to prevent auto created volume
WORKDIR /shared
EXPOSE 22 80 443
ENTRYPOINT ["/entrypoint.sh"]
