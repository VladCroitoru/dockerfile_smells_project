FROM debian

RUN apt-get update && \
  apt-get install -q -y python python-pip curl && \
  curl https://s3.amazonaws.com/aws-cloudwatch/downloads/latest/awslogs-agent-setup.py -O && \
  chmod +x ./awslogs-agent-setup.py

ADD awslogs.conf.dummy ./awslogs.conf
RUN mkdir /etc/cron.d &&\
  touch /etc/cron.d/awslogs && \
  ./awslogs-agent-setup.py -n -r ap-northeast-1 -c ./awslogs.conf

ADD aws.conf /var/awslogs/etc/aws.conf
ADD awslogs.conf /var/awslogs/etc/awslogs.conf

CMD /bin/sh /var/awslogs/bin/awslogs-agent-launcher.sh
