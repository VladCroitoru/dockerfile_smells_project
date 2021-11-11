FROM dohque/docker-play
MAINTAINER Ruslan Pilin

RUN echo "deb http://ppa.launchpad.net/ubuntu-toolchain-r/test/ubuntu trusty main" > /etc/apt/sources.list.d/toolchain.list && \
    echo "deb-src http://ppa.launchpad.net/ubuntu-toolchain-r/test/ubuntu trusty main" >> /etc/apt/sources.list.d/toolchain.list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 60C317803A41BA51845E371A1E9377A2BA9EF27F && \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --force-yes libstdc++6 libgtk2.0-0 libgstreamer0.10-0 libgstreamer-plugins-base0.10-0 libv4l-0 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists && \
    rm -rf /var/cache/oracle-jdk*
