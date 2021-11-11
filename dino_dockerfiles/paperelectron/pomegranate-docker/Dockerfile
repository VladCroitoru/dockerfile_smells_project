#Get baseimage up and running.

FROM phusion/baseimage:0.9.16

RUN apt-get update && apt-get -y install \
  build-essential \
  python \
  git \
  curl

RUN curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - && \
  echo 'deb https://deb.nodesource.com/node012 trusty main' > /etc/apt/sources.list.d/nodesource.list && \
  echo 'deb-src https://deb.nodesource.com/node012 trusty main' >> /etc/apt/sources.list.d/nodesource.list

RUN apt-get update && apt-get install -y nodejs && node -v && npm -v
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV POM_HOME /var/pom
ENV CONTENT_HOME $POM_HOME/content

# If you bind mount a volume from host/volume from a data container,
# ensure you use same uid

RUN useradd -d "$POM_HOME" -u 1000 -m -s /bin/bash pom

RUN mkdir /etc/service/pom-web
ADD pom-web.sh /etc/service/pom-web/run

EXPOSE 8080

VOLUME $CONTENT_HOME

ADD default_content/ $CONTENT_HOME

ADD index.js $POM_HOME/
WORKDIR $POM_HOME
RUN chown -R pom "$POM_HOME"
RUN npm install pomegranate lodash


CMD ["/sbin/my_init"]
