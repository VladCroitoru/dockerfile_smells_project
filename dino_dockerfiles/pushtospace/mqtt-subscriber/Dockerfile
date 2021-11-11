FROM ubuntu:16.04
MAINTAINER Gino Jongenelen <g.jongenelen@pushto.space>

RUN apt-get update && apt-get upgrade -y && apt-get install python3-pip -y && apt-get clean && pip3 install pymysql paho-mqtt

ADD ./start.py /root
ADD ./start.sh /root

RUN chmod +x /root/start.sh

CMD ["/root/start.sh"]