FROM fedora:22

RUN dnf update -y -q; dnf clean all
ADD logstash-1.5.repo /etc/yum.repos.d/logstash-1.5.repo
RUN dnf install -y -q java-1.8.0-openjdk-headless.x86_64 logstash which hostname; dnf clean all

ENV PATH=${PATH}:/opt/logstash/bin

RUN /opt/logstash/bin/plugin install logstash-filter-kubernetes
RUN /opt/logstash/bin/plugin install logstash-filter-json_encode
RUN /opt/logstash/bin/plugin install logstash-output-cloudwatchlogs
RUN /opt/logstash/bin/plugin install logstash-input-journald

COPY run.sh /run.sh
COPY conf.d/ /etc/logstash/conf.d/
COPY outputs.d/ /root/outputs/

VOLUME /var/log/logstash

CMD ["/run.sh"]
