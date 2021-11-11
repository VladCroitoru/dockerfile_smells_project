FROM i386/ubuntu
MAINTAINER Robin Appelman <robin@icewind.nl>

ADD ./install.sh /install.sh
RUN mkdir /data \
	&& mkdir /include \
	&& apt-get update \
	&& apt-get install -y wget unzip \
	&& rm -rf /var/lib/apt/lists/*
RUN /install.sh
WORKDIR /data

ADD ./spcomp.sh /spcomp.sh

ENTRYPOINT ["/spcomp.sh"]
