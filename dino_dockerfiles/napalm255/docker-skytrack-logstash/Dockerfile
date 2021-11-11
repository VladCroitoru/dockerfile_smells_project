FROM logstash:latest

RUN apt-get update; apt-get upgrade -y
RUN apt-get install -y git php5-cli php5-curl vim

RUN git clone https://github.com/napalm255/skytrack.org.git /opt/skytrack
RUN mkdir /opt/skytrack/json
RUN chown -R logstash:logstash /opt/skytrack

COPY skytrack.conf /etc/logstash/conf.d/skytrack.conf

RUN mkdir /root/.aws
RUN mkdir /var/lib/logstash/.aws

COPY skytrack.aws /root/.aws/credentials
COPY skytrack.aws /var/lib/logstash/.aws/credentials

RUN chown root:root /root/.aws/credentials
RUN chown logstash:logstash /var/lib/logstash/.aws/credentials

RUN chmod 0600 /root/.aws/credentials
RUN chmod 0600 /var/lib/logstash/.aws/credentials

CMD ["logstash", "-f /etc/logstash/conf.d/"]
