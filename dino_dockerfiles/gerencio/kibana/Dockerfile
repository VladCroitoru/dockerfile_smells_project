FROM openjdk:8u111-jre

MAINTAINER clayton@xdevel.com.br

ENV KIBANA_VERSION 5.6.2

#instalando nodejs
RUN apt-get update && apt-get install -y  curl git && \
    curl -sL https://deb.nodesource.com/setup_6.x | bash - && \
    apt-get install -y nodejs

ADD https://artifacts.elastic.co/downloads/kibana/kibana-${KIBANA_VERSION}-linux-x86_64.tar.gz /tmp/kibana.tgz

RUN tar -C /opt -xzf /tmp/kibana.tgz && rm /tmp/kibana.tgz

ENV KIBANA_HOME /opt/kibana-$KIBANA_VERSION-linux-x86_64

RUN mkdir -p $KIBANA_HOME/plugins

WORKDIR $KIBANA_HOME

WORKDIR $KIBANA_HOME/plugins

# RUN  git clone https://github.com/mstoyano/kbn_c3js_vis.git c3_charts && cd c3_charts && npm install
# RUN  git clone https://github.com/ommsolutions/kibana_ext_metrics_vis extended_metric_vis

WORKDIR $KIBANA_HOME

ADD start.sh /start

EXPOSE 5601

CMD ["/start"]
