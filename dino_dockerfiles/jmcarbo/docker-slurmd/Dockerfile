FROM jmcarbo/docker-slurmbase

MAINTAINER Joan Marc Carbo Arnau <jmcarbo@gmail.com>

RUN mkdir -p /usr/local/etc/slurm

ADD scripts/start.sh /root/start.sh
RUN chmod +x /root/start.sh

ADD etc/supervisord.d/slurmd.conf /etc/supervisor/conf.d/slurmd.conf

COPY etc/* etc/
COPY bin/* /usr/local/bin/
RUN chmod +x /usr/local/bin/slurmd-manage

#CMD ["/bin/bash","/root/start.sh"]
CMD containerpilot -config file:///etc/containerpilot.json /usr/sbin/slurmd -D -v 
