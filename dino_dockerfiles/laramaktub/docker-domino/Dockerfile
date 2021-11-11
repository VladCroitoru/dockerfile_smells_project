FROM ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive
ENV QT_PATH /opt/Qt
ENV QT_DESKTOP $QT_PATH/5.7/gcc_64
ENV PATH $QT_DESKTOP/bin:$PATH

# Install updates & requirements:
#  * git, openssh-client, ca-certificates - clone & build
#  * locales, sudo - useful to set utf-8 locale & sudo usage
#  * curl - to download Qt bundle
#  * build-essential, pkg-config, libgl1-mesa-dev - basic Qt build requirements
#  * libsm6, libice6, libxext6, libxrender1, libfontconfig1, libdbus-1-3 - dependencies of the Qt bundle run-file
RUN apt-get -qq update && apt-get -qq dist-upgrade && apt-get install -qq -y --no-install-recommends \
    git \
    openssh-client \
    ca-certificates \
    locales \
    sudo \
    curl \
    build-essential \
    pkg-config \
    libgl1-mesa-dev \
    libsm6 \
    libice6 \
    libxext6 \
    libxrender1 \
    libfontconfig1 \
    libdbus-1-3 \
    && apt-get -qq clean


RUN apt-get install -y xterm
COPY extract-qt-installer.sh /tmp/qt/

# Download & unpack Qt 5.7 toolchains & clean
RUN curl -Lo /tmp/qt/installer.run 'http://download.qt-project.org/official_releases/qt/5.7/5.7.1/qt-opensource-linux-x64-5.7.1.run' \
    && QT_CI_PACKAGES=qt.57.gcc_64 /tmp/qt/extract-qt-installer.sh /tmp/qt/installer.run "$QT_PATH" \
    && find "$QT_PATH" -mindepth 1 -maxdepth 1 ! -name '5.*' -exec echo 'Cleaning Qt SDK: {}' \; -exec rm -r '{}' \; \
    && rm -rf /tmp/qt

# Reconfigure locale
RUN locale-gen en_US.UTF-8 && dpkg-reconfigure locales

# Add group & user + sudo
RUN groupadd -r user && useradd --create-home --gid user user && echo 'user ALL=NOPASSWD: ALL' > /etc/sudoers.d/user

#Install some missing packages
RUN apt-get install -y wget unzip libqt5x11extras5 zlib1g-dev g++

#Install python 2.7.13
RUN apt-get install -y build-essential checkinstall libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
RUN apt-get install -y python

RUN apt-get install -y libncurses5-dev libncursesw5-dev

#Install qt and compile Domino
WORKDIR /opt
RUN wget https://github.com/molevol-ub/DOMINO/archive/master.zip
RUN unzip master.zip
WORKDIR /opt/DOMINO-master/src/Qt-c++
RUN qmake DOMINO.pro 
ENV LD_LIBRARY_PATH "$LD_LIBRARY_PATH:/opt/Qt/5.7/gcc_64/lib/"
RUN make
WORKDIR /opt/DOMINO-master/
RUN wget https://raw.githubusercontent.com/laramaktub/docker-domino/master/DOMINO_installer_docker.sh
RUN chmod a+x DOMINO_installer_docker.sh 
RUN ./DOMINO_installer_docker.sh
RUN cp /opt/DOMINO-master/src/Qt-c++/DOMINO /opt/DOMINO-master/bin
ENV PATH "$PATH:/opt/DOMINO-master/bin"
RUN apt-get install -qqy x11-apps
RUN apt-get install -y dbus
RUN dbus-uuidgen > /var/lib/dbus/machine-id

#Needed to be able to use the GUI
ENV DISPLAY :0


