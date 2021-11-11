FROM docker.elastic.co/logstash/logstash:5.5.0

# uninstall xpack
RUN /usr/share/logstash/bin/logstash-plugin remove x-pack

# install journald plugin
RUN /usr/share/logstash/bin/logstash-plugin install logstash-input-journald

# add logstash user to systemd-journald group
USER root
RUN usermod -a -G systemd-journal logstash
USER logstash
