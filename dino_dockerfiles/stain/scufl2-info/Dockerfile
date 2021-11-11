FROM tomcat:7-jre7
MAINTAINER "Stian Soiland-Reyes <orcid.org/0000-0001-9842-9718>"

RUN rm -rf /usr/local/tomcat/webapps/*

# Borrowed from https://registry.hub.docker.com/u/pandeiro/lein/dockerfile/
ENV LEIN_ROOT true
RUN wget -q -O /usr/bin/lein \
    https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein \
        && chmod +x /usr/bin/lein

WORKDIR /tmp

COPY project.clj /tmp/
COPY src /tmp/src/
COPY resources /tmp/resources/

RUN lein deps && lein ring uberwar && cp target/*war /usr/local/tomcat/webapps/ROOT.war && rm -rf /tmp/* /root/.lein /root/.m2
EXPOSE 8009
