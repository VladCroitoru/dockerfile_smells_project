FROM qnib/alpn-node

ARG KIBANA_VER=5.0.0-rc1
ARG KIBANA_URL=https://artifacts.elastic.co/downloads/kibana
ENV PATH="${PATH}:/opt/kibana/bin/"

RUN curl -sfL "${KIBANA_URL}/kibana-${KIBANA_VER}-linux-x86_64.tar.gz" |tar xfz - -C /opt/ \
 && mv /opt/kibana-${KIBANA_VER}-linux-x86_64 /opt/kibana/ \
 && sed -i''  -e 's#NODE=.*#NODE=/usr/bin/node#' /opt/kibana/bin/kibana \
 && sed -i''  -e 's#NODE=.*#NODE=/usr/bin/node#' /opt/kibana/bin/kibana-plugin
ADD etc/supervisord.d/kibana5.ini /etc/supervisord.d/
ADD etc/consul.d/kibana5.json /etc/consul.d/
ADD opt/qnib/kibana/5/bin/healthcheck.sh \
    opt/qnib/kibana/5/bin/start.sh \
    /opt/qnib/kibana/5/bin/
