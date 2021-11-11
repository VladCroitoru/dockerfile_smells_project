# This dockerfile uses the ubuntu image
# Author: Yale Huang
# Command format: Instruction [arguments / command] ..

# Base image to use, this must be set as the first line
FROM ubuntu

MAINTAINER Yale Huang <calvino.huang@gmail.com>

# Commands to update the image
RUN apt-get -y update && apt-get -y upgrade

RUN apt-get install openjdk-7-jre unzip \
	libpcap-dev wget -y
RUN wget -O /root/FinalSpeed_Client_CLI.zip https://github.com/zqhong/finalspeed/releases/download/v1.0/FinalSpeed_Client_CLI.zip
RUN mkdir -p /opt/finalspeed && cd /opt/finalspeed && unzip /root/FinalSpeed_Client_CLI.zip
RUN mkdir /conf

COPY start_finalspeed /opt/finalspeed/start_finalspeed

EXPOSE 1083/tcp

CMD ["/opt/finalspeed/start_finalspeed"]

