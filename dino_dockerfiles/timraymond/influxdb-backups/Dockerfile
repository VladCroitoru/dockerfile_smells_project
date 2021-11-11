FROM voidlock/heroku-gb-golang-docker:1.4.2-onbuild
ENV INFLUXDB_VERSION 0.9.1
RUN curl -s -o /tmp/influxdb_latest_amd64.deb https://s3.amazonaws.com/influxdb/influxdb_${INFLUXDB_VERSION}_amd64.deb && \
  dpkg -i /tmp/influxdb_latest_amd64.deb && \
  rm /tmp/influxdb_latest_amd64.deb && \
  rm -rf /var/lib/apt/lists/*
ENV PATH /opt/influxdb:$PATH
CMD ["bin/main"]
