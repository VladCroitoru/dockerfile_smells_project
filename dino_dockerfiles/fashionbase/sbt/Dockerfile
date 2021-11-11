FROM ubuntu:precise

RUN apt-get update

# install add-apt-repository tool
RUN apt-get install -y python-software-properties apt-transport-https

RUN add-apt-repository ppa:webupd8team/java

RUN apt-get install -y wget

RUN apt-get update

RUN echo 'debconf shared/accepted-oracle-license-v1-1 select true' | debconf-set-selections
RUN apt-get install -y oracle-java8-set-default

RUN echo "deb https://dl.bintray.com/sbt/debian /" | tee -a /etc/apt/sources.list.d/sbt.list
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823
RUN apt-get update
RUN apt-get install -y sbt

# print versions
RUN java -version

# fetches all sbt jars from Maven repo so that your sbt will be ready to be used when you launch the image
RUN sbt -v
