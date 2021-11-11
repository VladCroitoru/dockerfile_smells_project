FROM ivonet/openjdk-alpine:8u242 as builder

RUN apk add apache-ant git patch xmlstarlet certbot curl \
 && git clone --depth=1 https://github.com/jgraph/drawio.git \
 && cd /drawio/etc/build \
 && ant war \
 && mkdir /draw \
 && unzip /drawio/build/draw.war -d /draw

COPY PreConfig.js PostConfig.js /draw/js/

FROM tomcat:9-jre8-alpine

LABEL maintainer="Ivo Wolring - @ivonet"

RUN apk add xmlstarlet certbot curl \
 && mkdir -p $CATALINA_HOME/webapps/draw

COPY --from=builder /draw $CATALINA_HOME/webapps/draw/

# Update server.xml to set Draw.io webapp to root
RUN cd $CATALINA_HOME && \
    xmlstarlet ed \
    -P -S -L \
    -i '/Server/Service/Engine/Host/Valve' -t 'elem' -n 'Context' \
    -i '/Server/Service/Engine/Host/Context' -t 'attr' -n 'path' -v '/' \
    -i '/Server/Service/Engine/Host/Context[@path="/"]' -t 'attr' -n 'docBase' -v 'draw' \
    -s '/Server/Service/Engine/Host/Context[@path="/"]' -t 'elem' -n 'WatchedResource' -v 'WEB-INF/web.xml' \
    -i '/Server/Service/Engine/Host/Valve' -t 'elem' -n 'Context' \
    -i '/Server/Service/Engine/Host/Context[not(@path="/")]' -t 'attr' -n 'path' -v '/ROOT' \
    -s '/Server/Service/Engine/Host/Context[@path="/ROOT"]' -t 'attr' -n 'docBase' -v 'ROOT' \
    -s '/Server/Service/Engine/Host/Context[@path="/ROOT"]' -t 'elem' -n 'WatchedResource' -v 'WEB-INF/web.xml' \
    conf/server.xml

COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

WORKDIR $CATALINA_HOME

EXPOSE 8080 8443

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["catalina.sh", "run"]
