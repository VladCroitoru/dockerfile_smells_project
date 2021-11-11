FROM phusion/baseimage:0.9.18

# ------------------------------------------------------------------------------
# Install Dependencies
# ------------------------------------------------------------------------------

RUN apt-get update && apt-get install -y \
	make \
	wget \
	unrar \
	autoconf \
	automake \
	libtool \
	gcc \
	g++ \
	gperf \
	flex \
	bison \
	texinfo \
	gawk \
	ncurses-dev \
	libexpat-dev \
	python2.7-dev \
	python-serial \
	sed \
	git \
	unzip \
	bash \
	wget \
	bzip2 \
	vim \
	screen \
	sudo \
	help2man

# ------------------------------------------------------------------------------
# Install ESP8266 SDK
# ------------------------------------------------------------------------------

RUN useradd -d /home/espbuilder -m espbuilder && \
	usermod -a -G dialout espbuilder && \
	mkdir -p /etc/sudoers.d && \
	echo "espbuilder ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/espbuilder && \
	chmod 0440 /etc/sudoers.d/espbuilder

RUN cd /opt && git clone --recursive https://github.com/pfalcon/esp-open-sdk.git
RUN chmod 777 -R /opt/esp-open-sdk

USER espbuilder
RUN cd /opt/esp-open-sdk && make VENDOR_SDK=1.5.4 STANDALONE=y

USER root

# ------------------------------------------------------------------------------
# Cleanup
# ------------------------------------------------------------------------------

RUN rm -rf /home/espbuilder/esp-open-sdk/crosstool-NG/.build

# ------------------------------------------------------------------------------
# Set Environment
# ------------------------------------------------------------------------------

ENV PATH /opt/esp-open-sdk/xtensa-lx106-elf/bin:$PATH
ENV XTENSA_TOOLS_ROOT /opt/esp-open-sdk/xtensa-lx106-elf/bin
ENV SDK_BASE /opt/esp-open-sdk/sdk
ENV FW_TOOL /opt/esp-open-sdk/xtensa-lx106-elf/bin/esptool.py  

ENV ESP_HOME /opt/esp-open-sdk

# ------------------------------------------------------------------------------
# Install esptool.py
# ------------------------------------------------------------------------------

RUN wget https://github.com/themadinventor/esptool/archive/master.zip && unzip master.zip && mv esptool-master $ESP_HOME/esptool && rm master.zip

# ------------------------------------------------------------------------------
# Install esptool2
# ------------------------------------------------------------------------------

RUN cd  $ESP_HOME && git clone https://github.com/raburton/esptool2
RUN cd $ESP_HOME/esptool2 && make

ENV PATH $ESP_HOME/esptool2:$PATH
