# http://elk-docker.readthedocs.io/

FROM sebp/elk:562

LABEL MAINTAINER "Gary A. Stafford <gary.stafford@accenture.com>"
ENV REFRESHED_AT 2017-09-30

# overwrite existing logstash config file
ADD 03-logspout-input.conf /etc/logstash/conf.d/03-logspout-input.conf
ADD 04-gelf-input.conf /etc/logstash/conf.d/04-gelf-input.conf
ADD 30-output.conf /etc/logstash/conf.d/30-output.conf

# install elasticsearch plugins
# install curator to remove old data in elasticsearch
RUN echo 'deb [arch=amd64] http://packages.elastic.co/curator/5/debian stable main' >> /etc/apt/sources.list \
  && apt-get update -y && apt-get upgrade -y \
  && apt-get install wget -y \
  && wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | apt-key add - \
  && apt-get install elasticsearch-curator -y --allow-unauthenticated

WORKDIR /tmp
