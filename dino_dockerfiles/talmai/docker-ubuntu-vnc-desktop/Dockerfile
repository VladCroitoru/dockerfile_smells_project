FROM ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive

RUN sed -i 's#http://archive.ubuntu.com/#http://tw.archive.ubuntu.com/#' /etc/apt/sources.list

# built-in packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends software-properties-common curl \
    && sh -c "echo 'deb http://download.opensuse.org/repositories/home:/Horst3180/xUbuntu_16.04/ /' >> /etc/apt/sources.list.d/arc-theme.list" \
    && curl -SL http://download.opensuse.org/repositories/home:Horst3180/xUbuntu_16.04/Release.key | apt-key add - \
    && add-apt-repository ppa:fcwu-tw/ppa \
    && apt-get update \
    && apt-get install -y --no-install-recommends --allow-unauthenticated \
        supervisor \
        openssh-server pwgen sudo vim-tiny \
        net-tools \
        lxde x11vnc xvfb \
        gtk2-engines-murrine ttf-ubuntu-font-family \
        libreoffice firefox \
        fonts-wqy-microhei \
        language-pack-zh-hant language-pack-gnome-zh-hant firefox-locale-zh-hant libreoffice-l10n-zh-tw \
        nginx \
        python-pip python-dev build-essential \
        mesa-utils libgl1-mesa-dri \
        gnome-themes-standard gtk2-engines-pixbuf gtk2-engines-murrine pinta arc-theme \
        dbus-x11 x11-utils \
        ca-certificates \
        apt-utils \
        dbus-x11 \
        git \
        python \
        php7.0 \
        libcanberra-gtk-module \
        libgtk2.0-0 \
        libatk-adaptor \
        libgail-common \        
        texlive \        
        latexmk \    
        evince \
        guake \
        unzip \
        texlive-latex-extra \
        chromium-browser \
    && apt-get autoclean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/*

# Install Sublime
ARG SUBLIME_BUILD="${SUBLIME_BUILD:-3156}"
RUN curl -O https://download.sublimetext.com/sublime-text_build-"${SUBLIME_BUILD}"_amd64.deb && \
    dpkg -i -R sublime-text_build-"${SUBLIME_BUILD}"_amd64.deb || echo "\n Will force install of missing ST3 dependencies...\n" && \
    apt-get -y -f install && \
    rm -rvf sublime-text_build-"${SUBLIME_BUILD}"_amd64.deb
    
RUN locale-gen "en_US.UTF-8" && \
    dpkg-reconfigure locales

RUN apt-get update && \
    apt-get install -y golang-go openjdk-8-jre
    
# tini for subreap                                   
ENV TINI_VERSION v0.9.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /bin/tini
RUN chmod +x /bin/tini

ADD image /
RUN pip install setuptools wheel && pip install -r /usr/lib/web/requirements.txt

EXPOSE 80
WORKDIR /root
ENV HOME=/home/ubuntu \
    SHELL=/bin/bash
ENTRYPOINT ["/startup.sh"]
