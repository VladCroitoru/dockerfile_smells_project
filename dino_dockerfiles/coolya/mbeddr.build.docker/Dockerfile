FROM ubuntu:bionic
MAINTAINER Kolja Dummann <kolja.dummann@logv.ws>
RUN dpkg --add-architecture i386
RUN apt-get update && apt-get install -y \
	ant \
	build-essential \
	bison \
	ca-certificates \
	curl \
	flex \
	g++-8 \
	gcc-8 \
	gdb \
	git \
	lcov \
	libz-dev \
	libwww-perl \
	libxerces-c-dev \
	make \
	nsis \
	g++-4.8-multilib \
	libstdc++6:i386 libgcc1:i386 zlib1g:i386 libncurses5:i386 \
	openjdk-8-jdk=8u162-b12-1 openjdk-8-jre=8u162-b12-1 openjdk-8-jdk-headless=8u162-b12-1 openjdk-8-jre-headless=8u162-b12-1 \
	patch \
	subversion \
	supervisor \
	unzip \
	wget \
	xvfb \
	zip \
	ninja-build \
	&& apt-get autoremove \
	&& update-java-alternatives -s java-1.8.0-openjdk-amd64

RUN cd /tmp && \
	wget --progress=dot:mega https://github.com/aktau/github-release/releases/download/v0.6.2/linux-amd64-github-release.tar.bz2 && \
	tar -xjvf linux-amd64-github-release.tar.bz2 && \
	mv bin/linux/amd64/github-release /usr/bin/ && \
	rm -rf bin/

RUN \
	cmake_major_minor=3.10 && \
	cmake=cmake-${cmake_major_minor}.2-Linux-x86_64 && \
	cd /tmp && \
	wget --progress=dot:mega https://cmake.org/files/v${cmake_major_minor}/${cmake}.tar.gz && \
	tar -xzvf ${cmake}.tar.gz && \
	cp -R ${cmake}/bin ${cmake}/share /usr && \
	rm -rf ${cmake} ${cmake}.tar.gz

RUN mkdir /buildAgent && cd /buildAgent && \
	wget --progress=dot:mega https://build.mbeddr.com/update/buildAgent.zip && \
	unzip buildAgent.zip && \
	chmod +x /buildAgent/bin/agent.sh
ADD ./buildAgent.properties /buildAgent/conf/buildAgent.properties
ADD ./start.sh /start
RUN mkdir -p /root/.ssh /var/log/supervisor
ADD ./sshconfig /root/.ssh/config
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN chmod +x /start
CMD ["/usr/bin/supervisord"]
COPY ./bin/* /usr/bin/

# Install our own cppcheck because 1.67 in jessie is buggy
RUN \
	cppcheck_version=1.77 && \
	cd /tmp && \
	wget --progress=dot:mega -O cppcheck-${cppcheck_version}.tar.gz https://github.com/danmar/cppcheck/archive/${cppcheck_version}.tar.gz && \
	tar -zxf cppcheck-${cppcheck_version}.tar.gz && \
	apt-get -y install libpcre3-dev && \
	(cd cppcheck-${cppcheck_version} && make install -j`nproc` SRCDIR=build CFGDIR=/usr/share/cppcheck/cfg HAVE_RULES=yes CXXFLAGS="-O2 -DNDEBUG -Wall -Wno-sign-compare -Wno-unused-function") && \
	rm -rf cppcheck-${cppcheck_version}.tar.gz cppcheck-${cppcheck_version} && \
	apt-get -y purge libpcre3-dev && apt-get -y autoremove

RUN \
	z3_version=4.7.1 && \
	cd /tmp && \
	wget --progress=dot:mega -O z3.zip https://github.com/Z3Prover/z3/releases/download/z3-${z3_version}/z3-${z3_version}-x64-ubuntu-16.04.zip && \
	unzip z3.zip && \
	mv z3-${z3_version}-x64-ubuntu-16.04/bin/z3 /usr/bin/ && \
	mv z3-${z3_version}-x64-ubuntu-16.04/bin/libz3.so /usr/bin/ && \
	mv z3-${z3_version}-x64-ubuntu-16.04/bin/libz3java.so /usr/bin/ && \
	rm -rf /tmp/z3-${z3_version}-x64-ubuntu-16.04 z3.zip

RUN cd /tmp \
	&& wget --progress=dot:mega https://bootstrap.pypa.io/2.7/get-pip.py \
	&& python get-pip.py \
	&& rm get-pip.py \
	&& pip install mkdocs \
	&& pip install mkdocs-cinder


# install JetBrains JDK 8 with functional javafx
## for headless gtk
ENV DISPLAY :0
## needed for javafx
RUN apt-get install --yes libgtk2.0-0 libxslt1.1

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

## install JetBrains JDK 8
ENV JB_JAVA8_VERSION jbrsdk-8u202-linux-x64-b1483.37
RUN wget --progress=dot:giga -O /tmp/${JB_JAVA8_VERSION}.tar.gz https://bintray.com/jetbrains/intellij-jdk/download_file?file_path=${JB_JAVA8_VERSION}.tar.gz \
	&& mkdir /usr/lib/jvm/${JB_JAVA8_VERSION} \
	&& tar xzf /tmp/${JB_JAVA8_VERSION}.tar.gz --directory /usr/lib/jvm/${JB_JAVA8_VERSION} \
	&& rm /tmp/${JB_JAVA8_VERSION}.tar.gz
ENV JB_JAVA8_HOME /usr/lib/jvm/${JB_JAVA8_VERSION}
## echo "Installed JetBrains JDK 8 version `cat /usr/lib/jvm/${JB_JAVA8_VERSION}/release | grep JAVA_VERSION`" \
## echo "Run export JAVA_HOME=\"/usr/lib/jvm/${JB_JAVA8_VERSION}/\" PATH=\"/usr/lib/jvm/${JB_JAVA8_VERSION}/bin:$PATH\" to select this jdk"

## install JetBrains JDK 11
ENV JB_JAVA11_VERSION 11_0_9-b944.49
RUN wget --progress=dot:giga -O /tmp/${JB_JAVA11_VERSION}.tar.gz https://projects.itemis.de/nexus/content/repositories/mbeddr/com/jetbrains/jdk/jbrsdk/${JB_JAVA11_VERSION}/jbrsdk-${JB_JAVA11_VERSION}-linux-x64.tgz \
	&& tar xzf /tmp/${JB_JAVA11_VERSION}.tar.gz --directory /tmp \
	&& mv /tmp/jbrsdk /usr/lib/jvm/${JB_JAVA11_VERSION} \
	&& rm /tmp/${JB_JAVA11_VERSION}.tar.gz
ENV JB_JAVA11_HOME /usr/lib/jvm/${JB_JAVA11_VERSION}
## echo "Installed JetBrains JDK 8 version `cat /usr/lib/jvm/${JB_JAVA11_VERSION}/release | grep JAVA_VERSION`" \
## echo "Run export JAVA_HOME=\"/usr/lib/jvm/${JB_JAVA11_VERSION}/\" PATH=\"/usr/lib/jvm/${JB_JAVA11_VERSION}/bin:$PATH\" to select this jdk"

## configure locale to use UTF-8 encoding
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN chmod +x /usr/bin/*
