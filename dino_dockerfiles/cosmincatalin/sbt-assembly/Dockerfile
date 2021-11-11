FROM ubuntu:trusty

ENV DEBIAN_FRONTEND noninteractive

# Update package list
RUN apt-get -qq update

RUN apt-get -qq install software-properties-common -y
RUN apt-get install apt-transport-https

RUN add-apt-repository ppa:webupd8team/java \
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | sudo /usr/bin/debconf-set-selections \
&& echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a /etc/apt/sources.list.d/sbt.list \
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823

RUN apt-get -qq update \
&& apt-get -qq install \
oracle-java8-installer \
-y

RUN wget -q www.scala-lang.org/files/archive/scala-2.12.2.deb \
&& dpkg -i scala-2.12.2.deb \
&& apt-get update \
&& apt-get -qq install \
scala \
sbt \
-y

RUN sbt -sbt-version 0.13.12 clean

VOLUME /scala-project

WORKDIR /scala-project

CMD ["sbt", "assembly"]