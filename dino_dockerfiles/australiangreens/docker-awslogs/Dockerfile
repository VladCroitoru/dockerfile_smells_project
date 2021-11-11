FROM ubuntu:18.04
MAINTAINER Brett Neese <brett@neese.rocks>, Ryuta Otaki <otaki.ryuta@classmethod.jp>, Sergey Zhukov <sergey@jetbrains.com>

RUN apt-get update
RUN apt-get install -q -y python python-pip wget cron
RUN cd / ; wget https://s3.amazonaws.com/aws-cloudwatch/downloads/latest/awslogs-agent-setup.py

ADD awslogs.conf.dummy /
RUN python /awslogs-agent-setup.py -n -r ap-southeast-2 -c ./awslogs.conf.dummy

ADD run-services.sh /
RUN chmod a+x /run-services.sh
CMD /run-services.sh
