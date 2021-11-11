from ubuntu:precise
MAINTAINER joshjdevl < joshjdevl [at] gmail {dot} com>

ENV DEBIAN_FRONTEND noninteractive


RUN	    apt-get update
RUN   	apt-get install -y python-software-properties 
RUN     apt-get update
RUN     add-apt-repository ppa:ubuntu-toolchain-r/test
RUN  	apt-get update && apt-get install -y gcc-4.8 g++-4.8
RUN 	update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.8 20
RUN 	update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.8 20
RUN 	update-alternatives --config gcc
RUN	    update-alternatives --config g++
RUN 	apt-get install -y -q build-essential git qt4-qmake g++ libqtwebkit-dev
RUN 	cd / && git clone https://github.com/DeDiS/Dissent.git
RUN	    apt-get install -y wget unzip
RUN	    apt-get install -y libicu48
RUN	mkdir -p /compile/cryptopp && wget http://www.cryptopp.com/cryptopp562.zip && mv cryptopp562.zip /compile/cryptopp
RUN	cd /compile/cryptopp && unzip cryptopp562.zip && make -j 5
ADD dissent.pro /Dissent/dissent.pro
RUN	cd /compile/cryptopp make install
RUN 	cd /Dissent && qmake application.pro 
RUN     cd /compile/cryptopp && make install && cd /Dissent && make -j 5
RUN	apt-get install -y vim
RUN 	apt-get -y install wget
RUN 	apt-get install -y openssh-server
RUN 	mkdir /var/run/sshd
RUN 	/usr/sbin/sshd
RUN 	echo "root:josh" | chpasswd
RUN 	cp /Dissent/src/Web/Content/* /Dissent/
ADD	server.conf /Dissent/conf/server.conf
