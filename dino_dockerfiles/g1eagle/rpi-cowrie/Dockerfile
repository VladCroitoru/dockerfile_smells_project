FROM resin/rpi-raspbian
MAINTAINER g1eagle
 
# Upgrade and install required packages
RUN apt-get update && apt-get install -y \
    build-essential \
	git \
	libmpfr-dev \
	libssl-dev \
	libmpc-dev \
	libffi-dev \
	libpython-dev \
	openssh-client \
	python-configparser \
	python-crypto \
	python-pyasn1 \
	python-gmpy2 \
	python-mysqldb \
	python-pip \
	python-twisted \
	python-zope.interface \
	virtualenv \
	wget \
&& rm -rf /var/lib/apt/lists/*

# RUN sudo pip install configparser
# RUN sudo pip install enum34
# RUN pip install twisted[conch]
# RUN pip install cryptography
# RUN pip install pyopenssl
# RUN pip install gmpy2
# RUN pip install service_identity
 
# Install cowrie
# RUN sudo apk add python py-asn1 py-twisted py-zope-interface libffi-dev py-cryptography py-pip py-six py-cffi py-idna py-ipaddress py-openssl

RUN adduser --disabled-password --gecos '' cowrie
RUN sudo su - cowrie
RUN git clone http://github.com/micheloosterhof/cowrie
WORKDIR /cowrie
# RUN virtualenv cowrie-env
# RUN source cowrie-env/bin/activate





RUN cp cowrie.cfg.dist cowrie.cfg
WORKDIR /cowrie/data

RUN ssh-keygen -t dsa -b 1024 -f ssh_host_dsa_key
WORKDIR /cowrie
RUN export PYTHONPATH=/home/cowrie/cowrie
RUN wget https://raw.githubusercontent.com/g1eagle/Rpi-Cowrie/master/RPIStart.sh
RUN apt-get remove --purge wget


RUN chmod -R 755 /cowrie/log/
USER cowrie
ENTRYPOINT ["./RPIStart.sh"]
