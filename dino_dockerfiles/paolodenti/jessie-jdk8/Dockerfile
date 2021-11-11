FROM paolodenti/jessie-apt-utils:8.7

MAINTAINER Paolo Denti "paolo.denti@gmail.com"

# wget
RUN DEBIAN_FRONTEND=noninteractive apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y wget

# jdk 1.8
RUN wget -nv -O /tmp/jdk.tgz --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u121-b13/e9e7ea248e2c4826b92b3f075a80e441/jdk-8u121-linux-x64.tar.gz && tar zxf /tmp/jdk.tgz -C /opt
RUN update-alternatives --install /usr/bin/java java /opt/jdk1.8.0_121/bin/java 100
RUN update-alternatives --install /usr/bin/javac javac /opt/jdk1.8.0_121/bin/javac 100

# cleanup
RUN DEBIAN_FRONTEND=noninteractive apt-get purge -y wget && DEBIAN_FRONTEND=noninteractive apt-get -y autoremove
RUN rm -rf /var/lib/apt/lists/*
