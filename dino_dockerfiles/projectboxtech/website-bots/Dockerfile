FROM ubuntu:trusty

# Install dependencies
RUN apt-get update --fix-missing && \
	apt-get -y install \
	build-essential \
	g++ \
	flex \
	bison \
	gperf \
	ruby \
	perl \
	libsqlite3-dev \
	libfontconfig1-dev \
	libicu-dev \
	libfreetype6 \
	libssl-dev \
	libpng-dev \
	libjpeg-dev \
	python \
	libx11-dev \
	libxext-dev \
	wget \
	git
	
# Install PhantomJS
WORKDIR /opt
RUN git clone --depth=1 --recurse-submodules https://github.com/ariya/phantomjs.git && \
	./phantomjs/build.py && \
	ln -s /opt/phantomjs/bin/phantomjs /bin/phantomjs
