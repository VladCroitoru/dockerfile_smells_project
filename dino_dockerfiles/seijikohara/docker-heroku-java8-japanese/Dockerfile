FROM heroku/cedar:14

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get -y install software-properties-common python-software-properties

RUN add-apt-repository -y ppa:openjdk-r/ppa
RUN apt-get update
RUN apt-get -y install openjdk-8-jdk

RUN update-alternatives --set java /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java
RUN update-alternatives --set javac /usr/lib/jvm/java-8-openjdk-amd64/bin/javac

RUN echo 'LC_ALL=ja_JP.UTF-8' > /etc/default/locale && echo 'LANG=ja_JP.UTF-8' >> /etc/default/locale
RUN locale-gen ja_JP.UTF-8

RUN apt-get clean
