FROM bassoman/ubuntu-jdk:1.0.0
MAINTAINER Jon Lancelle <bassoman@gmail.com>

RUN wget "http://apache.mirrors.pair.com/xalan/xalan-j/binaries/xalan-j_2_7_2-bin.tar.gz" \
  -O /opt/xalan-j_2_7_2-bin.tar.gz && \
  cd /opt && tar -xzvf xalan-j_2_7_2-bin.tar.gz

RUN apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y g++ make git \
  && apt-get clean

RUN apt-get install -y libxerces2-java libxerces2-java-doc unzip \
  && wget "http://sourceforge.net/projects/saxon/files/Saxon-HE/9.7/SaxonHE9-7-0-1J.zip/download" \
  -O /opt/SaxonHE9-7-0-1J.zip \
  && cd /opt \
  && unzip SaxonHE9-7-0-1J.zip -d SaxonHE

ENV CLASSPATH /opt/xalan-j_2_7_2/*:/usr/share/java/*:/opt/SaxonHE/saxon9he.jar
