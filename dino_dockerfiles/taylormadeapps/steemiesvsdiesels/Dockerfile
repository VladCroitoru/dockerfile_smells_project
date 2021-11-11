FROM ubuntu:xenial
MAINTAINER Encircle Solutions Ltd support@encircle.co.uk


ENV HOME /root


# Install modules from apt-get
RUN	apt-get -y update

RUN	apt-get install -q -y openssh-server pwgen wget tar && \
		apt-get install -q -y gcc g++ groff groff-base make python-setuptools &&\
		apt-get install -q -y git cmake python-dev autotools-dev libicu-dev build-essential libbz2-dev libboost-all-dev libssl-dev libncurses5-dev doxygen libreadline-dev dh-autoreconf

#install defaulr public ssh key
ADD ./keys/miningkey.pub /root/.ssh/miningkey.pub 
RUN cat /root/.ssh/miningkey.pub >> /root/.ssh/authorized_keys

#config up sshd with public key
RUN chmod 600 /root/.ssh/authorized_keys && \
	mkdir -p /var/run/sshd && \
	sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config && \
	sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config && \
	sed -i "s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config

#install shell in a box
RUN mkdir /opt/shellinabox && \
    wget -qO- "https://shellinabox.googlecode.com/files/shellinabox-2.14.tar.gz" | tar -zx --strip-components=1 -C /opt/shellinabox && \
    cd /opt/shellinabox && \
    ./configure && \
    make

ADD ./conf/shellinabox/black-on-white.css /opt/shellinabox/shellinabox/black-on-white.css
ADD ./conf/shellinabox/white-on-black.css /opt/shellinabox/shellinabox/white-on-black.css

ADD ./scripts/supervisord-shellinabox.sh /etc/service/shellinabox/run.sh
RUN chmod -f 750 /etc/service/shellinabox/run.sh \
	&& chgrp -f users /etc/service/shellinabox/run.sh




#now start building steem
# taken from https://steemit.com/steemhelp/@joseph/mining-steem-for-dummies as of 29/07/2016

#add required git repos - these are submodules of our steemiesvsdiesels repo - might need to do do a git submodule update on the repo before this docker build i.e.:
# git submodule update --init --recursive



#download and build the boost library dependency
RUN cd ~ && \
	wget -O boost_1_60_0.tar.gz http://sourceforge.net/projects/boost/files/boost/1.60.0/boost_1_60_0.tar.gz/download && \
	tar xzvf boost_1_60_0.tar.gz && \
	cd boost_1_60_0 && \
	./bootstrap.sh --prefix=/usr/local && \
	./b2 install

#build the bitcoin secp256k1 library dependency from git submodule repo
RUN cd ~ && \
	git clone https://github.com/bitcoin/secp256k1 && \
	cd ~/secp256k1 && \
	./autogen.sh && \
	./configure && \
	make && \
	./tests

#build the steem codebase from git submodule repo
#ADD ./steem/ /root/steem/
RUN cd ~ && \
	git clone https://github.com/steemit/steem && \
  cd ~/steem && \
	git checkout tags/v0.12.2 && \
	git submodule update --init --recursive && \
	cmake -DCMAKE_BUILD_TYPE=Release -DENABLE_CONTENT_PATCHING=OFF -DLOW_MEMORY_NODE=ON && \
  make

#add the steemd to our supervisor service runner
ADD ./scripts/supervisord-steemd.sh /etc/service/steemd/run.sh
RUN chmod -f 750 /etc/service/steemd/run.sh \
	&& chgrp -f users /etc/service/steemd/run.sh

#add our steemd config file
ADD ./conf/steemd/steemd.config.ini /root/steem/programs/steemd/witness_node_data_dir/config.ini
RUN chmod -f 700 /root/steem/programs/steemd/witness_node_data_dir/config.ini

	
# supervisord config - this is our serrvice runner
RUN easy_install supervisor
ADD ./conf/supervisord.conf /etc/supervisord.conf
ADD ./scripts/startup.sh /services/startup.sh
RUN chmod 740 /services/startup.sh	
	

#clean up apt-get to finish the build process
#RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*



#VOLUME /tmp

#sshd box 
EXPOSE 22
#shell in box port
EXPOSE 4200


CMD ["/bin/bash", "/services/startup.sh"]
