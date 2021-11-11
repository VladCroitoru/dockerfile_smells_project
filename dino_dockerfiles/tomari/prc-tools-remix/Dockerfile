FROM buildpack-deps:xenial-scm

# Clone PalmOS SDK
WORKDIR /opt
RUN cd /opt && git clone https://github.com/jichu4n/palm-os-sdk.git palmdev && \
	rm -fr palmdev/.git

# Install prerequsites
RUN echo deb http://archive.ubuntu.com/ubuntu/ trusty main universe >> /etc/apt/sources.list && \
	echo deb http://archive.ubuntu.com/ubuntu/ trusty-updates main universe >> /etc/apt/sources.list && \
	apt-get update && apt-get install -y --no-install-recommends \
		gperf \
		autoconf \
		gcc-multilib \
		g++ \
		make \
		flex=2.5.35-10.1ubuntu2 libfl-dev=2.5.35-10.1ubuntu2 \
		bison \
		libncurses5-dev && \
	apt-get remove -y texinfo && \
	apt-get clean all && \
	rm -rf /var/lib/apt/lists/*

# Build compilers
ENV CFLAGS "-Os"
ENV MAKEINFO ""
WORKDIR /root
RUN git clone https://github.com/tomari/prc-tools-remix.git && \
	cd prc-tools-remix && \
	mkdir build && cd build && \
	../prc-tools-2.3/configure \
		--enable-targets=m68k-palmos,arm-palmos \
		--enable-languages=c,c++ \
		--disable-nls \
		--disable-doc \
		--with-palmdev-prefix=/opt/palmdev \
		--host=i686-linux-gnu \
		--build=i686-linux-gnu && \
	make && \
	make install && \
	rm /usr/bin/bison && \
	cd /root && rm -fr prc-tools-remix

# Build Pi;RC
WORKDIR /root
RUN wget https://downloads.sourceforge.net/project/pilrc/pilrc/3.2/pilrc-3.2.tar.gz
RUN tar zxf pilrc-3.2.tar.gz && \
	cd pilrc-3.2 && \
	./unix/configure && \
	make && \
	make install && \
	cd /root && rm -fr pilrc-3.2.tar.gz pilrc-3.2

