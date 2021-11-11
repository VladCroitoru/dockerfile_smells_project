FROM jmcarbo/docker-slurmbase

MAINTAINER Joan Marc Carbo Arnau <jmcarbo@gmail.com>

RUN apt-get update && apt-get install -y msmtp

RUN mkdir -p /usr/local/etc/slurm

ADD scripts/start.sh /root/start.sh
RUN chmod +x /root/start.sh

ADD etc/supervisord.d/slurmctld.conf /etc/supervisor/conf.d/slurmctld.conf

COPY etc/* etc/
COPY bin/* /usr/local/bin/

RUN chmod +x /usr/local/bin/slurmctld-manage
RUN chmod +x /usr/local/bin/mymsmtp.wrapper

#CMD ["/bin/bash","/root/start.sh"]
CMD containerpilot -config file:///etc/containerpilot.json /usr/sbin/slurmctld -D -v 
 
