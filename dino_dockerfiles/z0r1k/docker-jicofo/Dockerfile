FROM debian:jessie
MAINTAINER Mykhailo Lieibenson <gramatron@gmail.com>

ENV JICOFO_TAG=255
ENV JICOFO_USER=focus
ENV JICOFO_HOME=/jicofo
ENV HOME=$JICOFO_HOME
ENV PATH=$JICOFO_HOME/bin:/usr/sbin:/usr/bin:/sbin:/bin

ENV FOCUS_SECRET = "-secret-"
ENV XMPP_DOMAIN="example.com"
ENV XMPP_SUBDOMAIN="jitsi-focus"
ENV XMPP_HOST="localhost"
ENV XMPP_PORT="5347"
ENV FOCUS_USER = "focus"
ENV FOCUS_USER_SECRET = "#secret#"
ENV FOCUS_USER_DOMAIN = "example.com"

USER root
WORKDIR $JICOFO_HOME

RUN groupadd -r $JICOFO_USER \
    && useradd -r -m \
       -g $JICOFO_USER \
       -d $JICOFO_HOME \
       -c "Jitsi Meet Conference Focus User" \
       $JICOFO_USER \
    && chown -R $JICOFO_USER:$JICOFO_USER $JICOFO_HOME

ADD ./scripts $JICOFO_HOME/scripts

RUN chmod 0755 $JICOFO_HOME/scripts/*.sh \
    && chown $JICOFO_USER: $JICOFO_HOME/scripts/*.sh

RUN apt-get -y update \
    && apt-get -y install git wget unzip \
    && apt-get -y install default-jdk ant maven

USER $JICOFO_USER

RUN git clone https://github.com/jitsi/jicofo.git focus

RUN cd focus \
    && git checkout $JICOFO_TAG \
    && wget -O lib/maven-ant-tasks-2.1.3.jar http://central.maven.org/maven2/org/apache/maven/maven-ant-tasks/2.1.3/maven-ant-tasks-2.1.3.jar \
    && mvn dependency:resolve \
    && ant -lib lib/maven-ant-tasks-2.1.3.jar dist.lin64 \
    && unzip dist/linux/jicofo-linux-x64-build.SVN.zip

EXPOSE $XMPP_PORT

CMD ["scripts/run.sh"]
