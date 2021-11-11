FROM elifarley/docker-cep:alpine-jdk-8
MAINTAINER Elifarley <elifarley@gmail.com>

ENV CEP_LOG_FILES=/data/activemq.log:out
VOLUME /data
EXPOSE 61612 61613 61616 8161

COPY *app*.sh $HOME/

RUN \
  xinstall add activemq 5.13.3 && \
  xinstall cleanup && \
  chmod +x "$HOME"/*app*.sh && chown "$_USER":"$_USER" "$HOME"/*app.sh && \
  (\
    cd /usr/local/apache-activemq/conf && \
    chown :$_USER .. . jetty-realm.properties users.properties && \
    chmod g=u .. . jetty-realm.properties users.properties \
  )
