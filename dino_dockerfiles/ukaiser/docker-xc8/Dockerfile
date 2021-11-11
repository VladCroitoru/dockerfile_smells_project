FROM debian:jessie

MAINTAINER Michael Mitchell <mmitchel@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

# Microchip Tools Require i386 Compatability as Dependency

RUN dpkg --add-architecture i386 \
    && apt-get update -yq \
    && apt-get upgrade -yq \
    && apt-get install -yq --no-install-recommends build-essential bzip2 cpio curl python unzip wget \
    libc6:i386 libx11-6:i386 libxext6:i386 libstdc++6:i386 libexpat1:i386 \
    libxext6 libxrender1 libxtst6 libgtk2.0-0 libxslt1.1 libncurses5-dev bzip2 \
	unzip \
	xz-utils

# Download and Install XC8 Compiler, Current Version

RUN curl -fSL -A "Mozilla/4.0" -o /tmp/xc8.run "http://www.microchip.com/mplabxc8linux" \
    && chmod a+x /tmp/xc8.run \
    && /tmp/xc8.run --mode unattended --unattendedmodeui none \
        --netservername localhost --LicenseType FreeMode --prefix /opt/microchip/xc8 \
    && rm /tmp/xc8.run

ENV PATH $PATH:/opt/microchip/xc8/bin

# Download and Install XC16 Compiler, Current Version
#
#RUN curl -fSL -A "Mozilla/4.0" -o /tmp/xc16.run "http://www.microchip.com/mplabxc16linux" \
#    && chmod a+x /tmp/xc16.run \
#    && /tmp/xc16.run --mode unattended --unattendedmodeui none \
#        --netservername localhost --LicenseType FreeMode --prefix /opt/microchip/xc16 \
#    && rm /tmp/xc16.run
#
#ENV PATH $PATH:/opt/microchip/xc16/bin

# Download and Install XC32 Compiler, Current Version
#
#RUN curl -fSL -A "Mozilla/4.0" -o /tmp/xc32.run "http://www.microchip.com/mplabxc32linux" \
#    && chmod a+x /tmp/xc32.run \
#    && /tmp/xc32.run --mode unattended --unattendedmodeui none \
#        --netservername localhost --LicenseType FreeMode --prefix /opt/microchip/xc32 \
#    && rm /tmp/xc32.run
#
#ENV PATH $PATH:/opt/microchip/xc32/bin

# Download and Install MPLABX IDE, Current Version

RUN curl -fSL -A "Mozilla/4.0" -o /tmp/mplabx-installer.tar "http://www.microchip.com/mplabx-ide-linux-installer" \
    && tar xf /tmp/mplabx-installer.tar && rm /tmp/mplabx-installer.tar \
    && USER=root ./*-installer.sh --nox11 \
        -- --unattendedmodeui none --mode unattended --installdir /opt/microchip/mplabx \
    && rm ./*-installer.sh

ENV PATH $PATH:/opt/microchip/mplabx/mplab_ide/bin

VOLUME /tmp/.X11-unix

# Container Developer User Ident

RUN useradd user \
    && mkdir -p /home/user/MPLABXProjects \
    && touch /home/user/MPLABXProjects/.directory \
    && chown user:user /home/user/MPLABXProjects

VOLUME /home/user/MPLABXProjects

RUN echo 'deb http://httpredir.debian.org/debian jessie-backports main' > /etc/apt/sources.list.d/jessie-backports.list

# Default to UTF-8 file.encoding
ENV LANG C.UTF-8

# add a simple script that can auto-detect the appropriate JAVA_HOME value
# based on whether the JDK or only the JRE is installed
RUN { \
		echo '#!/bin/sh'; \
		echo 'set -e'; \
		echo; \
		echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \
	} > /usr/local/bin/docker-java-home \
	&& chmod +x /usr/local/bin/docker-java-home

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/jre

ENV JAVA_VERSION 8u102
ENV JAVA_DEBIAN_VERSION 8u102-b14.1-1~bpo8+1

# see https://bugs.debian.org/775775
# and https://github.com/docker-library/java/issues/19#issuecomment-70546872
ENV CA_CERTIFICATES_JAVA_VERSION 20140324

RUN set -x \
	&& apt-get update \
	&& apt-get install -y \
		openjdk-8-jre-headless="$JAVA_DEBIAN_VERSION" \
		ca-certificates-java="$CA_CERTIFICATES_JAVA_VERSION" \
	&& rm -rf /var/lib/apt/lists/* \
	&& [ "$JAVA_HOME" = "$(docker-java-home)" ]

# see CA_CERTIFICATES_JAVA_VERSION notes above
RUN /var/lib/dpkg/info/ca-certificates-java.postinst configure



# Container Tool Version Reports to Build Log

RUN [ -x /opt/microchip/xc8/bin/xc8 ] && xc8 --ver
#RUN [ -x /opt/microchip/xc16/bin/xc16-gcc ] && xc16-gcc --version
#RUN [ -x /opt/microchip/xc32/bin/xc32-gcc ] && xc32-gcc --version

#CMD ["/opt/microchip/mplabx/mplab_ide/bin/mplab_ide"]
