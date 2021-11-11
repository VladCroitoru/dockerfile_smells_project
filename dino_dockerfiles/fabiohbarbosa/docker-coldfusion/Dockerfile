FROM ubuntu:12.04

MAINTAINER fabiohbarbosa <fabiohbarbosa@gmail.com>

USER root
RUN apt-get update && apt-get install wget libstdc++5 -y

ADD installer.properties /opt/installer.properties
ENV COLD_FUSION_URL = https://www.dropbox.com/s/4p8e6p1j25yrmu6/coldfusion-801-lin64.bin?dl=0;
RUN wget -O /opt/coldfusion-801-lin64.bin -q --no-check-certificate $COLD_FUSION_URL && chmod +x /opt/coldfusion-801-lin64.bin && /opt/./coldfusion-801-lin64.bin -i silent -f /opt/installer.properties

EXPOSE 8500

ADD startup.sh /opt/startup.sh
CMD ["sh", "/opt/startup.sh"]
