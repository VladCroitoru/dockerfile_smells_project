FROM deyrakesh85/ubuntu:jdk8

MAINTAINER Rakesh Dey <deyrakesh85@gmail.com>

RUN groupadd -r kibana && useradd -r -g kibana -s /bin/bash -m kibana

RUN wget https://artifacts.elastic.co/downloads/kibana/kibana-6.2.2-linux-x86_64.tar.gz

RUN tar -xzf kibana-6.2.2-linux-x86_64.tar.gz

COPY kibana.yml /data/kibana-6.2.2-linux-x86_64/config

RUN chown -R kibana:kibana /data

USER kibana

RUN chmod -R 755 kibana-*

EXPOSE 5601

ENTRYPOINT ["/data/kibana-6.2.2-linux-x86_64/bin/kibana"]
