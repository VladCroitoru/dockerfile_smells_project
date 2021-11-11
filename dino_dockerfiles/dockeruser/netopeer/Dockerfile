from    ubuntu:12.04

run     echo "deb http://archive.ubuntu.com/ubuntu precise main universe multiverse" > /etc/apt/sources.list
run     apt-get update
run	apt-get install -y libxml2 libssh2-1 libdbus-1-dev doxygen libcurl4-gnutls-dev
run	apt-get install -y git
run	apt-get install -y build-essential checkinstall
run	git clone https://code.google.com/p/libnetconf/
run	apt-get install -y libxml2-dev libxslt1-dev libssh2-1-dev
run	git clone https://code.google.com/p/netopeer/
run	apt-get install -y libevent-dev openssh-server

run	cd /libnetconf && ./configure  --with-nacm-recovery-uid=0 && make && make install
run	cd /netopeer/server-sl && ./configure && make && make install
run	ln -s /usr/local/lib/libnetconf.so.0 /lib

RUN	mkdir /var/run/sshd
RUN	echo "root\nroot" > /password 
RUN	cat /password | passwd

RUN	echo 'Port 830' >> /etc/ssh/sshd_config
RUN	echo 'Subsystem netconf /usr/local/bin/netopeer-server-sl' >> /etc/ssh/sshd_config

CMD	/usr/sbin/sshd -D
EXPOSE 830
