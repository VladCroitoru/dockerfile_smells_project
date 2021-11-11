FROM tomcat:7-jre7
MAINTAINER Leonard Daume <lenny@daume-web.eu>

# upgrade & install
RUN \
  apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y libfreetype6 libfontconfig bzip2 subversion

# install maven
RUN wget http://apache.mirror.digionline.de/maven/maven-3/3.2.5/binaries/apache-maven-3.2.5-bin.tar.gz
RUN tar xvfz apache-maven-3.2.5-bin.tar.gz -C /opt
RUN rm -fv apache-maven-3.2.5-bin.tar.gz

RUN ln -s /opt/apache-maven-3.2.5/ /opt/apache-maven

ENV M2_HOME=/opt/apache-maven
ENV M2=$M2_HOME/bin
ENV PATH=$M2:$PATH

# install phantomjs
RUN curl -sSLO https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.8-linux-x86_64.tar.bz2
RUN tar xvjf phantomjs-1.9.8-linux-x86_64.tar.bz2 -C /opt
RUN rm -fv phantomjs-1.9.8-linux-x86_64.tar.bz2

RUN ln -s /opt/phantomjs-1.9.8-linux-x86_64/bin/phantomjs /usr/local/bin/phantomjs

ENV PHANTOM_BIN=/opt/phantomjs-1.9.8-linux-x86_64/bin
ENV PATH=$PHANTOM_BIN:$PATH

# install highcharts export server
RUN apt-get --yes --no-install-recommends install \
    openjdk-7-jdk \
  && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64
RUN svn co https://github.com/highslide-software/highcharts.com/trunk/exporting-server/java/highcharts-export
RUN mvn -f ./highcharts-export/pom.xml install
RUN mvn -f ./highcharts-export/highcharts-export-web/pom.xml clean package
RUN cp highcharts-export/highcharts-export-web/target/highcharts-export-web.war webapps
RUN rm -rf highcharts-export

EXPOSE 8080
