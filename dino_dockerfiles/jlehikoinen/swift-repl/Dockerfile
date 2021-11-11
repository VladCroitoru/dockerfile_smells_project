FROM ubuntu:16.04
MAINTAINER Janne Lehikoinen <jl@miltei.net>

RUN apt-get update && \
	apt-get install -y wget curl build-essential clang-3.6 libedit-dev python2.7 python2.7-dev libicu-dev libxml2 libcurl4-openssl-dev && \
	update-alternatives --install /usr/bin/clang clang /usr/bin/clang-3.6 100 && \
	update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-3.6 100 && \
	apt-get autoclean && \
	apt-get --purge -y autoremove && \
	rm -rf /var/lib/apt/lists/* && \
	wget -O - http://llvm.org/apt/llvm-snapshot.gpg.key | apt-key add - && \
	wget -q -O - https://swift.org/keys/all-keys.asc | gpg --import - && \
	gpg --keyserver hkp://pool.sks-keyservers.net --refresh-keys Swift

# ENV BRANCH development
# ENV VERSION DEVELOPMENT-SNAPSHOT-2016-02-08-a

ENV BRANCH swift-3.0.2-release
ENV VERSION 3.0.2-RELEASE
ENV PLATFORM ubuntu16.04

ENV SWIFT_PATH /usr/local
ENV PATH $SWIFT_PATH/swift/usr/bin:$PATH

RUN cd $SWIFT_PATH && \
	wget https://swift.org/builds/$BRANCH/ubuntu1604/swift-$VERSION/swift-$VERSION-$PLATFORM.tar.gz && \
	wget https://swift.org/builds/$BRANCH/ubuntu1604/swift-$VERSION/swift-$VERSION-$PLATFORM.tar.gz.sig && \
	tar xzf swift-$VERSION-$PLATFORM.tar.gz && \
	mv swift-$VERSION-$PLATFORM swift && \
	gpg --verify swift-$VERSION-$PLATFORM.tar.gz.sig && \
	rm swift-$VERSION-$PLATFORM.tar.gz*

CMD ["swift", "--version"]
