FROM lsiobase/alpine

LABEL maintainer "zaggash"

RUN \
  apk add --no-cache \
    python \
    ssmtp \
    docker \
    jq \
    libmnl \
    libuuid \
    python \
    curl \
    netcat-openbsd \
    lm_sensors \
    nodejs \
    py-mysqldb \
    py-psycopg2 \
    py-yaml && \
  
  # Compile
  curl -s https://my-netdata.io/kickstart-static64.sh >/tmp/kickstart-static64.sh && \
  bash /tmp/kickstart-static64.sh --dont-wait && \
  
  # cleanup


	
rm -rf /var/cache/apk/* /tmp/* /etc/init.d

# copy local files
COPY root/ /

# ports and volumes
EXPOSE 19999
VOLUME /config
