FROM oberthur/docker-ubuntu-java:jdk8_8.112.15

MAINTAINER Aleksey Lisun <lisun90@gmail.com>

ENV HOME=/opt/app

WORKDIR /opt/app


RUN apt-get update && apt-get install -y wget bzip2

RUN wget http://download-aws.ej-technologies.com/jprofiler/jprofiler_linux_8_1_2.tar.gz -P /tmp/ && \
tar -xzf /tmp/jprofiler_linux_8_1_2.tar.gz -C /usr/local && \
rm /tmp/jprofiler_linux_8_1_2.tar.gz

ENV JPAGENT_PATH="-agentpath:/usr/local/jprofiler8/bin/linux-x64/libjprofilerti.so=nowait"
EXPOSE 8849

RUN wget https://www.yourkit.com/download/yjp-2016.02-b43-linux.tar.bz2 && \ 
tar jxvf yjp-2016.02-b43-linux.tar.bz2

#EXPOSE PORT_TO_EXPOSE_YOURKIT