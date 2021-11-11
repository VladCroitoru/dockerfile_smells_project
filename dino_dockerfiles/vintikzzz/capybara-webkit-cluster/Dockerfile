FROM buildpack-deps:xenial

ENV NGINX_VER=1.9.12 \
  CONSUL_TEMPLATE_VER=0.14.0 \
  WEBKIT_PORT=40000 \
  NGINX_PIDFILE=/var/run/nginx.pid \
  CONSUL_TEMPLATE_PIDFILE=/var/run/consul-template.pid \
  CONSUL_URL=consul:8500 \
  CONSUL_TEMPLATE_LOGFILE=/var/log/consul-template.log

COPY consul-template.sh run.sh /opt/
COPY monitrc.template nginx.ctmpl /tmp/

RUN set -ex \
	&& apt-get update \
	&& apt-get install -y --no-install-recommends monit unzip gettext-base \
	&& rm -rf /var/lib/apt/lists/* \
	&& curl -fSL -o nginx.tar.gz "http://nginx.org/download/nginx-$NGINX_VER.tar.gz" \
	&& mkdir -p /tmp/nginx \
	&& tar -xzf nginx.tar.gz -C /tmp/nginx --strip-components=1 \
	&& rm -rf nginx.tar.gz \
  && cd /tmp/nginx \
  && ./configure --prefix=/opt/nginx --with-stream --with-cc-opt=-Wno-error --pid-path=$NGINX_PIDFILE \
  && make -j2 \
  && make install \
	&& rm -r /tmp/nginx \
  && ln -sf /dev/stdout /opt/nginx/logs/access.log \
	&& ln -sf /dev/stderr /opt/nginx/logs/error.log \
  && curl -fSL -o /tmp/consul-template.zip "https://releases.hashicorp.com/consul-template/$CONSUL_TEMPLATE_VER/consul-template_${CONSUL_TEMPLATE_VER}_linux_amd64.zip" \
	&& mkdir -p /opt/consul-template \
  && unzip /tmp/consul-template.zip -d /opt/consul-template \
  && rm -rf /tmp/consul-template.zip \
  && ln -sf /dev/stdout /var/log/monit.log \
	&& apt-get purge -y --auto-remove unzip \
	&& chmod +x /opt/consul-template.sh \
	&& chmod +x /opt/run.sh


WORKDIR /opt

EXPOSE $WEBKIT_PORT

CMD ["/bin/sh", "./run.sh"]
