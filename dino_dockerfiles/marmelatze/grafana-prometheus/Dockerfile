FROM grafana/grafana:2.0.2

RUN apt-get install -y curl
RUN curl -sSL https://github.com/grafana/grafana-plugins/archive/master.tar.gz \
         | tar -v -C /usr/share/grafana/public/app/plugins/datasource/ -xz --strip-components=2 grafana-plugins-master/datasources/prometheus
