FROM rocker/rstudio

RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections

# update repos
RUN apt-get update
RUN apt-get install gnupg -y
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886

RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee /etc/apt/sources.list.d/webupd8team-java.list
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list
RUN apt-get update


# install java
RUN apt-get install oracle-java8-installer -y

RUN apt-get clean

#RUN  mkdir -p /usr/lib/jvm/default-java/ && ln -s /usr/lib/jvm/java-8-oracle/ /usr/lib/jvm/default-java/
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle/jre/

RUN R CMD javareconf
