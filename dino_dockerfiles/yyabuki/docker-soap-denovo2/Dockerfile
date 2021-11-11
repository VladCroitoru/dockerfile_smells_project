FROM ubuntu:16.04
MAINTAINER Yukimitsu Yabuki, yukimitsu.yabuki@gmail.com

RUN apt-get update -y && apt-get install -y wget
RUN wget https://sourceforge.net/projects/soapdenovo2/files/SOAPdenovo2/bin/r240/SOAPdenovo2-bin-LINUX-generic-r240.tgz
RUN tar xvfz SOAPdenovo2-bin-LINUX-generic-r240.tgz
RUN cp /SOAPdenovo2-bin-LINUX-generic-r240/SOAPdenovo-127mer /usr/local/bin/
RUN cp /SOAPdenovo2-bin-LINUX-generic-r240/SOAPdenovo-63mer /usr/local/bin/
ADD run /usr/local/bin/
ADD Procfile /usr/local/bin/

ENTRYPOINT ["run"]
