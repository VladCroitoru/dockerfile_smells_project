FROM debian:stretch

RUN 	DEBIAN_FRONTENT=noninteractive apt-get update && \
	apt-get install -y \
		qtbase5-dev \
		qtbase5-dev-tools \
		qttools5-dev-tools \
		qtscript-tools \
		python-all-dev \
		build-essential \
		qt5-default \
		bison \
		flex \
		qtbase5-private-dev \
		qtconnectivity5-dev \
		qtdeclarative5-dev \
		qtdeclarative5-dev-tools \
		qtconnectivity5-dev \
		qt5keychain-dev \
		qt5-style-plugins \
		tcl8.6-dev \
		tk8.6-dev \
		tcl \
		libgsl-dev \
		libreadline-dev \
		python3 \
		mercurial \
		iverilog \
		gawk \
		cmake \
		clang \
		pkg-config \
		libkf5texteditor-dev \
		gettext \
		libqt5svg5-dev \
		qttools5-dev \
		qtmultimedia5-dev \
		libqt5xmlpatterns5-dev \
		libboost-all-dev \
		libpythonqt-dev

RUN	apt-get install -y \
		git \
		vim \
		ssh \
		debmake \
		locales-all \
		git-buildpackage

RUN mkdir /root/.ssh

WORKDIR /build

COPY ssh.sh /ssh.sh

COPY build.sh /build.sh

COPY authorized_keys /root/.ssh
