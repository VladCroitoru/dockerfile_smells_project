FROM debian:wheezy
MAINTAINER Quentin Devos <q.devos@student.uclouvain.be>, Loic Fortemps <loic.fortemps@student.uclouvain.be>
 
RUN apt-get update && apt-get install -y \
        --no-install-recommends \
        --no-install-suggests \
	autoconf \
	automake \
	ca-certificates \
	d-itg \
	gcc \
	git \
	g++ \
	libtool \
	make \
	net-tools \
	patch \
	tcpdump \
	unzip \
	wget

RUN mkdir experience

WORKDIR /tmp

RUN git clone https://github.com/multipathdtls/wolfssl-mpdtls.git && cd wolfssl-mpdtls/ && \
	./autogen.sh && \
	./configure --enable-mpdtls --enable-debug --enable-dh --enable-ecc --disable-examples --disable-oldtls && \
	make install && cd .. && \
	rm -rf *

RUN git clone https://github.com/mininet/mininet.git && \
	sed -e 's/sudo //g' \
	-e 's/\(apt-get -y install\)/\1 --no-install-recommends --no-install-suggests/g' \
	-i mininet/util/install.sh && \
	mininet/util/install.sh -a -s / && \
	rm -rf *

RUN git clone https://github.com/multipathdtls/mpdtls-vpn.git && cd mpdtls-vpn/ && \
	make && \
	cp -r client server certs/ /experience/ && cd .. && \
	rm -rf *

RUN apt-get clean && rm -rf /var/lib/apt/lists/*

COPY minitopo/src/ /tmp/minitopo

ENV PYTHONPATH /tmp/minitopo:$PYTHONPATH

WORKDIR /experience

COPY minitopo/src/mpPerf.py mpPerf.py

COPY conf conf

COPY xp xp

COPY script.itg script.itg

COPY bootstrap bootstrap

COPY run_var_bw run_var_bw

COPY run_var_loss run_var_loss

VOLUME ["/experience/data"]

ENTRYPOINT ["./bootstrap"]
