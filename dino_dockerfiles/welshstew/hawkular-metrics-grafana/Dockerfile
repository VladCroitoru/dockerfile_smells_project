FROM grafana/grafana

# This is the default for Linux Grafana installs. Change it to match yours, if needed.
#ENV GRAFANA_PLUGINS=/var/lib/grafana/plugins
WORKDIR root

RUN apt-get update && apt-get install -y wget unzip && apt-get clean

RUN wget https://github.com/hawkular/hawkular-grafana-datasource/archive/master.zip -O hawkular-grafana-datasource-master.zip
RUN unzip hawkular-grafana-datasource-master.zip
RUN mkdir -p /usr/share/grafana/public/app/plugins/datasource/hawkular && cp -R hawkular-grafana-datasource-master/dist/* /usr/share/grafana/public/app/plugins/datasource/hawkular

RUN rm -rf /root/