FROM datadog/docker-dd-agent
MAINTAINER Mariana Salcedo <mariana.salcedo@synergy-gb.com>

#Add and extract application
ADD  etcd.yaml /
ADD  replace.sh /replace.sh

CMD ["supervisord", "-n", "-c", "/etc/dd-agent/supervisor.conf"]
