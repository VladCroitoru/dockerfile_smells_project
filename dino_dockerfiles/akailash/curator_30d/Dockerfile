FROM centos:7
MAINTAINER akailash

RUN mkdir /etc/curator
ADD action_file.yml /etc/curator
ADD config.yml /etc/curator

# Install python-pip
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
RUN python get-pip.py

# Install curator (https://www.elastic.co/guide/en/elasticsearch/client/curator/4.2/installation.html)
RUN pip install elasticsearch-curator

# download go-cron
RUN curl -L -o /usr/local/bin/go-cron-linux.gz https://github.com/odise/go-cron/releases/download/v0.0.7/go-cron-linux.gz
RUN gunzip /usr/local/bin/go-cron-linux.gz
RUN chmod u+x /usr/local/bin/go-cron-linux

ENV PATH=/usr/local/bin:$PATH
ENV HOST "elasticsearch"
ENV PORT 9200
ENV DAYS 30
ENV SCHEDULE "0 0 0 * * ?"
ENV PREFIX logstash-
ENV COMMAND "curator --dry-run --config /etc/curator/config.yml /etc/curator/action_file.yml"
EXPOSE 8080
CMD go-cron-linux -s "$SCHEDULE" -p 8080 -- /bin/bash -c "$COMMAND"
