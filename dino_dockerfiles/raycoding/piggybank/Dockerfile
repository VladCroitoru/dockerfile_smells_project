FROM ubuntu:12.04
MAINTAINER Shuddhashil Ray rayshuddhashil@gmail.com

#Ensuring UTF-8
RUN locale-gen en_US.UTF-8
ENV LANG       en_US.UTF-8
ENV LC_ALL     en_US.UTF-8

# Installing bunch of essentials
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
RUN apt-get update && apt-get -y install  gcc g++ curl g++-multilib gcc-multilib openssl \
git htop vim screen wget unzip openssh-server openssh-client \
inetutils-ping sed telnet maven

# Installing Java7u60
RUN mkdir -p /usr/lib/jvm
RUN (cd /usr/lib/jvm && wget  -q -nc --no-cookies \
					--no-check-certificate \
					--header "Cookie: oraclelicense=accept-securebackup-cookie" \
					http://download.oracle.com/otn-pub/java/jdk/7u60-b19/jdk-7u60-linux-x64.tar.gz)
RUN tar -xzvf /usr/lib/jvm/jdk-7u60-linux-x64.tar.gz -C /usr/lib/jvm
RUN (update-alternatives --install /usr/bin/java java /usr/lib/jvm/jdk1.7.0_60/bin/java 1 && update-alternatives --set java /usr/lib/jvm/jdk1.7.0_60/bin/java)
RUN (update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/jdk1.7.0_60/bin/javac 1 && update-alternatives --set javac /usr/lib/jvm/jdk1.7.0_60/bin/javac)
RUN (update-alternatives --install /usr/bin/javaws javaws /usr/lib/jvm/jdk1.7.0_60/bin/javaws 1 && update-alternatives --set javaws /usr/lib/jvm/jdk1.7.0_60/bin/javaws)
ENV JAVA_HOME			/usr/lib/jvm/jdk1.7.0_60
ENV JRE_HOME		  /usr/lib/jvm/jdk1.7.0_60/jre

RUN rm -rf /usr/lib/jvm/jdk-7u60-linux-x64.tar.gz

# Default command.
CMD ["/bin/bash"]

