FROM debian:jessie

MAINTAINER pahudnet@gmail.com

ENV REGION ap-northeast-1

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -q -y python python-pip wget
RUN cd / ; wget https://s3.amazonaws.com/aws-cloudwatch/downloads/latest/awslogs-agent-setup.py

ADD ./awslogs.conf.dummy /root/awslogs.conf.dummy
RUN mkdir /etc/cron.d
#RUN python /awslogs-agent-setup.py -n -r us-west-2 -c /root/awslogs.conf.dummy
RUN python /awslogs-agent-setup.py -n -r us-west-2 -c /root/awslogs.conf.dummy

ADD start.sh /
RUN chmod a+x /start.sh
CMD /start.sh
