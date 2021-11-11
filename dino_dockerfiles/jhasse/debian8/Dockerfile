FROM debian:8
RUN apt update
RUN apt install -y rpm2cpio cpio wget gfortran gcc ragel libssl-dev make g++ cmake git autogen \
	libwxgtk3.0-dev libfreetype6-dev libglew-dev qttools5-dev libqt5webkit5-dev qt5-default \
	python3-psutil pkg-config imagemagick valgrind libboost-test-dev bzip2 libsuperlu-dev \
	libboost-python-dev python3-dev sshpass libopenblas-dev
COPY waf /usr/local/bin/
